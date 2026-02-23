# Versão 2: utilizando um dicionário para armazenar os tipos de heróis.
#Obs.: Poderia ser feito com arrays, porém, teríamos um problema, já que as posições precisam bater certinho. (Dados paralelos
class Hero:

    types = {
        1: ("Mago", "magia", 100),
        2: ("Guerreiro", "espada", 50),
        3: ("Monge", "artes marciais", 70),
        4: ("Ninja", "shuriken", 30)
    }

    def __init__(self, type_num, name):

        if type_num not in self.types:
            raise ValueError("Tipo inválido!")

        self.name = name
        self.type, self.attack, self.age = self.types[type_num]

    def attack(self):
        print(f"O {self.type} atacou usando {self.attack}")

def main():

    type = int(input(
        "1- Mago\n"
        "2- Guerreiro\n"
        "3- Monge\n"
        "4- Ninja\n"
        "Escolha o tipo do herói:\n"
    ))

    name = input("Digite o nome do herói: ")
    hero = Hero(type, name=name)

    hero.attack()

main()