from dash import Dash

from layouts.main_layout import create_layout

from callbacks.callbacks import register_callbacks

app = Dash(__name__)

app.layout = create_layout()
register_callbacks(app)

if __name__ == "__main__":
    app.run(debug=True, port=9091)