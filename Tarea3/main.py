from flask import Flask
from flask import jsonify
from config import config
from models import db
from models import Usuario
from models import Pais
from models import Cuenta_bancaria
from models import Moneda
from models import Precio_moneda
from models import Usuario_tiene_moneda
import datatime
from flask import request


def create_app(enviroment):
	app = Flask(__name__)
	app.config.from_object(enviroment)
	with app.app_context():
		db.init_app(app)
		db.create_all()
	return app

# Accedemos a la clase Config del archivo config.py entregado
enviroment = config['development']
app = create_app(enviroment)




#___TABLA___USUARIO___#
#Metodo para obtener algo de la tabla usuario#
@app.route('/api/usuario', methods=['GET'])
def get_usuario():
	users = [ usuario.json() for usuario in Usuario.query.all() ] 
	return jsonify({'users': users })

#Metodo para almacenar tal cosa en la tabla usuario#
@app.route('/api/usuario/', methods=['POST'])
def create_usuario():
	json = request.get_json(force=True)
	if json.get('nombre') is None:
		return jsonify({'message': 'El formato está mal'}), 400
	user = Usuario.create(json['nombre'],json['apellido'],json['correo'],json['contraseña'],json['pais'])

	return jsonify({'user': user.json() })

#Metodo para reemplazar o crear un nuevo elemento#
@app.route('/api/usuario/<id>', methods=['PUT'])
def update_usuario(id):
	usuario = Usuario.query.filter_by(id=id).first()
	if user is None:
		return jsonify({'message': 'Usuario no existe'}), 404

	json = request.get_json(force=True)
	if json.get('nombre') is None:
		return jsonify({'message': 'Bad request'}), 400
#Es indispensable pedir en este orden los datos
	user.nombre = json['nombre']
	user.apellido = json['apellido']
	user.correo = json['correo']
	user.contraseña = json['contraseña']
	user.pais = json['pais']

	user.update()

	return jsonify({'user': user.json() })

#Metodo para eliminar un usuario de la tabla"
@app.route('/api/usuario/<id>', methods=['DELETE'])
def delete_usuario(id):
	user = Usuario.query.filter_by(id=id).first()
	if user is None:
		return jsonify({'message': 'El usuario no existe'}), 404

	user.delete()

	return jsonify({'user': user.json() })





#___TABLA___PAIS___#
#Metodo para obtener algo de la tabla pais#
@app.route('/api/pais', methods=['GET'])
def get_pais():
	paises = [ pais.json() for pais in Pais.query.all() ] 
	return jsonify({'paises': paises })

#Metodo para almacenar tal cosa en la tabla Pais#
@app.route('/api/v1/pais/', methods=['POST'])
def create_pais():
	json = request.get_json(force=True)

	if json.get('nombre') is None:
		return jsonify({'message': 'El formato está mal'}), 400

	paises = Pais.create(json['nombre'])

	return jsonify({'paises': paises.json() })

#Metodo para reemplazar o crear un nuevo elemento#
@app.route('/api/pais/<id>', methods=['PUT'])
def update_pais(id):
	paises = Pais.query.get(id)
	if paises is None:
		return jsonify({'message': 'User does not exists'}), 404

	json = request.get_json(force=True)
	if json.get('nombre') is None:
		return jsonify({'message': 'Bad request'}), 400

	paises.nombre = json['nombre']
	paises.update()

	return jsonify({'paises': paises.json() })

@app.route('/api/pais/<id>', methods=['DELETE'])
def delete_pais(id):
	paises = Pais.query.get(id)
	if paises is None:
		return jsonify({'message': 'El usuario no existe'}), 404

	paises.delete()

	return jsonify({'paises': paises.json() })






#___TABLA___CUENTA_BANCARIA___#
#Metodo para obtener algo de la tabla usuario#
@app.route('/api/cuenta_bancaria', methods=['GET'])
def get_cuentas():
	cuentas = [ cuenta_bancaria.json() for cuenta_bancaria in Cuenta_bancaria.query.all() ] 
	return jsonify({'cuentas': cuentas })

#Metodo para almacenar tal cosa en la tabla usuario#
@app.route('/api/cuenta_bancaria/', methods=['POST'])
def create_cuentas():
	json = request.get_json(force=True)

	if json.get('id_usuario') is None:
		return jsonify({'message': 'El formato está mal'}), 400

	cuentas = Cuenta_bancaria.create(json['id_usuario'],json['balance'])

	return jsonify({'cuentas': cuentas.json() })

#Metodo para reemplazar o crear un nuevo elemento#
@app.route('/api/cuenta_bancaria/<id>', methods=['PUT'])
def update_cuentas(id):
	cuentas = Cuenta_bancaria.query.get(id)
	if cuentas is None:
		return jsonify({'message': 'User does not exists'}), 404

	json = request.get_json(force=True)
	if json.get('balance') is None:
		return jsonify({'message': 'Bad request'}), 400

	cuentas.balance = json['balance']
	cuentas.update()

	return jsonify({'cuentas': cuentas.json() })

@app.route('/api/cuenta_bancaria/<id>', methods=['DELETE'])
def delete_cuentas(id):
	cuentas = Cuenta_bancaria.query.get(id)
	if cuentas is None:
		return jsonify({'message': 'El usuario no existe'}), 404

	cuentas.delete()

	return jsonify({'cuentas': cuentas.json() })






#___TABLA___Moneda___#
#Metodo para obtener algo de la tabla usuario#
@app.route ('/api/moneda', methods=['GET'])
def get_moneda():
    currency = [ moneda.json() for moneda in Moneda.query.all() ] 
    return jsonify({'currency': currency })

