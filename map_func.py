import requests
from PIL import Image
from io import BytesIO


def scale():
    map_params = {'spn': ','.join(['123.21312', '123.43623']),
                  'll': ','.join(['122.1256', '24.2412']),
                  'apikey': 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'}

    map_api_server = "https://static-maps.yandex.ru/v1"
    response = requests.get(map_api_server, params=map_params)
    im = BytesIO(response.content)
    opened_image = Image.open(im)
    return opened_image