from application import app, db
from application.models import Country
from flask import render_template, request, redirect, url_for, Response, jsonify

@app.route('/create/country', methods=['POST'])
def create_country():
    package = request.json
    new_country = Country(country_name=package["country_name"])
    db.session.add(new_country)
    db.session.commit()
    return Response(f"Added country: {new_country.country_name}", mimetype='text/plain')

@app.route('/read/allCountries', methods=['GET'])
def read_countries():
    all_countries = Country.query.all()
    country_dict = {"country": []}
    for country in all_countries:
        country_dict["country"].append(
            {    
                "id": country.id,
                "country": country.country_name,
                "visited" : country.visited,
            }    
        )
    return jsonify(country_dict)

@app.route('/read/country/<int:id>', methods=['GET'])
def read_country(id):
    country = Country.query.get(id)
    country_dict = {
                    "id": country.id,
                    "country_name": country.country_name,
                    "visited": country.visited,
                }
    return jsonify(country_dict)

@app.route('/update/country/<int:id>', methods=['PUT'])
def update_country(id):
    package = request.json
    country = Country.query.get(id)
    country.country_name = package["country_name"]
    db.session.commit()
    return Response(f"Updated country (ID: {id}) to {country.country_name}", mimetype='text/plain')

@app.route('/delete/country/<int:id>', methods=['DELETE'])
def delete_country(id):
    country = Country.query.get(id)
    db.session.delete(country)
    db.session.commit()
    return Response(f"Deleted country with ID: {id}", mimetype='text/plain')

@app.route('/visited/country/<int:id>', methods=['PUT'])
def visited_country(id):
    country = Country.query.get(id)
    country.visited = True
    db.session.commit()
    return Response(f"Country with ID: {id} visited", mimetype='text/plain')

@app.route('/unvisited/country/<int:id>', methods=['PUT'])
def unvisited_country(id):
    country = Country.query.get(id)
    country.visited = False
    db.session.commit()
    return Response(f"Country with ID: {id} unvisited", mimetype='text/plain')
