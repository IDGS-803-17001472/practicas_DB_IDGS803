from wtforms import Form
from wtforms import StringField, SelectField, RadioField, EmailField, IntegerField, DecimalField
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