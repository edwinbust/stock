from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    change = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Stock {self.stock_name}>'
