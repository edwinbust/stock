from flask import Flask, render_template, request, redirect, url_for
from models import db, Stock

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stocks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Ruta para listar todas las acciones
@app.route('/')
def index():
    stocks = Stock.query.all()
    return render_template('index.html', stocks=stocks)

# Ruta para añadir nuevas acciones
@app.route('/add', methods=['POST'])
def add_stock():
    stock_name = request.form['stock_name']
    price = float(request.form['price'])
    change = float(request.form['change'])
    
    new_stock = Stock(stock_name=stock_name, price=price, change=change)
    db.session.add(new_stock)
    db.session.commit()
    
    return redirect(url_for('index'))

# CRUD de eliminación
@app.route('/delete/<int:id>')
def delete_stock(id):
    stock = Stock.query.get(id)
    db.session.delete(stock)
    db.session.commit()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crear las tablas en la base de datos
    app.run(debug=True)
