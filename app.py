import os

import boto3
from botocore.exceptions import ClientError
from flask import Flask, jsonify, make_response, request
from datetime import datetime

app = Flask(__name__)

dynamodb_client = boto3.client('dynamodb')

if os.environ.get('IS_OFFLINE'):
    dynamodb_client = boto3.client(
        'dynamodb', region_name='localhost', endpoint_url='http://localhost:8000'
    )


FAVORITES_TABLE = os.environ['USERS_TABLE']


# @app.route('/users/<string:user_id>')
# def get_user(user_id):
#     result = dynamodb_client.get_item(
#         TableName=USERS_TABLE, Key={'userId': {'S': user_id}}
#     )
#     item = result.get('Item')
#     if not item:
#         return jsonify({'error': 'Could not find user with provided "userId"'}), 404
#
#     return jsonify(
#         {'userId': item.get('userId').get('S'), 'name': item.get('name').get('S')}
#     )

#Tries to read and iterate through all elements in Favorites Table, and display them
@app.route('/')
def get_all_favorites():

    enterprises = []
    start_key = True
    try:
        while start_key:
            results = dynamodb_client.scan()
            enterprises.extend(results.get('Items', []))
            start_key = results.get('LastEvaluatedKey', None)
    except ClientError as err:
        return jsonify({'Error': 'Oopsie, something went wrong when loading your favorites!'})
    if not enterprises:
        return jsonify({'Warning': 'The table is empty, there are no favorites!"'})

    return jsonify(enterprises)


#
# @app.route('/users', methods=['POST'])
# def create_user():
#     user_id = request.json.get('userId')
#     name = request.json.get('name')
#     if not user_id or not name:
#         return jsonify({'error': 'Please provide both "userId" and "name"'}), 400
#
#     dynamodb_client.put_item(
#         TableName=USERS_TABLE, Item={'userId': {'S': user_id}, 'name': {'S': name}}
#     )
#
#     return jsonify({'userId': user_id, 'name': name})

#Tries to gather the provided enterprise ids, and adds them to the db alongside with the date and hour of the request
@app.route('/addfavorite', methods=['POST'])
def add_favorite():
    favourite_org_id = request.json.get('favourite_org_id')
    org_id = request.json.get('org_id')

    if not favourite_org_id or not org_id:
        return jsonify({'error': 'Please provide both "userId" and "name"'}), 400

    date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    dynamodb_client.put_item(TableName=FAVORITES_TABLE, Item={'favourite_org_id': {'S': favourite_org_id},
                                                              'org_id': {'S': org_id}, 'date': {'S': date}})

    return jsonify({'favourite_org_id': favourite_org_id, 'org_id': org_id, 'date': date})


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
