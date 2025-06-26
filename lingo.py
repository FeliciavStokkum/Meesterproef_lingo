# === Imports ===
import random
from lingowords import words
from colorama import Fore, Style, init
init(autoreset=True)

# === Bingo kaart genereren ===
def maak_bingo_kaart(soort):
    kaart = []  # Lege bingo kaart

    # Kies 16 willekeurige even of oneven getallen
    if soort == "even":
        getallen = random.sample(range(2, 100, 2), 16)
    elif soort == "oneven":
        getallen = random.sample(range(1, 100, 2), 16)

    # Verdeel de getallen over 4 rijen
    for i in range(0, 16, 4):
        rij = getallen[i:i+4]
        kaart.append(rij)
    return kaart

#Toon de bingokaart voor elk team
def print_bingo_kaart(kaart, team):
    print("\nBingo Kaart voor", team + ":")
    for rij in kaart:
        print("\t".join(str(getal) for getal in rij))


#markeer de bingo kaart als het nummer correct is
def markeer_bingo_kaart(kaart, nummer):
    for rij in kaart:
        for i in range(len(rij)):
            if rij[i] == nummer:
                rij[i] = Fore.MAGENTA + str(nummer) + Fore.RESET

#check of de je bingo hebt
def is_roze(waarde):
    return isinstance(waarde, str) and waarde.startswith(Fore.MAGENTA)

def check_bingo(kaart):
    # Horizontaal
    for rij in kaart:
        if all(is_roze(v) for v in rij):
            return True

    # Verticaal
    for kolom in range(4):
        if all(is_roze(kaart[rij][kolom]) for rij in range(4)):
            return True

    # Diagonaal ↘
    if all(is_roze(kaart[i][i]) for i in range(4)):
        return True

    # Diagonaal ↙
    if all(is_roze(kaart[i][3 - i]) for i in range(4)):
        return True

    return False

#Woord kiezen en raden
def kies_woord():
    return random.choice(words)

def woord_raden(woord):
    lengte = len(woord)
    poging = 0
    hint = ["_"] * lengte
    hint[0] = woord[0]

    print(woord)
    print("\nLingo Spel - Raad het woord!")
    print(" ".join(hint))

    while poging < 5:
        gok = input(f"Poging {poging+1}/5: ").lower()

        if len(gok) != lengte:
            print(f"Het woord moet {lengte} letters lang zijn!")
            continue

        if gok == woord:
            print(Fore.GREEN + "Gefeliciteerd! Je hebt het woord geraden!" + Fore.RESET)
            return True

        nieuwe_hint = []
        for i in range(lengte):
            if gok[i] == woord[i]:
                hint[i] = gok[i]
                nieuwe_hint.append(Fore.GREEN + gok[i] + Fore.RESET)
            elif gok[i] in woord:
                nieuwe_hint.append(Fore.YELLOW + gok[i] + Fore.RESET)
            else:
                nieuwe_hint.append(gok[i])

        print(" ".join(nieuwe_hint))
        poging += 1

    print(f"Helaas, het woord was: {woord}")
    return False

#Ballenbak mechanisme
def grabbelen(team_naam, ballenbak):
    ballen = []
    for i in range(2):
        if not ballenbak:
            break
        bal = random.choice(ballenbak)
        ballenbak.remove(bal)
        ballen.append(bal)

        if bal == "rood":
            print(f"{team_naam} heeft een {Fore.RED}RODE{Fore.RESET} bal getrokken!")
            break  # Geen tweede bal als eerste rood
        elif bal == "groen":
            print(f"{team_naam} heeft een {Fore.GREEN}GROENE{Fore.RESET} bal getrokken!")
        else:
            print(f"{team_naam} trekt bal nummer {bal}")

    return ballen

# === Spel starten ===
def start_spel():
    print("Lingo is begonnen!")
    team_1 = input("Team 1, voer een naam in: ")
    team_2 = input("Team 2, voer een naam in: ")

    while True:
        kaart1 = maak_bingo_kaart("even")    # Team 1 krijgt even kaart
        kaart2 = maak_bingo_kaart("oneven")  # Team 2 krijgt oneven kaart

        print_bingo_kaart(kaart1, team_1)
        print_bingo_kaart(kaart2, team_2)

        score1 = score2 = fout1 = fout2 = rood1 = rood2 = groen1 = groen2 = 0
        ballenbak = list(range(1, 33)) + ["groen"] * 3 + ["rood"] * 3

        while True:
            # === Beurt Team 1 ===
            print(f"\n {team_1} is aan de beurt!")
            if woord_raden(kies_woord()):
                score1 += 1
                fout1 = 0
                ballen = grabbelen(team_1, ballenbak)

                gewijzigd = False
                for bal in ballen:
                    if isinstance(bal, int):
                        markeer_bingo_kaart(kaart1, bal)
                        gewijzigd = True
                        if check_bingo(kaart1):
                            print_bingo_kaart(kaart1, team_1)
                            print(f"{team_1} wint met een bingo-lijn!")
                            return
                    elif bal == "rood":
                        rood1 += 1
                    elif bal == "groen":
                        groen1 += 1

                if gewijzigd:
                    print_bingo_kaart(kaart1, team_1)

                if score1 >= 10:
                    print(f" {team_1} wint met 10 juiste woorden!")
                    return
                if rood1 >= 3:
                    print(f" {team_1} verliest met 3 rode ballen!")
                    return
                if groen1 >= 3:
                    print(f" {team_1} wint met 3 groene ballen!")
                    return
            else:
                fout1 += 1
                if fout1 >= 3:
                    print(f" {team_1} verliest met 3 foute woorden!")
                    return

            # === Beurt Team 2 ===
            print(f"\n {team_2} is aan de beurt!")
            if woord_raden(kies_woord()):
                score2 += 1
                fout2 = 0
                ballen = grabbelen(team_2, ballenbak)

                gewijzigd = False
                for bal in ballen:
                    if isinstance(bal, int):
                        markeer_bingo_kaart(kaart2, bal)
                        gewijzigd = True
                        if check_bingo(kaart2):
                            print_bingo_kaart(kaart2, team_2)
                            print(f" {team_2} wint met een bingo-lijn!")
                            return
                    elif bal == "rood":
                        rood2 += 1
                    elif bal == "groen":
                        groen2 += 1

                if gewijzigd:
                    print_bingo_kaart(kaart2, team_2)

                if score2 >= 10:
                    print(f" {team_2} wint met 10 juiste woorden!")
                    return
                if rood2 >= 3:
                    print(f" {team_2} verliest met 3 rode ballen!")
                    return
                if groen2 >= 3:
                    print(f" {team_2} wint met 3 groene ballen!")
                    return
            else:
                fout2 += 1
                if fout2 >= 3:
                    print(f" {team_2} verliest met 3 foute woorden!")
                    return

        opnieuw = input("Wil je opnieuw spelen? (ja/nee): ").lower()
        if opnieuw != "ja":
            break

#Start het spel
start_spel()