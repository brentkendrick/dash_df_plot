from setuptools import setup, find_packages

setup(
    name="dash_df_plot",
    version="0.0.33",
    packages=find_packages(),
    include_package_data=True,  # Include package data from MANIFEST.in
    data_files=[("", ["pyproject.toml"])],  # Include at the package root
)
