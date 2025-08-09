# starting camera settings
FOV = 45
CAMERA_DISTANCE = 20
WINDOW_SIZE = (1500, 900)
WINDOW_POS = (100, 100)

# start function is preselected and will run when the program starts
START_FUNCTION = "a * X**2 + b * Y**2 + c"

# following functions are handpicked to showcase the functionality of the program
EXAMPLE_FUNCTIONS  = [  '(a * np.cos(np.pi * X) * np.cos(np.pi * Y) + b * np.sin(np.pi * X) * np.sin(np.pi * Y)) / (1 + c * np.sin(2 * np.pi * X) * np.sin(np.pi * Y))',
                        'a * (1 + Y * np.cos(np.pi * X)) * np.cos(2 * np.pi * X) + b * (1 + Y * np.cos(np.pi * X)) * np.sin(2 * np.pi * X) + c * Y * np.sin(np.pi * X)',
                        'a * (X**3 + Y**3) * np.log(np.abs(X * Y) + 1) + b * np.sin(X * Y) + c',
                        'a * (X**3 - 3*X*Y**2) + b * (3*X**2*Y - Y**3) + c',
                        'a * X**2 + b * Y**2 + c',
                        'a * X**2 + b * Y**33 + c',
                        'a * X**3 + b * Y**3 + c',
                        'a * np.arctan(X * Y) * np.tan(np.pi * X) + b * np.sinh(Y) * np.cos(X) + c',
                        'a * np.arctan(np.exp(X) * np.exp(Y)) + b * np.sin(X * Y) + c',
                        'a * np.cos(b * X) * np.cos(c * Y) + np.exp(-((X-0.5)**2 + (Y-0.5)**2) / (0.1 + a))',
                        'a * np.cos(X) + b * np.sin(Y) + c * np.sin(np.sqrt(X**2 + Y**2)) * np.log(np.abs(X * Y) + 1)',
                        'a * np.exp(-0.5 * (X**2 + Y**2)/2) * np.cos(b * np.sin(X**2 + Y**2)*3) + c',
                        'a * np.exp(-X**2 - Y**2) * np.tanh(X * Y) + b * np.arcsin(np.sin(np.pi * X) * np.sin(np.pi * Y)) + c',
                        'a * np.exp(np.sin(X) * np.cos(Y)) + b * (X**3 - 3*X*Y**2) + c',
                        'a * np.log(np.abs(np.sin(X) * np.cos(Y)) + 1) * np.exp(b * np.arctan(X * Y)) + c',
                        'a * np.log(np.abs(np.sin(X) * np.cos(Y)) + 1) * np.exp(b * np.arctan(X**2 * Y*3 + b * Y**3 + c))',
                        'a * np.arctan(X * Y) * np.tan(np.pi * b **2) + c',
                        'a * np.log(np.abs(np.sinh(X) * np.cosh(Y)) + 1) + b * np.sqrt(np.abs(X * Y)) + c',
                        'a * np.log(np.sqrt(X**2 + Y**2) + 1) * np.sin(b * np.arctan2(Y, X)) + c',
                        'a * np.sin(X) * np.sin(Y) + b * np.cos(X) * np.cos(Y) + c',
                        'a * np.sin(b * np.sqrt(X**2 + Y**2) +1) / (np.sqrt(X**2 + Y**2) +1) + c',
                        'a * np.sin(b * np.sqrt(X**2 + Y**2)) * np.cos(c * np.arctan2(Y, X))',
                        'a * np.sin(X * Y / b) * np.cos(np.sqrt(X**2 + Y**2)) + c * np.exp(b * np.sqrt(X**2 + Y**2)) * np.cos(c * np.arctan2(Y, X)) + np.exp(-0.1 * (X**2 + Y**2))',
                        'a * np.sin(np.log(np.abs(X) + 30) * np.cos(Y)) + b * np.cos(np.log(np.abs(Y) + 90) * np.sin(X)) +b * np.sqrt(X**2 + Y**2) +1 / (np.sqrt(X**2 + Y**2) +1) +  c',
                        'a * np.sin(np.pi * X) * np.cos(np.pi * Y) * np.exp(-np.abs(b) * (X**2 + 3 * Y**2)) + c * np.log(np.abs( 5 * X * Y) + 1)',
                        'a * np.sin(np.pi * X) * np.cosh(Y*c) + b * np.exp(-np.abs(X)) * np.cos(np.pi * Y *c)',
                        'a * np.sin(np.pi * X) * np.sin(np.pi * Y) + b * np.cos(np.pi * X) * np.cos(np.pi * Y) + c',
                        'a * np.sin(np.pi * X) * np.sqrt(np.abs(2 * np.pi * b * np.sqrt(X**2 + Y**2**c)))',
                        'a * np.sin(np.sqrt(X**2 + Y**2) + np.log(np.abs(X * Y) + 1)) + b * np.cosh(X * np.sqrt(np.abs(X**2 + Y**2 *c)))',
                        'a * np.sin(np.sqrt(np.abs(X**2 * b + Y**2 * c)) + np.log(np.abs(Y))) + c',
                        'a * np.sqrt(X**2 + Y**2) * np.sin(b * np.arctan2(Y, X) + c * np.sqrt(X**2 + Y**2)) * np.exp(-0.1 * np.sqrt(X**2 + Y**2))',
                        'np.exp(-(X**2 + Y**2) / (a + 0.1)) * np.cos(b * np.log(np.abs(X*Y) + 1)) + c * np.arctan(X*Y)',
                        'np.tanh(a * X) * np.cosh(b * Y) + c * np.sqrt(np.abs(np.sin(X*Y)))',
                        'np.log(np.abs(np.tan(a*X) + np.cos(b*Y)) + 1) * np.exp(c * np.arcsinh(X*Y))',
                        'np.arccos(np.sin(a*X*Y)) * np.arccosh(np.abs(b*X + c*Y) + 1) / (np.abs(X*Y) + 1)',
                        '(np.sin(a*X*Y) * np.cos(b*X**2 - c*Y**2)) / (1 + np.exp(-np.abs(X*Y)))',
                        'np.exp(np.cos(a*X) - np.sin(b*Y)) * np.tanh(c * np.sqrt(np.abs(X*Y)))',
                        'np.arctan(np.sinh(a*X*Y)) * np.cosh(b*np.sqrt(np.abs(X) + np.abs(Y))) + c*np.log(X**2 + Y**2 + 1)',
                        'np.exp(-((X-a)**2 + (Y-b)**2)) * np.cos(c * np.arctan2(Y,X) * np.sqrt(X**2 + Y**2))',
                        'np.log(np.abs(np.sinh(a*X) * np.cosh(b*Y)) + 1) * np.arctan(c * (X**2 - Y**2))',
                        'np.exp(-np.abs(X*Y)) * np.sin(a * np.arctan2(Y,X)) * np.cos(b * np.sqrt(X**2 + Y**2)) + c',
                        '(np.tanh(a*X) + np.cosh(b*Y)) * np.sin(c * np.log(np.abs(X*Y) + 1))',
                        'np.sqrt(np.abs(np.sin(a*X*Y))) * np.exp(-b*(X**2 + Y**2)) + c * np.arctan(X/Y)',
                        'np.exp(-(X**2 + Y**2)) * np.sin(a * 3 * np.arccos(np.sin(b*np.pi*X) * np.sin(c*np.pi*Y)))',
                        'np.arcsinh(a * np.sin(X*Y)) * np.arccosh(np.abs(b * np.cos(X-Y)) + 1) + c * np.exp(-np.abs(X*Y))',
                        'np.tanh(a * np.log(np.abs(X*Y) + 1)) * np.cos(b * np.arcsin(np.sin(np.pi*X) * np.sin(np.pi*Y))) + c * np.exp(-(X**2 + Y**2))',
                        'np.sin(a * np.arctan(X/Y)) * np.cos(b * np.sqrt(X**2 + Y**2)) * np.exp(-c * np.abs(X*Y))',
                        'np.exp(-np.abs(X*Y)) * np.sin(a * np.arcsinh(X+Y)) * np.cos(b * np.arccosh(np.abs(X-Y) + 1)) + c']

