import os
import subprocess

def run_scripts():
    # A futtatandó scriptek listája a megadott sorrendben
    scripts = [
        "gen_index.py",
        "gen_marc_15.py",
        "gen_kiegyezes.py",
        "gen_dualista.py",
        "gen_tisza.py",
        "gen_oszi_rozsas.py",
        "gen_parizs_trianon.py",
        "gen_horthy_rendszer.py",
        "gen_mussolini.py",
        "gen_summary.py"
    ]

    print("--- Történelem jegyzet generálás indítása ---\n")

    for script in scripts:
        if os.path.exists(script):
            # Ellenőrizzük, hogy nem üres-e a fájl
            if os.path.getsize(script) > 0:
                print(f"Futtatás: {script}...")
                try:
                    # Lefuttatjuk a scriptet
                    subprocess.run(["python", script], check=True)
                except subprocess.CalledProcessError:
                    print(f"HIBA: A(z) {script} futtatása közben hiba történt.")
            else:
                print(f"KIHAGYVA: {script} (a fájl üres).")
        else:
            print(f"HIBA: {script} nem található a mappában.")

    print("\n--- Folyamat befejezve! ---")

if __name__ == "__main__":
    run_scripts()