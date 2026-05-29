from dash import html
import dash_leaflet as dl


def map_section():
    return html.Div([
        html.Div([
            html.P("Ubicacion estimada", className="eyebrow"),
            html.H2("Mapa"),
        ], className="card-heading"),

        dl.Map(
            id="municipio-map",
            center=[4.5709, -74.2973],
            zoom=6,
            children=[
                dl.TileLayer(),
                dl.Marker(
                    id="municipio-marker",
                    position=[4.5709, -74.2973]
                )
            ],
            style={
                "width": "100%",
                "height": "360px"
            }
        )
    ], className="map-card")
