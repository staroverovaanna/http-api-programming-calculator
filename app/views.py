from flask import Flask, render_template, request, redirect, url_for, jsonify
from app import app
from .utils import Token, Expression


@app.route('/')
def hello_world():
    return render_template("start_page.html")


@app.route('/calculate', methods=['POST'])
def calculate_expression():
    try:
        data = request.json
        expression_string = data['expression']
        expression = Expression(value=expression_string)
        result = expression.calculate()
        return jsonify({'response': f'The answer is {result}'}), 200
    except ZeroDivisionError as e:
        return jsonify({'error': f"Message: {e}, status 400 Bad request"}), 400
    except Exception as e:
        return jsonify({'error': f"Message: {e}, status 500 Internal error"}), 500


@app.route('/result', methods=['POST'])
def calc_expression():
    try:
        expression_string = request.form.get("expression_string")
        expression = Expression(value=expression_string)
        result = expression.calculate()
        title = 'results'
        return render_template("result.html", title=title, expression_string=expression_string, result_string=result)
    except ZeroDivisionError as e:
        return jsonify({'error': f"Message: {e}, status 400 Bad request"}), 400
    except Exception as e:
        return jsonify({'error': f"Message: {e}, status 500 Internal error"}), 500
