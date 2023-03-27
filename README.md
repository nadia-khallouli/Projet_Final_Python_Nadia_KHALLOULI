# Projet_Final_Python
### Extraire des données
Nous avons utilisé la bibliothèque *requests* pour récupérer le contenu de la page web et la bibliothèque *BeautifulSoup* pour extraire les données à partir du HTML. Nous avons ensuite parcouru tous les éléments HTML correspondant à des produits (avec la classe "product-tile") et extrait le "nom" et le "prix" de chaque produit pour les stocker dans une liste de tableaux (data).

### Ingérer les données dans la bdd
Nous avons créé une base de données SQLite en utilisant la bibliothèque *sqlite3*. Nous avons ensuite créé une table pour stocker les données (les noms et les prix des produits) et inséré les données extraites précédemment dans cette table. Enfin, nous avons commité les changements et fermé la connexion à la base de données

### Afficher les données sous forme de graphiquesur un Dashboard de type streamlit
Nous avons utilisé la bibliothèque *Streamlit* pour créer un dashboard interactif et afficher les données stockées dans la base de données précédemment créée. Nous avons récupéré les données de la base de données dans un dataframe pandas et les avons affichées sous forme de graphique à l'aide de la bibliothèque Matplotlib et sous forme de tableau avec la fonction **st.write()** de *Streamlit*.

### Tests unitaires
Nous avons créé trois classes de tests, une pour chaque étape précédente. La première classe de tests vérifie que les données peuvent être extraites du site web. La deuxième classe de tests vérifie que les données peuvent être insérées dans la base de données. La troisième classe de tests vérifie que les données peuvent être affichées sur le dashboard.



