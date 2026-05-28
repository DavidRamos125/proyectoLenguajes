from dash import html

def results_section():

    return html.Div([

        html.H2("Resultados"),

        html.Div(id='plate-core'),
        
        html.Div(id='plate-color'),
        
        html.Div(id='color-type'),

        html.Div(id='plate-confidence')

    ])