from pathlib import Path
import tomllib

# Determine the path to pyproject.toml
current_file = Path(__file__).resolve()
project_root = current_file.parents[1]  # Go two levels up to the project root
pyproject_path = project_root / "pyproject.toml"

# Read and parse the pyproject.toml file
if pyproject_path.exists():
    with pyproject_path.open("rb") as pyproject_file:  # tomllib requires binary mode
        pyproject_data = tomllib.load(pyproject_file)
    # print(pyproject_data)
else:
    raise FileNotFoundError(f"pyproject.toml not found at {pyproject_path}")
# Extract the version information
version = pyproject_data["project"]["version"]

__app_name__ = "FP-Bio Dash DF Plot"
__version__ = version
