import toml
from pathlib import Path

# Get the directory of the root dir where pyproject.toml lives
module_dir = Path(__file__).parent.parent

# Load the pyproject.toml file
pyproject_path = module_dir / "pyproject.toml"
if not pyproject_path.exists():
    raise FileNotFoundError(f"Could not find pyproject.toml at {pyproject_path}")

with pyproject_path.open("r") as f:
    pyproject_data = toml.load(f)

# Extract the version information
version = pyproject_data["project"]["version"]

__app_name__ = "FP-Bio Dash DF Plot"
__version__ = version
