import requests
from PIL import Image
from io import BytesIO

def scale(now_spn, change=False, dir=None):
    if change:
        if dir == 'up':
            now_spn = [str(float(now_spn[0]) - 0.001), str(float(now_spn[1]) - 0.001)]
        else:
            now_spn = [str(float(now_spn[0]) + 0.001), str(float(now_spn[1]) + 0.001)]
    map_params = {'spn': ','.join(now_spn),
                  'll': ','.join(['37.530887', '55.703118']),
                  'apikey': 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'}

    map_api_server = "https://static-maps.yandex.ru/v1"
    response = requests.get(map_api_server, params=map_params)
    im = response.content
    with open('map.png', 'wb') as f:
        f.write(im)
    return ('map.png', now_spn)