#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PDF alapú Markdown fájl generátor
Történelem érettségi témakörökhöz
"""

import os
from pathlib import Path


def create_md_file(filename: str, title: str, content: str) -> None:
    """
    Markdown fájl létrehozása a megadott tartalommal.
    
    Args:
        filename: a fájl neve (pl. 'alkotmanyos_monarchia_usa.md')
        title: a dokumentum címe
        content: a dokumentum tartalma
    """
    filepath = Path(filename)
    
    # Teljes markdown dokumentum összeállítása
    full_content = f"""# {title}

{content}

---

## Fontos kifejezések és fogalmak

- **Demokrácia**: A nép hatalma, ahol a polgárok egyenlő jogokkal rendelkeznek
- **Monarchia**: Királyság, ahol egy személy (monarkha) gyakorolja a hatalmat
- **Polisz**: Az ókori görög városállam

## Tanulási tippek

1. Olvasd el figyelmesen az összes pontot
2. Készítsd el saját Notes-ait a fő fogalmakról
3. Próbáld meg felidézni a leckét anélkül, hogy megnéznéd az anyagot
4. Gyakorolj időmérés mellett

## Vizsgára készüléshez hasznos linkek

- Érettségi.com - történelem témakörök
- Wikipedia - történelmi cikkek
- YouTube - történelem előadások

## Végső megjegyzés

Ez a dokumentum a középszintű érettségi követelményeinek alapján készült.
Az összes szükséges információt tartalmazza, de javasolt az eredeti PDF tankönyvet is átnézni.

"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    print(f"✅ Létrehozva: {filename}")


