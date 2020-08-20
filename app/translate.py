import json
import requests
from flask_babel import _
from app import app

def translate(text, source_language, dest_language):
    if 'RAPI_TRANSLATOR_KEY' not in app.config or \
            not app.config['RAPI_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')

    url = "https://translated-mymemory---translation-memory.p.rapidapi.com/api/get"

    querystring = {"mt":"1","onlyprivate":"0","de":"blankclef.testing@gmail.com","langpair":f"{source_language}|{dest_language}","q":text}
    api_key = app.config["RAPI_TRANSLATOR_KEY"]
    headers = {
        'x-rapidapi-host': "translated-mymemory---translation-memory.p.rapidapi.com",
        'x-rapidapi-key': api_key
        }
    response = requests.request("GET", url, headers=headers, params=querystring)

    #print (response.text)

    #if response.status_code != 200:
    #    return _('Error: the translation service failed.')
    return json.loads(response.content.decode('utf-8-sig'))['responseData']['translatedText']

#translate('Hi, how are you today?', 'en', 'es')
