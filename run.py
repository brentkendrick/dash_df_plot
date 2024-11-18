# This must come before importing any components that use Redis
# so that the REDIS_URL is loaded from .env
from dash_df_plot.config.settings import (  # isort:skip
    ASSETS_PATH,
    DASHURLS,
)
from dash_df_plot.app import create_app

app = create_app(DASHURLS["fptrace"])  # Create the Dash app

server = app.server  # Expose the Flask server

if __name__ == "__main__":
    app.run(debug=True)
