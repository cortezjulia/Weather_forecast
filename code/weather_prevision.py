"""
the Requests library in Python serves to make requests on a database or dataset. 
Thus, it is essential to establish the interaction between a database and an application in Python.
Get - is used to get information.
Post - to create a source information
Patch - is indicated to update information
Delete - is for deleting information.


wttr is a console-oriented weather forecast service that comes with a number of information representation 
ways to make sure you get the weather data in the best form possible.
"""
import requests



# Function to Generate Report
def city_function(C):
    url = f'https://wttr.in/{C}'
    try:
        received_url = requests.get(url)
        result = received_url.text
    except:
        result = "Falha ao localizar essa cidade!"
    print(result)
    


city = input("Digite o nome da cidade que você deseja ver a previsão do tempo: ")
print("\n\n")

city_function(city)