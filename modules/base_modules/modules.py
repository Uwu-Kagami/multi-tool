import os

def install_requirements():
    requirements_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "requirements.txt")
    
    dependencies = ["requests", "cryptography", "wmi", "getmac", "PySide6"]

    try:
        with open(requirements_file, "w", encoding="utf-8") as f:
            f.write("\n".join(dependencies))

        print("Fichier requirements.txt créé avec succès.")

    except Exception as e:
        print(f"Erreur lors de la création du fichier requirements.txt : {e}")

install_requirements()
