import time
import json
import urllib.request


def download_as_json(url):
    response = urllib.request.urlopen(url)
    text = response.read().decode('utf-8')
    return json.loads(text)


def updateLight(traffic_light):
    try:
        stamp_url = "https://api-maps.yandex.ru/services/coverage/v2/layers_stamps?lang=ru_RU&l=trf"
        stamp_data = download_as_json(stamp_url)
        stamp = stamp_data["trf"]["version"]
        print(stamp)
        url = 'https://jgo.maps.yandex.net/description/traffic-light?lang=ru_RU&ids=47&tm={}'.format(stamp)
        print(url)
        data = download_as_json(url)
        level = data["data"]["features"][0]["properties"]["JamsMetaData"]["level"]
        print("level=", level)
        if level < 4:
            traffic_light.set_constant(traffic_light.GREEN, True)
            traffic_light.set_constant(traffic_light.YELLOW, False)
            traffic_light.set_constant(traffic_light.RED, False)
        elif level < 7:
            traffic_light.set_constant(traffic_light.GREEN, False)
            traffic_light.set_constant(traffic_light.YELLOW, True)
            traffic_light.set_constant(traffic_light.RED, False)
        else:
            traffic_light.set_constant(traffic_light.GREEN, False)
            traffic_light.set_constant(traffic_light.YELLOW, False)
            traffic_light.set_constant(traffic_light.RED, True)
    except Exception as e:
        print("error", e)
        traffic_light.set_constant(traffic_light.GREEN, False)
        traffic_light.set_periodic(traffic_light.YELLOW, [4, 4])
        traffic_light.set_constant(traffic_light.RED, False)



