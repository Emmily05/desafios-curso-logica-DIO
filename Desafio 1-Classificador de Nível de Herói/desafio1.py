def classifies_hero_level(xp_hero):
    if xp_hero <= 1000:
        return "ferro"
    elif xp_hero <= 2000:
        return "bronze"
    elif xp_hero <= 5000:
        return "prata"
    elif xp_hero <= 7000:
        return "ouro"
    elif xp_hero <= 8000:
        return "platina"
    elif xp_hero <= 9000:           
        return "ascendente"
    elif xp_hero <= 10000:
        return "imortal"
    else:
        return "radiante"

def main():
    name_hero = input("Digite o nome do herói: ")
    xp_hero = int(input("Digite a quantidade de XP do herói: "))

    level = classifies_hero_level(xp_hero)
    print(f"O Herói de nome {name_hero} está no nível de {level}") 
    
