----
TITLE
Pardee_Theme
----
DESCRIPTION
Package used internally at the Pardee Center to create a consistent and recognizable theme for visualizations and data presentations
----
VERSION
version 0.1
Note: Early Production - Likely Unstable - Frequent Updates Expected
----
AUTHOR
Created by Cory Vandenberg for use by the Pardee Center for International Futures
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
----
STYLE DICTIONARIES
Accessed through style_dictionaries.py
Contains one style dictionary "standard_style"
----
TEST PACKAGES
Accessed through test_packages.py
Contains functions for testing all color pallets with a standardized sin graph
----
EXAMPLE
Contains usage of all included files in the package
	proper import naming
	proper argument inputs
	useage with a dataset (COLT_data)
	typical dependencies and imports when working with Pardee_Theme