# following np functions are allowed to be written in the input line
ALLOWED_CALCULATIONS = ["np.arcsinh", "np.arccosh", "np.arctanh",
                        "np.arcsin", "np.arccos", "np.arctan", 
                        "np.sinh", "np.cosh", "np.tanh",
                        "np.sin", "np.cos", "np.tan",
                        "np.sqrt", "np.exp", "np.log", "np.abs", 
                        "np.pi", "np.e"]

STANDARD_COLOR = "#0078d7"
STANDARD_COLOR_DARK = "#005a9e"
STANDARD_BACKGROUND_COLOR = "#ebebeb"#f9f9f9

STYLE_SHEET = """
                 QWidget { 
                     background-color: #ebebeb; 
                     font-family: 'Segoe UI', sans-serif; 
                 }
                 /* Subtle section cards */
                 QFrame#sectionPanel {
                     background-color: #ffffff;
                     border: 1px solid #e5e5e5;
                     border-radius: 6px;
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
                 /* Keep shared styling for line edits and combo boxes */
                 QLineEdit, QComboBox { 
                     border: 1px solid #ccc; 
                     border-radius: 4px; 
                     padding: 4px; 
                 }
                 /* Ensure checkbox indicator is visible with stylesheet-based rendering */
                 QCheckBox {
                     color: #333333;
                     spacing: 8px;
                 }
                 QCheckBox::indicator {
                     width: 16px;
                     height: 16px;
                     border: 1px solid #666666;
                     border-radius: 3px;
                     background: #ffffff;
                 }
                 QCheckBox::indicator:hover {
                     border-color: #005a9e;
                 }
                 QCheckBox::indicator:checked {
                     background-color: #0078d7;  /* filled to indicate checked state */
                     border-color: #005a9e;
                 }
                 QCheckBox::indicator:disabled {
                     background: #eeeeee;
                     border-color: #aaaaaa;
                 }
                 QLabel { 
                     color: #333333; 
                     background-color: transparent;  /* ensure labels show white panel background */
                 }
              """

