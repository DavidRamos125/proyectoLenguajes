from dash import html


def image_section():
    return html.Div([
        html.Div([
            html.H2("Analisis visual"),
            html.P("Imagen original, deteccion del modelo, recorte y lectura en escala de grises.")
        ], className="section-heading"),

        html.Div([
            html.Figure([
                html.Img(id='original-image'),
                html.Figcaption("Original")
            ], className="image-card"),
            html.Figure([
                html.Img(id='yolo-image'),
                html.Figcaption("Deteccion")
            ], className="image-card"),
            html.Figure([
                html.Img(id='crop-image'),
                html.Figcaption("Recorte")
            ], className="image-card"),
            html.Figure([
                html.Img(id='grayscale-image'),
                html.Figcaption("Escala de grises")
            ], className="image-card"),
        ], className="image-grid")
    ], className="visual-section")
