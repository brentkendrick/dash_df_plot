import uuid

import dash_bootstrap_components as dbc
from dash import Dash, dcc, html
from flask import Flask

# This must come before importing any components that use Redis
# so that the REDIS_URL is loaded from .env
from dash_df_plot.config.settings import (  # isort:skip
    ASSETS_PATH,
    DASHURLS,
)


# *** CREATE APP ***


def create_app():
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
            dcc.Store(data=session_id, id="session-id"),
            trace_file_upload_layout,
            controls,
            main_graph_container,
            html.Div(
                [
                    output_tables,
                    primary_exporter,
                ],
                className="bottom-row",
            ),
        ],
        className="grid-container",
        id=ids.grid_container.id(),
    )

    sphinx.render(server, url_base)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
