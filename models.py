from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()

# Creamos la entidad User

class Usuario(db.Model):
	__tablename__ = 'usuario'
	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String(50), nullable=False)
	apellido = db.Column(db.String(50), nullable=False)
	correo = db.Column(db.String(50), nullable=False)
	contraseña = db.Column(db.String(50), nullable=False)
	pais = db.Column(db.Integer,db.ForeignKey('pais.cod_pais'))
	pais_id = db.relationship("Pais")
	fecha_registro = db.Column(db.DateTime, default=db.func.current_timestamp())
	cuentas = db.relationship('Cuenta_bancaria',cascade="all,delete", lazy='dynamic')
	monedas_usuario = db.relationship('Usuario_tiene_moneda', cascade="all,delete", lazy='dynamic')
	
	@classmethod
	def create(cls, nombre, apellido, correo, contraseña, pais):
		# Instanciamos un nuevo usuario y lo guardamos en la bd
		usuario = Usuario(nombre=nombre, apellido=apellido, correo=correo, contraseña=contraseña, pais=pais)
		return usuario.save()

	def save(self):
		try:
			db.session.add(self)
			db.session.commit()

			return self
		except:
			return False
	def json(self):
		return {
			'id': self.id,
			'nombre': self.nombre,
			'apellido':self.apellido,
			'correo':self.correo,
			'contraseña':self.contraseña,
			'pais':self.pais,
			'fecha_registro': self.fecha_registro
		}
	def update(self):
		self.save()
	def delete(self):
		try:
			db.session.delete(self)
			db.session.commit()

			return True
		except:
			return False


class Pais(db.Model):
	__tablename__ = 'pais'
	cod_pais = db.Column(db.Integer, primary_key=True)
	usuarios = db.relationship('Usuario', cascade="all,delete", lazy='dynamic')
	nombre = db.Column(db.String(50), nullable=False)
	
	
	@classmethod
	def create(cls, nombre):
		# Instanciamos un nuevo usuario y lo guardamos en la bd
		paises = Pais(nombre=nombre)
		return paises.save()

	def save(self):
		try:
			db.session.add(self)
			db.session.commit()

			return self
		except:
			return False
	def json(self):
		return {
			'cod_pais': self.cod_pais,
			'nombre': self.nombre
		}
	def update(self):
		self.save()
	def delete(self):
		try:
			db.session.delete(self)
			db.session.commit()

			return True
		except:
			return False


class Cuenta_bancaria(db.Model):
	__tablename__ = 'cuenta_bancaria'
	numero_cuenta = db.Column(db.Integer, primary_key=True)
	id_usuario = db.Column(db.Integer,db.ForeignKey('usuario.id'))
	usuarios_id = db.relationship("Usuario")
	balance = db.Column(db.Float, nullable=False)
	
	
	@classmethod
	def create(cls, id_usuario, balance):
		# Instanciamos un nuevo usuario y lo guardamos en la bd
		cuenta = Cuenta_bancaria(id_usuario=id_usuario, balance=balance)
		return cuenta.save()
	
	def custom(max_id):
		try:
			result = db.session.execute('SELECT * FROM cuenta_bancaria WHERE balance >= :max', {'max': max_id})
			return result
		except:
			return False

	def save(self):
		try:
			db.session.add(self)
			db.session.commit()

			return self
		except:
			return False
	def json(self):
		return {
			'numero_cuenta': self.numero_cuenta,
			'id_usuario': self.id_usuario,
			'balance': self.balance
		}
	def update(self):
		self.save()
	def delete(self):
		try:
			db.session.delete(self)
			db.session.commit()

			return True
		except:
			return False

class Moneda(db.Model):
    tablename="moneda"
    id = db.Column(db.Integer, primary_key=True)
    sigla= db.Column(db.String(10),nullable=False)
    nombre= db.Column(db.String(80),nullable=False)
    precio_monedas= db.relationship('Precio_moneda',cascade="all,delete",backref="parent",lazy='dynamic')
    usuario_tiene = db.relationship('Usuario_tiene_moneda',cascade="all,delete",backref="parent",lazy='dynamic')
    @classmethod
    def create(cls,sigla,nombre):
        #instanciamos una nueva moneda y lo guardamos en la bd
        moneda=Moneda(nombre=nombre,sigla=sigla)
        return moneda.save()
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()

            return self
        except:
            return False
    def json(self):
        return {
            'id': self.id,
            'sigla': self.sigla,
            'nombre': self.nombre
        }
    def update(self):
        self.save()
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()

            return True
        except:
            return False


class Precio_moneda(db.Model):
    __tablename__="precio_moneda"
    id = db.Column(db.Integer, db.ForeignKey('moneda.id'),primary_key=True )
    moneda = db.relationship("Moneda")
    fecha= db.Column(db.DateTime, default=db.func.current_timestamp(),primary_key=True)
    valor= db.Column(db.Float,nullable=False)

    @classmethod
    def create(cls,id,valor):
        #instanciamos un nuevo valor a una moneda y lo guardamos en la bd
        precio_moneda=Precio_moneda(id=id,valor=valor)
        return precio_moneda.save()
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()

            return self
        except:
            return False
    def json(self):
        return {
            'id': self.id,
            'fecha': self.fecha,
            'valor': self.valor
        }
    def update(self):
        self.save()
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()

            return True
        except:
            return False
	


class Usuario_tiene_moneda(db.Model):
    __tablename__ ="usuario_tiene_moneda"
    id_usuario = db.Column(db.Integer,db.ForeignKey("usuario.id"),primary_key=True)
    user = db.relationship("Usuario",foreign_keys=[id_usuario])
    id_moneda = db.Column(db.Integer,db.ForeignKey("moneda.id"),primary_key=True)
    moneda = db.relationship("Moneda",foreign_keys=[id_moneda])
    balance = db.Column(db.Float, nullable=False)

    @classmethod
    def create(cls, id_usuario, id_moneda, balance):
        #instanciamos un nuevo valor a una moneda y lo guardamos en la bd
        usuario_tiene_moneda = Usuario_tiene_moneda(id_usuario=id_usuario,id_moneda=id_moneda,balance=balance)
        return usuario_tiene_moneda.save()
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()

            return self
        except:
            return False
    def json(self):
        return {
            'id_usuario': self.id_usuario,
            'id_moneda': self.id_moneda,
            'balance': self.balance
        }
    def update(self):
        self.save()
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()

            return True
        except:
            return False



			