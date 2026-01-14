import os

def create_github_readme():
    # Az általad megadott pontos index tartalom
    index_content = """# Történelem Érettségi Jegyzetek

Ez a központi jegyzet a megadott történelmi témakörökhöz. Az egyes linkekre kattintva érheted el a részletes vázlatokat.

## Témakörök

### 1. Újkori Magyarország (1848 - 1914)
* [1848. március 15. és a forradalom](marc_15.md)
* [A kiegyezés (1867) folyamata és értékelése](kiegyezes.md)
* [Dualista gazdaság és társadalom](dualista_gazdasag.md)
* [Tisza Kálmán kora és a politikai rendszer](tisza_kalman.md)
* [Nemzetiségi kérdés a dualizmus korában](dualis_nemzetisegek.md)

### 2. A 20. század első fele
* [Az őszirózsás forradalom és a polgári demokratikus fordulat](oszi_rozsas.md)
* [Párizs környéki békék](parizs_bekek.md)
* [A trianoni békeszerződés](trianon.md)
* [A Horthy-rendszer jellemzői és konszolidációja](horthy_rendszer.md)
* [Mussolini és az olasz fasizmus](mussolini.md)

---
*Készült a megadott témakörök alapján.*

* [Összegzés és Tanulási Segédlet](summary.md)
"""

    # Létrehozzuk az index.md-t
    with open("index.md", "w", encoding="utf-8") as f:
        f.write(index_content)
    print("Siker: index.md frissítve.")

    # Létrehozzuk a README.md-t (ami GitHubon a főoldal lesz)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(index_content)
    print("Siker: README.md létrehozva (GitHub kezdőlap).")

if __name__ == "__main__":
    create_github_readme()