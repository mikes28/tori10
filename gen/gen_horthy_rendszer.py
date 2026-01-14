import os

def create_horthy_rendszer_md():
    content = """# A Horthy-rendszer jellemzői és konszolidációja (1920–1931)

## A rendszer jellege és Horthy Miklós hatalomra kerülése
Az 1919-es tanácsköztársaság bukása után a Nemzeti Hadsereg élén álló **Horthy Miklóst** 1920. március 1-jén a parlament **kormányzóvá** választotta. Magyarország államformája király nélküli királyság maradt.
* **A rendszer jellege**: Korlátozott parlamentarizmus, tekintélyelvű (autoriter) vonásokkal, de megmaradt a többpártrendszer és az országgyűlési kontroll.
* **Ellenforradalmi rendszer**: A korszak önmeghatározása, amely a forradalmak (1918, 1919) elutasítására és a keresztény-nemzeti értékekre épült.

## A bethleni konszolidáció (1921–1931)
Bethlen István miniszterelnöksége alatt az ország kilábalt a politikai és gazdasági káoszból.
* **Politikai stabilitás**: Létrehozta az Egységes Pártot (kormánypárt), és kiegyezett a szociáldemokratákkal (**Bethlen–Peyer-paktum**), akik legálisan működhettek, de nem szervezkedhettek a közalkalmazottak körében.
* **Választójog**: 1922-ben rendeleti úton korlátozta a választójogot, és vidéken visszaállította a **nyílt szavazást**, biztosítva a kormánypárt győzelmét.
* **Felsőház**: Visszaállította a kétkamarás országgyűlést (1926).



## Gazdasági talpraállás
* **Népszövetségi kölcsön**: 1924-ben Magyarország jelentős hitelt kapott, ami lehetővé tette az infláció megállítását.
* **Új pénz**: 1927-ben bevezették a **pengőt**, amely a korszak stabil fizetőeszköze lett.
* **Magyar Nemzeti Bank**: Megalakult az önálló jegybank (1924).
* **Iparfejlesztés**: Kiemelt figyelmet kapott a textilipar, a villamosipar és a vegyipar (pl. péti műtrágyagyártás).

## Klebelsberg Kuno kultúrpolitikája
A korszak vallás- és közoktatási minisztere szerint a "kultúrfölény" az egyetlen eszköz a revízió eléréséhez.
* **Népiskolai program**: Több ezer tanterem és tanítói lakás épült vidéken.
* **Egyetemek**: A határon túlról elmenekült egyetemeket (Kolozsvár, Pozsony) Szegeden és Pécsett helyezte el.
* **Külföldi intézetek**: Létrehozta a Collegium Hungaricumokat (Bécs, Berlin, Róma) a magyar tudományosság nemzetközi elismertetéséért.

## Külpolitika: A revízió és az elszigeteltség törése
A korszak legfőbb célja a **trianoni béke felülvizsgálata (revízió)** volt.
* **Kisantant**: Magyarországot ellenséges gyűrű fogta körül (Csehszlovákia, Románia, Jugoszlávia).
* **Olasz–magyar barátsági szerződés (1927)**: Bethlennek sikerült kitörnie a nemzetközi elszigeteltségből Mussolini Olaszországával kötött szövetség révén.

---
[Vissza a főoldalra](index.md)
"""
    
    with open("horthy_rendszer.md", "w", encoding="utf-8") as f:
        f.write(content)
    print("Siker: horthy_rendszer.md létrehozva!")

if __name__ == "__main__":
    create_horthy_rendszer_md()