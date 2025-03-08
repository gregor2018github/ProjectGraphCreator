import sys
from PyQt6 import QtWidgets
from vispy import app

from ui import FunctionPlotterUI
from constants import WINDOW_POS, WINDOW_SIZE

def main():
    """Entry point for the application."""
    appQt = QtWidgets.QApplication(sys.argv)
    function_plotter = FunctionPlotterUI()
    function_plotter.setGeometry(WINDOW_POS[0], WINDOW_POS[1], WINDOW_SIZE[0], WINDOW_SIZE[1])
    function_plotter.setWindowTitle("Function Plotter")
    function_plotter.show()
    app.run()

if __name__ == '__main__':
    main()
