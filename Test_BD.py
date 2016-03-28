import unittest
import sqlite3
from testBD import gestBD

class test_bd(unittest.TestCase):

    
    def test_selectAllNomEquipements(self):
        connexion= gestBD.connexion(gestBD)
        self.assertEqual( gestBD.selectAllNomEquipements(gestBD,connexion.cursor())[0][0], "Terrain de football engazonné" )
        
    def test_selectCoordEquipements(self):
        connexion= gestBD.connexion(gestBD)
        self.assertEqual(gestBD.selectCoordEquipements(gestBD,connexion.cursor(), "Terrain de football engazonné")[0], ('-1.53106000','47.55761000') )

    def test_selectCoordEquipements(self):
        connexion= gestBD.connexion(gestBD)
        self.assertEqual(gestBD.selectCoordEquipements(gestBD,connexion.cursor(), "Terrain de football engazonné", "Abbaretz")[0], ('-1.53106000','47.55761000') )
        
    def test_selectAllCom(self):
        connexion= gestBD.connexion(gestBD)
        self.assertEqual(str(gestBD.selectAllCom(gestBD,connexion.cursor())[0][0]), "Abbaretz")


        
    def test_selectAllNomEquipementsActivite(self):
        connexion= gestBD.connexion(gestBD)
        self.assertEqual(gestBD.selectAllNomEquipementsActivite(gestBD,connexion.cursor())[0][0], "Football / Football en salle (Futsal)" )

if __name__ == '__main__':
    unittest.main()