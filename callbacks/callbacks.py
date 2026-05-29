from dash import Input, Output, no_update, html
import re

from services.ocr_service import OCRService
from services.yolo_service import YoloService
from services.colorService import ColorService
from services.grayScale import GrayScale
from services.municipioService import MunicipioMatcher
from utils.imgTobase64 import toBase64,toImg



def register_callbacks(app):
    yolo = YoloService()
    ocr =  OCRService()
    color = ColorService()
    grayScale = GrayScale()
    municipio = MunicipioMatcher()

    @app.callback(
        [
            Output('original-image', 'src'),
            Output('yolo-image', 'src'),
            Output('crop-image', 'src'),
            Output('plate-color', 'children'),
            Output('grayscale-image', 'src'),
            Output('plate-core', 'children'),
            Output('color-type', 'children'),
            Output('municipio-map', 'viewport'),
            Output('municipio-marker', 'position')
        ],

        Input('upload-image', 'contents')
    )
    def detect_plate(contents):
        if contents is None:

            return [
                no_update,
                no_update,
                no_update,
                no_update,
                no_update,
                no_update,
                no_update,
                no_update,
                no_update
            ]

        img = toImg(contents)

        yoloResults = yolo.detect(img)

        yoloImage = toBase64(
            yoloResults[0].plot()
        )

        box = yoloResults[0].boxes[0]
        x1, y1, x2, y2 = map(
            int,
            box.xyxy[0]
        )

        cropimg = img[y1:y2, x1:x2]

        cropBase64 = toBase64(cropimg)

        grayImage = grayScale.to_grayscale(
            cropimg
        )

        grayBase64 = toBase64(grayImage)

        colores = color.detect_dominant_colors(
            cropimg
        )
        colorType = color.detect_type(colores)


        text = ocr.read_text(grayImage)

        text = ocr.validate_plate(text)

        origin = ""

        match = re.search(
            r"ORIGEN:(.*)",
            text
        )
        if match:
            origin = match.group(1).strip()


        ubicacion = municipio.buscar(origin)
        ciudad = ubicacion["CIUDAD"].iloc[0] 
        departamento = ubicacion["DEPARTAMENTO"].iloc[0] 
        ubicacion_texto = f"{ciudad} - {departamento}"
        text = re.sub( r"ORIGEN:.*", f"ORIGEN: {ubicacion_texto}", text )
        

        lat = float(ubicacion["LAT"].iloc[0])
        lng = float(ubicacion["LNG"].iloc[0])

        coords = [lat, lng]
        zoom = 6
        if ciudad != "COLOMBIA": zoom = 12  

        return [

            contents,

            yoloImage,

            cropBase64,

            f"COLORES: {colores[0]['color'].upper()} ({colores[0]['percent']:.2f}%), "
            f"{colores[1]['color'].upper()} ({colores[1]['percent']:.2f}%)",

            grayBase64,
            text.upper(),

            f"TIPO POR COLOR: {colorType}",
            {
                "center": coords,
                "zoom": zoom
            },

            coords
        ]

