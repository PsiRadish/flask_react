import json
from flask import Flask, Response, request

from models.fighter import *
connect('Ultimate_Showdown')

app = Flask(__name__)

def dictify(mongo_thing):
    dictified = mongo_thing.to_mongo().to_dict()
    dictified['id'] = str(dictified.pop('_id')) # remove unJSONifiable weirdness and store id as a simple string
    
    return dictified

# ROOT
@app.route('/')
def index():
  return app.send_static_file('index.html')

# I don't know what this is.
@app.route('/<path:path>')
def static_path(path):
  return app.send_static_file(path)

# GET ALL FIGHTERS
@app.route('/api/fighter', methods=['GET'])
def all_fighters():
    # fighters_mong = Fighter.objects()
    fighters = [dictify(fighter) for fighter in Fighter.objects()]
    
    # for fighter in fighters:
    #     fighter['id'] = str(fighter.pop('_id')) # remove unJSONifiable weirdness and store id as a simple string
    
    return Response(json.dumps(fighters), mimetype='application/json')

# GET ONE FIGHTER
@app.route('/api/fighter/<id>', methods=['GET'])
def one_fighter(id):
    fighter = dictify(Fighter.objects(id=id)[0])
    # fighter['id'] = str(fighter.pop('_id')) # remove unJSONifiable weirdness and store id as a simple string
    
    return Response(json.dumps(fighter), mimetype='application/json')

# CREATE FIGHTER
@app.route('/api/fighter', methods=['POST'])
def create_fighter():
    print('POST /api/fighter toally made it typo lol')
    print('request.form', str(request.form))
    
    # fighter_params = { permitted_key: request.form[permitted_key] for permitted_key in ['name', 'gender', 'blood_type', 'img_src']}
    fighter_params = {}
    
    for permitted_key in ['name', 'gender', 'blood_type', 'img_src']:
        if permitted_key in request.form:
            fighter_params[permitted_key] = request.form[permitted_key]            
    
    print('fighter_params', str(fighter_params))
    new_fighter = Fighter(**fighter_params)
    
    print('about to try')
    
    try:
        # print('tryin')
        new_fighter.save()
        # print('wait wut')
        Response(json.dumps(dictify(new_fighter)), mimetype='application/json')
    except ValidationError as validation_error:
        # print('validation_error:  ' + str(validation_error))
        print([thing for thing in validation_error])
        # return str(validation_error)
        return Response(json.dumps(validation_error), mimetype='application/json')


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
