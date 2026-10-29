import os
from jinja2 import Template
from datetime import datetime

# Structure du Dashboard
DASHBOARD_TEMPLATE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Radar PrevalEcoPilot</title>
    <style>
        body { font-family: sans-serif; line-height: 1.6; margin: 20px; background: #f4f4f4; }
        .pilier { background: #fff; padding: 15px; margin-bottom: 20px; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; }
        h2 { color: #34495e; border-bottom: 2px solid #3498db; }
        .version-info { font-size: 0.8em; color: #7f8c8d; }
    </style>
</head>
<body>
    <h1>Radar de Veille PrevalEcoPilot</h1>
    <p>Dernière mise à jour : {{ date }}</p>
    {% for pilier, content in piliers.items() %}
    <div class="pilier">
        <h2>{{ pilier }}</h2>
        <pre>{{ content }}</pre>
    </div>
    {% endfor %}
</body>
</html>
"""

def generate_dashboard():
    knowledge_dir = "C:/Coordinateur_Preval/knowledge"
    data = {}

    # Lister les dossiers de piliers (sauf SOURCES)
    for p in os.listdir(knowledge_dir):
        if os.path.isdir(os.path.join(knowledge_dir, p)) and p != "SOURCES":
            veile_file = os.path.join(knowledge_dir, p, f"{p}_veille.md")
            if os.path.exists(veile_file):
                with open(veile_file, 'r', encoding='utf-8') as f:
                    data[p] = f.read()

    template = Template(DASHBOARD_TEMPLATE)
    html_output = template.render(date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), piliers=data)

    with open("C:/Coordinateur_Preval/dashboard.html", "w", encoding="utf-8") as f:
        f.write(html_output)
    print("[DASHBOARD] : Page générée avec succès.")

if __name__ == "__main__":
    generate_dashboard()
