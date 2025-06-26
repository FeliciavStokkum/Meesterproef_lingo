from colorama import Fore, init
from lingo_functies import (
    maak_bingo_kaart, markeer_bingo_kaart, check_bingo,
    grabbelen, is_roze
)
import random

init(autoreset=True)

def test_maak_bingo_kaart_even():
    print("🔹 Test: maak_bingo_kaart (even)")
    kaart = maak_bingo_kaart("even")
    print("Gegenereerde kaart:", kaart)
    assert len(kaart) == 4
    for rij in kaart:
        assert len(rij) == 4
        for getal in rij:
            assert getal % 2 == 0
    print("✅ Test geslaagd: alle getallen zijn even.\n")


def test_maak_bingo_kaart_oneven():
    print("🔹 Test: maak_bingo_kaart (oneven)")
    kaart = maak_bingo_kaart("oneven")
    print("Gegenereerde kaart:", kaart)
    assert len(kaart) == 4
    for rij in kaart:
        assert len(rij) == 4
        for getal in rij:
            assert getal % 2 == 1
    print("✅ Test geslaagd: alle getallen zijn oneven.\n")


def test_markeer_bingo_kaart_en_is_roze():
    print("🔹 Test: markeer_bingo_kaart en is_roze")
    kaart = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    markeer_bingo_kaart(kaart, 6)
    print("Kaart na markeren:")
    for rij in kaart:
        print("\t".join(str(getal) for getal in rij))

    assert is_roze(kaart[1][1])
    assert kaart[1][1].startswith(Fore.MAGENTA)
    assert not is_roze(kaart[0][0])
    print("✅ Test geslaagd: 6 is roze, andere getallen niet.\n")


def test_check_bingo_horizontaal():
    print("🔹 Test: check_bingo horizontaal")
    kaart = [[Fore.MAGENTA + str(i) + Fore.RESET for i in range(4)], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    assert check_bingo(kaart)
    print("✅ Test geslaagd: horizontale bingo gedetecteerd.\n")


def test_check_bingo_verticaal():
    print("🔹 Test: check_bingo verticaal")
    kaart = [[Fore.MAGENTA + '1' + Fore.RESET], [Fore.MAGENTA + '1' + Fore.RESET], [Fore.MAGENTA + '1' + Fore.RESET], [Fore.MAGENTA + '1' + Fore.RESET]]
    kaart = [rij + [0, 0, 0] for rij in kaart]  # Maak 4x4
    assert check_bingo(kaart)
    print("✅ Test geslaagd: verticale bingo gedetecteerd.\n")


def test_check_bingo_diagonaal_links_naar_rechts():
    print("🔹 Test: check_bingo diagonaal ↘")
    kaart = [[Fore.MAGENTA + 'x' + Fore.RESET if i == j else 0 for j in range(4)] for i in range(4)]
    assert check_bingo(kaart)
    print("✅ Test geslaagd: diagonale ↘ bingo gedetecteerd.\n")


def test_check_bingo_diagonaal_rechts_naar_links():
    print("🔹 Test: check_bingo diagonaal ↙")
    kaart = [[Fore.MAGENTA + 'x' + Fore.RESET if j == 3 - i else 0 for j in range(4)] for i in range(4)]
    assert check_bingo(kaart)
    print("✅ Test geslaagd: diagonale ↙ bingo gedetecteerd.\n")


def test_grabbelen_geeft_ballen():
    print("🔹 Test: grabbelen() trekt ballen")
    ballenbak = list(range(1, 10)) + ['groen', 'rood']
    teamnaam = "Testteam"
    getrokken = grabbelen(teamnaam, ballenbak)
    print("Getrokken ballen:", getrokken)
    assert isinstance(getrokken, list)
    assert 1 <= len(getrokken) <= 2
    for bal in getrokken:
        assert bal not in ballenbak
    print("✅ Test geslaagd: ballen correct getrokken en verwijderd.\n")


if __name__ == "__main__":
    test_maak_bingo_kaart_even()
    test_maak_bingo_kaart_oneven()
    test_markeer_bingo_kaart_en_is_roze()
    test_check_bingo_horizontaal()
    test_check_bingo_verticaal()
    test_check_bingo_diagonaal_links_naar_rechts()
    test_check_bingo_diagonaal_rechts_naar_links()
    test_grabbelen_geeft_ballen()
    print("✅ Alle tests geslaagd!")
