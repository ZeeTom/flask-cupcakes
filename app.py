"""Flask app for Cupcakes"""

from models import Cupcake, db, connect_db
from flask import Flask, request, jsonify

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "gfudhiaskhjl543278489grhuiger8934"

@app.route('/api/cupcakes')
def show_cupcakes():
    """Shows information on all cupcakes
    
    Return JSON {'cupcakes': [{id, flavor, size, rating, image},...]}"""
    
    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)

@app.route('/api/cupcakes/<int:cupcake_id>')
def show_cupcake(cupcake_id):
    """Shows information on a specific cupcake
    
    Return JSON {'cupcake': {id, flavor, size, rating, image}}"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)

@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    """Create cupcake from request data & return it.
    
    Return JSON {'cupcake': {id, flavor, size, rating, image}}
    """

    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json['image'] or None

    cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    db.session.add(cupcake)
    db.session.commit()

    return (jsonify(cupcake=cupcake.serialize()), 201)