from dash import html

def image_section():

    return html.Div([

        html.Img(id='original-image'),

        html.Img(id='yolo-image'),

        html.Img(id='crop-image'),
        
        html.Img(id='grayscale-image')

    ])