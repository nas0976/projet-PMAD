import sys
import subprocess

def vider_cache_dns():
    """Vide le cache DNS de la machine cible selon son OS."""
    if sys.platform.startswith('win'):
        commande = "ipconfig /flushdns"
    elif sys.platform.startswith('darwin'):
        commande = "sudo killall -HUP mDNSResponder"
    else:
        # Pour Linux (systemd-resolved)
        commande = "resolvectl flush-caches 2>/dev/null || systemd-resolve --flush-caches 2>/dev/null || echo 'Pas de service systemd-resolved actif'"
    
    return commande

def optimiser_espace_disque():
    """Nettoie les fichiers temporaires de base."""
    if sys.platform.startswith('win'):
        commande = "del /q/f/s %TEMP%\\*"
    else:
        # Pour Linux : nettoyage des paquets inutilisés et du cache apt
        commande = "sudo apt-get autoremove -y && sudo apt-get clean"
    
    return commande

def lister_processus_critiques():
    """Affiche les processus consommant le plus de ressources."""
    if sys.platform.startswith('win'):
        commande = "tasklist | sort"
    else:
        commande = "ps aux --sort=-%cpu | head -n 10"
    
    return commande

# Zone de test du catalogue
if __name__ == "__main__":
    print("=== Catalogue de Scripts One-Click Initialisé ===")
    print(f"[DNS] Commande générée pour cet OS : {vider_cache_dns()}")
    print(f"[Disque] Commande générée pour cet OS : {optimiser_espace_disque()}")
