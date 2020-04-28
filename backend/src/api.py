import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS, cross_origin

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

CORS(app, resources={r"*": {"origins": "*"}})
# CORS Headers


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,PATCH')
    return response

# db_drop_and_create_all()


# ROUTES
@app.route("/drinks", methods=["GET"])
def get_drinks():
    drinks = Drink.query.all()

    return jsonify({
        "success": True,
        "drinks": drinks
    })


@app.route("/drinks-detail")
@requires_auth('get:drinks-detail')
def get_drinks_detail(payload):
    drinks = [drink.long() for drink in Drink.query.all()]

    if drinks is None:
        abort(404)

    # add get:drinks-detail permission
    return jsonify({
        "success": True,
        "drinks": drinks
    })


@app.route("/drinks", methods=["POST"])
@requires_auth('post:drinks')
def create_drink(payload):

    body = request.get_json()

    if 'title' and 'recipe' not in body:
        abort(422)

    title = body['title']
    recipe_json = json.dumps(body['recipe'])

    drink = Drink(title=title, recipe=recipe_json)

    drink.insert()

    return jsonify({
        'success': True,
        'drinks': [drink.long()]
    })


@app.route("/drinks/<int:drink_id>", methods=["PATCH"])
@requires_auth('patch:drinks')
def update_drink(payload, drink_id):
    body = request.get_json()

    try:
        drink = Drink.query.get(drink_id)

        if drink is None:
            abort(404)

        elif body is None:
            abort(404)

        else:
            if "title" in body:
                drink.title = body["title"]

            if "recipe" in body:
                drink.recipe = json.dumps(body["recipe"])

            drink.update()

            updated_drink = Drink.query.get(drink_id)
        return jsonify({
            "success": True,
            "drinks": [updated_drink.long()]
        })

    except Exception as error:
        abort(422)


@app.route("/drinks/<int:drink_id>", methods=["DELETE"])
@requires_auth('delete:drinks')
def delete_drink(payload, drink_id):
    try:
        drink = Drink.query.get(drink_id)
        if (drink is None):
            abort(404)
        drink.delete()
        return jsonify({
            "success": True,
            "delete": drink_id
        })
    except Exception as error:
        abort(422)


# Error Handling
'''
Example error handling for unprocessable entity
'''
@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "not found"
    }), 404


@app.errorhandler(AuthError)
def not_found(error):
    response = jsonify(error.error)
    response.status_code = error.status_code
    return response
    # return jsonify({
    #     "success": False,
    #     "error": error,
    #     "message": error.error["code"]
    # }), AuthError
