from js import XMLHttpRequest, document
import json
from time import gmtime, strftime
from datetime import datetime, timedelta

now = datetime.utcnow() + timedelta(hours=7)
today_time = now.strftime("%a, %H:%M, %d %b")
document.getElementById("time").innerText = today_time


def make_request(url):
    req = XMLHttpRequest.new(url)
    req.open("GET", url, False)
    req.send(None)
    output = str(req.response)
    return output

def update_time():
    now = datetime.utcnow() + timedelta(hours=7)  # Menambahkan 7 jam untuk WIB
    current_time = now.strftime("%a, %H:%M, %d %b")  
    document.getElementById("time").innerText = current_time

def get_ip():
    API_key = 'c5353e5225f64d51895f9dde3389ca97'
    out_put = make_request(f'https://api.ipgeolocation.io/ipgeo?apiKey={API_key}')
    ip_address = json.loads(out_put)
    return(ip_address)


def get_weather():
    out_put = make_request(f'https://api.openweathermap.org/data/2.5/weather?lat=-2.9170&lon=104.7285&appid=47e28d589c912d35b8aed44a6681c3c2')
    weather = json.loads(out_put)
    return weather

def display_parameters():
    document.getElementById("temp").innerText = str(round(get_weather()['main']['temp_min']-273.15))+'°'
    document.getElementById("location").innerText = get_weather()['name']
    document.getElementById("cloud_info").innerText = str(get_weather()['weather'][0]['description']).title()
    document.getElem    entById("wind_speed").innerText = str(get_weather()['wind']['speed'])+' '+'km/h'
    document.getElementById("pressure").innerText = str(get_weather()['main']['pressure'])+' '+'hPa'
    document.getElementById("humidity").innerText = str(get_weather()['main']['humidity'])+' '+'%'

if __name__ == "__main__":
    display_parameters()
