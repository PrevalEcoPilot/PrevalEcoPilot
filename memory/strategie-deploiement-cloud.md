---
name: strategie-deploiement-cloud
description: "Migration du projet PrevalEcoPilot vers GitHub pour automatisation 24/7 et accès collaboratif"
metadata:
  type: project
---

# Stratégie de Déploiement : Cloud et Automatisation

## Problématique
- Dépendance à la disponibilité locale de l'ordinateur de l'utilisateur.
- Risque de perte de données en cas de panne matérielle.
- Difficulté de partage de l'outil avec les collègues du syndicat Preval.

## Solution retenue : Écosystème GitHub
- **Versionnage :** Utilisation de Git pour la sécurité des données et l'historique complet.
- **Automatisation (GitHub Actions) :** Exécution du script de veille (`automation_engine.py`) sans intervention humaine, 24h/24.
- **Publication (GitHub Pages) :** Hébergement gratuit et public (ou privé si besoin) du Dashboard (`dashboard.html`) pour un accès immédiat par les collègues via URL.

## Étapes de mise en œuvre
1. Initialisation Git et push vers un dépôt GitHub.
2. Configuration des GitHub Actions pour l'exécution quotidienne du moteur de veille.
3. Activation des GitHub Pages pour l'affichage collaboratif du Dashboard.

**Pourquoi cette solution :** Fiabilité maximale, coût nul, accessibilité totale et pérennité du savoir syndical.
