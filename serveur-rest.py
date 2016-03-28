
from testBD import *
from bottle import *
from googlemaps import *
import json
import os




if __name__ == "__main__":

    def closecallback():
        exit(0)


    #Méthode permettant de renvoyer sous la forme de Json les num premiers équipements pour la commune name
    @route('/equipements/<name>/<num>', method='post')
    def index(name, num):
        response.set_header('Access-Control-Allow-Origin','*')
        i=0
        strl='{ "item" :  ['
        activ = gestBD.selectEquipementObjetSearch(gestBD, connexion.cursor(),name)
        numRep = int(num) if int(num)<=len(activ) else len(activ)
        if len(activ) > 0: #Test de contenance 
            for i in range(int(numRep)):
                strl = strl +"""
                         {"Commune" :\""""+trim(activ[i][0])+"""\","InsNom" :  \""""+trim(activ[i][1])+"""\","EquNom" : \""""+trim(activ[i][2])+"""\","EquGpsX" : \""""+trim(activ[i][3])+"""\","EquGpsY" : \""""+trim(activ[i][4])+"""\"},"""
            
            strl=strl[:-1];
            
        strl=strl + "]}";

        return strl


    #Méthode permettant de récupérer sous la forme de Json tout les équipements permettant de pratiquer une activité sportive ( name) pour une ville choisie
    @route('/search/<commune>/<name>', method='post')
    def index(commune,name):
        response.set_header('Access-Control-Allow-Origin','*')
        strl='{"item" : ['
        i=0
        activ = gestBD.selectTypeForCom(gestBD, connexion.cursor(),commune, name)
        if len(activ) > 0:#Test de contenance 
            for i in range(len(activ)):
                strl = strl +"""
                             {"Commune" :\""""+activ[i][0].replace('"','\\"')+"""\","InsNom" :  \""""+activ[i][1].replace('"','\\"')+"""\","EquNom" : \""""+activ[i][2].replace('"','\\"')+"""\","EquGpsX" : \""""+activ[i][3].replace('"','\\"')+"""\","EquGpsY" : \""""+activ[i][4].replace('"','\\"')+"""\"},"""
            strl=strl[:-1];
        strl=strl + "]}"
        return strl;
    

      #Méthode permettant la récupération des villes dont le nom ressemble a la proposition. Utilisée pour l'autocomplétion. 
    @route('/<villes>', method='get')
    def index(villes):
        response.set_header('Access-Control-Allow-Origin','*')
        strl='jsoncallback({';
        activ = gestBD.selectAllCom(gestBD, connexion.cursor(), villes)
        i=0
        if len(activ) > 0: #Test de contenance 
            for i in range(len(activ)):
                strl = strl + '"'+str(i+1)+'":{ "ville" :"'+trim(activ[i][0])+'","cp":"40090"},';
                i=i+1;
        strl= strl +'"count":'+str(i)+',"typeretour":"cp"});' 
        return strl
        
        
    def trim(strl):
        strl.replace("'","\\'")
        return strl.replace('"','\\"')

    connexion= gestBD.connexion(gestBD) #Création de la connexion à la base de donnée.
    run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080))) # Démarrage du serveur.