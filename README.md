**Description du Projet : Impression et Suppression Automatisées de Documents**

Ce projet Python vise à automatiser le processus d'impression et de suppression des documents présents dans un répertoire spécifié. Il utilise les modules intégrés `os` et `time` pour effectuer ces tâches de manière efficace et systématique.

L'algorithme commence par vérifier l'existence du chemin d'accès au répertoire spécifié. S'il n'existe pas, un message approprié est affiché et le processus s'arrête. Ensuite, il parcourt tous les fichiers dans le répertoire spécifié. Pour chaque fichier rencontré, le programme vérifie s'il s'agit effectivement d'un fichier (et non d'un sous-répertoire). Si c'est le cas, le fichier est envoyé à l'imprimante via la fonction `os.startfile()`, avec l'option "print" pour imprimer le fichier. Un message est alors affiché pour indiquer que le fichier est en cours d'impression.

Pour garantir que l'impression est terminée avant de passer à la suppression, le programme attend quelques secondes (dans ce cas, 5 secondes) à l'aide de la fonction `time.sleep()`. Après cette attente, le fichier est supprimé à l'aide de la fonction `os.remove()` et un message est affiché pour indiquer que le fichier a été supprimé avec succès.

En cas d'erreur pendant l'exécution du programme, un message d'erreur est affiché, fournissant des informations sur l'erreur rencontrée.

L'utilisateur doit spécifier le chemin d'accès du répertoire contenant les documents à imprimer à l'aide de la variable `directory_path`. Ensuite, en appelant la fonction `print_and_delete_documents_in_directory()` avec ce chemin d'accès, le processus d'impression et de suppression est déclenché pour ce répertoire spécifique.

Ce projet peut être utile dans divers contextes où des documents doivent être imprimés et supprimés automatiquement après traitement, comme dans le cadre de flux de travail automatisés ou de tâches de maintenance régulières.
