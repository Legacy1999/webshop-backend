from flask import Flask, request, jsonify
from models import db, Product
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route("/products", methods=["GET"])
def get_all_products():
    products = Product.query.all()
    return jsonify([{
        "id": p.id, "name": p.name, "description": p.description,
        "price": p.price, "image_path": p.image_path
    } for p in products])

@app.route("/products/<int:id>", methods=["GET"])
def get_product(id):
    p = Product.query.get_or_404(id)
    return jsonify({
        "id": p.id, "name": p.name, "description": p.description,
        "price": p.price, "image_path": p.image_path
    })

@app.route("/products", methods=["POST"])
def create_product():
    data = request.get_json()
    new_p = Product(**data)
    db.session.add(new_p)
    db.session.commit()
    return jsonify({"message": "Produkt hinzugefügt", "id": new_p.id}), 201

@app.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    p = Product.query.get_or_404(id)
    db.session.delete(p)
    db.session.commit()
    return jsonify({"message": "Produkt gelöscht"})
