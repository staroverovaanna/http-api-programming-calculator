from flask import render_template, request, redirect, url_for, jsonify
from app import app
from .utils import Token, Expression
# from .models import User
# from app import db
import sys

@app.route('/')
def hello_world():
    return "Hello, world!"

@app.route('/calculate', methods=['POST'])
def calc_expression():
    try:
        data = request.json
        expression_string = data['expression']
        expression = Expression(value = expression_string)
        result = expression.calculate()
        return jsonify({'response': f'The answer is {result}'}), 200

    except ZeroDivisionError as e:
        return jsonify({'error': f"Message: {e}, status 400 Bad request"}), 400
    except Exception as e:
        return jsonify({'error': f"Message: {e}, status 500 Internal error"}), 500
# curl 127.0.0.1:5000/calculate --header 'Content-Type: application/json' -X POST --data '{"expression": "-2 * (3 + 4) - 5 / 2"}'

