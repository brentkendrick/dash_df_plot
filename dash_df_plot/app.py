# This must come before importing any components that use Redis
# so that the REDIS_URL is loaded from .env
from dash_df_plot.config.settings import (  # isort:skip
    ASSETS_PATH,
    DASHURLS,
)
import uuid

import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from dash import Dash, dcc, html
from flask import Flask
from .utils import reset_df_stores
from .ids import ids


# *** CREATE APP ***
# Sample data
df = pd.DataFrame(
    {
        "Fruit": ["Apples", "Oranges", "Bananas", "Grapes"],
        "Amount": [4, 1, 2, 5],
        "City": ["SF", "SF", "NYC", "NYC"],
    }
)

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")


def create_app():
    """Using Factory Pattern to instantiate app.  Since we want relative imports to work
    a run.py in the project root is implemented.
    """
    server = Flask(__name__)

    url_base = DASHURLS["fptrace"]

    app = Dash(
        server=server,  # type: ignore
        url_base_pathname=url_base,
        assets_folder=ASSETS_PATH,
        external_stylesheets=[
            dbc.themes.SPACELAB,
            "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css",
        ],
    )

    session_id = str(uuid.uuid4())
    reset_df_stores(session_id)

    app.layout = html.Div(
        [
            html.H1(children="Hello Dash"),
            html.Div(children="A simple web app with Dash."),
            dcc.Graph(id="example-graph", figure=fig),
        ],
        className="grid-container",
        id=ids.grid_container.id(),
    )

    return app
