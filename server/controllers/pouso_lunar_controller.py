from flask import Blueprint
from http import HTTPStatus
import numpy as np
import matplotlib.pyplot as plt

from flask import Blueprint, jsonify, request
from server.core.context import Context
from server.decorators import with_context

from server.resources.pouso_lunar_resource import VelocidadesResource
from server.services import pouso_lunar

bp = Blueprint("pouso_lunar", __name__)


@bp.route("/pouso/curva/velocidade", methods=["POST"], endpoint="pls")
@with_context()
def curva_velocidade(ctx: Context):
    query = request.get_json()
    data = VelocidadesResource(**query)
    result = pouso_lunar.curvas_velocidade(data)

    # Encontra os índices dos elementos NaN
    nan_indices = np.isnan(result["velocidade"])

    # Remove os elementos NaN do array velocidade e altura
    velocidades = result["velocidade"][~nan_indices]
    y = result["altura"][~nan_indices]

    # Arredonda os valores para uma casa decimal
    velocidades = np.round(velocidades, 2)
    y = np.round(y, 2)

    vf = velocidades.tolist()
    y = y.tolist()

    # Retorna os dados em formato JSON
    return jsonify(velocidade=vf, altura=y)
