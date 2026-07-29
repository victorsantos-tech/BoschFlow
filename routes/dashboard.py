from flask import Blueprint, jsonify

from services.dashboard_service import DashboardService

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/api/dashboard")
def api_dashboard():

    dados = DashboardService.indicadores()

    return jsonify({

        "entradas": dados["entradas"],

        "saidas": dados["saidas"],

        "categorias_labels": dados["categorias_labels"],

        "categorias_valores": dados["categorias_valores"]

    })