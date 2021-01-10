# Déployement du modèle ML avec Flask

![model_API](https://raw.githubusercontent.com/VLNTNF/online-shoppers-dataset/main/WATCHme/flask_API_1.png)

Déployement du modèle Machine Learning pour la prédition des intention des acheteurs en ligne sur un site de e-commerce.


## Pré-réquis


Vous devez avoir **Scikit Learn** _(pour le model de machine learning)_, **Pandas** _(pour la manipulation des dataframe)_, **Numpy** _(pour la manipulation des matrices et tableaux multidimensionnels)_ et **Flask** _(pour l'API)_ installés.


## Structure du projet


Ce projet comprend quatre grandes parties:

- **Online_Shoppers_Dataset.ipynb** - Il contient tout le code python depuis l'analyse des données, passant par l'essai de plusieurs modèles d'apprentissage automatique pour prédire les intentions des acheteurs en ligne sur les données du fichier online_shoppers_intention.csv, jusqu'à la sélection et la sauvegarde du meilleur modèle.

- **app.py** - Il contient l'API Flask qui reçoit les détails des visiteurs du site d'e-commerce via internet et un navigateur, et prédit si le visiteur aura l'intention de faire un achat ou pas.

- **templates** - Ce dossier contient le modèle HTML pour permettre à l'utilisateur d'entrer les détails d'un visiteur du site d'e-commerce et affiche l'intention du visiteur à faire un achat ou pas.

- **module_preprocessing.py** - C'est un module de pré-traitement et de préparation des données entrées par l'utilisateur, avant d'être passées au modèle pour étude.

- **static** - Il contient tout les fichiers relatifs au front-end comme les css, js, images, fonts.

- **onlineShopper_model.pickel** - c'est la sauvegarde de notre modèle de machine learning pour les prédictions.

- **minmaxscaler_model.pickel** - c'est la sauvegarde de notre modèle de remise à échelle.


## Lancement de l'API


1. Télécharger le dossier du projet 'Project_API'.

2. Se placer à la racine du dossier téléchargé.

3. Le dossier contient déjà le modele de machine learning **'onlineShopper_model.pickel'** et celui de remise à échelle **minmaxscaler_model.pickel** c'est OK.

4. Exécutez app.py en utilisant la commande ci-dessous pour démarrer l'API Flask.
    **`python app.py`**
    
Par défaut, flask fonctionnera sur le **port 5000**.

5. Accédez à l'URL **`http://localhost:5000`**

![index](https://raw.githubusercontent.com/VLNTNF/online-shoppers-dataset/main/WATCHme/flask_API_1.png)

Entrez ou sélectionnez les valeurs appropriées dans chaque entrée du formulaire.

![remplissage du formulaire](https://raw.githubusercontent.com/VLNTNF/online-shoppers-dataset/main/WATCHme/flask_API_2.png)

Cliquez ensuite sur **`Predict`** et vous devrez voir la prédiction True ou False exprimant signifiant l'intention du visiteur d'effectuer un achat ou pas.

![résultat de la prédiction](https://raw.githubusercontent.com/VLNTNF/online-shoppers-dataset/main/WATCHme/flask_API_3.png)


## Liens utiles

Repository : https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset  
Article source : https://link.springer.com/article/10.1007%2Fs00521-018-3523-0
