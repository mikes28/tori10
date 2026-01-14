import os

def create_summary_md():
    content = """# Összegzés és Tanulási Segédlet

## A kidolgozott témakörök
Ezzel a sorozattal a magyar történelem legfontosabb fordulópontjait fedtük le a 19. század közepétől a 20. század derekáig:
1. **Reformkor vége és Forradalom**: Az alapok lefektetése (1848).
2. **Dualizmus**: A politikai kompromisszum (Kiegyezés), a gazdasági aranykor és a belső feszültségek (Nemzetiségek, Tisza-korszak).
3. **Összeomlás**: Az első világháború vége, az őszirózsás forradalom és a trianoni trauma.
4. **Két világháború között**: A Horthy-rendszer stabilizációja és a nemzetközi környezet (Mussolini).



## Hogyan használd ezeket a jegyzeteket?
* **Összefüggések**: Figyeld meg, hogyan vezetett a dualizmus nemzetiségi politikája Trianonhoz, vagy a trianoni gazdasági sokk a bethleni reformokhoz.
* **Fogalmak**: Minden fájlban kiemeltem a kulcsfogalmakat (pl. *korporatív állam, passzív ellenállás, kvóta*).
* **Személyek**: Keresd a visszatérő szereplőket és hatásukat a korszakra.

## Technikai tipp
A Markdown fájlokat a legszebben az alábbi programokkal láthatod:
* **VS Code** (beépített Preview móddal: `Ctrl+Shift+V`).
* **Obsidian** (ez egy remek jegyzetelő alkalmazás, ami kezeli a linkeket a fájlok között).
* **Typora** vagy bármilyen online Markdown editor.

Sok sikert a felkészüléshez!
---
[Vissza a főoldalra](index.md)
"""
    
    with open("summary.md", "w", encoding="utf-8") as f:
        f.write(content)
    
    # Frissítjük az indexet, hogy ez is szerepeljen benne
    with open("index.md", "a", encoding="utf-8") as f:
        f.write("\n* [Összegzés és Tanulási Segédlet](summary.md)\n")
        
    print("Siker: summary.md létrehozva és index.md frissítve!")

if __name__ == "__main__":
    create_summary_md()