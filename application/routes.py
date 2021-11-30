from application import app, db
from application.models import Travel_wishlist

@app.route('/create/place')
def create_place():
    new_place = Travel_wishlist(destination_name="New Place")
    db.session.add(new_place)
    db.session.commit()
    return f"Added new place with id: {new_place.id} to database"

@app.route('/read/allPlaces')
def read_places():
    all_places = Travel_wishlist.query.all()
    places_dict = {"places": []}
    for place in all_places:
        places_dict["places"].append(
            {    
                "id": place.id,
                "destinaton": place.destination_name,
                "visited" : place.visited
            }    
        )
    return places_dict

@app.route('/update/place/<int:id>/<new_place>')
def update_place(id, new_place):
    place = Travel_wishlist.query.get(id)
    place.destination_name = new_place
    db.session.commit()
    return f"Place with id: {id} updated to {new_place}"

@app.route('/delete/place/<int:id>')
def delete_place(id):
    place = Travel_wishlist.query.get(id)
    db.session.delete(place)
    db.session.commit()
    return f"Place with id: {id} deleted"

@app.route('/visited/place/<int:id>')
def visited_place(id):
    place = Travel_wishlist.query.get(id)
    place.visited = True
    db.session.commit()
    return f"Place with id: {id} has been visited"

@app.route('/unvisited/place/<int:id>')
def unvisited_place(id):
    place = Travel_wishlist.query.get(id)
    place.visited = False
    db.session.commit()
    return f"Place with id: {id} is unvisited"