#Metodo para almacenar tal cosa en la tabla usuario#
@app.route('/api/moneda/', methods=['POST'])
def create_moneda():
    json = request.get_json(force=True)

    if json.get('nombre') is None:
        return jsonify({'message': 'El formato está mal'}), 400

    currency = Moneda.create(json['nombre'],json['sigla'])

    return jsonify({'currency': currency.json() })

#Metodo para reemplazar o crear un nuevo elemento#
@app.route('/api/moneda/<id>', methods=['PUT'])
def update_moneda(id):
    currency = Moneda.query.get(id)
    if currency is None:
        return jsonify({'message': 'currency does not exists'}), 404

    json = request.get_json(force=True)
    if json.get('nombre') is None:
        return jsonify({'message': 'Bad request'}), 400

    currency.nombre = json['nombre']
    currency.sigla = json['sigla']

    currency.update()
    return jsonify({'currency': currency.json() })

@app.route('/api/moneda/<id>', methods=['DELETE'])
def delete_moneda(id):
    currency = Moneda.query.filter_by(id=id).first()
    if currency is None:
        return jsonify({'message': 'currency no existe'}), 404

    currency.delete()

    return jsonify({'currency': currency.json() })





#___TABLA___PRECIO_MONEDA___#
#Metodo para obtener algo de la tabla precio_moneda#
@app.route ('/api/precio_moneda', methods=['GET'])
def get_precio_moneda():
    precio = [ precio_moneda.json() for precio_moneda in Precio_moneda.query.all() ] 
    return jsonify({'precio': precio })

#Metodo para almacenar tal cosa en la tabla usuario#
@app.route ('/api/precio_moneda', methods=['POST'])
def create_precio_moneda():
    json = request.get_json(force=True)
    if json.get('id') is None:
        return jsonify({'message': 'El formato está mal'}), 400

    currency = Precio_moneda.create(json['id'],json['valor'])

    return jsonify({'currency': currency.json() })

#Metodo para reemplazar o crear un nuevo elemento#
@app.route('/api/precio_moneda/<id>', methods=['PUT'])
def update_precio_monedas(id):
    json = request.get_json(force=True)
    precio = Precio_moneda.query.filter_by(fecha=json['fecha'],id=id).first()
    if precio is None:
        return jsonify({'message': 'currency does not exists'}), 404

    precio.valor = json['valor']

    precio.update()

    return jsonify({'precio': precio.json() })
@app.route('/api/precio_moneda/<id>', methods=['DELETE'])
def delete_precio_usuario(id):
    precio = Precio_moneda.query.filter_by(id=id).first()
    if precio is None:
        return jsonify({'message': 'moneda no existe'}), 404

    precio.delete()

    return jsonify({'precio': precio.json() })






#___TABLA___USUARIO_TIENE_MONEDA___#
#Metodo para obtener algo de la tabla usuario_tiene_moneda#
@app.route('/api/usuario_tiene_moneda', methods=['GET'])
def get_usuario_tiene_moneda():
    tener = [ moneda.json() for moneda in Usuario_tiene_moneda.query.all() ] 
    return jsonify({'tener': tener})

#Metodo para almacenar tal cosa en la tabla usuario_tiene_moneda#
@app.route('/api/usuario_tiene_moneda', methods=['POST'])
def create_usuario_tiene_moneda():
    json = request.get_json(force=True)
    if json.get('id_usuario') is None:
        return jsonify({'message': 'El formato está mal'}), 400

    currency = Usuario_tiene_moneda.create(json['id_usuario'],json['id_moneda'],json['balance'])

    return jsonify({'currency': currency.json() })

#Metodo para reemplazar o crear un nuevo elemento#
@app.route('/api/usuario_tiene_moneda/<id_usuario>/<id_moneda>', methods=['PUT'])
def update_usuario_tiene_moneda(id_usuario,id_moneda):
	user = Usuario_tiene_moneda.query.filter_by(id_usuario=id_usuario,id_moneda=id_moneda).first()
	if user is None:
		return jsonify({'message': 'User does not exists'}), 404
	json = request.get_json(force=True)
	if json.get('balance') is None:
		return jsonify({'message': 'Bad request'}), 400
	user.balance = json['balance']
	user.update()
	return jsonify({'user': user.json() })

@app.route('/api/usuario_tiene_moneda/<id_usuario>/<id_moneda>', methods=['DELETE'])
def delete_usuario_tiene_moneda(id_usuario,id_moneda):
    tener= Usuario_tiene_moneda.query.filter_by(id_usuario=id_usuario,id_moneda=id_moneda).first()
	
    if tener is None:
        return jsonify({'message': 'No existe'}), 404

    tener.delete()

    return jsonify({'tener': tener.json() })




##############################################################################################################################
#Consultas, solo se me pidieron 3#
@app.route('/api/consulta/2/<max_id>', methods=['GET'])
def get_custom(max_id):
	tasks = [dict(cuenta_bancaria) for cuenta_bancaria in Cuenta_bancaria.custom(max_id=max_id).fetchall()]
	return jsonify({'tasks': tasks })

@app.route('/api/consulta/4/<monedas>', methods=['GET'])
def get_precio_monedass(monedas):
	tasks = [dict(moneda) for moneda in Moneda.maximo_historico(monedas=monedas).fetchall()]
	return jsonify({'tasks': tasks })

@app.route('/api/consulta/5/<monedas>', methods=['GET'])
def get_precio_circulacion(monedas):
	tasks = [dict(moneda) for moneda in Moneda.circulacion(monedas=monedas).fetchall()]
	return jsonify({'tasks': tasks })


if __name__ == '__main__':
	app.run(debug=True)
