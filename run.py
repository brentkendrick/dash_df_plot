from dash_df_plot.app import create_app

app = create_app()  # Create the Dash app
server = app.server  # Expose the Flask server

if __name__ == "__main__":
    app.run(debug=True)
