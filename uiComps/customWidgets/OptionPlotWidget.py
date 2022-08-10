from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import pyqtgraph as pg
import numpy as np
from Constants import Constants
import sys
from Constants import OrderType
from QHelper import Validator, find_nearest
from .StrikeLineObject import StrikeLineObject


class OptionPlotWidget(pg.PlotWidget):
    
    data_mid = None

    def __init__(self, delegate):
        super().__init__()

        self.delegate = delegate
        self.setupGraphs()

    def setupGraphs(self):     

        self.addCrossHair()
        self.proxy = pg.SignalProxy(self.scene().sigMouseMoved, rateLimit=60, slot=self.mouseMoved)
        self.setMouseEnabled(y=False)

        self.setupCurves()
        self.setupCurveHooks()


    def setupCurves(self):

        self.curve_bid = pg.PlotCurveItem()
        self.curve_ask = pg.PlotCurveItem()
        self.bid_ask_band = pg.FillBetweenItem(self.curve_ask, self.curve_bid, brush=(50,50,200,50))
        self.addItem(self.bid_ask_band)
        self.curve_mid = self.plot(np.array([0]), np.array([0]), color='r', symbol='x')

    def setupCurveHooks(self):
        self.curvePoints = pg.CurvePoint(self.curve_mid)
        self.addItem(self.curvePoints)
        self.arrow_mid = pg.ArrowItem(angle=240,pen=(255,255,0),brush=(255,0,0))
        self.arrow_mid.setParentItem(self.curvePoints)
        self.text_mid = pg.TextItem('MID',color=(80,80,80),anchor=(0.5,2.0))
        self.text_mid.setParentItem(self.curvePoints)

    def addCrossHair(self):
        self.hLine = pg.InfiniteLine(angle=0,movable=False)
        self.addItem(self.hLine,ignoreBounds=True)
        self.vLine = pg.InfiniteLine(angle=90,movable=False)
        self.addItem(self.vLine,ignoreBounds=True)

    def mouseMoved(self, evt): 
        pos = evt[0] 
        if self.sceneBoundingRect().contains(pos):
            mousePoint = self.plotItem.vb.mapSceneToView(pos)
            self.vLine.setPos(mousePoint.x())
            self.hLine.setPos(mousePoint.y())

    def getDataMid(self, df, index_name):
        filled_df = df[["BID", "ASK", index_name]].dropna()
        if not(filled_df.empty):
            data_ask = filled_df['ASK'].to_numpy()
            data_bid = filled_df['BID'].to_numpy()
            data_x = filled_df[index_name].to_numpy()
            data_mid = (data_bid + data_ask)/2.0
            
            return data_x, data_mid, data_bid, data_ask
        
        close_df = df[["CLOSE", index_name]].dropna()
        if not(close_df.empty):
            data_x = close_df[index_name].to_numpy()
            data_mid = close_df['CLOSE'].to_numpy()
            return data_x, data_mid, None, None
        
        return None, None, None, None


    def findIndex(self, array, value):
        result = np.where(array == value)
        return result[0][0]


