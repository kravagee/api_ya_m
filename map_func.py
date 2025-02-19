import requests

def scale(now_spn, now_ll, change=False, dir=None):
    if change:
        if dir == 'p_up':
            now_spn = [str(float(now_spn[0]) - 0.001), str(float(now_spn[1]) - 0.001)]
        elif dir == 'p_down':
            now_spn = [str(float(now_spn[0]) + 0.001), str(float(now_spn[1]) + 0.001)]
        elif dir == 'up':
            now_ll = [now_ll[0], str(float(now_ll[1]) + 0.01)]
        elif dir == 'down':
            now_ll = [now_ll[0], str(float(now_ll[1]) - 0.01)]
        elif dir == 'right':
            now_ll = [str(float(now_ll[0]) + 0.01), now_ll[1]]
        elif dir == 'left':
            now_ll = [str(float(now_ll[0]) - 0.01), now_ll[1]]
    map_params = {'spn': ','.join(now_spn),
                  'll': ','.join(now_ll),
                  'apikey': 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'}

    map_api_server = "https://static-maps.yandex.ru/v1"
    response = requests.get(map_api_server, params=map_params)
    im = response.content
    with open('map.png', 'wb') as f:
        f.write(im)
    return ('map.png', now_spn, now_ll)