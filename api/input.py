from http.server import BaseHTTPRequestHandler
from urllib import parse


class handler(BaseHTTPRequestHandler):


    def do_GET(self):
        # add query name to take name  as input
        #/api/input?name="alaa"  
        s= self.path
        print("hiii",s)
        url_components=parse.urlsplit(s)
        query_string_list=parse.parse_qsl(url_components.query)
        print(query_string_list)
        dictionary=dict(query_string_list)

        name=dictionary.get('name',False)
        if name:
            message=f'Hello {name}'
        else :
            message="Hello Stranger"

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())
        return