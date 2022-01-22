import random

MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

class User:

    def __init__(self):
        pass


    def generate_password(self):

        caracteres =  MAYUS + MINUS + NUMS +CHARS
        contrasena = []
        
        for i in range(15):
            caracter_random = random.choice(caracteres)
            contrasena.append(caracter_random)
        
        contrasena = ''.join(contrasena)
        return contrasena



    def generate_id(self):
        
        NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        id = []

        for i in range(5):
            caracter_random_id = random.choice(NUMS)
            id.append(caracter_random_id)
        id = ''.join(id)
        return id