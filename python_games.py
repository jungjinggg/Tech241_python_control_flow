import random

role_class = {"warrior": {"health": 14,
                          "damage": 1},
              "healer": {"health": 10,
                         "damage": 2},
              "mage": {"health": 7,
                       "damage": 4},
              "gunner": {"health": 8,
                         "damage": 3},
              "hunter": {"health": 8,
                         "damage": 3}}


def attack():
    roll_attack = random.randint(1, 4)
    return roll_attack


def defence():
    roll_defence = random.randint(1, 4)
    return roll_defence


# Game set up
player1_role = input("""Player 1 please select a character:
warrior
healer
mage
gunner
hunter: """)
print(f"Player1: {player1_role}")

player2_role = input("""\nPlayer2 please select a character:
warrior
healer
mage
gunner
hunter: """)
print(f"Player2: {player2_role}\n")

# player selection
if player1_role in role_class.keys():
    player1 = player1_role

if player2_role in role_class.keys():
    player2 = player2_role

player1_hp = role_class[player1_role]["health"]
player2_hp = role_class[player2_role]["health"]

game_on = True
while game_on:
    # player1 Turn
    print(f"\nplayer 1 current health {player1_hp}")
    print(f"player 2 current health {player2_hp}\n")

    if player1_hp <= 0:
        print("Game over! Player2 wins")
        game_on = False
        break
    else:
        print("player1 Attack Turn")
        attack_roll = attack()
        print(f"Your roll is {attack_roll}")

        defence_roll = defence()
        print(f"Player2's roll is {defence_roll}")

        if attack_roll > defence_roll:
            player2_hp -= role_class[player1_role]['damage']
            print(f"{role_class[player1_role]['damage']} damage inflicted! Player2's health point is {player2_hp}")
        elif attack_roll == defence_roll:
            print("You do no damage")
        else:
            player1_hp -= 1
            print(f"1 damage taken, your health point is {player1_hp}")

    # Player2 Turn
    if player2_hp <= 0:
        print("Game over! Player1 wins")
        game_on = False
        break

    else:
        print("\nPlayer2 Attack Turn")
        attack_roll = attack()
        print(f"Your roll is {attack_roll}")

        defence_roll = defence()
        print(f"Player1's roll is {defence_roll}")

        if attack_roll > defence_roll:
            player1_hp -= role_class[player2_role]['damage']
            print(f"{role_class[player2_role]['damage']} damage inflicted! Player1's health point is {player1_hp}")
        elif attack_roll == defence_roll:
            print("You do no damage")
        else:
            player2_hp -= 1
            print(f"1 Damage taken, your health point is {player2_hp}")