class PremiumPlotWidget(OptionPlotWidget):

    no_strike_set = True
    selected_strike = None
    
    price = None

    def setupGraphs(self):     

        self.addChangeAxis()
        super().setupGraphs()

        self.setLabels(left='Premium', bottom='Days')
        
        self.addPriceLine()
        
        self.plotItem.vb.sigResized.connect(self.updateViews)
        self.updateViews()


    def setupCurves(self):
        super().setupCurves()

        self.absolute_change_line = pg.PlotCurveItem()
        self.changePlot.addItem(self.absolute_change_line)
        self.relative_change_line = pg.PlotCurveItem()
        self.changePlot.addItem(self.relative_change_line)


    def addPriceLine(self):
        self.price_line = pg.InfiniteLine(pos=0.0, angle=90, pen=pg.mkPen(color=(100,100,100),width=5, style=QtCore.Qt.DashLine),movable=False)
        self.addItem(self.price_line)

    def addChangeAxis(self):
        ## create a new ViewBox, link the right axis to its coordinate system
        self.changePlot = pg.ViewBox()
        self.plotItem.showAxis('right')
        self.plotItem.scene().addItem(self.changePlot)
        self.plotItem.getAxis('right').linkToView(self.changePlot)
        self.changePlot.setXLink(self.plotItem)
        self.plotItem.getAxis('right').setLabel('Change', color='#0000ff', angle=180)


    ## Handle view resizing 
    def updateViews(self):
        ## view has resized; update auxiliary views to match
        self.changePlot.setGeometry(self.plotItem.vb.sceneBoundingRect())
        
        ## need to re-update linked axes since this was called
        ## incorrectly while views had different shapes.
        ## (probably this should be handled in ViewBox.resizeEvent)
        self.changePlot.linkedViewChanged(self.plotItem.vb, self.changePlot.XAxis)

    def updatePlot(self, strike_frame, option_type):

        self.data_x, self.data_mid, self.data_bid, self.data_ask = self.getDataMid(strike_frame, "STRIKE")
        
        if not (self.price is None) and not(self.data_x is None):
            if option_type == Constants.CALL_TYPE:
                differences = self.price - self.data_x
            elif option_type == Constants.PUT_TYPE:
                differences = self.data_x - self.price
            
            differences = differences.clip(min=0)
            self.premium_mid = self.data_mid - differences

            pen = pg.mkPen(color=(80,80,80),width=5)
            self.curve_mid.setData(self.data_x, self.premium_mid, pen=pen, clickable=True)

            if not(self.data_bid is None) and not(self.data_ask is None):
                self.premium_bid = self.data_bid - differences
                self.premium_ask = self.data_ask - differences
                self.curve_ask.setData(self.data_x, self.premium_ask)
                self.curve_bid.setData(self.data_x, self.premium_bid)


            self.setYRange(0, self.premium_mid.max()*1.4)
            self.drawPremiumLines(option_type)

            if self.no_strike_set and hasattr(self, 'data_x'):
                self.no_strike_set = False

                self.strike_object = StrikeLineObject(self, self.delegate)
                
                index = find_nearest(self.data_x, self.price)    
                self.selected_strike = self.data_x[index]
                self.strike_object.updatePosition(self.data_x[index])
                self.updateStrikeSelection(self.selected_strike)
    

    def updatePrice(self, price):
        self.price = price
        self.price_line.setPos(price)


    def drawPremiumLines(self, option_type):
        if option_type == Constants.CALL_TYPE:
            absolute_data = (self.data_mid[:-1] - self.data_mid[1:])/(self.data_x[1:]-self.data_x[:-1])
            relative_data = ((self.data_mid[:-1] - self.data_mid[1:])/(self.data_x[1:]-self.data_x[:-1])).clip(min=0.001)/(self.data_mid[:-1]).clip(min=0.001)
            self.absolute_change_line.setData(self.data_x[:-1], absolute_data, pen=pg.mkPen(color=(0,150,0),width=5))
            self.relative_change_line.setData(self.data_x[:-1], relative_data, pen=pg.mkPen(color=(150,0,0),width=5))
        elif option_type == Constants.PUT_TYPE:
            absolute_data = (self.data_mid[1:] - self.data_mid[:-1])/(self.data_x[1:]-self.data_x[:-1])
            relative_data = ((self.data_mid[1:] - self.data_mid[:-1])/(self.data_x[1:]-self.data_x[:-1])).clip(min=0.001)/(self.data_mid[1:]).clip(min=0.001)
            self.absolute_change_line.setData(self.data_x[1:], absolute_data, pen=pg.mkPen(color=(0,150,0),width=5))
            self.relative_change_line.setData(self.data_x[1:], relative_data, pen=pg.mkPen(color=(150,0,0),width=5))


    def mouseMoved(self, evt): 
        super().mouseMoved(evt)

        if hasattr(self, 'data_mid') and hasattr(self, 'data_x'):
            pos = evt[0] 
            if self.sceneBoundingRect().contains(pos):
                mousePoint = self.plotItem.vb.mapSceneToView(pos)
                index = find_nearest(self.data_x, mousePoint.x())
                self.curvePoints.setPos(float(index)/float(len(self.data_mid)-1))
                self.text_mid.setText("[%0.2f,%0.2f]:"%(self.data_x[index], self.data_mid[index])+"MID")


    def updatePlotPrice(self, price):
        self.price = price
        self.price_line.setPos(price)


class PricePlotWidget(OptionPlotWidget):

    def setupGraphs(self):     

        super().setupGraphs()

        self.setLabels(left='Price', bottom='Days')

    def updatePlot(self, expiration_frame, option_type):
        self.data_x, self.data_mid, self.data_bid, self.data_ask = self.getDataMid(expiration_frame, "DAYS_TILL_EXP")

        self.expiration_names = expiration_frame['NAMES']

        if not(self.data_x is None):
            pen = pg.mkPen(color=(80,80,80),width=5)
            self.curve_mid.setData(self.data_x, self.data_mid,pen=pen, clickable=True)
            self.setYRange(0, self.data_mid.max()*1.4)

            if not(self.data_bid is None) and not(self.data_ask is None):
                self.curve_ask.setData(self.data_x, self.data_ask)
                self.curve_bid.setData(self.data_x, self.data_bid)


    def mouseMoved(self, evt): 
        super().mouseMoved(evt)

        if not(self.data_mid is None):
            pos = evt[0] 
            if self.sceneBoundingRect().contains(pos):
                mousePoint = self.plotItem.vb.mapSceneToView(pos)
                index = find_nearest(self.data_x, mousePoint.x())
                self.curvePoints.setPos(float(index)/float(len(self.data_mid)-1))
                self.text_mid.setText(self.expiration_names[index] + ": %0.2f"%(self.data_mid[index]))

