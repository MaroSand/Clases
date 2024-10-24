
def comprobarLogin(usuarioIngresado, contraseniaIngresada):
    if (usuarioIngresado == estUsuario and contraseniaIngresada == estContrasenia):
        print("Ha ingresado correctamente!")
        return True
    else:
        print("Lo siento, datos incorrectos! Pruebe nuevamente,",intentos,"/3 intentos, le quedan: ",3-intentos," intentos.")
        return False

estUsuario = "usuario1"
estContrasenia = "asdasd"
intentos = 1

while (intentos <= 3):

    usuarioIngresado = input("Ingrese el usuario: ")
    contraseniaIngresada = input("Ingrese la contraseña: ")

    if (comprobarLogin(usuarioIngresado, contraseniaIngresada) == True):
        break
    else:
        intentos = intentos + 1
if(intentos >=3):
    print("Lo siento, se le ha denegado el acceso.")




