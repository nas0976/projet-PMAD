import subprocess
import sys
import time

def executer_commande_discrete(commande):
    try:
        process = subprocess.Popen(
            commande,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate()
        return f"[SUCCESS]\n{stdout}" if process.returncode == 0 else f"[ERROR]\n{stderr}"
    except Exception as e:
        return f"[EXCEPTION] Erreur : {str(e)}"

def connecter_au_serveur_souverain():
    # Coordonnées de ton infrastructure Kubernetes locale (NodePort)
    SERVEUR_IP = "127.0.0.1"
    PORT_SIGNALEMENT = 31116
    
    print(f"[Agent] Connexion au serveur PMAD Souverain ({SERVEUR_IP}:{PORT_SIGNALEMENT})...")
    time.sleep(1) # Simulation de la latence réseau
    print("[Agent] Statut : CONNECTÉ et prêt à recevoir des requêtes discrètes.")
    
    # Simulation d'une boucle d'écoute de commandes envoyées par le technicien
    commandes_distantes_simulees = [
        "whoami",                          # Étape 1 : Le tech vérifie les privilèges de l'agent
        "netstat -an | grep 31116"        # Étape 2 : Le tech vérifie les connexions réseau actives
    ]
    
    for cmd in commandes_distantes_simulees:
        print(f"\n[Réseau] Requête reçue du Technicien : '{cmd}'")
        res = executer_commande_discrete(cmd)
        print(f"[Réseau] Renvoi du résultat au panneau Tech :\n{res}")
        time.sleep(1)

if __name__ == "__main__":
    print("=== Démarrage de l'Agent PMAD Personnalisé ===")
    connecter_au_serveur_souverain()
