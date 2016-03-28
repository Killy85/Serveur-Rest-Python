import csv
import os
import sqlite3
import webbrowser
from bottle import *


class EqActi:
    def __init__(self, comlib, actcode, actlib, actniv):
        self.ComLib = comlib
        self.ActCode = actcode
        self.ActLib = actlib
        self.ActNivLib = actniv

    def toString(self):
        return self.ActCode + " </a> <BR> " + self.ActLib + " <BR> " + self.ActNivLib + " <BR> " + self.ComLib


class EqActiLat:
    def __init__(self, ComLib, InsNom, EquNom, EquGpsX, EquGpsY):
        self.ComLib = ComLib
        self.InsNom = InsNom
        self.EquNom = EquNom
        self.EquGpsX = EquGpsX
        self.EquGpsY = EquGpsY

    def toString(self):
        return self.InsNom + " </a> <BR> " + self.EquNom + " <BR> " + self.ComLib
class Com:
    def __init__(self, ComLib):
        self.ComLib = ComLib

    def __str__(self):
        return self.ComLib


class gestBD:
    lb = None

    def connexion(self):
        return sqlite3.connect('ma_base.db')

    def insertUser(self, curs, name, age):
        data = {"name": name, "age": age}
        curs.execute("""INSERT INTO users(name, age) VALUES(:name, :age)""", data)

    def deleteUser(self, curs, name, age):
        data = {"name": name, "age": age}
        curs.execute("""DELETE FROM users where name=:name and age=:age""", data)

    def getOneByNameUser(self, curs, name):
        data = {"name": name}
        ls = curs.execute("""SELECT * FROM users where name = :name """, data)
        return ls.fetchone()

    def selectAllUser(self, curs):
        ls = curs.execute("""SELECT * FROM users""")
        return ls.fetchall()

    def selectAllNomEquipements(self, curs):
        ls = curs.execute("""SELECT EquNom FROM equipements""")
        return ls.fetchall()

    def selectCoordEquipements(self, curs, nom):
        data = {"lib": nom}
        ls = curs.execute("""SELECT EquGpsX,EquGpsY  FROM equipements where InsNom = :lib""", data)
        return ls.fetchall()

    def selectCoordEquipements(self, curs, nom, com):
        data = {"lib": nom, "com": com}
        ls = curs.execute("""SELECT EquGpsX,EquGpsY  FROM equipements where EquNom = :lib and ComLib=:com""", data)
        return ls.fetchall()
        
    def selectAllFromType(self, curs, nom, com):
        data = {"lib": nom, "com": com}
        ls = curs.execute("""SELECT ComLib,ActCode,ActLib,ActNivLib  FROM equipements where EquNom = :lib and ComLib=:com""", data)
        
    def selectAllComForType(self, curs, nom):
        data = {"lib": nom}
        ls = curs.execute("""SELECT ComLib,ActCode,ActLib,ActNivLib  FROM equipements where ComLib=:lib""", data)
        return ls.fetchall()

    def selectAllCom(self, curs, name):
        ls = curs.execute("""SELECT distinct ComLib  FROM equipements where ComLib Like """)
        ls = curs.execute("""SELECT distinct ComLib  FROM equipements where ComLib Like '%:lib% """, data)
        return ls.fetchall()

    def selectAllNomEquipementsActivite(self, curs):
        ls = curs.execute("""SELECT ActLib FROM equipements_activites""")
        return ls.fetchall()

    def selectTrucObjetSearch(self, curs, com):
        data = {"lib": com}
        ls = curs.execute("""SELECT ComLib,ActCode,ActLib,ActNivLib FROM equipements_activites WHERE ComLib = :lib """,
                          data)
        return ls.fetchall()

    def selectEquipementObjetSearch(self, curs, com):
        data = {"lib": com}
        ls = curs.execute("""SELECT ComLib,InsNom,EquNom,EquGpsX, EquGpsY FROM equipements WHERE ComLib = :lib """,
                          data)
        return ls.fetchall()

    def getOneByActLib(self, curs, lib):
        data = {"lib": lib}
        ls = curs.execute("""SELECT * FROM equipements_activites where ActLib = :lib """, data)
        return ls.fetchall()

    def getOneByCom(self, curs, com):
        data = {"lib": com}
        ls = curs.execute("""SELECT * FROM equipements_activites where ComLib = :lib """, data)
        return ls.fetchall()

    def fillDB(self, curs):
        with open('installations.csv') as (csvfile):
            reader = csv.DictReader(csvfile)
            for row in reader:
                data = {
                    "DateDeMajFiche": row["Nom usuel de l'installation"]}
                curs.execute(
                    """INSERT INTO installations(Nom,Numero,Commune,INSEE,CP,LieuDit,NumVoie,Location,) VALUES(:name, :
                    age)""",
                    data)

    def loadMap(self, city):
        url = "https://www.google.fr/maps/place/" + city
        webbrowser.open(url)

    def loadMapCoord(self, gpsX, gpsY):
        filler = ","
        if gpsX[0]=='.':
            filler += "0"
        url = "https://google.fr/maps?f=q&t=k&z=23&hl=fr&q=" + str(gpsY) + filler + str(gpsX)
        webbrowser.open(url)

    def getMapCoor(self, gpsX, gpsY):
        filler = ","
        if gpsX[0]=='.':
            filler += "0"
        url = "https://google.fr/maps?f=q&t=k&z=23&hl=fr&q=" + str(gpsY) + filler + str(gpsX)
        return url
