from setuptools import setup, find_packages

setup(
    name="dash_df_plot",
    version="0.0.27",
    packages=find_packages(),
    package_data={
        "dash_df_plot": ["pyproject.toml"],  # Include pyproject.toml in the package
    },
)
