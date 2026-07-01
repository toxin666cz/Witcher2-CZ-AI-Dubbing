from pathlib import Path

GAME_PATH = Path(r"C:\Program Files (x86)\Steam\steamapps\common\The Witcher 2\CookedPC")

print("=" * 50)
print(" Witcher 2 Czech AI Dubbing Toolkit")
print("=" * 50)

if not GAME_PATH.exists():
    print("❌ Složka hry nebyla nalezena.")
    print("Uprav proměnnou GAME_PATH podle své instalace.")
    exit()

print("\nNalezené jazykové soubory:\n")

for file in sorted(GAME_PATH.glob("*.w2strings")):
    print("📄", file.name)

speech = GAME_PATH / "en0.w2speech"

if speech.exists():
    print("\n✅ Nalezen anglický dabing.")
else:
    print("\n❌ Soubor en0.w2speech nebyl nalezen.")
