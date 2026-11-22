from dotenv import load_dotenv
from pathlib import Path
import os
import json
import csv

load_dotenv()
print(f"Password : {os.getenv("API_KEY")}")

dossier_data = Path("data")
fichier_entree = dossier_data / "logs_bruts.json"
print(f"Je lis {fichier_entree}")

try:
    with open(fichier_entree, "r", encoding="utf-8") as f:
        donnees = json.load(f)
        print(f"J'ai lu {len(donnees)} lignes brutes")
except FileNotFoundError:
    print(f"Dossier introuvable : {fichier_entree}")
    donnees = []

erreurs = [ligne for ligne in donnees if ligne["status"] == "ERROR"]
print(f"Il y'a {len(erreurs)} lignes ERROR")

dossier_sortie = Path("output")
dossier_sortie.mkdir(exist_ok=True)
fichier_sortie = dossier_sortie / "logs_netoyees.csv"

with open(fichier_sortie, "w", newline="", encoding="utf-8") as f:
    ecrivain = csv.DictWriter(f, fieldnames=["id", "message", "status"])
    ecrivain.writeheader()
    ecrivain.writerows(erreurs)

print(f"Données nettoyées à retrouver sur {fichier_sortie}")