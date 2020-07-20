import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pardeeVisualizationPackage",
    version="0.1.0",
    author="Cory Vandenberg",
    author_email="cory.vandenberg@du.edu",
    description="Package for converting seaborn visualizations into Pardee Center Friendly Packages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Coryv221/Pardee_Theme",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)