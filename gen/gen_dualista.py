import os

def create_dualista_gazdasag_md():
    content = """# Dualista gazdaság és társadalom (1867–1914)

## A gazdasági fejlődés alapjai
A kiegyezés után Magyarországon látványos gazdasági fellendülés kezdődött. Ennek motorja a **közös piac** (60 milliós belső felvevőpiac az Osztrák–Magyar Monarchián belül), a stabil valuta (korona) és a nyugati tőke beáramlása volt. Az állam aktív iparpártoló politikát folytatott (pl. adókedvezmények az új gyáraknak).

## Kulcságazatok: Mezőgazdaság és Élelmiszeripar
* **Mezőgazdaság**: Továbbra is a vezető ágazat maradt. A nagybirtokok modernizálódtak, megjelentek a gépek (cséplőgép) és a műtrágya. A gabonatermelés világelsők közé emelte az országot.
* **Élelmiszeripar**: A magyar ipar húzóágazata. Budapest a világ második legnagyobb malomipari központjává vált (Minneapolis után). Jelentős volt a cukorgyártás és a szeszipar is.

## Infrastruktúra és Nehézipar
* **Vasúthálózat**: Baross Gábor ("a vasminiszter") idején épült ki a sugaras szerkezetű vasúthálózat, Budapest központtal. Ez tette lehetővé az áruk gyors szállítását.
* **Nehézipar**: A bányászat (szén, vasérc) és a gépgyártás fejlődése kiemelkedő volt. Olyan világhírű cégek jöttek létre, mint a **Ganz Ábrahám** vezette Ganz-gyár (elektrotechnika, mozdonyok) vagy a Weiss Manfréd Művek Csepelen.
* **Innovációk**: A magyar mérnöki zsenialitás kora (Puskás Tivadar – telefonközpont, Bláthy-Zipernowsky-Déri – transzformátor).



## A társadalom szerkezete: A "Torlódó Társadalom"
Magyarországon egymás mellett élt a régi, rendi jellegű és az új, tőkés társadalmi szerkezet:

1. **A régi szerkezet (Hagyományos):**
   - **Arisztokrácia**: A politikai hatalom birtokosai, hatalmas földbirtokokkal.
   - **Dzsentrik**: Elszegényedett nemesek, akik birtokukat vesztették, ezért főleg az államigazgatásban (vármegyei hivatalok) vállaltak munkát.
   - **Parasztság**: A társadalom többsége (kb. 60-70%). Rétegzett: a gazdagparaszttól a nincstelen napszámosig ("hárommillió koldus").

2. **Az új szerkezet (Polgári):**
   - **Nagypolgárság**: Szűk, főleg zsidó és német származású réteg (bankárok, gyárosok), akik gazdasági hatalmukat politikai befolyásra váltották.
   - **Középpolgárság és Értelmiség**: Orvosok, ügyvédek, mérnökök, tanárok.
   - **Városi munkásság**: Számuk a gyáriparral párhuzamosan nőtt. Megjelent a szakmunkás réteg és a képzetlen segédmunkások tömege.

## Urbanizáció
Budapest világvárossá fejlődött. Ekkor épült ki az Andrássy út, a Nagykörút, a Parlament és a kontinens első földalatti vasútja (Millenniumi Fájdalmi). A lakosság száma ugrásszerűen megnőtt a belső migráció miatt.

---
[Vissza a főoldalra](index.md)
"""
    
    with open("dualista_gazdasag.md", "w", encoding="utf-8") as f:
        f.write(content)
    print("Siker: dualista_gazdasag.md létrehozva bővített tartalommal!")

if __name__ == "__main__":
    create_dualista_gazdasag_md()