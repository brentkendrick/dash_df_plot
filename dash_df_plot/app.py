import uuid

import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from dash import Dash, dcc, html

from dash_df_plot.config.settings import ASSETS_PATH

# from flask import Flask
from dash_df_plot.utils import __version__
from dash_df_plot.ids import ids

# import warnings
# from redis import Redis

# This must come before importing any components that use Redis
# so that the REDIS_URL is loaded from .env
# from .config.settings import REDIS_URL  # isort:skip


# def check_redis():
#     """Run a check on redis connection."""
#     r = Redis.from_url(REDIS_URL)

#     try:
#         r.ping()
#         print("Redis connection active!")
#     except Exception:
#         # Without a broker and backend, no celery
#         warnings.warn(
#             "Redis connection failed: No redis storage.",
#             category=RuntimeWarning,
#         )


# check_redis()

# *** CREATE APP ***
# Sample data

# print("Assets path: ", ASSETS_PATH)
df = pd.DataFrame(
    {
        "Fruit": ["Apples", "Oranges", "Bananas", "Grapes"],
        "Amount": [4, 1, 2, 5],
        "City": ["SF", "SF", "NYC", "NYC"],
    }
)

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")


def create_app(dash_url):
    """Using Factory Pattern to instantiate app.  Since we want relative imports to work
    a run.py in the project root is implemented.
    """
    # server = Flask(__name__)

    app = Dash(
        # server=server,  # type: ignore
        url_base_pathname=dash_url,
        assets_folder=ASSETS_PATH,
        external_stylesheets=[
            dbc.themes.SPACELAB,
            "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css",
        ],
    )

    # session_id = str(uuid.uuid4())
    # reset_df_stores(session_id)

    app.layout = html.Div(
        [
            html.H1(children="Hello Dash"),
            html.Div(children=f"A simple web app with Dash. Version: {__version__}"),
            dcc.Graph(id="example-graph", figure=fig),
        ],
        className="grid-container",
        id=ids.grid_container.id(),
    )

    return app


app = create_app("/fptrace/")

if __name__ == "__main__":
    app.run(debug=False)
