print(10 > 2)
print(10> 2 > 4)
print(10 >= 3)
print(2.2 >=2)


print(30 == 40)
print("ctrlplay" == "cltrPlay")
print(9.1 == 9)

print(9 != 6)


if True:
    print("voce e legal")

brincoucomfogo = True
if brincoucomfogo:
    print("voce se queimou!")

SeAcordouAtrasado = True
if SeAcordouAtrasado:
    print("voce se atrasou!")

SeAcordouAtrasado = input("voce se atrasou? ")
if SeAcordouAtrasado == "sim":
    print("voce perdeu o horario")
elif SeAcordouAtrasado == "nao":
    print("voce nao se atrasou!")


nome = input("qual e o seu nome? ")
idade = int(input("quantos anos voce tem?"))
cidade = input("onde voce mora? ")
print("ola", nome, "!")

if idade >18:
    print("voce e maior de idade!")
elif idade <18:
    print("voce e menor de idade!")
else:
    print("encerrando programa...")