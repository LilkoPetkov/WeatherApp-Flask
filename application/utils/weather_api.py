import random

import requests
from decouple import config

cities = [
    'Abidjan', 'Abu Dhabi', 'Abuja', 'Accra', 'Addis Ababa', 'Ahmedabad', 'Aleppo', 
    'Alexandria', 'Algiers', 'Almaty', 'Amman', 'Amsterdam', 'Anchorage', 'Andorra la Vella', 'Ankara',
    'Antananarivo', 'Apia', 'Arnold', 'Ashgabat', 'Asmara', 'Asuncion', 'Athens', 'Auckland', 'Avarua',
    'Baghdad', 'Baku', 'Bamako', 'Banda Aceh', 'Bandar Seri Begawan', 'Bandung', 'Bangkok', 'Bangui',
    'Banjul', 'Barcelona', 'Barranquilla', 'Basrah', 'Basse-Terre', 'Basseterre', 'Beijing', 'Beirut',
    'Bekasi', 'Belem', 'Belgrade', 'Belmopan', 'Belo Horizonte', 'Bengaluru', 'Berlin', 'Bern', 'Bishkek',
    'Bissau', 'Bogota', 'Brasilia', 'Bratislava', 'Brazzaville', 'Bridgetown', 'Brisbane', 'Brussels', 
    'Bucharest', 'Budapest', 'Buenos Aires', 'Bujumbura', 'Bursa', 'Busan', 'Cairo', 'Cali', 'Caloocan', 'Camayenne', 
    'Canberra', 'Cape Town', 'Caracas', 'Casablanca', 'Castries', 'Cayenne', 'Charlotte Amalie', 'Chengdu', 
    'Chennai', 'Chicago', 'Chisinau', 'Chittagong', 'Chongqing', 'Colombo', 'Conakry', 'Copenhagen', 'Cordoba', 'Curitiba',
    'Daegu', 'Daejeon', 'Dakar', 'Dallas', 'Damascus', 'Dar es Salaam', 'Delhi', 'Denver', 'Dhaka', 'Dili', 'Djibouti',
    'Dodoma', 'Doha', 'Dongguan', 'Douala', 'Douglas', 'Dubai', 'Dublin', 'Durban', 'Dushanbe', 'Faisalabad',
    'Fort-de-France', 'Fortaleza', 'Freetown', 'Fukuoka', 'Funafuti', 'Gaborone', 'George Town', 'Georgetown',
    'Gibraltar', 'Gitega', 'Giza', 'Guadalajara', 'Guangzhou', 'Guatemala City', 'Guayaquil', 'Gujranwala', 
    'Gustavia', 'Gwangju', 'Hamburg', 'Hanoi', 'Harare', 'Havana', 'Helsinki', 'Ho Chi Minh City', 'Hong Kong',
    'Honiara', 'Honolulu', 'Houston', 'Hyderabad', 'Hyderabad', 'Ibadan', 'Incheon', 'Isfahan', 'Islamabad',
    'Istanbul', 'Izmir', 'Jaipur', 'Jakarta', 'Jeddah', 'Jerusalem', 'Johannesburg', 'Juarez', 'Juba', 'Kabul',
    'Kaduna', 'Kampala', 'Kano', 'Kanpur', 'Kaohsiung', 'Karachi', 'Karaj', 'Kathmandu', 'Kawasaki', 'Kharkiv', 'Khartoum',
    'Khulna', 'Kigali', 'Kingsburg', 'Kingston', 'Kingstown', 'Kinshasa', 'Kobe', 'Kolkata', 'Kota Bharu', 'Kowloon', 
    'Kuala Lumpur', 'Kumasi', 'Kuwait', 'Kyiv', 'Kyoto', 'La Paz', 'Lagos', 'Lahore', 'Libreville', 'Lilongwe', 'Lima', 
    'Lisbon', 'Ljubljana', 'Lome', 'London', 'Los Angeles', 'Luanda', 'Lubumbashi', 'Lusaka', 'Luxembourg', 'Macau', 'Madrid', 
    'Majuro', 'Makassar', 'Malabo', 'Male', 'Mamoudzou', 'Managua', 'Manama', 'Manaus', 'Manila', 'Maputo', 'Maracaibo', 
    'Maracay', 'Mariehamn', 'Marigot', 'Maseru', 'Mashhad', 'Mbabane', 'Mecca', 'Medan', 'Medellin', 'Medina', 'Melbourne', 
    'Mexico City', 'Miami', 'Minsk', 'Mogadishu', 'Monaco', 'Monrovia', 'Montevideo', 'Montreal', 'Moroni', 'Moscow', 'Mosul', 
    'Multan', 'Mumbai', 'Muscat', "N'Djamena", 'Nagoya', 'Nairobi', 'Nanchong', 'Nanjing', 'Nassau', 'Nay Pyi Taw', 'New York', 
    'Niamey', 'Nicosia', 'Nouakchott', 'Noumea', 'Novosibirsk', "Nuku'alofa", 'Nur-Sultan', 'Nuuk', 'Oranjestad', 'Osaka', 
    'Oslo', 'Ottawa', 'Ouagadougou', 'Pago Pago', 'Palembang', 'Palo Alto', 'Panama', 'Papeete', 'Paramaribo', 'Paris', 'Perth', 
    'Philadelphia', 'Phnom Penh', 'Phoenix', 'Podgorica', 'Port Louis', 'Port Moresby', 'Port of Spain', 'Port-Vila', 'Port-au-Prince', 
    'Porto Alegre', 'Porto-Novo', 'Prague', 'Praia', 'Pretoria', 'Pristina', 'Puebla', 'Pune', 'Pyongyang', 'Quezon City', 
    'Quito', 'Rabat', 'Rawalpindi', 'Recife', 'Reykjavik', 'Riga', 'Rio de Janeiro', 'Riyadh', 'Road Town', 'Rome', 'Roseau', 
    "Saint George's", 'Saint Helier', "Saint John's", 'Saint Peter Port', 'Saint Petersburg', 'Saint-Denis', 'Saint-Pierre', 
    'Saipan', 'Salvador', 'San Antonio', 'San Diego', 'San Francisco', 'San Jose', 'San Juan', 'San Marino', 'San Salvador', 
    'Sanaa', 'Santa Cruz de la Sierra', 'Santiago', 'Santo Domingo', 'Sao Paulo', 'Sao Tome', 'Sapporo', 'Sarajevo', 'Seattle', 
    'Semarang', 'Seoul', 'Shanghai', 'Sharjah', 'Shenzhen', 'Singapore', 'Skopje', 'Sofia', 'South Tangerang', 'Soweto', 
    'Stockholm', 'Sucre', 'Surabaya', 'Surat', 'Suva', 'Sydney', 'Tabriz', 'Taipei', 'Tallinn', 'Tangerang', 'Tarawa', 
    'Tashkent', 'Tbilisi', 'Tegucigalpa', 'Tehran', 'Tel Aviv', 'Thimphu', 'Tianjin', 'Tijuana', 'Tirana', 'Tokyo', 'Toronto', 
    'Torshavn', 'Tripoli', 'Tunis', 'Ulan Bator', 'Vaduz', 'Valencia', 'Valletta', 'Vancouver', 'Victoria', 'Vienna', 
    'Vientiane', 'Vilnius', 'Warsaw', 'Washington', 'Wellington', 'Willemstad', 'Windhoek', 'Wuhan', "Xi'an", 'Yamoussoukro', 
    'Yangon', 'Yaounde', 'Yekaterinburg', 'Yerevan', 'Yokohama', 'Zagreb'
]


