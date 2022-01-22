import json

class Data:

    def __init__(self):
       pass


    def get_date(self, nombre, identificador, contrasena, edad, pais, dominio):
        my_data = {}
        my_data['clientes'] = []

        my_data['clientes'].append({
            'nombre': nombre,
            'id': identificador,
            'contrasena': contrasena,
            'edad': edad,
            'pais': pais,
            'dominio': dominio})

        with open("./archivos/data.json", "w", encoding="utf-8") as f:
            json.dump(my_data, f, indent=4)
        return my_data