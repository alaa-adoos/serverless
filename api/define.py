from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests



class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    '''
        you can send response to vercel as a country or a capital
        and send request to API to get a response of the capital of the country
        or the country to this capital  and if you didint sent any 
        it will give you a message said provide a country or a capital
    '''

    path=self.path
    url_Component=parse.urlsplit(path)
    query_string=parse.parse_qsl(url_Component.query)
    dictionary=dict(query_string)
    
    if "country" in dictionary:
        country=dictionary["country"]
        api_url="https://restcountries.com/v3.1/name/"
        r=requests.get(api_url + country)
        data=r.json()
        capital=str(data[0]["capital"][0])
        message = f'the capital of {country} is {capital} '    

    elif "capital" in dictionary:
        capital=dictionary["capital"]
        api_url="https://restcountries.com/v3.1/capital/"
        r=requests.get(api_url+capital)
        data=r.json()
        country=str(data[0]["name"]["common"])
        message = f'{capital} is the capital of {country} '    
    else :
        message="please provide me with a country or a capital"
     

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(message.encode())
    return