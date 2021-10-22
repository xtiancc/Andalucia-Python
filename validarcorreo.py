print("VALIDAR CORREO")
print("--------------")

mail = input("Por favor, indique un correo electrónico: ")

# Validar:
# Que el mail tenga un @
# Que tengamos un punto (.)
# Que el mail no empiece ni termine con @ ni punto
# Que el mail solo tenga un @
# Que contenga un punto (.) después del @
# Que el dominio (.com) tenga de 2 a 4 char

hosting = mail[mail.find("@") + 1:]
dominio = mail[mail.find(".") + 1:]

if ((
    mail.__contains__("@"))
    and mail.__contains__(".")
    and (mail.startswith("@") or mail.endswith("@") or mail.startswith(".") or mail.endswith(".")) is False
    and (hosting.__contains__("@")) is False
    and (hosting.__contains__("."))
    and (len(dominio) >= 2 and len(dominio) <= 4)
    ):
    print("¡Está bien!")
else:
    print("Está mal.")

print("FIN DEL PROGRAMA")
