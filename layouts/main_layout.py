from dash import html

from layouts.upload_section import upload_section
from layouts.image_section import image_section
from layouts.results_section import results_section
from layouts.map_section import map_section


def create_layout():
    return html.Div([
        html.Div([
            html.Div([
                html.P("Vision artificial para placas colombianas", className="eyebrow"),
                html.H1("Detector de Placas"),
                html.P(
                    "Carga una imagen, revisa la deteccion de la placa y ubica el municipio "
                    "de origen en el mapa.",
                    className="hero-copy"
                ),
            ], className="hero-copy-wrap"),
            upload_section(),
        ], className="hero"),

        html.Main([
            image_section(),

            html.Div([
                results_section(),
                map_section()
            ], className="insights-grid")
        ], className="app-shell")
    ], className="page")
