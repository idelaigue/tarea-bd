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
from flask import request

def create_app(enviroment):
	app = Flask(__name__)
	app.config.from_object(enviroment)
	with app.app_context():
		db.init_app(app)
		db.create_all()
	return app

# Accedemos a la clase config del archivo config.py
enviroment = config['development']
app = create_app(enviroment)



#### Tabla usuario ####
@app.route('/api/v1/usuario', methods=['GET'])
def get_usuario():
	users = [ usuario.json() for usuario in Usuario.query.all() ] 
	return jsonify({'users': users })

@app.route('/api/v1/usuario/', methods=['POST'])
def create_usuario():
	json = request.get_json(force=True)

	if json.get('nombre') is None:
		return jsonify({'message': 'El formato está mal'}), 400

	user = Usuario.create(json['nombre'],json['apellido'],json['correo'],json['contraseña'],json['pais'])

	return jsonify({'user': user.json() })

@app.route('/api/v1/usuario/<id>', methods=['PUT'])
def update_usuario(id):
	user = Usuario.query.filter_by(id=id).first()
	if user is None:
		return jsonify({'message': 'User does not exists'}), 404

	json = request.get_json(force=True)
	if json.get('nombre') is None:
		return jsonify({'message': 'Bad request'}), 400

	user.nombre = json['nombre']
	user.apellido = json['apellido']
	user.correo = json['correo']
	user.contraseña = json['contraseña']
	user.pais = json['pais']

	user.update()

	return jsonify({'user': user.json() })

@app.route('/api/v1/usuario/<id>', methods=['DELETE'])
def delete_usuario(id):
	user = Usuario.query.filter_by(id=id).first()
	if user is None:
		return jsonify({'message': 'El usuario no existe'}), 404

	user.delete()

	return jsonify({'user': user.json() })

### tabla Pais ###

@app.route('/api/v1/pais', methods=['GET'])
def get_pais():
	paises = [ pais.json() for pais in Pais.query.all() ] 
	return jsonify({'paises': paises })

@app.route('/api/v1/pais/', methods=['POST'])
def create_pais():
	json = request.get_json(force=True)

	if json.get('nombre') is None:
		return jsonify({'message': 'El formato está mal'}), 400

	paises = Pais.create(json['nombre'])

	return jsonify({'paises': paises.json() })

@app.route('/api/v1/pais/<id>', methods=['PUT'])
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

@app.route('/api/v1/pais/<id>', methods=['DELETE'])
def delete_pais(id):
	paises = Pais.query.get(id)
	if paises is None:
		return jsonify({'message': 'El usuario no existe'}), 404

	paises.delete()

	return jsonify({'paises': paises.json() })

### tabla cuenta bancaria ###

@app.route('/api/v1/cuenta_bancaria', methods=['GET'])
def get_cuentas():
	cuentas = [ cuenta_bancaria.json() for cuenta_bancaria in Cuenta_bancaria.query.all() ] 
	return jsonify({'cuentas': cuentas })

@app.route('/api/v1/cuenta_bancaria/', methods=['POST'])
def create_cuentas():
	json = request.get_json(force=True)

	if json.get('id_usuario') is None:
		return jsonify({'message': 'El formato está mal'}), 400

	cuentas = Cuenta_bancaria.create(json['id_usuario'],json['balance'])

	return jsonify({'cuentas': cuentas.json() })

@app.route('/api/v1/cuenta_bancaria/<id>', methods=['PUT'])
def update_cuentas(id):
	cuentas = Cuenta_bancaria.query.get(id)
	if cuentas is None:
		return jsonify({'message': 'User does not exists'}), 404

	json = request.get_json(force=True)
	if json.get('id_usuario') is None:
		return jsonify({'message': 'Bad request'}), 400

	cuentas.id_usuario = json['id_usuario']
	cuentas.balance = json['balance']
	cuentas.update()

	return jsonify({'cuentas': cuentas.json() })

@app.route('/api/v1/cuenta_bancaria/<id>', methods=['DELETE'])
def delete_cuentas(id):
	cuentas = Cuenta_bancaria.query.get(id)
	if cuentas is None:
		return jsonify({'message': 'El usuario no existe'}), 404

	cuentas.delete()

	return jsonify({'cuentas': cuentas.json() })

#### Tabla Moneda ####
@app.route ('/api/v1/moneda', methods=['GET'])
def get_moneda():
    currency = [ moneda.json() for moneda in Moneda.query.all() ] 
    return jsonify({'currency': currency })

@app.route('/api/v1/moneda/', methods=['POST'])
def create_moneda():
    json = request.get_json(force=True)

    if json.get('nombre') is None:
        return jsonify({'message': 'El formato está mal'}), 400

    currency = Moneda.create(json['nombre'],json['sigla'])

    return jsonify({'currency': currency.json() })