def generate_all_files():
    """Összes szükséges markdown fájl generálása."""
    
    files_to_create = {
        'alkotmanyos_monarchia_usa.md': {
            'title': 'Alkotmányos Monarchia és USA',
            'content': """## Az amerikai alkotmány

### A forradalom után

Az Amerikai Függetlenségi Háború után (1776) az amerikai államok szövetkezete alkotmányt hoztak létre.

### Jellemzők

- **Alkotmányos monarchia helyett köztársaság**: Az USA nem királysággal, hanem elnökkel rendelkezik
- **Hatalommegosztás**: Végrehajtó (elnök), törvényhozó (kongresszus) és bírói hatalom
- **Emberijogok védelme**: Az első 10. módosítás (Bill of Rights) biztosítja az állampolgári jogokat
- **Föderatív rendszer**: Az egyes államok megőriznek bizonyos függetlenséget

### Ábrahám Lincoln és a polgárháború

- **1861-1865**: Az amerikai polgárháború az osztály-ellentétek miatt
- Az USA egyesítésének megvédése
- A rabszolgaság eltörlése

### Amerikai jellemzők

1. Önálló igazságszolgáltatás
2. Legalitás és törvényi szabályozottság
3. Politikai pluralizmus (többpárti rendszer)
4. Szabad sajtó és közlekedési szabadság

## Az alkotmányos monarchia Európában

### Nagy-Britannia modellje

- Parlament már a középkorban fennállt
- Hatalommegosztás a király és a parlament között
- Fokozatos fejlődés a demokrácia felé (Reform Act-ek)

### Jellemzői

- Erős törvényhozás
- Korlátozott királyi hatalom
- Parlamenten alapuló kormányrendszer
- Garantált polgári szabadságjogok
"""
        },
        
        'erdely_helyzete.md': {
            'title': 'Erdély Helyzete a 16-17. Században',
            'content': """## Az Erdélyi Fejedelemség virágkora

### Történeti háttér

A 16. században Magyarország három részre szakadt:
- **Magyarország nyugati része**: Habsburg uralom
- **Középső rész**: Oszmán birodalom
- **Erdély**: Önálló fejedelemség

### Erdély politikai helyzete

#### Függetlenség és félüggetlenség

- Oszmán vazallusként működött Erdély
- De belső autonómiája megmaradt
- Saját fejedelemmel rendelkezett
- Saját céhes és jobbágyi rendszer

#### Vallási sokszínűség

Erdély a koraújkorban több vallási közösség otthona volt:
- **Római katolikus**: Magyar nemesség
- **Református**: Szász települések
- **Unitárius**: Szintén magyar közösség
- **Ortodox**: Román lakosság

**Vallási tolerancia**: Az Erdélyi Fejedelemség híres volt a vallási tűrésről

### Gazdaság és társadalom

1. **Földművelés**: Gabonatermesztés, gulyatartás
2. **Kereskedelem**: Külföldi és belföldi kereskedelmi kapcsolatok
3. **Bányászat**: Arany-, ezüst-, sóbányák
4. **Kézművesség**: Céhekbe szervezett iparosok

### Kiemelt fejedelmek

- **Báthory Gábor** (1608-1613): Erős központi hatalom
- **Báthory Zsigmond** (1588-1602): Vallási reformok
- **Apáfi Mihály**: A 17. század közepének fejedelme

### Jellegzetességek

- Vegyes összetételű lakosság
- Relatív függetlenség az Oszmán Birodalom alatt
- Erős nemesi hatalom
- Vallásilag toleráns rendszer
"""
        },
        
        'ipari_forradalom.md': {
            'title': 'Az Ipari Forradalom Hullámai és Hatásai',
            'content': """## Az Ipari Forradalom Periodizálása

### Első hullám (1760-1830)

#### Kezdete és helyszíne

- **Nagy-Britanniában** indul ki
- Textile ipar az első befogadott szektora
- Gőzmotor feltalálása (James Watt)

#### Jellemzői

1. **Textilgyártás gépesítése**
   - Jenny-fonógép (1764)
   - Szerző-gép
   - Vasműves gépek

2. **Energiagazdálkodás**
   - Szén-kőszén bányászat
   - Gőzmotor elterjedése
   - Vasúti közlekedés fejlődése

3. **Termelési szervezet**
   - Manufaktúrából gyárrá
   - Munkaerő-koncentráció
   - Zártvány-szervezet helyett nyitott termelés

### Második hullám (1830-1870)

#### Terjedési területek

- **Francia birodalom**
- **Német államok**
- **Belgium, Hollandia**

#### Technikai újítások

1. Vasipar fejlődése
2. Vasúti közlekedés kiépítése
3. Hajózás fejlődése (gőzhajók)

### Harmadik hullám (1870-1914)

#### Új technológiák

- **Elektromosság**: Villanymotor, villanyvilágítás
- **Kémia**: Műtrágya, festékek, gyógyszerek
- **Olaj**: Petróleumipari kezdetek
- **Acélgyártás**: Bessemer-eljárás

#### Új iparágak

1. Elektrotechnika
2. Chemiai ipar
3. Olajfinomítás
4. Gépgyártás

## Az Ipari Forradalom Hatásai

### Gazdasági hatások

- Tömegtermelés
- Fokozott árucikk-termelés
- Világkereskedelem bővülése
- Tőkefelhalmozódás

### Szociális hatások

1. **Városi népesség növekedése**
   - Land-to-city migráció
   - Szegénynegyedek kialakulása
   - Munkanélküliség

2. **Munkaviszonyok**
   - Hosszú munkaidő (12-16 óra)
   - Alacsony bérek
   - Gyermek- és női munka
   - Veszélyes munkakörülmények

3. **Új társadalmi osztály**
   - Ipari burzsoázia
   - Munkásság
   - Értelmiség bővülése

### Politikai hatások

- Szabadkereskedelmi mozgalmak
- Szociális mozgalmak
- Munkásmozgalmak
- Szocializmus megjelenése

### Kulturális hatások

- Képzőművészeti modernizmus
- Irodalmi realizmus
- Szociológia megjelenése
"""
        },
        
        'reformkor.md': {
            'title': 'A Reformkor Magyarországon (1790-1848)',
            'content': """## A Reformkor Politikai és Társadalmi Jellegzetességei

### Időhatárok és történeti háttér

- **1790-1848**: A hosszú 19. századi reformmozgalmak kora
- A francia forradalom hatása Európára
- A nemzetiségi mozgalmak kora

### Főbb jellemzők

#### Politikai reformok követelése

1. **Alkotmányosság igénye**
   - Irántott hatalom korlátozása
   - Jogállamiság követelése
   - Parlamentárizmus igénye

2. **Gazdasági reformok**
   - Parasztság felszabadítása
   - Céhrendszer feloldása
   - Szabad kereskedelem igénye

3. **Nemzetiségi kérdés**
   - Magyar nemzeti tudatosodás
   - Szlávok emancipációjára törekvése
   - Román nemzeti ébredés

### Kiemelt reformerek

#### Gróf Széchenyi István

- **"A magyar játékos" programja**
- Gazdasági fejlesztések szorgalmazása
- Közlekedési reformok (Lánchíd, Dunagőzös)
- Pesti Redoute megalapítása
- Kultúra és tudomány támogatása

#### Deák Ferenc

- Jogi reformok
- Jogalmanyok felszabadítása
- Egyenlő polgári jogi követelése

#### Kossuth Lajos

- Parlamentáris alkotmány követelése
- Sajtó szabadságáért küzdése
- Közösségek politikai aktivizálása

### Gazdasági fejlődés

1. **Mezőgazdaság modernizálása**
   - Igavonó-lófejlesztés
   - Vetésváltási módszerek
   - Nagyobb területű művelés

2. **Közlekedés fejlesztése**
   - Út-, híd-, csatornázás
   - Vasúti vonalak megépítése
   - Dunai gőzhajózás indítása

3. **Iparosodás kezdete**
   - Manufaktúrák alapítása
   - Gépek behozatala
   - Céhrendszer feloldása

### Kultúra és tudomány

#### Magyarnyelvű fejlődés

- Magyar nyelvtan kidolgozása
- Nyelvújítás (Kazinczy Ferenc)
- Nemzeti irodalom nascere

#### Tudományos fejlődés

- Magyar Tudományos Akadémia (1825)
- Természettudományok oktatása
- Történetírás fejlődése

### Szociális reformok

1. **Jobbágyi viszonyok javítása**
   - Jobbágyok terhi csökkentése
   - Jobbági telkek nagyobbítása
   - Jobbági költségvetés meghatározása

2. **Városok fejlesztése**
   - Pesti-Budai fejlesztések
   - Nyilvános közlekedés
   - Köztéri szépítés

### Reformkor vége

- **1848. március**: A forradalmi mozgalmak kirobbantása
- A reformkor fokozatos átmenetele forradalmakba
- Nemzeti felszabadító mozgalmak erősödése
"""
        },
        
        'szabadsagharc_48.md': {
            'title': 'Az 1848-as Forradalom és Szabadságharc Magyarországon',
            'content': """## Az 1848-as Magyarországi Forradalom és Szabadságharc

### Történeti előzmények

#### 1848. március 15.

- **Pesten kitörnek** a forradalmi megmozdulások
- Nemzeti ébredés kinyilvánítása
- 12 pont program elfogadása (képviseleti kormányzat, sajtószabadság, etc.)

#### 1848. április

- Elfogadják a **szabad sajtó törvényt**
- Feloszlatják a céhrendszert
- Parasztokat felszabadítják a jobbágyi kötelezettség alól

### A Forradalmi Kormány

#### Vezetői

- **Batthyány Lajos gróf**: Az első független magyar miniszterelnök
- **Széchenyi István**: Közlekedési miniszter
- **Eötvös József**: Kulturális reformok
- **Kossuth Lajos**: Pénzügyi politika

#### Fontos törvényi reformok

1. **Polgári jogok kiterjesztése**
   - Jobbágyok felszabadítása
   - Egyenlő polgári jogi garantálás
   - Cehhel hatalmi jellegzetességek eltörlése

2. **Politikai reformok**
   - Parlamentarizmus bevezetése
   - Felelős kormányzat
   - Sajtó- és gyülekezési szabadság

3. **Gazdasági reformok**
   - Közös gazdasági terv
   - Marastási kötöttség feloldása
   - Szabad kereskedelem

### A Szabadságharc (1848-1849)

#### Kiindulópontjai

- Az osztrákok és az oroszok militar tapogatózásai
- Nemzeti önrendelkezés követelése
- Jogállami rendszerek megteremtése

#### Főparancsnokuk

- **Görgei Artúr**: A szabadságharc fő parancsoka
- **Bem József**: Lengyel tábornok, Erdély felszabadítója

#### Harci szakaszok

1. **Kezdeti magyar sikerei** (1848 nyara-ősze)
   - Pákozdon megerősödnek
   - Defenderé a Tisza-vonalat
   - Önkéntes hadsereg szervezése

2. **Orosz beavatkozás** (1849. április)
   - II. Miklós cár sereget küld
   - Az osztrák hadseregek megerősödnek
   - Szigetvár heroikus védjelme

3. **Vereség és összeomlás** (1849. augusztus)
   - Görgei kapitulációja Világosnál
   - A szabadságharc véget ér
   - Haynau tábornok szovétsége

### A Szabadságharc Hősei

#### Segesvárnál (augusztus 31., 1849)

- Bem József vereség és halála
- Czartoryski herceg támogatás nélkülisége
- Az erdélyi szabadságharc összeomlik

#### Világosnál (augusztus 13., 1849)

- Görgei Artúr kapitulációja
- 47 szabadságharcos meghurcolása
- Arad 13. vértanúja

### Véres megtorlások

- **Pesten**: Haynau betelepítése
- **Arad**: A 13 vértanú végeztetése (1849. október 6.)
- **Számos politikai fogoly halálra ítélkezése**

### A Forradalom és Szabadságharc Eredménye

#### Pozitív

- Jobbágyság felszabadítása
- Sajtó- és gondolatszabadság követelése
- Nemzeti identitás erősödése

#### Negatív

- Habsburg uralom erősödése
- Abszolút politika bevezetése
- Nemzeti jogok korlátozása
- Gazdasági kutatások visszavonása

### Nemzeti Emlékezet

- **Október 6.**: A 13 vértanú emléknapja
- **Március 15.**: A szabadságharc kezdete
- **Világos**: Emléktábla és panteont

### Lezárulás

- **1867**: A kiegyezés
- Austro-Magyarország duális birodalmának megalakulása
- Az 1848-as ideálok részleges megvalósulása

"""
        }
    }
    
    # Fájlok generálása
    print("=" * 50)
    print("📝 Markdown Fájl Generátor - Történelem Érettségi")
    print("=" * 50)
    print()
    
    for filename, data in files_to_create.items():
        create_md_file(filename, data['title'], data['content'])
    
    print()
    print("=" * 50)
    print(f"✨ Kész! Összesen {len(files_to_create)} fájl lett létrehozva.")
    print("=" * 50)
    print()
    print("Generált fájlok:")
    for i, filename in enumerate(files_to_create.keys(), 1):
        print(f"  {i}. {filename}")


if __name__ == '__main__':
    generate_all_files()
