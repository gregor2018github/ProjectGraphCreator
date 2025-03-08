import numpy as np
from vispy import app
from vispy.scene import visuals
from vispy.color.colormap import get_colormap

class FunctionPlotter:
    def __init__(self, view, props):
        """Initialize the function plotter with view and UI properties"""
        self.view = view
        self.props = props
        
        # Initialize parameters
        self.time = 0
        self.a = 1
        self.b = 1
        self.c = 0
        self.function_input = self.props.function_input.text()
        
        # Initialize plot settings
        self.GRID_POINTS = self.props.grid_points.value()
        self.X_LIMITS = (self.props.x_limits.value() * -1, self.props.x_limits.value())
        self.Y_LIMITS = (self.props.y_limits.value() * -1, self.props.y_limits.value())
        
        # Initialize colormap
        self.cm = get_colormap(self.props.combo.currentText())
        
        # Create initial data and surface
        self.X, self.Y, self.Z = self.create_function(self.a, self.b, self.c)
        self.setup_surface_plot()
        self.setup_timer()
        
    def setup_surface_plot(self):
        """Setup the surface plot visualization"""
        self.surface = visuals.SurfacePlot(x=self.X, y=self.Y, z=self.Z, shading='smooth')
        self.view.add(self.surface)
        
    def setup_timer(self):
        """Setup the timer for updating the plot"""
        self.timer = app.Timer(connect=self.update, interval='auto')
        self.timer.start()
        
    def create_function(self, a, b, c):
        """Generate data for the 3D function"""
        x = np.linspace(*self.X_LIMITS, self.GRID_POINTS)
        y = np.linspace(*self.Y_LIMITS, self.GRID_POINTS)
        X, Y = np.meshgrid(x, y)

        # Evaluate the function
        context = {'X': X, 'Y': Y, 'a': a, 'b': b, 'c': c, 'np': np}
        try:
            Z = eval(self.function_input, context)
        except Exception as e:
            print(f"Error during create_function: {e}")
            Z = np.zeros_like(X)
        return X, Y, Z
        
    def plot_function(self, X, Y, Z):
        """Update the surface plot with new data"""
        try:
            # Normalize Z values for colormap if there's a range
            if Z.max() != Z.min():
                norm_Z = (Z - Z.min()) / (Z.max() - Z.min())
            else:
                norm_Z = np.zeros_like(Z)
                
            colors = self.cm.map(norm_Z)

            # Update the mesh data
            self.surface.mesh_data.set_vertices(np.column_stack([X.ravel(), Y.ravel(), Z.ravel()]))
            self.surface.set_data(z=Z, x=X, y=Y, colors=colors)
        except Exception as e:
            print(f"Error during plot_function: {e}")
    
    def update_function(self, new_function):
        """Change the function definition"""
        self.function_input = new_function
        self.X, self.Y, self.Z = self.create_function(self.a, self.b, self.c)
        self.plot_function(self.X, self.Y, self.Z)
    
    def update_x_limits(self, value):
        """Update X axis limits"""
        self.X_LIMITS = (value * -1, value)
        self.update_plot()
    
    def update_y_limits(self, value):
        """Update Y axis limits"""
        self.Y_LIMITS = (value * -1, value)
        self.update_plot()
    
    def update_grid_points(self, value):
        """Update grid resolution"""
        self.GRID_POINTS = value
        self.update_plot()
    
    def update_colormap(self, colormap_name):
        """Update the colormap"""
        self.cm = get_colormap(colormap_name)
        self.update_plot()
    
    def update_plot(self):
        """Regenerate the function plot with current parameters"""
        self.X, self.Y, self.Z = self.create_function(self.a, self.b, self.c)
        self.plot_function(self.X, self.Y, self.Z)
    
    def update(self, event):
        """Update the function coefficients and replot."""
        try:
            self.time += event.dt
            self.update_parameters()
            self.X, self.Y, self.Z = self.create_function(self.a, self.b, self.c)
            self.plot_function(self.X, self.Y, self.Z)
        except Exception as e:
            print(f"Error during update: {e}")
    
    def update_parameters(self):
        """Update a, b, c parameters based on scaling rules"""
        # Get speed percentages from UI
        speed_percent_a = int(self.props.scaling_speed_a.currentText().split()[-2]) / 100
        speed_percent_b = int(self.props.scaling_speed_b.currentText().split()[-2]) / 100
        speed_percent_c = int(self.props.scaling_speed_c.currentText().split()[-2]) / 100
        
        # Update parameter a
        rule_a = self.props.scaling_rule_a.currentIndex()
        if rule_a == 0:  # sin(t)
            self.a = np.sin(self.time * speed_percent_a)
        elif rule_a == 1:  # cos(t)
            self.a = np.cos(self.time * speed_percent_a)
        elif rule_a == 2:  # tan(t)
            self.a = np.tan(self.time * speed_percent_a)
        else:  # static
            self.a = 1
            
        # Update parameter b
        rule_b = self.props.scaling_rule_b.currentIndex()
        if rule_b == 0:  # sin(t)
            self.b = np.sin(self.time * speed_percent_b)
        elif rule_b == 1:  # cos(t)
            self.b = np.cos(self.time * speed_percent_b)
        elif rule_b == 2:  # tan(t)
            self.b = np.tan(self.time * speed_percent_b)
        else:  # static
            self.b = 1
            
        # Update parameter c
        rule_c = self.props.scaling_rule_c.currentIndex()
        if rule_c == 0:  # sin(t)
            self.c = np.sin(self.time * speed_percent_c)
        elif rule_c == 1:  # cos(t)
            self.c = np.cos(self.time * speed_percent_c)
        elif rule_c == 2:  # tan(t)
            self.c = np.tan(self.time * speed_percent_c)
        else:  # static
            self.c = 1
