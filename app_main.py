import sys
from PyQt6 import QtWidgets
from vispy import app

from app_ui import FunctionPlotterUI
from app_config import WINDOW_POS, WINDOW_SIZE
import app_config 

def main():
    """Entry point for the application."""
    appQt = QtWidgets.QApplication(sys.argv)
    appQt.setStyleSheet(app_config.STYLE_SHEET)  # apply stylesheet globally
    function_plotter = FunctionPlotterUI()
    function_plotter.setGeometry(WINDOW_POS[0], WINDOW_POS[1], WINDOW_SIZE[0], WINDOW_SIZE[1])
    function_plotter.setWindowTitle("Function Plotter")
    function_plotter.show()
    app.run()

if __name__ == '__main__':
    main()
