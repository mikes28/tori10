import os

def setup_github_readme():
    # 1. Megnézzük, létezik-e az index.md (vagy main.md)
    source_file = "index.md"
    
    if not os.path.exists(source_file):
        print(f"Hiba: {source_file} nem található!")
        return

    # 2. Létrehozunk egy README.md-t, ami beágyazza az index tartalmát
    # Vagy egyszerűen átmásoljuk a tartalmát
    with open(source_file, "r", encoding="utf-8") as f:
        content = f.read()

    readme_content = f"""# Projekt Főoldal
> **Megjegyzés:** Ez a fájl automatikusan generálódik az `{source_file}` alapján.

{content}
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    print("Siker: A README.md elkészült, GitHub-on ez fog megjelenni alapértelmezettként.")

if __name__ == "__main__":
    setup_github_readme()