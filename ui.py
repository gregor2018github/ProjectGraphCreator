import numpy as np
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QVBoxLayout, QPushButton, QWidget, QSplitter, QLabel,
                           QSpinBox, QComboBox, QGridLayout, QLineEdit)
from vispy import scene
from vispy.color.colormap import get_colormaps

from constants import FOV, CAMERA_DISTANCE, EXAMPLE_FUNCTIONS, ALLOWED_CALCULATIONS
from logic import FunctionPlotter

class ObjectWidget(QWidget):
    def __init__(self, parent=None, main_window=None):
        super(ObjectWidget, self).__init__(parent)
        self.main_window = main_window
        
        # Added global stylesheet for modern, polished look
        self.setStyleSheet("""
            QWidget { 
                background-color: #f9f9f9; 
                font-family: 'Segoe UI', sans-serif; 
            }
            QPushButton { 
                background-color: #0078d7; 
                color: white; 
                border: none; 
                border-radius: 4px; 
                padding: 6px 12px; 
            }
            QPushButton:hover { 
                background-color: #005a9e; 
            }
            QLineEdit, QSpinBox, QComboBox { 
                border: 1px solid #ccc; 
                border-radius: 4px; 
                padding: 4px; 
            }
            QLabel { 
                color: #333333; 
            }
        """)
        
        self.create_function_section()
        self.create_scaling_section()
        self.create_limits_section()
        self.create_info_section()

        # Layout setup
        self.setup_layout()

    def create_function_section(self):
        """Create the function definition section"""
        self.l_function_title = QLabel("Function Definition")
        self.l_function_title.setStyleSheet("font-size: 20px;")

        self.change_function_button = QPushButton("Show Example Function")
        self.change_function_button.clicked.connect(self.pick_example_function)

        self.l_function_label = QLabel("Define Your Own Function: Z = ...           (must include X, Y, a, b, c)")
        self.function_input = QLineEdit("a * X**2 + b * Y**2 + c")
        self.function_input.setReadOnly(False)
        
        self.l_function_refresher = QPushButton("Refresh")
        self.l_function_refresher.clicked.connect(self.change_function)

        self.info_label = QLabel("")
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.info_label.setStyleSheet("color: red")

    def create_scaling_section(self):
        """Create the dynamic scaling rules section"""
        self.l_scaling_placeholder = QLabel("")
        self.l_scaling_placeholder.setStyleSheet("font-size: 40px;")
        self.l_scaling_title = QLabel("Dynamic Scaling Rules")
        self.l_scaling_title.setStyleSheet("font-size: 20px;")

        # Parameter scaling rules
        self.scaling_rule_a = QComboBox(self)
        self.scaling_rule_a.addItems(["a = sin(t)", "a = cos(t)", "a = tan(t)" , "a = 1; static"])
        
        self.scaling_rule_b = QComboBox(self)
        self.scaling_rule_b.addItems(["b = sin(t)", "b = cos(t)", "b = tan(t)" , "b = 1; static"])
        
        self.scaling_rule_c = QComboBox(self)
        self.scaling_rule_c.addItems(["c = sin(t)", "c = cos(t)", "b = tan(t)" , "c = 1; static"])
        self.scaling_rule_c.setCurrentIndex(3)

        # Speed controls
        speed_options = ["Speed = 5 %", "Speed = 10 %", "Speed = 25 %", "Speed = 50 %", 
                         "Speed = 100 %", "Speed = 150 %", "Speed = 200 %"]
        
        self.scaling_speed_a = QComboBox(self)
        self.scaling_speed_a.addItems(speed_options)
        self.scaling_speed_a.setCurrentIndex(4)
        
        self.scaling_speed_b = QComboBox(self)
        self.scaling_speed_b.addItems(speed_options)
        self.scaling_speed_b.setCurrentIndex(4)
        
        self.scaling_speed_c = QComboBox(self)
        self.scaling_speed_c.addItems(speed_options)
        self.scaling_speed_c.setCurrentIndex(4)

    def create_limits_section(self):
        """Create grid limits and color map section"""
        self.l_limits_placeholder = QLabel("")
        self.l_limits_placeholder.setStyleSheet("font-size: 40px;")
        self.l_limits_title = QLabel("Grid Limits and Color Map")
        self.l_limits_title.setStyleSheet("font-size: 20px;")

        # X limits
        self.l_x_limits = QLabel("X Limits (between 1 and 10)")
        self.x_limits = QSpinBox()
        self.x_limits.setMinimum(1)
        self.x_limits.setMaximum(10)
        self.x_limits.setValue(2)

        # Y limits
        self.l_y_limits = QLabel("Y Limits (between 1 and 10)")
        self.y_limits = QSpinBox()
        self.y_limits.setMinimum(1)
        self.y_limits.setMaximum(10)
        self.y_limits.setValue(2)

        # Grid resolution
        self.l_grid_points = QLabel("Grid Resolution (between 10 and 1000)")
        self.grid_points = QSpinBox()
        self.grid_points.setMinimum(10)
        self.grid_points.setMaximum(1000)
        self.grid_points.setValue(100)

        # Color map selection
        self.l_cmap = QLabel("Color Map ")
        self.cmap = sorted(get_colormaps().keys())
        self.combo = QComboBox(self)
        self.combo.addItems(self.cmap)
        self.combo.setCurrentIndex(5)

    def create_info_section(self):
        """Create guidelines section"""
        self.l_info_placeholder = QLabel("")
        self.l_info_placeholder.setStyleSheet("font-size: 40px;")
        self.l_info_title = QLabel("Guidelines")
        self.l_info_title.setStyleSheet("font-size: 20px;")
        
        info_text = ("You must use the following variables in your equation:\n"
                    "X, Y, a, b, c\nOther variables are not allowed.\n\n"
                    "You can use the following np calculations in your formula:\n"
                    "np.sqrt(), np.exp(), np.log(), np.abs(), np.pi(), np.e()\n"
                    "np.arctan(), np.arcsin(), np.arccos(), np.arccosh(), np.arcsinh(), \n"
                    "np.arctanh(), np.sinh(), np.cosh(), np.tanh(), np.sin(), np.cos(), np.tan()\n\n"
                    "Example functions are available to show you the possibilities.")
        
        self.l_info = QLabel(info_text)
        self.l_info.setStyleSheet("border: 1px solid black;")

    def setup_layout(self):
        """Position widgets in the layout"""
        gbox = QGridLayout()
        # Set modern margins and spacing
        gbox.setContentsMargins(15, 15, 15, 15)
        gbox.setSpacing(10)
        
        # Function section
        gbox.addWidget(self.l_function_title, 1, 0, 1, 2)
        gbox.addWidget(self.change_function_button, 2, 0, 1, 2)
        gbox.addWidget(self.l_function_label, 3, 0)
        gbox.addWidget(self.function_input, 4, 0)
        gbox.addWidget(self.l_function_refresher, 4, 1)
        gbox.addWidget(self.info_label, 5, 0, 1, 2)

        # Scaling section
        gbox.addWidget(self.l_scaling_placeholder, 6, 0, 1, 2)
        gbox.addWidget(self.l_scaling_title, 7, 0, 1, 2)
        gbox.addWidget(self.scaling_rule_a, 9, 0)
        gbox.addWidget(self.scaling_speed_a, 9, 1)
        gbox.addWidget(self.scaling_rule_b, 10, 0)
        gbox.addWidget(self.scaling_speed_b, 10, 1)
        gbox.addWidget(self.scaling_rule_c, 11, 0)
        gbox.addWidget(self.scaling_speed_c, 11, 1)

        # Limits section
        gbox.addWidget(self.l_limits_placeholder, 12, 0, 1, 2)
        gbox.addWidget(self.l_limits_title, 13, 0, 1, 2)
        gbox.addWidget(self.l_x_limits, 14, 0)
        gbox.addWidget(self.x_limits, 14, 1)
        gbox.addWidget(self.l_y_limits, 15, 0)
        gbox.addWidget(self.y_limits, 15, 1)
        gbox.addWidget(self.l_grid_points, 16, 0, 1, 2)
        gbox.addWidget(self.grid_points, 16, 1)
        gbox.addWidget(self.l_cmap, 17, 0)
        gbox.addWidget(self.combo, 17, 1)

        # Info section
        gbox.addWidget(self.l_info_placeholder, 18, 0, 1, 2)
        gbox.addWidget(self.l_info_title, 19, 0, 1, 2)
        gbox.addWidget(self.l_info, 20, 0, 1, 2)

        vbox = QVBoxLayout()
        vbox.addLayout(gbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

    def change_color(self):
        if self.main_window:
            self.main_window.change_color()
    
    def change_function(self):
        if self.main_window:
            self.main_window.change_function()

    def pick_example_function(self):
        if self.main_window:
            self.function_input.setText(EXAMPLE_FUNCTIONS[np.random.randint(len(EXAMPLE_FUNCTIONS))])
            # Check if the randomly picked example function is already displayed
            while self.function_input.text() == self.main_window.plotter.function_input:
                self.function_input.setText(EXAMPLE_FUNCTIONS[np.random.randint(len(EXAMPLE_FUNCTIONS))])
            
            self.main_window.change_function()

class FunctionPlotterUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Setup splitter for UI sections
        splitter = QSplitter(Qt.Orientation.Horizontal)
        self.setCentralWidget(splitter)

        # Setup object widget (controls panel)
        self.props = ObjectWidget(self, main_window=self)
        splitter.addWidget(self.props)

        # Setup canvas for 3D visualization
        self.canvas = scene.SceneCanvas(keys='interactive', show=True)
        self.view = self.canvas.central_widget.add_view()
        self.view.camera = 'turntable'
        self.view.camera.fov = FOV
        self.view.camera.distance = CAMERA_DISTANCE

        # Add the canvas to the splitter
        splitter.addWidget(self.canvas.native)

        # Create the plotter that handles the 3D function
        self.plotter = FunctionPlotter(self.view, self.props)
        
        # Connect UI signals
        self.connect_signals()

    def connect_signals(self):
        """Connect UI controls to update methods"""
        self.props.x_limits.valueChanged.connect(self.update_x_limits)
        self.props.y_limits.valueChanged.connect(self.update_y_limits)
        self.props.grid_points.valueChanged.connect(self.update_grid_points)
        self.props.combo.currentIndexChanged.connect(self.update_colormap)

    def update_x_limits(self):
        self.plotter.update_x_limits(self.props.x_limits.value())
        
    def update_y_limits(self):
        self.plotter.update_y_limits(self.props.y_limits.value())
        
    def update_grid_points(self):
        self.plotter.update_grid_points(self.props.grid_points.value())
        
    def update_colormap(self):
        self.plotter.update_colormap(self.props.combo.currentText())
        
    def change_function(self):
        """Validate and update the function"""
        function_input = self.props.function_input.text()
        
        # Validate function input
        valid, error_message = self.validate_function_input(function_input)
        if not valid:
            self.props.info_label.setText(error_message)
            return
        
        # Clear error message and update function
        self.props.info_label.setText("")
        self.plotter.update_function(function_input)
        
    def validate_function_input(self, function_input):
        """Validate if the function input contains required variables and no illegal ones"""
        # Filter out allowed special functions
        filtered_input = function_input
        for func in ALLOWED_CALCULATIONS:
            filtered_input = filtered_input.replace(func, "")
            
        # Check for required variables
        for var in ['X', 'Y', 'a', 'b', 'c']:
            if var not in filtered_input:
                return False, f"The function input must contain X, Y, a, b, c. You are missing {var}."
                
        # Check for illegal variables
        illegal_chars = [char for char in filtered_input if char.isalpha() and char not in ['X', 'Y', 'a', 'b', 'c']]
        if illegal_chars:
            return False, f"The function input contains other variables than X, Y, a, b, c. Remove the character {illegal_chars[0]}."
            
        return True, ""
