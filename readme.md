# Flask Weather App

Flask Weather App with basic frontend setup. The App uses Postgres and has feature for getting the weather forcast for
specific city, generate data and compare it for 5 random cities from a list of 371 one. The user can create a separate
list with cities and get a compared result of the last 10 added. 

# Table of contents
* [Installation](#Installation)
* [Setup](#Setup)
* [Technologies](#Technologies)
* [Contributing](#Contributing)
* [License](#License)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements located in requirements.txt.

```bash
pip install -r requirements.txt
```

#### Postgre setup

The project requires [PostgreSQL](https://www.postgresql.org/download/) . In the link it can be found available 
for all operating systems. In order to create and manage the database it is also needed to download a sql client for example
[PgAdmin](https://www.pgadmin.org/download/).

## Setup

1. Make sure to update the sample_env with the correct details for Postgre and additional services [API-KEY](https://home.openweathermap.org/api_keys).
2. The **sample_env** file should be renamed to: **.env**
3. After the environment variables are set, it is needed to run the database migrations.
    - ```export FLASK_APP=app.py```
    - ```flask db init```
    - ```flask db migrate -m "Add comment here"```
    - ```flask db upgrade```
4. Start the app.py file:
    - ```python3 app.py```

## Technologies
 - Python 3.9 / 3.11
 - pgAdmin4 v6.21
 - PostgreSQL 13.10 
    

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Screenshots

![Screenshot 2023-05-22 at 12 17 39](https://github.com/LilkoPetkov/WeatherApp-Flask/assets/99439480/55ba898b-4831-488b-9bbe-dd78bb676c01)
![Screenshot 2023-05-22 at 12 18 07](https://github.com/LilkoPetkov/WeatherApp-Flask/assets/99439480/8fdb44dc-7efa-4a9d-9079-b099c2807b88)
![Screenshot 2023-05-22 at 12 18 29](https://github.com/LilkoPetkov/WeatherApp-Flask/assets/99439480/2523bf30-bb6a-4695-b6d9-8092d4f7510b)
![Screenshot 2023-05-22 at 12 19 16](https://github.com/LilkoPetkov/WeatherApp-Flask/assets/99439480/99383e49-8cba-46bd-a6a5-b691c1fa06a0)

## License

[MIT](https://choosealicense.com/licenses/mit/)