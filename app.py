import json
from flask import Flask, Response

from models.fighter import *
connect('Ultimate_Showdown')

app = Flask(__name__)

@app.route('/')
def index():
  return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_path(path):
  return app.send_static_file(path)

@app.route('/api/fighter', methods=['GET'])
def all_fighters():
    # fighters_mong = Fighter.objects()
    fighters = [fighter.to_mongo().to_dict() for fighter in Fighter.objects()]
    
    for fighter in fighters:
        fighter['id'] = str(fighter.pop('_id')) # remove unJSONifiable weirdness and store id as a simple string
    
    return Response(json.dumps(fighters), mimetype='application/json')

@app.route('/api/fighter/<id>', methods=['GET'])
def one_fighter(id):
    fighter = Fighter.objects(id=id)[0].to_mongo().to_dict()
    fighter['id'] = str(fighter.pop('_id')) # remove unJSONifiable weirdness and store id as a simple string
    
    return Response(json.dumps(fighter), mimetype='application/json')

# @app.route('/stuff')
# def stuff():
#   stuff = {
#     'artist1': 'Red Hot Chili Peppers',
#     'artist2': 'Vampire Weekend',
#     'artist3': 'Chicago'
#   }

#   return json.dumps(stuff)
#   # return stuff

app.run(debug=True)
