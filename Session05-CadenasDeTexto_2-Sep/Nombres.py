Nombres = input("Escribe tu nombre: ")
apellidoPaterno = input("Escribe tu apellido paterno: ")
apellidoMaterno = input("Escribe tu apellido materno: ")

nombreCompleto = Nombres + " " + apellidoPaterno + " " + apellidoMaterno
print()
print("Tu nombre completo es: ", nombreCompleto)

Iniciales = Nombres[0] + apellidoPaterno[0] + apellidoMaterno[0]

print()
print("Tus iniciales son: ", Iniciales)

print()
print("Tu nombre al reves es: ", nombreCompleto[::-1])
print()
print("Numero de letras en tu nombre: ", len(Nombres+apellidoPaterno+apellidoMaterno))

print()
print("Veces que se repite la vocal 'a': ", nombreCompleto.count("a"))
print("Veces que se repite la vocal 'e': ", nombreCompleto.count("e"))
print("Veces que se repite la vocal 'i': ", nombreCompleto.count("i"))
print("Veces que se repite la vocal 'o': ", nombreCompleto.count("o"))
print("Veces que se repite la vocal 'u': ", nombreCompleto.count("u"))
