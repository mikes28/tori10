import os

def create_trianon_md():
    content = """# Párizs környéki békék és a trianoni békeszerződés

## Az első világháborút lezáró békék (1919–1920)
A győztes antant hatalmak Párizs környéki kastélyokban diktálták a békefeltételeket a vesztes központi hatalmaknak. A békék fő célja Németország meggyengítése és az Osztrák–Magyar Monarchia feldarabolása volt.
* **Versailles**: Németországgal kötött béke.
* **Saint-Germain**: Ausztriával kötött béke (szétválasztották Magyarországtól).
* **Neuilly**: Bulgáriával kötött béke.
* **Sèvres / Lausanne**: Törökországgal kötött béke.

## A trianoni békeszerződés (1920. június 4.)
A magyar békedelegációt **Apponyi Albert** vezette, aki híres "védőbeszédében" etnikai és történelmi érvekkel próbálta meggyőzni a győzteseket, de a döntések ekkor már megszülettek. A békét végül a versailles-i Trianon-kastélyban írták alá.



### Főbb rendelkezések
1. **Területi és demográfiai veszteségek**:
   - Magyarország elveszítette területének **67%-át** (Horvátország nélkül).
   - Lakosságának száma 18,2 millióról 7,6 millióra csökkent.
   - Kb. **3,3 millió magyar** került az új határokon kívülre (főleg a határ menti sávban és Székelyföldön).
2. **Katonai korlátozások**:
   - Maximált hadilétszám: **35 000 fő**.
   - Megtiltották az általános hadkötelezettséget (csak önkéntes haderő).
   - Tilos volt modern fegyvernemek (tankok, repülőgépek, hadihajók) tartása.
3. **Gazdasági és egyéb feltételek**:
   - Jóvátétel fizetése a győzteseknek.
   - Az ország elveszítette termőföldjeinek, erdeinek, vasútvonalainak és bányáinak (só, vas, réz) jelentős részét.
   - A vasúti hálózat sugaras szerkezete megszakadt.

## A béke következményei
* **Társadalmi sokk**: A magyar társadalom nem tudott belenyugodni a döntésbe. Megszületett a **"Nem, nem, soha!"** jelszó és a revíziós mozgalom (a területek visszacsatolásának igénye).
* **Menekültkérdés**: Százezrek (főleg tisztviselők és értelmiségiek) menekültek el az utódállamokból az anyaországba (vagonlakók).
* **Külpolitikai elszigeteltség**: Magyarországot ellenséges államok vették körül (**Kisantant**: Csehszlovákia, Románia, Jugoszlávia szövetsége), amelyek célja a trianoni határok fenntartása volt.

## Értékelés
Trianon az etnikai elvet figyelmen kívül hagyva (pl. tiszta magyar lakosságú területek elcsatolása) és a gazdasági életképességet rontva hosszú évtizedekre meghatározta a közép-európai feszültségeket.

---
[Vissza a főoldalra](index.md)
"""
    
    with open("trianon.md", "w", encoding="utf-8") as f:
        f.write(content)
    print("Siker: trianon.md létrehozva!")

if __name__ == "__main__":
    create_trianon_md()