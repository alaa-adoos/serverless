from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):


    def do_GET(self):
        s=self.path
        url_components=parse.urlsplit(s)
        query_string_list=parse.parse_qsl(url_components.query)
        dictionary=dict(query_string_list)
        definsions=[]
        if 'word' in dictionary:
            word=dictionary['word']
            url='https://api.dictionaryapi.dev/api/v2/entries/en'
            r=requests.get(url+word)
            data=r.json

            for word_data in data:
                definsion=word_data['meanings'][0]['definitions'][0]['definitions']
                definsions(definsion)
            message=str(definsions)
        else:
            message="please enter a word"


        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(message.encode())
        return