from flask import Flask, render_template, request, redirect, url_for, jsonify

import csv


app = Flask(__name__)

@app.route('/')
def card():
    return render_template('/card.html')


def cards():
    card_number = request.json.get('card_number')
    name = request.json.get('name')
    expiry = request.json.get('expiry')
    cvv = request.json.get('cvv')
    
    with open('card.csv', 'a+') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([card_number, name, expiry, cvv])
        
        return jsonify({
            'message': 'Card added successfully'
            }), 200
    

if __name__ == '__main__':
    app.run(debug=True)