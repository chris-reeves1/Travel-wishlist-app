from application import app, db
from application.models import Country, Rating
from application.forms import CountryForm
from flask import render_template, request, redirect, url_for

@app.route('/')
@app.route('/home')
def home():
    all_countries = Country.query.all()
    return render_template('index.html', title="Home", all_countries=all_countries)


@app.route('/create/country', methods=['GET', 'POST'])
def create_country():
    form = CountryForm()

    if request.method == "POST":
        new_country = Country(country_name=form.country_name.data)
        db.session.add(new_country)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("create_country.html", title="Add country to Wishlist", form=form)

@app.route('/read/allCountries')
def read_countries():
    all_countries = Country.query.all()
    country_dict = {"country": []}
    for country in all_countries:
        country_dict["country"].append(
            {    
                "id": country.id,
                "country": country.country_name,
                "visited" : country.visited,
                "Recommend" : country.recommend
            }    
        )
    return country_dict

# @app.route('/recommend/<int:id>')
# def recommend_country(id):
#     country = Country.query.get(id)
#     country.recommend = True
#     db.session.commit()
#     return f"Place with id: {id} now recommended"

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_country(id):
    form = CountryForm()
    country = Country.query.get(id)

    if request.method == "POST":
        country.country_name = form.country_name.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('update_country.html', title="Rename a Country", country=country, form=form)

@app.route('/delete/country/<int:id>')
def delete_country(id):
    country = Country.query.get(id)
    db.session.delete(country)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/visited/country/<int:id>')
def visited_country(id):
    country = Country.query.get(id)
    country.visited = True
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/unvisited/country/<int:id>')
def unvisited_country(id):
    country = Country.query.get(id)
    country.visited = False
    db.session.commit()
    return redirect(url_for('home'))