class WeatherForecast:
    coldest_city = {}
    average_temp = []
    all_cities = []

    def __init__(self):
        self.nums = random.sample(range(371), 5)
        self.api_key = config("API_KEY")
    
    def get_data_specific_city(self, city_name):
        url_city = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={self.api_key}"

        if requests.get(url_city).json():
            data = self.process_data(url_city)

            adjusted_data = [data["name"], data["weather"], data["temp"], data["humidity"]]

            return adjusted_data
        else:
            return None

    def generate_city_data(self):
        for idx in range(5):
            url_city = f"http://api.openweathermap.org/geo/1.0/direct?q={cities[self.nums[idx]]}&limit=5&appid={self.api_key}"
            
            data = self.process_data(url_city)

            self.coldest_city[data["name"]] = data["temp"]
            self.average_temp.append(data["temp"])

            self.all_cities.append(data)

        self.nums = random.sample(range(371), 5)
        return self.all_cities

    def process_data(self, url):
            data = {}
            response = requests.get(url)
                
            data["name"] = response.json()[0]["name"]
            data["lat"] = response.json()[0]["lat"]
            data["lon"] = response.json()[0]["lon"]

            url_forecast = f"https://api.openweathermap.org/data/2.5/weather?lat={data['lat']}&lon={data['lon']}&appid={self.api_key}"
            forecast_data = requests.get(url_forecast)

            data["weather"] = forecast_data.json()["weather"][0]["main"]
            data["temp"] = forecast_data.json()["main"]["temp"] - 273.15
            data["humidity"] = forecast_data.json()["main"]["humidity"]

            return data

    def get_coldest_of_cities(self):
        sorted_dict = sorted(self.coldest_city.items(), key=lambda x:x[1])
        
        return {"cities": [s for s in self.coldest_city], "coldest_city": sorted_dict[0][0], "temperature": sorted_dict[0][1]}

    def get_average_temp(self):
        return {"avg_temp": sum(self.average_temp) / len(self.average_temp)}

    @staticmethod
    def clear_generated_data():
        WeatherForecast.all_cities.clear()

# forecast = WeatherForecast()
# print(forecast.generate_city_data())
# print(forecast.get_coldest_of_cities())
# print(forecast.get_average_temp())

# print(forecast.get_data_specific_city("Sofia"))
