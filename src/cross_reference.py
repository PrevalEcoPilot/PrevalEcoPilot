import os

def load_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def analyze_compliance(site_path, veille_path):
    site_data = load_file(site_path)
    veille_data = load_file(veille_path)

    print(f"--- ANALYSE DE CROISEMENT ---")
    print(f"Site : {os.path.basename(site_path)}")
    print(f"Veille : {os.path.basename(veille_path)}")
    print("-" * 30)

    # Logique simplifiée de croisement
    if "cuve" in site_data.lower() and "icpe" in veille_data.lower():
        print("[ALERTE] : La nouvelle veille 2026 sur les ICPE impose un contrôle renforcé des cuves.")
        print("Action Terrain : Vérifier l'étanchéité de la cuve 120 m³ à Maîche.")

    if "séparateur" in site_data.lower():
        print("[CONSIGNE] : Conformité 2026 : Contrôle périodique du séparateur à hydrocarbures requis.")

# Chemins
site_file = "C:/Coordinateur_Preval/knowledge/ICPE/maiche_technique.md"
veille_file = "C:/Coordinateur_Preval/knowledge/ICPE/veille_2026.md"

analyze_compliance(site_file, veille_file)
