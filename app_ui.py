import numpy as np
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QVBoxLayout, QPushButton, QWidget, QSplitter, QLabel,
                           QSpinBox, QComboBox, QGridLayout, QLineEdit, QHBoxLayout, QCheckBox)
from vispy import scene
from vispy.color.colormap import get_colormaps

import app_config
from logic import FunctionPlotter

class ObjectWidget(QWidget):
    def __init__(self, parent=None, main_window=None):
        super(ObjectWidget, self).__init__(parent)
        self.main_window = main_window
        
        # Added global stylesheet for modern, polished look
        self.setStyleSheet(app_config.STYLE_SHEET)
        
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
        self.function_input = QLineEdit(app_config.START_FUNCTION)
        self.function_input.setReadOnly(False)
        
        self.l_function_refresher = QPushButton("Refresh")
        self.l_function_refresher.clicked.connect(self.change_function)

        self.info_label = QLabel("")
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.info_label.setStyleSheet("color: red")

        # Add a small collapse button for hiding settings (will be placed at bottom)
        self.collapse_button = QPushButton("<")
        self.collapse_button.setFlat(True)
        self.collapse_button.setFixedWidth(30)
        self.collapse_button.setToolTip("Hide settings")
        self.collapse_button.clicked.connect(self.minimize_settings)
        # Label shown next to the button
        self.l_hide_settings = QLabel("Hide Settings")

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
        
        self.scaling_speed_a = QComboBox(self)
        self.scaling_speed_a.addItems(app_config.SPEED_OPTIONS)
        self.scaling_speed_a.setCurrentIndex(4)
        
        self.scaling_speed_b = QComboBox(self)
        self.scaling_speed_b.addItems(app_config.SPEED_OPTIONS)
        self.scaling_speed_b.setCurrentIndex(4)
        
        self.scaling_speed_c = QComboBox(self)
        self.scaling_speed_c.addItems(app_config.SPEED_OPTIONS)
        self.scaling_speed_c.setCurrentIndex(4)

    def create_limits_section(self):
        """Create grid limits and color map section"""
        self.l_limits_placeholder = QLabel("")
        self.l_limits_placeholder.setStyleSheet("font-size: 40px;")
        self.l_limits_title = QLabel("Grid Limits and Color Map")
        self.l_limits_title.setStyleSheet("font-size: 20px;")

        # X limits
        self.l_x_limits = QLabel("X Limits (between 1 and 100)")
        self.x_limits = QSpinBox()
        self.x_limits.setMinimum(1)
        self.x_limits.setMaximum(100)
        self.x_limits.setValue(2)

        # Y limits
        self.l_y_limits = QLabel("Y Limits (between 1 and 100)")
        self.y_limits = QSpinBox()
        self.y_limits.setMinimum(1)
        self.y_limits.setMaximum(100)
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
        self.cmap = [c for c in self.cmap if c in app_config.ALLOWED_COLORMAPS] # filter out incompatible colormaps
        self.combo = QComboBox(self)
        self.combo.addItems(self.cmap)
        # define default color map
        self.combo.setCurrentText(app_config.DEFAULT_CMAP)

    def create_info_section(self):
        """Create guidelines section"""
        self.l_info_placeholder = QLabel("")
        self.l_info_placeholder.setStyleSheet("font-size: 40px;")
        self.l_info_title = QLabel("Guidelines")
        self.l_info_title.setStyleSheet("font-size: 20px;")
        
        self.l_info = QLabel(app_config.INFO_TEXT)
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
        gbox.addWidget(self.l_grid_points, 16, 0)
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

        # Bottom bar with "Hide Settings" label and the collapse button
        bottom_bar = QHBoxLayout()
        bottom_bar.setContentsMargins(15, 0, 15, 15)

        # Show FPS toggle
        self.show_fps_checkbox = QCheckBox("Show FPS")
        self.show_fps_checkbox.setChecked(True)
        self.show_fps_checkbox.setToolTip("Toggle FPS display on the canvas")

        # Reordered: left align checkbox, right align hide controls
        bottom_bar.addWidget(self.show_fps_checkbox)
        bottom_bar.addStretch(1)
        bottom_bar.addWidget(self.l_hide_settings)
        bottom_bar.addWidget(self.collapse_button)
        vbox.addLayout(bottom_bar)

        self.setLayout(vbox)

    def minimize_settings(self):
        if self.main_window:
            self.main_window.minimize_settings()

    def change_color(self):
        if self.main_window:
            self.main_window.change_color()
    
    def change_function(self):
        if self.main_window:
            self.main_window.change_function()

    def pick_example_function(self):
        if self.main_window:
            self.function_input.setText(app_config.EXAMPLE_FUNCTIONS[np.random.randint(len(app_config.EXAMPLE_FUNCTIONS))])
            # Check if the randomly picked example function is already displayed
            while self.function_input.text() == self.main_window.plotter.function_input:
                self.function_input.setText(app_config.EXAMPLE_FUNCTIONS[np.random.randint(len(app_config.EXAMPLE_FUNCTIONS))])
            
            self.main_window.change_function()

class FunctionPlotterUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Setup splitter for UI sections
        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        self.setCentralWidget(self.splitter)

        # A thin restore handle on the far left (hidden by default)
        self.restore_handle = QWidget()
        self.restore_handle.setFixedWidth(35)  # widen to accommodate styled button
        rh_layout = QVBoxLayout(self.restore_handle)
        rh_layout.setContentsMargins(3, 0, 0, 0)
        rh_layout.addStretch()
        self.restore_button = QPushButton(">")
        self.restore_button.setFlat(False)     # use styled QPushButton (blue bg, white text)
        self.restore_button.setFixedSize(30, 26)
        self.restore_button.setToolTip("Show settings")
        self.restore_button.clicked.connect(self.restore_settings)
        rh_layout.addWidget(self.restore_button, alignment=Qt.AlignmentFlag.AlignHCenter)
        rh_layout.addStretch()
        self.restore_handle.setVisible(False)

        # Setup object widget (controls panel)
        self.props = ObjectWidget(self, main_window=self)

        # Setup canvas for 3D visualization
        self.canvas = scene.SceneCanvas(keys='interactive', show=True)
        self.view = self.canvas.central_widget.add_view()
        self.view.camera = 'turntable'
        self.view.camera.fov = app_config.FOV
        self.view.camera.distance = app_config.CAMERA_DISTANCE

        # Add widgets to the splitter in order: [restore handle | settings | canvas]
        self.splitter.addWidget(self.restore_handle)
        self.splitter.addWidget(self.props)
        self.splitter.addWidget(self.canvas.native)

        # Create the plotter that handles the 3D function
        self.plotter = FunctionPlotter(self.view, self.props)
        
        # Connect UI signals
        self.connect_signals()

        # Ensure initial FPS state matches checkbox
        self.plotter.set_show_fps(self.props.show_fps_checkbox.isChecked())

        # Optional: initial proportions
        self.splitter.setSizes([0, 380, 1000])

    def connect_signals(self):
        """Connect UI controls to update methods"""
        self.props.x_limits.valueChanged.connect(self.update_x_limits)
        self.props.y_limits.valueChanged.connect(self.update_y_limits)
        self.props.grid_points.valueChanged.connect(self.update_grid_points)
        self.props.combo.currentIndexChanged.connect(self.update_colormap)
        # connect FPS toggle
        self.props.show_fps_checkbox.toggled.connect(self.update_show_fps)

    # Add the two missing methods to control the collapse/restore behavior
    def minimize_settings(self):
        # Hide the settings pane, show the left restore handle, give the rest to the canvas
        self.props.setVisible(False)
        self.restore_handle.setVisible(True)
        handle_w = max(1, self.restore_handle.width() or 20)
        self.splitter.setSizes([handle_w, 0, max(1, self.width() - handle_w)])

    def restore_settings(self):
        # Show the settings pane again and hide the left handle
        self.restore_handle.setVisible(False)
        self.props.setVisible(True)
        props_w = 380
        self.splitter.setSizes([0, props_w, max(1, self.width() - props_w)])

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
        
    # forward checkbox state to plotter
    def update_show_fps(self, checked=None):
        self.plotter.set_show_fps(self.props.show_fps_checkbox.isChecked())

    def validate_function_input(self, function_input):
        """Validate if the function input contains required variables and no illegal ones"""
        # Filter out allowed special functions
        filtered_input = function_input
        for func in app_config.ALLOWED_CALCULATIONS:
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
        return True, ""
