from flask import Blueprint, request, jsonify
from app.api.models.product import Product


products_bp = Blueprint('products', __name__)

@products_bp.route('/add', methods=['POST'])
def add_product():
    data = request.json
    nombre = data.get('nombre')
    precio = data.get('precio')
    descripcion = data.get('descripcion')

    if not nombre or not precio or not descripcion:
        return jsonify({"error": "Todos los campos son obligatorios"}), 400

    new_product = Product(nombre, precio, descripcion)
    # Aquí podrías interactuar con tu repositorio o base de datos para guardar el producto

    return jsonify({"message": "Producto añadido correctamente"}), 201
