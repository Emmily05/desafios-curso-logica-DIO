def ranked_win_loss_balance(wins, losses):
    return wins - losses

def classify_hero_level(wins):
    if wins < 10:
        return "ferro"
    elif wins < 20:
        return "bronze"
    elif wins < 50:
        return "prata"
    elif wins < 80:
        return "ouro"
    elif wins < 90:
        return "diamante"
    elif wins < 100:
        return "lendário"
    else:
        return "imortal"
    
def main():
    wins = int(input("Digite o número de vitórias do herói:"))
    losses = int(input("Digite o número de derrotas do herói:"))
    balance = ranked_win_loss_balance(wins, losses)
    level = classify_hero_level(wins)

    print(f"O Herói tem de saldo de {balance} está no nível de **{level}**")
