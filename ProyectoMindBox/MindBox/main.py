from menu.menu import Menu
from usuario import Usuario
from estudiante import Estudiante
from maestro import Maestro
from coordinador import Coordinador

# Usuarios de prueba
usuarios_registrados = {
    'estudiante1': {'password': '1234', 'role': 'estudiante'},
    'maestro1': {'password': 'abcd', 'role': 'maestro'},
    'coordinador1': {'password': 'coor123', 'role': 'coordinador'}
}
# main.py


def main():
    coordinador1 = Coordinador("Karen", "karen@correo.com", "1234", 50000, "RFC123456", 5)
    print(coordinador1.mostrar_informacion())

if __name__ == "__main__":
    main()

def iniciar_sesion():
    print("Bienvenido al sistema")
    usuario = input("Ingrese su usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    if usuario in usuarios_registrados and usuarios_registrados[usuario]['password'] == contrasena:
        print(f"Bienvenido {usuario}")
        return usuarios_registrados[usuario]['role']
    else:
        print("Usuario o contraseña incorrectos")
        return None

if __name__ == "__main__":
    role = iniciar_sesion()

    if role == 'estudiante':
        print("Eres un estudiante")
        estudiante = Estudiante()
        Menu(estudiante).mostrar_menu()

    elif role == 'maestro':
        print("Eres un maestro")
        maestro = Maestro()
        Menu(maestro).mostrar_menu()

    elif role == 'coordinador':
        print("Eres el coordinador")
        Menu().mostrar_menu()

    else:
        print("No se pudo iniciar sesión correctamente.")
