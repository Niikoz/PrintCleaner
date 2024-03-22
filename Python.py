import os
import time

def print_and_delete_documents_in_directory(directory):
    try:
        # Vérifier si le chemin d'accès existe
        if not os.path.exists(directory):
            print("Le repertoire specifie n'existe pas.")
            return
        
        # Parcourir tous les fichiers dans le répertoire
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            # Vérifier si c'est un fichier
            if os.path.isfile(file_path):
                # Imprimer le fichier
                os.startfile(file_path, "print")
                print(f"Impression du fichier : {file_path}")
                # Attendre quelques secondes pour permettre à l'impression de se terminer
                time.sleep(5)
                # Supprimer le fichier après impression
                os.remove(file_path)
                print(f"Fichier supprime : {file_path}")
    except Exception as e:
        print(f"Une erreur est survenue : {str(e)}")

# Chemin d'accès du répertoire contenant les documents à imprimer
directory_path = r"Ton_Chemin_D'acces"

# Appel de la fonction pour imprimer et supprimer les documents dans le répertoire spécifié
print_and_delete_documents_in_directory(directory_path)