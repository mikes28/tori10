import os

# Az összes hiányzó téma kidolgozása (fél A4-es terjedelem, érettségi kulcsszavakkal)
hianyzo_anyagok = {
    "felfedezesek_kapitalizmus.md": """# A nagy földrajzi felfedezések és a korai kapitalizmus

## 1. Előzmények és mozgatórugók
A 15. század végén a levantei kereskedelem megdrágult az oszmán terjeszkedés miatt. Európában nemesféméhség alakult ki. A technikai feltételek adottak voltak: a **karavella** (hajótípus), az iránytű és a térképészet fejlődése (Ptolemaiosz).

## 2. A felfedezések menete
- **Portugálok:** Afrika megkerülése (Vasco da Gama, 1498 - India).
- **Spanyolok:** Kolumbusz Kristóf 1492-ben eléri Amerikát. Magellán flottája (1519-22) körbehajózza a Földet. A konkvisztádorok (Cortés, Pizarro) leigázzák az azték és inka birodalmakat.

## 3. Gazdasági következmények
A beáramló nemesfém miatt **árforradalom** alakult ki (az árak nőttek, a pénz értéke csökkent). Kialakult a **világkereskedelem**: Amerika nemesfémet és növényeket (kukorica, burgonya, dohány) adott, Európa késztermékeket, Afrika rabszolgákat.
- **Kapitalizmus:** A céheket felváltották a **manufaktúrák** (bérmunka, munkamegosztás).
- **Második jobbágyság:** Kelet-Közép-Európában a mezőgazdasági igény miatt fokozták a robotot.

---
[Vissza a főoldalra](index.md)""",

    "reformacio_megujulas.md": """# A reformáció és a katolikus megújulás

## 1. A reformáció irányzatai
Luther Márton 1517-es wittenbergi fellépése indította el a mozgalmat a búcsúcédulák ellen.
- **Lutheránus (evangélikus):** Sola Fide (csak a hit által). Két szentség, anyanyelvi liturgia.
- **Kálvini (református):** **Predesztináció** (eleve elrendelés), zsarnokölési tan, egyszerű templombelső.
- **Antitrinitárius:** Szentháromság-tagadó (Erdélyben unitárius).

## 2. Katolikus megújulás
A tridenti zsinat (1545-63) rögzítette a reformokat: betiltották a búcsúcédulákat, papneveldéket alapítottak. Megalakult a **Jezsuita rend** (Loyolai Szent Ignác), amely az oktatás és diplomácia eszközeivel küzdött.

## 3. Barokk művészet
A katolikus egyház erejét hirdető stílus. Jellemzői a mozgalmasság, pompa, fény-árnyék hatások, érzelmi túlfűtöttség.

---
[Vissza a főoldalra](index.md)""",

    "mohacs_harom_resz.md": """# A mohácsi csata és az ország három részre szakadása

## 1. Mohács (1526)
A magyar sereg vereséget szenvedett az oszmán túlerőtől. II. Lajos meghalt, ami politikai válsághoz és kettős királyválasztáshoz (Szapolyai János és Habsburg Ferdinánd) vezetett.

## 2. 1541: Az ország szakadása
Szulejmán szultán csellel elfoglalta Budát. Az ország három részre szakadt:
- **Királyi Magyarország (Nyugat):** Habsburg irányítás, rendi dualizmus.
- **Hódoltság (Közép):** Török igazgatás, vilajetek, kettős adózás.
- **Erdélyi Fejedelemség (Kelet):** Török vazallus, de belső önállóság.

## 3. Várháborúk
A 16. század a végvári harcok kora (pl. Eger - Dobó István, Szigetvár - Zrínyi Miklós). A várak az ország védelmének és a keresztény kultúra megmaradásának bástyái voltak.

---
[Vissza a főoldalra](index.md)""",

    "rakoczi_szabadsagharc.md": """# A Rákóczi-szabadságharc és a szatmári béke

## 1. Kiváltó okok
A török kiűzése után a Habsburgok abszolutista módon kormányoztak (Újszerzeményi Bizottság, fegyverváltság, vallási sérelmek). 1703-ban a tiszaháti felkeléssel kezdődött a harc.

## 2. Fordulópontok
- 1705: Szécsényi országgyűlés (Rákóczi vezérlő fejedelem).
- 1707: Ónodi országgyűlés (**Habsburg-ház trónfosztása**).
- 1708: Trencséni vereség után a mozgalom katonailag meggyengült.

## 3. Szatmári béke (1711)
Kompromisszumos zárás: a nemesség megtarthatta kiváltságait és birtokait, biztosították a vallásszabadságot, cserébe elismerték a Habsburgok trónigényét.

---
[Vissza a főoldalra](index.md)""",

    "magyarorszag_18szazad.md": """# Újranépesülés és felvilágosult abszolutizmus

## 1. Demográfia
A török háborúk után az ország lakossága megfogyatkozott. A 18. században **betelepítések** (pl. svábok) és önkéntes bevándorlás történt, Magyarország soknemzetiségű állammá vált.

## 2. Mária Terézia (1740-1780)
- **Ratio Educationis:** Oktatási reform.
- **Urbárium:** A jobbágyterhek (robot) maximalizálása a védelem érdekében.
- **Kettős vámrendelet:** A birodalmon belüli munkamegosztás elősegítése.

## 3. II. József (1780-1790)
A "kalapos király". Rendeletekkel kormányzott: **Türelmi rendelet** (vallásszabadság), Jobbágyrendelet (szabad költözés), nyelvrendelet (német nyelv erőltetése - ellenállást váltott ki).

---
[Vissza a főoldalra](index.md)"""
}

# Fájlok létrehozása
for filename, content in hianyzo_anyagok.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Létrehozva: {filename}")