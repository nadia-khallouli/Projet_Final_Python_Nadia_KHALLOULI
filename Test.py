import unittest
import sqlite3
import requests
from bs4 import BeautifulSoup
import pandas as pd

class TestExtraction(unittest.TestCase):
    def test_extractions(self):
        # Obtention du contenu HTML de la page web
        response = requests.get('https://www.carrefour.fr/r/bio-et-ecologie/bio-petit-prix')
        html = response.content
        
        # Parsing du contenu HTML avec BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        
        # Extraction des noms et des prix des produits
        produits = []
        for product in soup.find_all('div', class_='product-tile'):
            nom = product.find('a', class_='product-tile-title').text.strip()
            prix = float(product.find('span', class_='value').text.strip().replace(',', '.'))
            produits.append({'nom': nom, 'prix': prix})
        
        # Vérification que la liste de produits n'est pas vide
        self.assertTrue(len(produits) > 0)


class TestInsertion(unittest.TestCase):
    def test_insertion(self):
        # Création d'une base de données SQLite en mémoire
        conn = sqlite3.connect(':memory:')
        
        # Création d'une table pour les produits
        conn.execute('CREATE TABLE produits (nom TEXT, prix REAL)')
        
        # Insertion de données dans la table
        produits = [{'nom': 'produit 1', 'prix': 1.99}, {'nom': 'produit 2', 'prix': 2.99}]
        for produit in produits:
            conn.execute('INSERT INTO produits (nom, prix) VALUES (?, ?)', (produit['nom'], produit['prix']))
        
        # Récupération du nombre de lignes dans la table
        cursor = conn.execute('SELECT COUNT(*) FROM produits')
        result = cursor.fetchone()[0]
        
        # Vérification que le nombre de lignes correspond au nombre de données insérées
        self.assertEqual(result, len(produits))


class TestDashboard(unittest.TestCase):
    def test_dashboard(self):
        # Création d'une base de données SQLite en mémoire
        conn = sqlite3.connect(':memory:')
        
        # Création d'une table pour les produits
        conn.execute('CREATE TABLE produits (nom TEXT, prix REAL)')
        
        # Insertion de données dans la table
        produits = [{'nom': 'produit 1', 'prix': 1.99}, {'nom': 'produit 2', 'prix': 2.99}]
        for produit in produits:
            conn.execute('INSERT INTO produits (nom, prix) VALUES (?, ?)', (produit['nom'], produit['prix']))
        
        # Récupération des données de la table avec pandas
        df = pd.read_sql_query('SELECT * FROM produits', conn)
        
        # Vérification que le nombre de lignes correspond au nombre de données insérées
        self.assertTrue(len(df) == len(produits))


if __name__ == '__main__':
    # Exécution des tests avec unittest
    unittest.main()
