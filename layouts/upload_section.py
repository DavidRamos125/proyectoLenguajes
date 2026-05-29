from dash import html, dcc


def upload_section():
    return html.Div([
        dcc.Upload(
            id='upload-image',
            children=html.Div([
                html.Div("Subir imagen", className="upload-title"),
                html.Div("Arrastra una foto o haz clic para seleccionarla", className="upload-subtitle")
            ], className="upload-content"),
            className="upload-zone"
        )
    ], className="upload-panel")
