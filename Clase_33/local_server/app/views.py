from flask import jsonify
from app.database import testear_conexion, crear_tabla_tareas

def index():
    return jsonify({"mesaje": "Soy una api nuevita nuevita"}), 200


def test():
    return jsonify({"mesaje": "ESTO ES UN TEST"}), 200

def teastar_base():
    try:
        testear_conexion()
        return jsonify({"mesaje": "La conexión es un EXITO"}), 200
    except BaseException as be:
        return jsonify({"mesaje": f"NO ANDA NADA {be}"}), 500



def crear_tabla():
    try:
        crear_tabla_tareas()
        return jsonify({"mesaje": "Ya se creó la tabla o ya existía"}), 200
    except BaseException as be:
        return jsonify({"mesaje": f"Se rompió todo {be}"}), 500