# dispayed in the UI
INFO_TEXT = ("You must use the following variables in your equation:\n"
             "X, Y, a, b, c\nOther variables are not allowed.\n\n"
             "You can use the following np calculations in your formula:\n"
             "np.sqrt(), np.exp(), np.log(), np.abs(), np.pi(), np.e()\n"
             "np.arctan(), np.arcsin(), np.arccos(), np.arccosh(), np.arcsinh(), \n"
             "np.arctanh(), np.sinh(), np.cosh(), np.tanh(), np.sin(), np.cos(), np.tan()\n\n"
             "Example functions are available to show you the possibilities.")

# Speed controls
SPEED_OPTIONS = ["Speed = 5 %", 
                 "Speed = 10 %", 
                 "Speed = 25 %", 
                 "Speed = 50 %", 
                 "Speed = 100 %", 
                 "Speed = 150 %", 
                 "Speed = 200 %"]

# Possible colormaps for the plot, some others are not compatible with the program
ALLOWED_COLORMAPS = ["GrBu",
                     "GrBu_d",
                     "PuGr",
                     "RdBu",
                     "RdYeBuCy",
                     "autumn",
                     "blues",
                     "cool",
                     "coolwarm",
                     "cubehelix",
                     "diverging",
                     "greens",
                     "hsl",
                     "husl",
                     "light_blues",
                     "orange",
                     "reds",
                     "single_hue",
                     "spring",
                     "summer",
                     "viridis"]

# Starting colormap
DEFAULT_CMAP = "viridis"
# Possible colormaps for the plot, some others are not compatible with the program
ALLOWED_COLORMAPS = ["GrBu",
                     "GrBu_d",
                     "PuGr",
                     "RdBu",
                     "RdYeBuCy",
                     "autumn",
                     "blues",
                     "cool",
                     "coolwarm",
                     "cubehelix",
                     "diverging",
                     "greens",
                     "hsl",
                     "husl",
                     "light_blues",
                     "orange",
                     "reds",
                     "spring",
                     "summer",
                     "viridis"]

# Starting colormap
DEFAULT_CMAP = "viridis"
