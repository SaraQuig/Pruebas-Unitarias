from flask import Blueprint, request, jsonify
from app.api.models.user import User


users_bp = Blueprint('users', __name__)

@users_bp.route('/register', methods=['POST'])
def register_user():
    data = request.json
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    correo = data.get('correo')
    cedula = data.get('cedula')
    celular = data.get('celular')

    if not nombre or not apellido or not correo or not cedula or not celular:
        return jsonify({"error": "Todos los campos son obligatorios"}), 400

    new_user = User(nombre, apellido, correo, cedula, celular)
    # Aquí podrías interactuar con tu repositorio o base de datos para guardar el usuario

    return jsonify({"message": "Usuario registrado correctamente"}), 201
