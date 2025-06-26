# Guide d'Installation et d'Utilisation pour PlantDiseaseDetection

## Étape 1 : Télécharger le Dataset
1. Téléchargez le dataset depuis le lien suivant :  
   [Télécharger le Dataset](https://storage.googleapis.com/kaggle-data-sets/277323/658267/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20250327%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20250327T161204Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=8d7eb7fc58b311ec1a2dd81c7563c908ff8dc97b7eaff90874dd2717723ec53e56d96982b4f5c2ca9911974eede67161edf4cca7b51a2ae207f3d66a4a0951364a4112526e8bc5447d950fc69d5f508dcb17050736c820d4d14e062adae79a192c6897d60c7b6ade8cebad3fc9bc7eaf9b2b486f2d9c1ed0dcea6b8851b220af58b977411930df84ccec9b7a8dd81684bc04c3fb61928ae533ed449fd71ce371bd37e93d35d984e6158d1ce77698f056affb3747efde8851eba2dc0df4c3a959b975731760a449bac6e891fd28419175e24a9606fb5a09c3137e34b6e1198c9abe66cd50b482407c1d38d8d9ac27d511028199892cc8bbd80e9aa92590881351)

2. Une fois téléchargé, extrayez l'archive et renommez le dossier extrait en `dataset`.

3. Déplacez le dossier `dataset` dans le répertoire `PlantDiseaseDetection/`.

---

## Étape 2 : Organiser le Répertoire `color`
1. Dans le répertoire `color`, créez un répertoire nommé `train`.

2. Déplacez le contenu actuel de `color` vers `color/train`.

3. Dans le répertoire `color`, créez un autre répertoire nommé `test`.

4. Copiez le même contenu de `color/train` dans `color/test`.

---

## Étape 3 : Entraîner le Modèle
Pour créer le fichier modèle `.h5`, exécutez la commande suivante dans votre terminal :

```bash
py.exe train.py
```

---

## Étape 4 : Tester le Modèle
Une fois le fichier modèle `.h5` généré, testez-le en exécutant la commande suivante :

```bash
py.exe test.py
```

---

Le modèle est maintenant prêt à être utilisé pour détecter les maladies des plantes !
```