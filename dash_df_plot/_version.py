from pathlib import Path
import tomllib
import importlib.resources

# Access pyproject.toml as a resource
with importlib.resources.open_text("your_package_name", "pyproject.toml") as f:
    pyproject_content = f.read()

print(pyproject_content)

# Locate the directory where this module resides
module_dir = Path(__file__).parent

print("module_dir: ", module_dir)
# Construct the path to pyproject.toml relative to the module's directory
pyproject_path = module_dir / "pyproject.toml"

if not pyproject_path.exists():
    raise FileNotFoundError(f"pyproject.toml not found at {pyproject_path}")

with pyproject_path.open("rb") as pyproject_file:  # tomllib requires binary mode
    pyproject_data = tomllib.load(pyproject_file)
    # print(pyproject_data)
# Extract the version information
version = pyproject_data["project"]["version"]

__app_name__ = "FP-Bio Dash DF Plot"
__version__ = version
