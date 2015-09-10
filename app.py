import json
from flask import Flask, Response, request

from models.fighter import *
connect('Ultimate_Showdown')

app = Flask(__name__)

def dictify(mongo_thing):
    dictified = mongo_thing.to_mongo().to_dict()
    
    if '_id' in dictified:
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
        
    fighter_params = {}
    for permitted_key in ['name', 'gender', 'blood_type', 'img_src']:
        if permitted_key in request.form:
            fighter_params[permitted_key] = request.form[permitted_key]            
    
    new_fighter = Fighter(**fighter_params)
    
    try:
        new_fighter.save()
        return Response(json.dumps(dictify(new_fighter)), mimetype='application/json')
    except ValidationError as validation_error:
        errors = {'validationErrors': validation_error.to_dict()}
        return Response(json.dumps(errors), status=400, mimetype='application/json')

# ADD MOVE
@app.route('/api/fighter/<id>/move', methods=['POST'])
def add_move(id):
    fighter = Fighter.objects(id=id)[0]
    
    move_params = {}
    for permitted_key in ['name', 'attack_type', 'input_seq']:
        if permitted_key in request.form:
            move_params[permitted_key] = request.form[permitted_key]
    
    if 'input_seq' in move_params:
        move_params['input_seq'] = move_params['input_seq'].split(', ')   # expecting input_seq as ",<space>"-separated list
    
    new_move = fighter.moves.create(**move_params)
    
    try:
        fighter.save()
        return Response(json.dumps(dictify(new_move)), mimetype='application/json')
    except ValidationError as validation_error:
        errors = {'validationErrors': validation_error.to_dict()}  # put validation errors under key 'validationErrors' so they can be more easily checked for on the front-end
        return Response(json.dumps(errors), status=400, mimetype='application/json')

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
