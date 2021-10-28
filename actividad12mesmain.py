from actividad12mesclass import Mes

print("MESES Y TEMPERATURAS")
print("--------------------")

meslist = []

for i in range(12):
    mes = Mes()
    mes.name = "Mes " + str(i+1)
    meslist.append(mes)

for mes in meslist:
    print(mes)
