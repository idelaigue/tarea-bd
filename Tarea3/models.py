from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from datetime import datetime


#Libreria SQL, por eso la inclusión del db. en la columna de los atributos#
db = SQLAlchemy()

# Creación de la entidad Usuario (user) #
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
		usuario = Usuario(nombre=nombre, apellido=apellido, correo=correo, contraseña=contraseña, pais=pais)
        #Creamos un nuevo usuario y lo guardamos en la bd, con sus respectivos atributos en un orden especifico#
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
			'fecha_registro': self.fecha_registro.strftime('%Y-%m-%d %H:%M:%S.%f') #Al usar Datatime este es el formato de la hora día, año, etc#
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
	def fechas(fechaini, fechafinal):
		try:
			resultado = db.session.execute('SELECT * FROM usuario WHERE fecha_registro >= :ini and fecha_registro <= :fin', {'ini': fechaini,'fin': fechafinal})
			return resultado
		except:
			return False
    
	def Mayor(usuarios):
		try:
			resultado = db.session.execute('SELECT usuario.nombre as "Nombre" , usuario.apellido as "Apellido", muv2.name_mon as "Nombre Moneda", muv2.bal as "Cantidad" FROM usuario INNER JOIN (SELECT muvs.nombre as name_mon, usuario_tiene_moneda.balance as bal, usuario_tiene_moneda.id_usuario as usu FROM usuario_tiene_moneda INNER join (SELECT nombre, id FROM moneda) as muvs on muvs.id=usuario_tiene_moneda.id_usuario)as muv2 on muv2.usu=usuario.id WHERE usuario.nombre= :usuarios ORDER BY muv2.bal desc LIMIT 1', {'usuarios': usuarios})
			return resultado
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
	__tablename__ = 'cuenta bancaria'
	numerocuenta = db.Column(db.Integer, primary_key=True)
	usuarios_id = db.relationship("Usuario")
    id_usuario = db.Column(db.Integer,db.ForeignKey('usuario.id'))
	balance = db.Column(db.Float, nullable=False)
	
	
	@classmethod
	def create(cls, id_usuario, balance):
		# Instanciamos un nuevo usuario y lo guardamos en la bd
		cuenta = Cuenta_bancaria(id_usuario=id_usuario, balance=balance)
		return cuenta.save()
	
	def custom(max_id):
		try:
			resultado = db.session.execute('SELECT * FROM cuenta_bancaria WHERE balance >= :max', {'max': max_id})
			return resultado
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
			'numero_cuenta': self.numerocuenta,
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


#Se crea la clase Moneda
class Moneda(db.Model):
    tablename="moneda"
    id = db.Column(db.Integer, primary_key=True)
    sigla= db.Column(db.String(10),nullable=False)
    nombre= db.Column(db.String(80),nullable=False)
    precio_monedas= db.relationship('Precio_moneda',cascade="all,delete",backref="parent",lazy='dynamic')
    usuario_tiene = db.relationship('Usuario_tiene_moneda',cascade="all,delete",backref="parent",lazy='dynamic')

    @classmethod
    def create(cls,sigla,nombre):
        #añadimos una nueva moneda y la guardamos en la bd
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

    def cambio_valor(fechaini,fechafinal):
        try:
            resultado= db.session.execute('SELECT agrup_id."Moneda", agrup_id."Veces que cambio el valor" FROM (SELECT moneda.nombre as "Moneda",COUNT(precio_moneda.valor) as "Veces que cambió valor" FROM moneda INNER JOIN precio_moneda on moneda.id=precio_moneda.id WHERE precio_moneda.fecha > :fechaini and precio_moneda.fecha < :fechafinal  GROUP BY moneda.id)AS agrup_id ORDER BY agrup_id."Veces que cambio el valor" desc LIMIT 1',{'fechaini':fechaini,'fechafin':fechafinal})
            return resultado
        except:
            return False

    def cambio_moneda(monedas):
        try:
            resultado = db.session.execute('SELECT nombre,sum(balance)as Cantidad_Total FROM moneda inner join usuario_tiene_moneda on moneda.id=usuario_tiene_moneda.id_moneda WHERE nombre= :moneda GROUP BY nombre',{'moneda':monedas})
            return resultado
        except:
            return False
	
    def maximo3(monedas):
        try:
            resultado = db.session.execute('SELECT nombre,COUNT(id) as cantidad FROM moneda inner join usuario_tiene_moneda on moneda.id=usuario_tiene_moneda.id_moneda GROUP BY nombre ORDER BY cantidad desc LIMIT 3')
            return resultado
        except:
            return False

    def maximo_historico(monedas):
        try:
            resultado= db.session.execute('SELECT nombre,max(precio_moneda.valor) as Valor_Maximo FROM moneda inner join precio_moneda on moneda.id=precio_moneda.id WHERE nombre= :moneda GROUP BY nombre',{'moneda':monedas})
            return resultado
        except:
            return False




#Se crea la clase precio_moneda
class Precio_moneda(db.Model):
    __tablename__="precio_moneda"
    id = db.Column(db.Integer, db.ForeignKey('moneda.id'),primary_key=True )
    moneda = db.relationship("Moneda")
    fecha= db.Column(db.DateTime, default=db.func.current_timestamp(),primary_key=True)
    valormon= db.Column(db.Float,nullable=False)

    @classmethod
    def create(cls,id,valormon):
        #obtenemos un nuevo valor de la moneda y lo guardamos en la bd
        precio_moneda=Precio_moneda(id=id,valormon=valormon)
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
            'fecha': self.fecha.strftime('%Y-%m-%d %H:%M:%S.%f'),
            'valor': self.valormon
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
	

#Se crea la clase usuario_tiene_moneda
class usuario_tiene_moneda(db.Model):
    __tablename__ ="Usuario tiene estas moneda"
    id_usuario = db.Column(db.Integer,db.ForeignKey("usuario.id"),primary_key=True)
    user = db.relationship("Usuario",foreign_keys=[id_usuario])
    id_moneda = db.Column(db.Integer,db.ForeignKey("moneda.id"),primary_key=True)
    moneda = db.relationship("Moneda",foreign_keys=[id_moneda])
    balance = db.Column(db.Float, nullable=False)

    @classmethod
    def create(cls, id_usuario, id_moneda, balance):
        usuario_tiene_moneda = Usuario_tiene_moneda(id_usuario=id_usuario,id_moneda=id_moneda,balance=balance)
        #Nuevo valor de la moneda que guardaremos en la bd#
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



			