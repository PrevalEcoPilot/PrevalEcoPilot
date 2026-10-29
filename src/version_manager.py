import shutil
import os
from datetime import datetime

class VersionManager:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.history_dir = os.path.join(base_dir, "history")
        os.makedirs(self.history_dir, exist_ok=True)

    def backup_rule(self, rule_path):
        """Sauvegarde une version avant modification."""
        if os.path.exists(rule_path):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.basename(rule_path)
            backup_path = os.path.join(self.history_dir, f"{timestamp}_{filename}")
            shutil.copy2(rule_path, backup_path)
            print(f"[VERSIONING] : Backup effectué -> {backup_path}")

if __name__ == "__main__":
    vm = VersionManager("C:/Coordinateur_Preval/knowledge/ICPE")
    vm.backup_rule("C:/Coordinateur_Preval/knowledge/ICPE/veille_2026.md")
