import os

# Témakör 1: Új eszmék
uj_eszmek_content = """# Új eszmék a 19. században: liberalizmus, nacionalizmus, konzervativizmus, szocializmus

## 1. Liberalizmus (szabadelvűség)
A felvilágosodásban gyökerező eszmeáramlat, amely az egyén szabadságát tekinti alapértéknek.
* **Alapelvei**: Az egyéni szabadságjogok (szólás-, sajtó-, vallásszabadság) biztosítása, a törvény előtti egyenlőség és a képviseleti demokrácia[cite: 344].
* **Gazdaság**: Az állam ne avatkozzon be a gazdaságba (szabad verseny), védje a magántulajdont[cite: 344].
* **Államszervezet**: A hatalmi ágak megosztása és az alkotmányosság alapvető követelmény[cite: 344].

## 2. Nacionalizmus
A nemzeti öntudatra, a közös nyelvre, történelemre és kultúrára építő mozgalom.
* **Célja**: A nemzeti egység megteremtése és az önálló nemzetállam létrehozása[cite: 344].
* **Jellemzői**: A lojalitás központjában nem az uralkodó, hanem a nemzet áll. Gyakran összefonódott a liberalizmussal a szabadságharcok idején[cite: 344].

## 3. Konzervativizmus
A francia forradalom radikalizmusára (terrorára) adott válaszreakcióként alakult ki.
* **Fő elve**: A hagyományok megőrzése és a lassú, szerves fejlődés támogatása a radikális változásokkal szemben[cite: 344].
* **Társadalom**: Fontosnak tartja a vallás, a család és a tekintélytisztelet megtartó erejét[cite: 344].

## 4. Szocializmus
Az ipari forradalom okozta társadalmi ellentmondások és a munkásság (proletariátus) nyomora hívta életre.
* **Alapvetése**: A közösségi érdek és a társadalmi egyenlőség előbbre való az egyéni haszonnál[cite: 345].
* **Kritikája**: A magántulajdont tartja a bajok forrásának, mivel az igazságtalan elosztáshoz vezet[cite: 345].
* **Célja**: A javak igazságos elosztása, a munkásréteg életkörülményeinek javítása, akár a magántulajdon korlátozásával is[cite: 345].

---
[Vissza a főoldalra](index.md)
"""

# Témakör 2: Pesti forradalom
pesti_forradalom_content = """# A pesti forradalom (1848. március 15.)

## 1. Előzmények és a forradalom kitörése
A párizsi és bécsi forradalmak hírére a pesti Fiatal Magyarország (Petőfi Sándor, Jókai Mór, Vasvári Pál) cselekvésre szánta el magát a Pilvax kávéházban.
* **Cél**: A reformellenzék követeléseinek érvényesítése és a polgári átalakulás kikényszerítése.
* **Főbb események**:
    1. **Egyetem**: Az egyetemi hallgatók csatlakoztak a mozgalomhoz.
    2. **Landerer-nyomda**: A cenzúra engedélye nélkül kinyomtatták a **12 pontot** és a **Nemzeti dalt** (ez a sajtószabadság első gyakorlati megnyilvánulása)[cite: 344, 349].
    3. **Nemzeti Múzeum**: Nagygyűlés tartása, ahol a tömeg elfogadta a követeléseket.

## 2. A 12 pont legfontosabb követelései
A követelések a polgári átalakulás alapjait fektették le:
* **Sajtószabadság** (a cenzúra eltörlése).
* **Felelős minisztérium** Buda-Pesten (önálló kormány).
* **Törvény előtti egyenlőség** vallási és polgári tekintetben.
* **Közteherviselés** (a nemesi adómentesség megszűnése).
* **Úrbéri viszonyok megszüntetése** (jobbágyfelszabadítás).

## 3. A forradalom győzelme Pesten
Délután a tömeg Budára, a Helytartótanácshoz vonult:
* **Táncsics Mihály kiszabadítása**: A politikai fogoly szabadon bocsátása a forradalom jelképes aktusa volt.
* **Helytartótanács meghajlása**: A hatalom nem mert katonai erőt alkalmazni, elfogadták a 12 pontot.
* **Eredmény**: Létrejött a Közcsendbizottmány a rend fenntartására.

## 4. Következmények: Az áprilisi törvények
A pesti forradalom vértelen győzelme kényszerítette ki az uralkodótól a változásokat, amelyeket az **1848. április 11-i törvények** szentesítettek:
* **Alkotmányos monarchia**: Létrejött a független, felelős magyar kormány.
* **Társadalmi modernizáció**: A jobbágyfelszabadítás és a népképviseleti országgyűlés alapjaiban változtatta meg az országot.

---
[Vissza a főoldalra](index.md)
"""

# Fájlok generálása
def generate_files():
    files = {
        "uj_eszmek.md": uj_eszmek_content,
        "pesti_forradalom.md": pesti_forradalom_content
    }
    
    for filename, content in files.items():
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Sikeresen legenerálva: {filename}")

if __name__ == "__main__":
    generate_files()