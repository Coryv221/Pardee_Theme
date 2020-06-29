----
TITLE
Pardee_Theme
----
DESCRIPTION
Package used internally at the Pardee Center to create a consistent and recognizable theme for visualizations and data presentations
----
VERSION
version 1.0
Note: Early Production - Frequent Updates Expected
----
AUTHOR
Created by Cory Vandenberg for use by the Pardee Center for International Futures
Contact at: cory.vandenberg@du.edu
----
USAGE
Standardized package for consistency for the following aspects of visualizations:
	Fonts
	Backgrounds
	Data Colors
	Tick Markers
Expected to be used with seaborn
	Not tested or designed for other visualization packages on Python
----
INCLUDED FILES
1. color_palletes.py
2. style_dictionaries.py
3. test_packages.py
4. example.py
----
COLOR PALLETES
Accessed through color_palletes.py
Contains functions for calling all primary color palletes for visualizations
	all functions act as getters, allows for ease of import of color palletes
Contains functions for calling individual, primary DU colors
	all functions act as getters, allows for ease of import of individual colors
	For all academic journal or CMS visualizations, use the grayscale_color_pallete()
----
STYLE DICTIONARIES
Accessed through style_dictionaries.py
Contains two style dictionaries "standard_style" and "grayscale_style"
	For all internal and report visualizations, use the standard_style
	For all academic journal or CMS visualizations, use the grayscale_style
----
TEST PACKAGES
Accessed through test_packages.py
Contains functions for testing all color pallets with a standardized sin graph
This package assures that the package has downloaded and pip installed correctly
If error occurs, please send a bug report to cory.vandenberg@du.edu
----
EXAMPLE
Contains usage of all included files in the package
	proper import naming
	proper argument inputs
	useage with a dataset (COLT_data)
	typical dependencies and imports when working with Pardee_Theme
	will execute the test_packages.py
----
HOW TO INSTALL
1. Download the package as a zip
2. Unzip to any folder of your choice (This folder MUST ONLY CONTAIN FILES FROM THIS PACKAGE)
3. Open any python command console, or the windows command console (if using windows command console, put "python3" before any commands
4. run the following line of code in your command prompt:
	pip install directory_to_folder_containing_package
	Make sure to put the directory in quotes
5. The following final line of code should be output:
	"Successfully installed pardeevis-0.0.1"
6. You now have the full visualization package for creating "Pardee Style" data visualizations!



