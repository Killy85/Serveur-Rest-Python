import csv
import os

import sqlite3

class gestionnaireCsvNom:
        def AfficherTous(self):
                ls = " "
                try:
                        f = open('nom.csv')
                except IOError:
                        print("erreur d'ouverture du fichier");
                else:
                        with f as csvfile:
                                reader = csv.reader(csvfile, delimiter=" ")
                                for row in reader:
                                        ls = row[0].split(";")
                                        p = Personne(ls[0], ls[1], ls[2])
                                        print(p)

        def ajouter(self, nom, prenom, pseudo):
                try:
                        f = open('nom.csv', 'a+')
                except IOError:
                        print("erreur d'ouverture du fichier");
                else:
                        with open('nom.csv', 'a+') as csvfile:
                                writer = csv.writer(csvfile, delimiter=";")
                                writer.writerow([nom, prenom, pseudo])

        def supprimer(self,nom):
                liste_pers = []
                try:
                        f = open('nom.csv')
                except IOError:
                        print("erreur d'ouverture du fichier");
                else:
                        with f as csvfile:
                                reader = csv.reader(csvfile, delimiter=" ")
                                for row in reader:
                                        ls = row[0].split(";")
                                        liste_pers.append(Personne(ls[0], ls[1], ls[2]))
                        os.remove("nom.csv")
                        for pers in liste_pers:
                                if (pers.nom != nom):
                                        gestionnaireCsvNom.ajouter(self, pers.nom, pers.prenom, pers.pseudo)


class Personne:
        def __init__(self, nom, prenom, pseudo):
                self.prenom = prenom
                self.nom = nom
                self.pseudo = pseudo

        def __str__(self):
                return self.nom + " " + self.prenom + " " + self.pseudo

if __name__ == "__main__":
        g = gestionnaireCsvNom()
        print("--------------------------------")
        g.AfficherTous()
        print("--------------------------------")
        g.ajouter("salaun", "nathan" ,"biflan")
        g.AfficherTous()
        print("--------------------------------")
        g.supprimer("salaun")
        g.AfficherTous()
        print("--------------------------------")