@app.route('/api/v1/moneda/<id>', methods=['PUT'])
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

@app.route('/api/v1/moneda/<id>', methods=['DELETE'])
def delete_moneda(id):
    currency = Moneda.query.filter_by(id=id).first()
    if currency is None:
        return jsonify({'message': 'currency no existe'}), 404

    currency.delete()

    return jsonify({'currency': currency.json() })


#### Tabla Precio moneda #####

@app.route ('/api/v1/precio_moneda', methods=['GET'])
def get_precio_moneda():
    precio = [ precio_moneda.json() for precio_moneda in Precio_moneda.query.all() ] 
    return jsonify({'precio': precio })

@app.route ('/api/v1/precio_moneda', methods=['POST'])
def create_precio_moneda():
    json = request.get_json(force=True)
    if json.get('id') is None:
        return jsonify({'message': 'El formato está mal'}), 400

    currency = Precio_moneda.create(json['id'],json['valor'])

    return jsonify({'currency': currency.json() })

@app.route('/api/v1/precio_moneda/<id>', methods=['PUT'])
def update_precio_monedas(id):
    precio = Precio_moneda.query.filter_by(id=id).first()
    if precio is None:
        return jsonify({'message': 'currency does not exists'}), 404

    json = request.get_json(force=True)
    
    precio.id = json['id']
    precio.valor = json['valor']

    precio.update()

    return jsonify({'precio': precio.json() })
@app.route('/api/v1/precio_moneda/<id>', methods=['DELETE'])
def delete_precio_usuario(id):
    precio = Precio_moneda.query.filter_by(id=id).first()
    if precio is None:
        return jsonify({'message': 'moneda no existe'}), 404

    precio.delete()

    return jsonify({'precio': precio.json() })

###### usuario tiene moneda #####
@app.route('/api/v1/usuario_tiene_moneda', methods=['GET'])
def get_usuario_tiene_moneda():
    tener = [ moneda.json() for moneda in Usuario_tiene_moneda.query.all() ] 
    return jsonify({'tener': tener})

@app.route('/api/v1/usuario_tiene_moneda', methods=['POST'])
def create_usuario_tiene_moneda():
    json = request.get_json(force=True)
    if json.get('id_usuario') is None:
        return jsonify({'message': 'El formato está mal'}), 400

    currency = Usuario_tiene_moneda.create(json['id_usuario'],json['id_moneda'],json['balance'])

    return jsonify({'currency': currency.json() })

@app.route('/api/v1/usuario_tiene_moneda/<id_usuario>', methods=['PUT'])
def update_usuario_tiene_moneda(id_usuario):
	user = Usuario_tiene_moneda.query.filter_by(id_usuario=id_usuario).first()
	if user is None:
		return jsonify({'message': 'User does not exists'}), 404

	json = request.get_json(force=True)
	if json.get('id_usuario') is None:
		return jsonify({'message': 'Bad request'}), 400

	user.id_usuario = json['id_usuario']
	user.id_moneda = json['id_moneda']
	user.balance = json['balance']

	user.update()

	return jsonify({'user': user.json() })

@app.route('/api/v1/usuario_tiene_moneda/<id_usuario>', methods=['DELETE'])
def delete_usuario_tiene_moneda(id_usuario):
    tener= Usuario_tiene_moneda.query.filter_by(id_usuario=id_usuario).first()
    if tener is None:
        return jsonify({'message': 'No existe'}), 404

    tener.delete()

    return jsonify({'tener': tener.json() })


### Consultas ####
@app.route('/api/v1/cuenta_bancaria/max_id/<max_id>', methods=['GET'])
def get_custom(max_id):
	tasks = [dict(cuenta_bancaria) for cuenta_bancaria in Cuenta_bancaria.custom(max_id=max_id).fetchall()]
	return jsonify({'tasks': tasks })

@app.route('/api/v1/consulta/1/<id>', methods=['GET'])
def get_tasks_user(id):
	tasks_users = [ {**(pais.json()),**(usuario.json())} for pais,usuario in db.session.query(Pais,Usuario).join(Usuario, Pais.cod_pais == Usuario.pais).filter(Pais.nombre == id).all()]
	return jsonify({'tasks_users': tasks_users })

@app.route('/api/v1/consulta/2/<id>', methods=['GET'])
def get_precio_historico(id):
	tasks_users = [ {**(moneda.json()),**(precio_moneda.json())} for moneda,precio_moneda in db.session.query(Moneda,Precio_moneda).join(Precio_moneda, Moneda.id == Precio_moneda.id).filter(Moneda.nombre == id).all()]
	return jsonify({'tasks_users': tasks_users })


if __name__ == '__main__':
	app.run(debug=True)
