from flask import Flask, jsonify
from api.functions.operators import df_to_json
from api.config.variables import sep, path
from collections import OrderedDict
import json

app = Flask(__name__) #Indicando que o __name__ é igual o nome do meu arquivo


@app.route('/pokemon', methods=['GET'])
def get_pokemons():
    return json.loads(df_to_json(path, sep), object_pairs_hook=OrderedDict)

#Consultar(id)
@app.route('/pokemon/<type>', methods=['GET'])
def get_pokemon_type(type):
    pokemons = json.loads(df_to_json(path, sep))
    pokemon_list = []

    for pokemon in pokemons:
        if pokemon.get('type_1') == type:

            pokemon_list.append(pokemon)

    return jsonify(pokemon_list)


app.run(port=5000, host='localhost', debug=True)
