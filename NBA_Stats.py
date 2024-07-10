from requests import get
from pprint import PrettyPrinter

BASE_URL="https://testbooru.donmai.us/posts/6.json"

printer=PrettyPrinter()
def api_init():
    global media_asset
    data=get(BASE_URL).json()
    media_asset=data['media_asset']

def getvarients():
    varients=media_asset['variants']
    hell=varients[0]['url']
    hell2=get(hell)
    return hell2

api_init()
variants=getvarients()
printer.pprint(variants)