from main import return_backwards_string, get_mode
import unittest
import os

class TestMain(unittest.TestCase):
    def test_return_backwards_string(self):
        # Simuler une erreur en passant une valeur incorrecte à la fonction
        random_string = 12345  # Valeur incorrecte
        # Ceci va échouer car la fonction ne peut pas inverser un entier
        with self.assertRaises(TypeError):
            return_backwards_string(random_string)

    def test_get_mode(self):
        # Simuler une erreur en modifiant l'environnement pour qu'il manque une clé
        del os.environ["MODE"]  # Supprimer la clé MODE de l'environnement
        # Ceci va échouer car la fonction s'attend à trouver la clé MODE dans l'environnement
        with self.assertRaises(TypeError):
            get_mode()

if __name__ == "__main__":
    unittest.main()
