from setuptools import setup, find_packages

setup(
    name="dash_df_plot",
    version="0.0.30",
    packages=find_packages(),
    include_package_data=True,  # Include package data from MANIFEST.in
    package_data={
        "dash_df_plot": ["pyproject.toml", "csv/*"],  # Specify files to include
    },
)
