from user import User
from data import Data

user = User()
data = Data()


def run():
    nombre = input('Escribe tu nombre: ')
    edad = input('Escribe tu edad: ')
    pais = input('Escribe tu país: ')
    dominio = input('En que plataforma te encuentras: ')
    password = user.generate_password()
    id = user.generate_id()
    datos_usuarios = data.get_date(nombre, id, password, edad, pais, dominio)
    
    print(f'Hola {nombre.upper()} tu id es: {id} y tu contraseña es: {password}')

    

if __name__ == '__main__':
    while True:
        run()