import json
import urllib

from flask import request, redirect, url_for, flash, render_template, Response

from application import app
from application.db import db
from application.models import Entry
from application.utils.get_coldest_city import get_coldest_city
from application.utils.weather_api import WeatherForecast

ForeCast = WeatherForecast()


@app.route("/", methods=["GET", "POST"])
def index():
    # Submit button for single city forecast 5 days every 3 hours
    if request.method == "POST":
        if request.form["submit_btn"] == "Submit":
            global city
            city = request.form.get("city")

            return redirect(url_for("forecast"))

        # Submit button for random generated data from the list
        elif request.form["submit_btn"] == "Generate":
            return redirect(url_for("generated_data"))

        # Submit button to clear data from the DB
        elif request.form["submit_btn"] == "Clear Data":
            flash(f'History cleared', category="success")
            Entry.query.delete()
            db.session.commit()
            return render_template('index.html')

        # Submit button for adding a city to the list
        elif request.form["submit_btn"] == "Add to list":
            city = request.form.get("c")
            if ForeCast.get_data_specific_city(city):
                city, weather, temp, humidity = ForeCast.get_data_specific_city(city)
                entry = Entry(city_name=city, weather=weather, temp=temp, humidity=humidity)

                if entry.city_name not in [e.city_name for e in Entry.query.all()]:
                    db.session.add(entry)
                    db.session.commit()
                    flash(f'{city} added successfully', category="success")
                    return render_template('index.html')
                else:
                    flash(f'{city} is already added', category="danger")
                    return render_template('index.html')
            else:
                return redirect(url_for("four_o_four"))

        # Submit button for redirect to the comparison page with the last 10 cities from the DB
        elif request.form["submit_btn"] == "Compare":
            global city_compare_data
            city_compare_data = Entry.query.all()[-10:]

            if not city_compare_data:
                flash(f'No data to compare', category="danger")
                return render_template('index.html')

            return redirect(url_for("compare_city_data"))

    return render_template("index.html")  # , specific_city=result)


# Random data route
@app.route("/cities-data", methods=["GET"])
def generated_data():
    ForeCast.clear_generated_data()
    if request.method == 'POST':
        if request.form["submit_btn"] == "Back":
            return redirect(url_for("index"))
    selected_data = []
    avg_temp = []
    generate_data = ForeCast.generate_city_data()[-5:]
    for entry in generate_data:
        selected_data.append(
            [entry["name"], entry["temp"], entry["humidity"], entry["weather"]]
        )

    avg_temp.append(
        [", ".join([e["name"] for e in generate_data]), sum([s["temp"] for s in generate_data]) / len(generate_data)])

    coldest_city_data = get_coldest_city(generate_data)
    coldest_city = [coldest_city_data['name'], coldest_city_data['temp']]

    return render_template("random-cities.html", data=selected_data, avg_temp=avg_temp, coldest_city=coldest_city)


# Specific city forecast route
@app.route("/city-forecast", methods=["GET", "POST"])
def forecast():
    full_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid=d2c3aeff213fb19e232735ce0bab8f6f&units=metric"

    try:
        data = urllib.request.urlopen(full_url)
    except:
        return redirect(url_for("four_o_four"))

    resp = Response(data)
    resp.status_code = 200

    return render_template('forecast.html', title='Weather App', data=json.loads(data.read().decode('utf8')))


# Comparison route
@app.route("/compare-city-data", methods=["GET"])
def compare_city_data():
    city_data = Entry.query.all()[-10:]
    cities = ', '.join([c.city_name for c in city_data])
    temp = sum([c.temp for c in city_data]) / len(city_data)
    coldest_city = [c for c in city_data if c.temp == min([c.temp for c in city_data])][0]

    return render_template("cities.html", data=city_data, cities=cities, temp=temp, coldest_city=coldest_city)


# Missing city 404 page
@app.route("/invalid-city", methods=["GET", "POST"])
def four_o_four():
    if request.method == "POST":
        if request.form["submit_btn"] == "Back":
            return redirect(url_for("index"))

    return render_template("error_page.html")
