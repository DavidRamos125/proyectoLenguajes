from dash import html


def results_section():
    return html.Div([
        html.Div([
            html.P("Lectura OCR", className="eyebrow"),
            html.H2("Resultados"),
        ], className="card-heading"),

        html.Div([
            html.Div("Placa y origen", className="metric-label"),
            html.Div(id='plate-core', className="metric-value primary")
        ], className="metric-card"),

        html.Div([
            html.Div("Colores dominantes", className="metric-label"),
            html.Div(id='plate-color', className="metric-value")
        ], className="metric-card"),

        html.Div([
            html.Div("Tipo detectado", className="metric-label"),
            html.Div(id='color-type', className="metric-value")
        ], className="metric-card"),

        html.Div(id='plate-confidence', className="metric-note")
    ], className="results-card")
