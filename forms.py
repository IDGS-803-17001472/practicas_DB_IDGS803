from wtforms import Form
from wtforms import StringField, SelectField, RadioField, EmailField, IntegerField, DateField, DecimalField, BooleanField
from wtforms import validators

class EmpleadoForm(Form):
    id=IntegerField('id')
    nombre = StringField('nombre', [
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=10, message='ingresa un nombre valido')
    ])
    sueldo = DecimalField('sueldo',[
        validators.DataRequired(message='el campo es requerido'),
       validators.number_range(min=1, max=9999999999, message='valor no valido')
    ])
    telefono = IntegerField('telefono', [
        validators.DataRequired(message='el campo es requerido'),
       validators.number_range(min=1, max=9999999999, message='valor no valido')
    ])
    email = EmailField('email',[
        validators.Email(message='Ingrese un correo válido')
    ])
    direccion = StringField('direccion', [
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=100, message='ingresa una direccion valida')
    ])

class UserForm2(Form):
    id=IntegerField('id')
    nombre = StringField('nombre', [
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=10, message='ingresa un nombre valido')
    ])
    apaterno = StringField('apaterno',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=10, message='ingresa un nombre valido')
    ])
    email = EmailField('email',[
        validators.Email(message='Ingrese un correo válido')
    ])


class DicRegistroForm(Form):
    txtPalaIngles=StringField('txtPalaIngles',[
        validators.DataRequired(message='el campo es requerido')
    ])
    txtPalaEsp=StringField('txtPalaEsp',[
        validators.DataRequired(message='el campo es requerido')
    ])
class DicTraerPalabra(Form):
    txtPalaIngles=StringField('txtPalaIngles',[
        validators.DataRequired(message='el campo es requerido')
    ])
    txtPalaEsp=StringField('txtPalaEsp',[
        validators.DataRequired(message='el campo es requerido')
    ])

class PizzaForm(Form):
    tamanio= RadioField('Tamaño Pizza', choices=[('chica','Chica $40'),
                                           ('mediana','Mediana $80'),('grande','Grande $120')])
    jamon=BooleanField('jamon')
    pina=BooleanField('pina')
    champinones=BooleanField('champinones')
    cantidad = IntegerField('cantidad', [
        validators.DataRequired(message='el campo es requerido'),
       validators.number_range(min=1, max=30, message='valor no valido')
    ])

class VentaPizzaForm(Form):
    nombre=StringField('nombre',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=50, message='ingresa un nombre valido')
    ])
    direccion=StringField('direccion',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=50, message='ingresa una direccion valida')
    ])
    telefono=IntegerField('telefono', [
        validators.DataRequired(message='el campo es requerido'),
       validators.number_range(min=1, max=9999999999, message='valor no valido')
    ])
    

class ConsultaVentasForm(Form):
    filtro= SelectField('filtro', choices=[('0','Hoy'),('1', 'Dia'), ('2', 'Mes')])
    dia = SelectField('', choices=[
    ('0', 'Lunes'), 
    ('1', 'Martes'),
    ('2', 'Miércoles'), 
    ('3', 'Jueves'),
    ('4', 'Viernes'), 
    ('5', 'Sábado'), 
    ('6', 'Domingo')
])
    mes = SelectField('', choices=[
    ('1', 'Enero'), 
    ('2', 'Febrero'), 
    ('3', 'Marzo'), 
    ('4', 'Abril'), 
    ('5', 'Mayo'), 
    ('6', 'Junio'), 
    ('7', 'Julio'),
    ('8', 'Agosto'), 
    ('9', 'Septiembre'),
    ('10', 'Octubre'), 
    ('11', 'Noviembre'),
    ('12', 'Diciembre')
]) 