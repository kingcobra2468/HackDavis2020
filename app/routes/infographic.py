from flask import Blueprint, request, Response, render_template, make_response
from models import compare_images
from utils.transport_data import get_transport_distances, dist_to_kWh


graphic_blueprint = Blueprint('graphic', __name__, template_folder="templates")

@graphic_blueprint.route('/graphic', methods=['POST'])
def feed():

    start_pos = request.form["start_pos"]
    destination_pos = request.form["destination_pos"]

    print(f'here {start_pos} {destination_pos}')
    #get_transport_distances(start_pos, destination_pos);

    return render_template('graphic.html')