import requests
import json
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

#Funkcja sprawdzająca czy odpowiedź jest poprawna
def check_url(url:str) -> bool:
    response = requests.get(url)
    if response.status_code >=200 or response.status_code <=299:
        print("Odpowiedz poprawna")
        return True
    else:
        print("Odpowiedz niepoprawna")
        return False

#url = 'https://api.gios.gov.pl/pjp-api/rest/station/findAll'
#print(check_url(url))

#Funkcja sprawdzająca pogodę w danym mieście na 4 godziny
def temp(miasto:str) -> str:
    response = requests.get(f"https://www.meteoprog.pl/pl/weather/{miasto}/")
    if response.status_code < 200 or response.status_code > 299:
        print(f"Błąd. Kod odpowiedzi: {response.status_code}")
    else:
        data = response.content.decode('utf-8')
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find('ul', class_="today-hourly-weather hide-scroll").find_all("li")
        godziny = []
        temperatury= []
        print(table)
        for prognoza in table:
            temperatura = soup.find('span', class_="today-hourly-weather__temp").text.strip()
            godzina = soup.find('span', class_="today-hourly-weather__name").text.strip()
            temperatury.append(temperatura)
            godziny.append(godzina)
        print(temperatury)




print(temp('Olsztyn'))




































#response = requests.get(url)
#content = response.content.decode('utf-8')
#parsed_content = json.loads(content)

#print(type(response.content), type(content), type(parsed_content))
#for station in parsed_content:
#    print(
#        f'ID: {station["id"]}, nazwa: {station["stationName"]}, miasto: {station["city"]["name"]}, lokalizacja: {station["addressStreet"]}')
