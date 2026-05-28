from dash import html
import dash_leaflet as dl


def map_section():

    return html.Div([

        html.H2("Mapa"),

        dl.Map(

            id="municipio-map",

            center=[4.5709, -74.2973],  # Colombia

            zoom=6,

            children=[

                # Fondo del mapa
                dl.TileLayer(),

                # Marcador dinámico
                dl.Marker(

                    id="municipio-marker",

                    position=[4.5709, -74.2973]
                )
            ],

            style={
                "width": "50%",
                "height": "250px",
                "marginTop": "20px"
            }
        )
    ])
