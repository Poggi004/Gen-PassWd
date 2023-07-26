# Librerias Necesarias
import secrets
import string


# Definicion de Variables
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars


# Longitud de la contraseña solicitada al usuario
while True:
    try:
        pwd_length = int(input("Ingresa la longitud deseada para la contraseña: "))
        if pwd_length < 1:
            print("Por favor, ingresa un número positivo mayor a cero.")
        else:
            break
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Crea la contraseña
pwd = ''

for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alphabet))

print("Contraseña generada:")
print(pwd)

# Generar Restricciones de Reunion de Contraseña
while True:
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))

    if (any(char in special_chars for char in pwd) and 
        sum(char in digits for char in pwd) >= 2):
        break

print("Contraseña con restricciones generada:")
print(pwd)

# Para que se cierre el programa
input("Presiona Enter para salir...")
