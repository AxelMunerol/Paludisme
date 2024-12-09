# Project: CNN Model and Flask Application

Ce projet consiste à créer un modèle de réseau de neurones convolutifs (CNN) pour la classification d'images, puis à déployer ce modèle à l'aide d'une application Flask. Voici les étapes à suivre pour exécuter le projet.

## Prérequis

Avant de commencer, assurez-vous que vous avez installé les outils et dépendances suivants :

1. **Python** (version 3.x recommandée)
2. **Docker** (si vous souhaitez exécuter l'application dans un conteneur)
3. **pip** (le gestionnaire de paquets Python)

Vous devrez également installer les bibliothèques Python suivantes (indiquées dans le fichier `requirements.txt`):


pip install -r requirements.txt
Les principales bibliothèques requises sont :

TensorFlow (pour la création du modèle CNN)
Flask (pour déployer l'application web)
NumPy et Pandas (pour la gestion des données)
Matplotlib (pour la visualisation des résultats)
Étape 1 : Lancer le modèle CNN
Le modèle CNN est construit dans le notebook Jupyter. Voici les étapes pour créer et entraîner le modèle :

Ouvrir le Notebook Jupyter :

bash
Copier le code
jupyter notebook
Exécuter les cellules du notebook :

Chargez les données (par exemple, un jeu de données d'images pour la classification).
Construisez le modèle CNN à l'aide de TensorFlow ou Keras.
Entraînez le modèle en exécutant la cellule d'entraînement.
Le modèle sera sauvegardé après l'entraînement dans un fichier (par exemple, cnn_model.h5).

Étape 2 : Déployer l'application Flask
Une fois que le modèle est formé et sauvegardé, vous pouvez déployer l'application Flask pour servir ce modèle. Voici comment procéder :

Exécuter l'application Flask :

Ouvrez un terminal, allez dans le répertoire du projet, puis exécutez la commande suivante pour démarrer l'application Flask :

bash
Copier le code
python app.py
Cela lancera le serveur Flask sur http://127.0.0.1:5000, et vous pourrez interagir avec l'application via le navigateur.

Docker (facultatif) : Si vous préférez exécuter l'application dans un conteneur Docker, vous pouvez le faire en suivant ces étapes :

Construire l'image Docker :

bash
Copier le code
docker build -t cnn-flask-app .
Lancer le conteneur Docker :

bash
Copier le code
docker run -p 5000:5000 cnn-flask-app
Cela exposera l'application Flask sur le port 5000 de votre machine.

Structure du projet
Voici la structure du répertoire du projet :

php
Copier le code
.
├── app.py                # Code de l'application Flask
├── cnn_model.keras       # Modèle CNN sauvegardé
├── dl_preprocess_modified.ipynb  # Notebook pour la prétraitement des données
├── Dockerfile            # Fichier de configuration Docker
├── requirements.txt      # Liste des dépendances Python
├── .venv                 # Environnement virtuel Python
├── static                # Dossier pour les fichiers statiques (images, etc.)
├── templates             # Dossier pour les templates HTML
└── .ipynb_checkpoints    # Dossier pour les checkpoints de Jupyter
Fonctionnalités de l'application Flask
Page d'accueil : Affiche une interface simple où vous pouvez télécharger une image à classer.
Classification d'image : Le modèle CNN classifie l'image téléchargée et affiche le résultat.
Dépannage
Si vous rencontrez des erreurs liées à Flask, vérifiez si le port 5000 est déjà utilisé par une autre application.
Si l'application ne démarre pas, assurez-vous que toutes les dépendances sont installées correctement en exécutant pip install -r requirements.txt.
Conclusion
Ce projet démontre comment créer un modèle CNN avec TensorFlow et le déployer dans une application Flask. Vous pouvez l'utiliser comme point de départ pour des projets de classification d'images ou d'autres tâches de machine learning avec un modèle préexistant.
