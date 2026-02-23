class Hero:
    def __init__(self, type, name, age):
        self.type = type
        self.name = name
        self.age = age

    def attack(self):

        if self.type == "Mago":
            self.attack = "magia"
        elif self.type == "Guerreiro":
            self.attack = "espada"
        elif self.type == "Monge":
            self.attack = "artes marciais"
        else:
            self.attack = "shuriken"

        print(f"O {self.type} atacou usando {self.attack}")


def main():

    print("1- Mago")
    print("2- Guerreiro")
    print("3- Monge")
    print("4- Ninja")

    option = int(input("Escolha o tipo: "))

    name = input("Digite o nome do herói: ")
    age = int(input("Digite a idade: "))

    if option == 1:
        type = "Mago"
    elif option == 2:
        type = "Guerreiro"
    elif option == 3:
        type = "Monge"
    else:
        type = "Ninja"

    heroi = Hero(type=type, name=name, age=age)

    heroi.attack()

main()