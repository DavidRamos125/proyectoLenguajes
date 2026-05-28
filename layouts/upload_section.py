from dash import html, dcc

def upload_section():

    return html.Div([

        dcc.Upload(
            id='upload-image',
            children=html.Button('Subir Imagen')
        )

    ])