from flask import Blueprint, request, jsonify
# Imports from another files if needed

def sample_function(par_1, par_2):
    return par_1 / par_2

sample_app = Blueprint('sample_app', __name__)

@sample_app.route('/health', methods = ['GET'])
def health():
    if request.method == 'GET':
        return 'ok'


@sample_app.route('/v1/sample_endpoint', methods = ['POST'])
def optimal_bid():
    if request.method == 'POST':
        json_data = request.get_json()

        dum_operation = sample_function(par_1 = float(json_data['par_1']),
                                    par_2 = float(json_data['par_2']))
        return jsonify({'result': dum_operation})
