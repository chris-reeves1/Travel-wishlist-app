from application import app
from application.forms import CountryForm
from flask import render_template, request, redirect, url_for, jsonify
import requests

backend_host = "wishlist-app_backend:5000"

@app.route('/')
@app.route('/home')
def home():
    all_countries = requests.get(f"http://{backend_host}/read/allCountries").json()
    app.logger.info(f"Country: {all_countries}")
    return render_template('index.html', title="Home", all_countries=all_countries["country"])


@app.route('/create/country', methods=['GET', 'POST'])
def create_country():
    form = CountryForm()

    if request.method == "POST":
        response = requests.post(f"http://{backend_host}/create/country",
        json={"country_name": form.country_name.data})
        return redirect(url_for('home'))

    return render_template("create_country.html", title="Add country to Wishlist", form=form)

@app.route('/update/country/<int:id>', methods=['GET','POST'])
def update_country(id):
    form = CountryForm()
    country = requests.get(f"http://{backend_host}/update/country/{id}").json()
    app.logger.info(f"Country: {country}")

    if request.method == "POST":
        response = requests.put(
            f"http://{backend_host}/update/country/{id}",
            json={"country_name": form.country_name.data})
        return redirect(url_for('home'))

    return render_template('update_country.html', country=country, form=form)

@app.route('/delete/country/<int:id>')
def delete_country(id):
    response = requests.delete(f"http://{backend_host}/delete/country/{id}")
    app.logger.info(f"Response: {response.text}")
    return redirect(url_for('home'))

@app.route('/visited/country/<int:id>')
def visited_country(id):
    response = requests.put(f"http://{backend_host}/visited/country/{id}")
    app.logger.info(f"Response: {response.text}")
    return redirect(url_for('home'))

@app.route('/unvisited/country/<int:id>')
def unvisited_country(id):
    response = requests.put(f"http://{backend_host}/unvisited/country/{id}")
    app.logger.info(f"Response: {response.text}")
    return redirect(url_for('home'))