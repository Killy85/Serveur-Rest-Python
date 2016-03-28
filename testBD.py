import csv
import os
import sqlite3

class gestBD:
    lb = None

    def connexion(self): # Méthode de connexion. Permet de retourner l'élément nécessaire a chaque requète sur la base
        return sqlite3.connect('ma_base.db')


    def selectAllCom(self, curs, name):  # Séléction de toute les communes apparentées au nom données. Utilisé pour l'auto-complétion
        data = {"lib": name}
        ls = curs.execute("""SELECT distinct ComLib  FROM equipements where ComLib Like '%"""+name+"""%';""")
        
        return ls.fetchall()
        
    def selectTypeForCom(self, curs, commune, name): # Sélection des équipement dont l'activité et la commune correspondent au paramètres.
        data = { "com" : commune, "name" : name}
        ls = curs.execute("""Select e.ComLib,e.InsNom,e.EquNom,e.EquGpsX, e.EquGpsY FROM equipements_activites as  ea, equipements as e WHERE ea.ActLib  Like '%"""+name+"""%' and ea.ComLib Like '%"""+commune+"""%' and e.EquipementID = ea.EquipementID""")
        return ls.fetchall();
        
    def selectAllNomEquipementsActivite(self, curs): # Selection des Activités disponible #TODO Implémenter une aut-complétion sur les activités
        ls = curs.execute("""SELECT ActLib FROM equipements_activites""")
        return ls.fetchall()

    def selectEquipementObjetSearch(self, curs, com): #Selection des équipement pour une commune donnée
        data = {"lib": com}
        ls = curs.execute("""SELECT ComLib,InsNom,EquNom,EquGpsX, EquGpsY FROM equipements WHERE ComLib = :lib """,
                          data)
        return ls.fetchall()

    def fillDB(self, curs): # Remplissage de la base de donnée depuis CSV #Deprecated
        with open('installations.csv') as (csvfile):
            reader = csv.DictReader(csvfile)
            for row in reader:
                data = {
                    "DateDeMajFiche": row["Nom usuel de l'installation"]}
                curs.execute(
                    """INSERT INTO installations(Nom,Numero,Commune,INSEE,CP,LieuDit,NumVoie,Location,) VALUES(:name, :
                    age)""",
                    data)