# Gets redis running before importing create_app
# from dash_df_plot.config.settings import REDIS_URL  # isort:skip

from dash_df_plot.app import create_app

app = create_app("/fptrace/")  # Create the Dash app

server = app.server  # Expose the Flask server

if __name__ == "__main__":
    app.run(debug=True)
