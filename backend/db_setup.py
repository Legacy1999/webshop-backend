from flask import Flask
from models import db, Product
import config
import os

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

def seed_data():
    with app.app_context():
        db.drop_all()
        db.create_all()
        for i in range(10):
            p = Product(
                name=f"Weed Sorte {i+1}",
                description=f"Beschreibung für Weed {i+1}",
                price=4.20 + i,
                image_path=f"/app/images/weed{i+1}.jpg"
            )
            db.session.add(p)
        db.session.commit()
        print("Seeded 10 Produkte.")

if __name__ == "__main__":
    seed_data()
