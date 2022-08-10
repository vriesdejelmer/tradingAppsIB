from generalFunctionality.Singleton import Singleton

@Singleton
class Logger:

    log_window = None

    def setLogWindow(self, log_window):
        self.log_window = log_window

    def printLine(self, line):
        self.log_window.appendPlainText(line)
