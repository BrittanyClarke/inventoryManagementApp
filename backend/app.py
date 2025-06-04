from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app, origins=["http://192.168.1.155:3000"])

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    barcode = db.Column(db.String(100), unique=True, nullable=False)
    quantity = db.Column(db.Integer, default=0)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([
        {'barcode': item.barcode, 'quantity': item.quantity}
        for item in items
    ])

@app.route('/items', methods=['POST'])
def add_item():
    data = request.json
    barcode = data.get('barcode')
    quantity = data.get('quantity', 1)

    if not barcode:
        return jsonify({'error': 'Barcode is required'}), 400

    item = Item.query.filter_by(barcode=barcode).first()
    if item:
        item.quantity += quantity
    else:
        item = Item(barcode=barcode, quantity=quantity)
        db.session.add(item)

    db.session.commit()
    return jsonify({'success': True, 'item': {'barcode': item.barcode, 'quantity': item.quantity}})

@app.route('/items/<barcode>', methods=['DELETE'])
def delete_item(barcode):
    item = Item.query.filter_by(barcode=barcode).first()
    if not item:
        return jsonify({'error': 'Item not found'}), 404

    if item.quantity > 1:
        item.quantity -= 1
        db.session.commit()
        return jsonify({'success': True, 'quantity': item.quantity})
    else:
        db.session.delete(item)
        db.session.commit()
        return jsonify({'success': True, 'quantity': 0})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, threaded=True)

