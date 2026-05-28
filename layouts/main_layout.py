from dash import html

from layouts.upload_section import upload_section
from layouts.image_section import image_section
from layouts.results_section import results_section
from layouts.map_section import map_section



def create_layout():

    return html.Div([

        html.H1("Detector de Placas"),

        upload_section(),

        image_section(),

        results_section(),

        map_section()
    ])