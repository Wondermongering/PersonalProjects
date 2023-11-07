#silly dice simulator


import random

def roll_dice(num_sides):
    "Role um único dado com um determinado número de faces"
    return random.randint(1, num_sides)

def simulate_dice_rolls(num_dice, num_sides):
    "Simulando roladas"
    roll_results = []
    for _ in range(num_dice):
        roll_result = roll_dice(num_sides)
        roll_results.append(roll_result)
    return roll_results

def main():
    "Função principal do rolador"
    print("Bem vindo os dados")

while True:
    try:
        num_dice = int(input("Quantos dados você quer rolar?"))
        num_sides = int(input("Quantos lados os dados têm?"))

        if num_dice <= 0 or num_sides <= 0:
            print("Os dados precisam ser positivos")
            continue

    except ValueError as e: 
                print("Input inválido: {e}")
                continue

    results = simulate_dice_rolls(num_dice, num_sides)
    total = sum(results)
    print(f"Você rolou: {results}")
    print(f"Total de roladas de dados:{total}")


    roll_again = input("Quer rolar de novo? (y/n):").lower()
    if roll_again != "y":
                print ("Obrigado por usar o simulador de dados")
                break

if __name__ == "__main__":
    main()
