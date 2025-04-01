import random
from lingowords import words 
from colorama import Fore

print("Lingo is begonnen")
team_1 = input("team 1, Voer een naam in: ")
team_2 = input("team 2, Voer een naam in: ")

ronde_teller = 0 
pogingen = 0        

even_nummers = [i for i in range(2, 33, 2)]  
oneven_nummers = [i for i in range(1, 32, 2)]  

random.shuffle(even_nummers)
random.shuffle(oneven_nummers)

def maak_bingo_kaart(nummers):
    kaart = [nummers[i:i+4] for i in range(0, 16, 4)]
    return kaart

bingo_kaart_team1 = maak_bingo_kaart(even_nummers[:16])  
bingo_kaart_team2 = maak_bingo_kaart(oneven_nummers[:16])  

def print_bingo_kaart(kaart, team):
    print(f"\n🎉 Bingo Kaart voor {team}:")
    for rij in kaart:
        print(" | ".join(f"{n:2}" for n in rij))
    print("-" * 20)

print_bingo_kaart(bingo_kaart_team1, "Team 1 (Even)")
print_bingo_kaart(bingo_kaart_team2, "Team 2 (Oneven)")

















# # Bingo-kaart (4x4)
# def maak_bingo_kaart():
#     return [[0] * 4 for _ in range(4)]

# # Ballenbak met nummers (even = team 1, oneven = team 2) en speciale ballen
# BALLENBAK = [i for i in range(1, 17)] + ["groen", "groen", "groen", "rood", "rood", "rood"]

# # Functie om een willekeurig woord te kiezen uit de geïmporteerde lijst
# def kies_woord():
#     return random.choice(words)

# # Woordraden mechanisme
# def woord_raden(woord):
#     lengte = len(woord)
#     poging = 0
#     goed_geraden = False
#     hint = ["_"] * lengte
#     hint[0] = woord[0]  # Eerste letter tonen

#     print(woord)
#     print("\nLingo Spel - Raad het woord!")
#     print(" ".join(hint))

#     while poging < 5:
#         gok = input(f"Poging {poging+1}/5: ").lower()

#         if len(gok) != lengte:
#             print(f"Het woord moet {lengte} letters lang zijn!")
#             continue

#         if gok == woord:
#             print("Gefeliciteerd! Je hebt het woord geraden!")
#             return True
        
#         # Update hint
#         for i in range(lengte):
#             if gok[i] == woord[i]:
#                 hint[i] = f"\033[32m{gok[i]}\033[0m"  # Groen (juiste plek)
#             elif gok[i] in woord:
#                 hint[i] = f"\033[33m{gok[i]}\033[0m"  # Geel (verkeerde plek)
#             else:
#                 hint[i] = gok[i]  # Blijf wit

#         print(" ".join(hint))
#         poging += 1

#     print(f"Helaas, het woord was: {woord}")
#     return False

# # Ballenbak mechanisme
# def grabbelen(team, ballenbak):
#     ballen = []
#     for _ in range(2):
#         if not ballenbak:
#             break
#         bal = random.choice(ballenbak)
#         ballenbak.remove(bal)
#         ballen.append(bal)

#         if bal == "rood":
#             print(f"{team} heeft een \033[31mRODE\033[0m bal getrokken! ")
#             return ballen
#         elif bal == "groen":
#             print(f"{team} heeft een \033[32mGROENE\033[0m bal getrokken! ")
#         else:
#             print(f"{team} trekt bal nummer {bal}")

#     return ballen

# # Spel starten
# def start_spel():
#     team1_score = 0
#     team2_score = 0
#     rode_ballen_team1 = 0
#     rode_ballen_team2 = 0
#     fout_count_team1 = 0
#     fout_count_team2 = 0
#     bingo_kaart_team1 = maak_bingo_kaart()
#     bingo_kaart_team2 = maak_bingo_kaart()
#     ballenbak = BALLENBAK.copy()
    
#     while True:
#         for team in ["Team 1", "Team 2"]:
#             print(f"\n{team} is aan de beurt!")

#             woord = kies_woord()
#             if woord_raden(woord):
#                 if team == "Team 1":
#                     team1_score += 1
#                     fout_count_team1 = 0
#                 else:
#                     team2_score += 1
#                     fout_count_team2 = 0
                
#                 ballen = grabbelen(team, ballenbak)

#                 if "rood" in ballen:
#                     if team == "Team 1":
#                         rode_ballen_team1 += 1
#                     else:
#                         rode_ballen_team2 += 1

#                 if team == "Team 1" and team1_score >= 10:
#                     print(" Team 1 wint door 10 woorden goed te raden!")
#                     return
#                 if team == "Team 2" and team2_score >= 10:
#                     print(" Team 2 wint door 10 woorden goed te raden!")
#                     return

#                 if rode_ballen_team1 >= 3:
#                     print(" Team 1 heeft 3 rode ballen getrokken en verliest!")
#                     return
#                 if rode_ballen_team2 >= 3:
#                     print(" Team 2 heeft 3 rode ballen getrokken en verliest!")
#                     return

#             else:
#                 if team == "Team 1":
#                     fout_count_team1 += 1
#                 else:
#                     fout_count_team2 += 1
                
#                 if fout_count_team1 >= 3:
#                     print(" Team 1 heeft 3 woorden fout op rij en verliest!")
#                     return
#                 if fout_count_team2 >= 3:
#                     print(" Team 2 heeft 3 woorden fout op rij en verliest!")
#                     return

#         opnieuw = input("Wil je opnieuw spelen? (ja/nee): ").lower()
#         if opnieuw != "ja":
#             break

# # Start het spel
# start_spel()
