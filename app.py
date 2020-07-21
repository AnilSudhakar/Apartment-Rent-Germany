# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 10:23:58 2020

@author: Anil
"""
from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("apartment_rf.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("Prototype3.html")

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        federal=0
        # Federal State
        region_one=request.form['federal_state']
        if(region_one=="Bayern"):
        	 federal=15
        elif(region_one=="Berlin"):
        	 federal=14
        elif(region_one=="Hessen"):
        	 federal=13
        elif(region_one=="Hamburg"):
        	 federal=12
        elif(region_one=="Baden Württemberg"):
        	 federal=11
        elif(region_one=="Rheinland Pfalz"):
        	 federal=10
        elif(region_one=="Schleswig Holstein"):
        	 federal=9
        elif(region_one=="Bremen"):
        	 federal=8
        elif(region_one=="Saarland"):
        	 federal=7
        elif(region_one=="Niedersachsen"):
        	 federal=6
        elif(region_one=="Nordrhein Westfalen"):
        	 federal=5
        elif(region_one=="Sachsen"):
        	 federal=4
        elif(region_one=="Brandenburg"):
        	 federal=3
        elif(region_one=="Mecklenburg Vorpommern"):
        	 federal=2
        elif(region_one=="Thüringen"):
        	 federal=1
        else:
              if(region_one=="Sachsen Anhalt"):
        	      federal=0

        #Living area in sq meters
        living = int(request.form["Living_Area"])
       
        
        #Region
        region=0
        region_two=request.form["region"]
        if(region_two=="Brandenburg an der Havel"):
        	 region=0
        elif(region_two=="Neubrandenburg"):
        	 region=1
        elif(region_two=="Greifswald"):
        	 region=2
        elif(region_two=="Plauen"):
        	 region=3
        elif(region_two=="Görlitz Kreis"):
        	 region=4
        elif(region_two=="Saalekreis"):
        	 region=5
        elif(region_two=="Mittelsachsen Kreis"):
        	 region=6
        elif(region_two=="Mansfeld Südharz Kreis"):
        	 region=7
        elif(region_two=="Greiz Kreis"):
        	 region=8
        elif(region_two=="Börde Kreis"):
        	 region=9
        elif(region_two=="Zwickau Kreis"):
        	 region=10
        elif(region_two=="Gera"):
        	 region=11
        elif(region_two=="Oberspreewald Lausitz Kreis"):
        	 region=12
        elif(region_two=="Erzgebirgskreis"):
        	 region=13
        elif(region_two=="Burgenlandkreis"):
        	 region=14
        elif(region_two=="Salzlandkreis"):
        	 region=15
        elif(region_two=="Uckermark Kreis"):
        	 region=16
        elif(region_two=="Chemnitz"):
        	 region=17
        elif(region_two=="Altenburger Land Kreis"):
        	 region=18
        elif(region_two=="Nordhausen Kreis"):
        	 region=19
        elif(region_two=="Dessau Roßlau"):
        	 region=20
        elif(region_two=="Anhalt Bitterfeld Kreis"):
        	 region=21
        elif(region_two=="Mecklenburg Strelitz Kreis"):
        	 region=22
        elif(region_two=="Salzgitter"):
        	 region=23
        elif(region_two=="Zwickau"):
        	 region=24
        elif(region_two=="Wilhelmshaven"):
        	 region=25
        elif(region_two=="Harz Kreis"):
        	 region=26
        elif(region_two=="Halle Saale"):
        	 region=27
        elif(region_two=="Stendal Kreis"):
        	 region=28
        elif(region_two=="Nordwestmecklenburg Kreis"):
        	 region=29
        elif(region_two=="Bautzen Kreis"):
        	 region=30
        elif(region_two=="Nordsachsen Kreis"):
        	 region=31
        elif(region_two=="Helmstedt Kreis"):
        	 region=32
        elif(region_two=="Leipzig Kreis"):
        	 region=33
        elif(region_two=="Bremerhaven"):
        	 region=34
        elif(region_two=="Unstrut Hainich Kreis"):
        	 region=35
        elif(region_two=="Gelsenkirchen"):
        	 region=36
        elif(region_two=="Meißen Kreis"):
        	 region=37
        elif(region_two=="Sächsische Schweiz Osterzgebirge Kreis"):
        	 region=38
        elif(region_two=="Magdeburg"):
        	 region=39
        elif(region_two=="Nordvorpommern Kreis"):
        	 region=40
        elif(region_two=="Hagen"):
        	 region=41
        elif(region_two=="Duisburg"):
        	 region=42
        elif(region_two=="Northeim Kreis"):
        	 region=43
        elif(region_two=="Märkischer Kreis"):
        	 region=44
        elif(region_two=="Schwerin"):
        	 region=45
        elif(region_two=="Goslar Kreis"):
        	 region=46
        elif(region_two=="Gotha Kreis"):
        	 region=47
        elif(region_two=="Eisenach"):
        	 region=48
        elif(region_two=="Cottbus"):
        	 region=49
        elif(region_two=="Recklinghausen Kreis"):
        	 region=50
        elif(region_two=="Ludwigslust Kreis"):
        	 region=51
        elif(region_two=="Ennepe Ruhr Kreis"):
        	 region=52
        elif(region_two=="Barnim Kreis"):
        	 region=53
        elif(region_two=="Wuppertal"):
        	 region=54
        elif(region_two=="Kiel"):
        	 region=55
        elif(region_two=="Bochum"):
        	 region=56
        elif(region_two=="Kassel"):
        	 region=57
        elif(region_two=="Essen"):
        	 region=58
        elif(region_two=="Hildesheim Kreis"):
        	 region=59
        elif(region_two=="Erfurt"):
        	 region=60
        elif(region_two=="Schleswig Flensburg Kreis"):
        	 region=61
        elif(region_two=="Darmstadt Dieburg Kreis"):
        	 region=62
        elif(region_two=="Rendsburg Eckernförde Kreis"):
        	 region=63
        elif(region_two=="Neunkirchen Kreis"):
        	 region=64
        elif(region_two=="Stadtverband Saarbrücken Kreis"):
        	 region=65
        elif(region_two=="Krefeld"):
        	 region=66
        elif(region_two=="Mayen Koblenz Kreis"):
        	 region=67
        elif(region_two=="Mönchengladbach"):
        	 region=68
        elif(region_two=="Dortmund"):
        	 region=69
        elif(region_two=="Saarpfalz Kreis"):
        	 region=70
        elif(region_two=="Celle Kreis"):
        	 region=71
        elif(region_two=="Oldenburg Oldenburg"):
        	 region=72
        elif(region_two=="Passau"):
        	 region=73
        elif(region_two=="Trier"):
        	 region=74
        elif(region_two=="Marburg Biedenkopf Kreis"):
        	 region=75
        elif(region_two=="Mettmann Kreis"):
        	 region=76
        elif(region_two=="Leipzig"):
        	 region=77
        elif(region_two=="Flensburg"):
        	 region=78
        elif(region_two=="Gießen Kreis"):
        	 region=79
        elif(region_two=="Herzogtum Lauenburg Kreis"):
        	 region=80
        elif(region_two=="Göttingen Kreis"):
        	 region=81
        elif(region_two=="Rostock"):
        	 region=82
        elif(region_two=="Dresden"):
        	 region=83
        elif(region_two=="Stade Kreis"):
        	 region=84
        elif(region_two=="Aachen"):
        	 region=85
        elif(region_two=="Hannover Kreis"):
        	 region=86
        elif(region_two=="Pinneberg Kreis"):
        	 region=87
        elif(region_two=="Augsburg"):
        	 region=88
        elif(region_two=="Bad Kreuznach Kreis"):
        	 region=89
        elif(region_two=="Erlangen"):
        	 region=90
        elif(region_two=="Saarlouis Kreis"):
        	 region=91
        elif(region_two=="Main Kinzig Kreis"):
        	 region=92
        elif(region_two=="Lüneburg Kreis"):
        	 region=93
        elif(region_two=="Osnabrück"):
        	 region=94
        elif(region_two=="Braunschweig"):
        	 region=95
        elif(region_two=="Nürnberg"):
        	 region=96
        elif(region_two=="Harburg Kreis"):
        	 region=97
        elif(region_two=="Koblenz"):
        	 region=98
        elif(region_two=="Groß Gerau Kreis"):
        	 region=99
        elif(region_two=="Mainz Bingen Kreis"):
        	 region=100
        elif(region_two=="Segeberg Kreis"):
        	 region=101
        elif(region_two=="Fürth"):
        	 region=102
        elif(region_two=="Ingolstadt"):
        	 region=103
        elif(region_two=="Westerwaldkreis"):
        	 region=104
        elif(region_two=="Würzburg"):
        	 region=105
        elif(region_two=="Karlsruhe Kreis"):
        	 region=106
        elif(region_two=="Dahme Spreewald Kreis"):
        	 region=107
        elif(region_two=="Bergstraße Kreis"):
        	 region=108
        elif(region_two=="Rheingau Taunus Kreis"):
        	 region=109
        elif(region_two=="Mannheim"):
        	 region=110
        elif(region_two=="Potsdam Mittelmark Kreis"):
        	 region=111
        elif(region_two=="Potsdam"):
        	 region=112
        elif(region_two=="Hannover"):
        	 region=113
        elif(region_two=="Rhein Neckar Kreis"):
        	 region=114
        elif(region_two=="Wetteraukreis"):
        	 region=115
        elif(region_two=="Mainz"):
        	 region=116
        elif(region_two=="Karlsruhe"):
        	 region=117
        elif(region_two=="Aschaffenburg"):
        	 region=118
        elif(region_two=="Regensburg"):
        	 region=119
        elif(region_two=="Stormarn Kreis"):
        	 region=120
        elif(region_two=="Offenbach Kreis"):
        	 region=121
        elif(region_two=="Bonn"):
        	 region=122
        elif(region_two=="Bremen"):
        	 region=123
        elif(region_two=="Offenbach am Main"):
        	 region=124
        elif(region_two=="Esslingen Kreis"):
        	 region=125
        elif(region_two=="Lörrach Kreis"):
        	 region=126
        elif(region_two=="Heilbronn"):
        	 region=127
        elif(region_two=="Darmstadt"):
        	 region=128
        elif(region_two=="Heilbronn Kreis"):
        	 region=129
        elif(region_two=="Ludwigsburg Kreis"):
        	 region=130
        elif(region_two=="Hamburg"):
        	 region=131
        elif(region_two=="Rosenheim Kreis"):
        	 region=132
        elif(region_two=="Düsseldorf"):
        	 region=133
        elif(region_two=="Main Taunus Kreis"):
        	 region=134
        elif(region_two=="Köln"):
        	 region=135
        elif(region_two=="Wiesbaden"):
        	 region=136
        elif(region_two=="Böblingen Kreis"):
        	 region=137
        elif(region_two=="Hochtaunuskreis"):
        	 region=138
        elif(region_two=="Berlin"):
        	 region=139
        elif(region_two=="München Kreis"):
        	 region=140
        elif(region_two=="Stuttgart"):
        	 region=141
        elif(region_two=="Heidelberg"):
        	 region=142
        elif(region_two=="Frankfurt am Main"):
        	 region=143
        else:
              if(region_two=="München"):
        	      region=144

        #Number of rooms
        rooms=int(request.form["Rooms"])
        
        
        #Cities within the regions
        Adalbertsteinweg=0
        Adlershof_Treptow=0
        Ahrensburg=0
        Alfeld_Leine=0
        Alt_Hamborn=0
        Alt_Hohenschönhausen_Hohenschönhausen=0
        Altena=0
        Altenburg=0
        Altenessen_Süd=0
        Altenhagen=0
        Altlindenau=0
        Altstadt_Neustadt_Nord=0
        Altstadt_Neustadt_Süd=0
        Altstadt_Innenstadt=0
        Altstadt_St_Sebald=0
        Andernach=0
        Andreasvorstadt=0
        Annaberg_Buchholz=0
        Aschersleben=0
        Aubing=0
        Aue=0
        Bad=0
        Bad_Aibling=0
        Bad_Cannstatt=0
        Bad_Dürrenberg=0
        Bad_Gandersheim=0
        Bad_Godesberg=0
        Bad_Harzburg=0
        Bad_Homburg_vor_der_Höhe=0
        Bad_Kreuznach=0
        Bad_Langensalza=0
        Bad_Münster_am_Stein_Ebernburg=0
        Bad_Nauheim=0
        Bad_Orb=0
        Bad_Rappenau=0
        Bad_Soden_am_Taunus=0
        Bad_Vilbel=0
        Bahnhofsviertel=0
        Bahnhofsvorstadt=0
        Bahnstadt=0
        Barmen=0
        Barsinghausen=0
        Barth=0
        Bautzen=0
        Beckhausen=0
        Beeck=0
        Bendorf=0
        Bensheim=0
        Bergedorf=0
        Bergen=0
        Bernau_am_Chiemsee=0
        Bernau_bei_Berlin=0
        Bessungen=0
        Beuel=0
        Biebrich=0
        Biesdorf_Marzahn=0
        Bietigheim_Bissingen=0
        Bilk=0
        Bingen_am_Rhein=0
        Bismarck=0
        Bitterfeld_Wolfen=0
        Blasewitz=0
        Bockenheim=0
        Bockum=0
        Bogenhausen=0
        Boizenburg_Elbe=0
        Borna=0
        Braunsbedra=0
        Bretten=0
        Briesnitz=0
        Bruchsal=0
        Bruck=0
        Buchholz_in_der_Nordheide=0
        Buckau=0
        Buer=0
        Bulmke_Hüllen=0
        Buxtehude=0
        Böblingen=0
        Böhlen=0
        Bühlau_Weißer_Hirsch=0
        Bürgerfelde=0
        Calau=0
        Castrop_Rauxel=0
        Celle=0
        Charlottenburg_Charlottenburg=0
        Chrieschwitz=0
        Clausthal_Zellerfeld=0
        Connewitz=0
        Coswig=0
        Cotta=0
        Cracau=0
        Crimmitschau=0
        Damm=0
        Darmstadt_Mitte=0
        Darmstadt_Nord=0
        Datteln=0
        Datzeviertel=0
        Debschwitz=0
        Delitzsch=0
        Dellviertel=0
        Derendorf=0
        Dieburg=0
        Dodesheide=0
        Dorsten=0
        Dotzheim=0
        Dreieich=0
        Drewitz=0
        Duissern=0
        Durlach=0
        Döbeln=0
        Düsseltal=0
        Eberswalde=0
        Eckernförde=0
        Eilenburg=0
        Einbeck=0
        Elberfeld=0
        Elberfeld_West=0
        Elmshorn=0
        Ennepetal=0
        Erkrath=0
        Erle=0
        Eschborn=0
        Esslingen_am_Neckar=0
        Ettlingen=0
        Eversten=0
        Fedderwardergroden=0
        Fermersleben=0
        Filderstadt=0
        Flingern_Nord=0
        Frankenberg=0
        Frankenberg_Sachsen=0
        Frauenland=0
        Freital=0
        Friedberg_Hessen=0
        Friedrichsdorf=0
        Friedrichsfelde_Lichtenberg=0
        Friedrichshain_Friedrichshain=0
        Friedrichstadt=0
        Frohnhausen=0
        Gaarden_Ost=0
        Galgenhof=0
        Gallusviertel=0
        Garbsen=0
        Gartenfeld=0
        Gebiet_Reichenbacher_Str_Freiheitssiedlung=0
        Geestemünde=0
        Geesthacht=0
        Gelnhausen=0
        Gera_Ost=0
        Gevelsberg=0
        Gießen=0
        Gladbach=0
        Gladbeck=0
        Glauchau=0
        Gleisdreieck=0
        Glockenhof=0
        Gohlis_Mitte=0
        Gohlis_Nord=0
        Gohlis_Süd=0
        Golzheim=0
        Gorbitz_Süd=0
        Goslar=0
        Gotha=0
        Greiz=0
        Grevesmühlen=0
        Grimma=0
        Groß_Buchholz=0
        Großenhain=0
        Gruna=0
        Göttingen=0
        Haar=0
        Haidenhof_Nord=0
        Haidhausen=0
        Hainichen=0
        Halberstadt=0
        Hamme=0
        Hanau=0
        Handelshäfen=0
        Hangeweiher=0
        Harburg=0
        Hartenberg_Münchfeld=0
        Haselbrunn=0
        Haspe=0
        Hassel=0
        Hattingen=0
        Heckinghausen=0
        Heilbronner_Kernstadt=0
        Heiligenhaus=0
        Hellersdorf_Hellersdorf=0
        Helmstedt=0
        Heppenheim_Bergstraße=0
        Heppens=0
        Herten=0
        Hettstedt=0
        Hilden=0
        Hildesheim=0
        Hochemmerich=0
        Hochheide=0
        Hofheim_am_Taunus=0
        Hohenlimburg=0
        Hohenstein_Ernstthal=0
        Hohenstücken=0
        Holsterhausen=0
        Homburg=0
        Huckarde=0
        Hörde=0
        Idstein=0
        Ingelheim_am_Rhein=0
        Innenstadt_Jungbusch=0
        Innere_Altstadt=0
        Innere_Neustadt=0
        Innerstädtischer_Bereich_Mitte=0
        Innerstädtischer_Bereich_Nord=0
        Innerstädtischer_Bereich_Süd=0
        Innstadt=0
        Iserlohn=0
        Johannstadt_Nord=0
        Johannstadt_Süd=0
        Kaiserlei=0
        Kaltenkirchen=0
        Kamenz=0
        Katernberg=0
        Katzwang_Reichelsdorf_Ost_Reichelsdorfer_Keller=0
        Kaßberg=0
        Kelkheim_Taunus=0
        Kirchditmold=0
        Kirchrode=0
        Kitzscher=0
        Kray=0
        Kreuzberg_Kreuzberg=0
        Kruppwerke=0
        Krämpfervorstadt=0
        Kröpeliner_Tor_Vorstadt=0
        Käfertal=0
        Königstein_im_Taunus=0
        Köpenick_Köpenick=0
        Köthen_Anhalt=0
        Langen_Hessen=0
        Langenfeld_Rheinland=0
        Langenhagen=0
        Langenhorn=0
        Langerfeld_Beyenburg=0
        Lauchhammer=0
        Lausen_Grünau=0
        Lebenstedt=0
        Lechhausen=0
        Leipziger_Str=0
        Leipziger_Vorstadt=0
        Leonberg=0
        Leuben=0
        Leubnitz_Neuostra=0
        Lichtenberg_Lichtenberg=0
        Lichtenstein_Sachsen=0
        Lichterfelde_Steglitz=0
        Limbach_Oberfrohna=0
        List=0
        Loschwitz_Wachwitz=0
        Ludwigsburg=0
        Ludwigslust=0
        Ludwigsvorstadt_Isarvorstadt=0
        Lusan_Brüte=0
        Lusan_Laune=0
        Lutherplatz_Thüringer_Bahnhof=0
        Lutherstadt_Eisleben=0
        Lutherviertel=0
        Löbau=0
        Löbtau_Nord=0
        Löbtau_Süd=0
        Lörrach=0
        Lüdenscheid=0
        Lüneburg=0
        Maintal=0
        Marburg=0
        Marienthal_Ost=0
        Markkleeberg=0
        Markranstädt=0
        Marl=0
        Marxloh=0
        Marzahn_Marzahn=0
        Maximin=0
        Maxvorstadt=0
        Mayen=0
        Meerane=0
        Meißen=0
        Merseburg=0
        Metternich=0
        Mettmann=0
        Meuselwitz=0
        Mickten=0
        Milbertshofen=0
        Mitte_Mitte=0
        Mitte_Nord=0
        Mitte_West=0
        Mittelmeiderich=0
        Mittelstadt=0
        Mittweida=0
        Montabaur=0
        Mueßer_Holz=0
        Möckern=0
        Mörfelden_Walldorf=0
        Mühlhausen_Thüringen=0
        Mülheim=0
        Mürwik=0
        Naumburg_Saale=0
        Naußlitz=0
        Neckarstadt_Ost_Wohlgelegen=0
        Neckarstadt_West=0
        Neckarsulm=0
        Nette=0
        Neu_Isenburg=0
        Neu_Olvenstedt=0
        Neue_Neustadt=0
        Neuenheim=0
        Neuhausen=0
        Neukölln_Neukölln=0
        Neumühl=0
        Neundorfer_Vorstadt=0
        Neunkirchen=0
        Neuplanitz=0
        Neustrelitz=0
        Niederrad=0
        Nord_Holland=0
        Nordend_Ost=0
        Nordend_West=0
        Norderstedt=0
        Nordhausen=0
        Nordost=0
        Nordvorstadt=0
        Northeim=0
        Nördliche_Innenstadt=0
        Nördliche_Neustadt=0
        Oberbarmen=0
        Oberbilk=0
        Obergiesing=0
        Obermarxloh=0
        Obermeiderich=0
        Obermenzing=0
        Oberschöneweide_Köpenick=0
        Obersendling=0
        Oberstadt=0
        Oberursel_Taunus=0
        Oschatz=0
        Oschersleben_Bode=0
        Ost=0
        Ostend=0
        Ottobrunn=0
        Pankow_Pankow=0
        Pasing=0
        Paulsstadt=0
        Pempelfort=0
        Perlach=0
        Pieschen_Nord_Trachenberge=0
        Pieschen_Süd=0
        Pinneberg=0
        Pirna=0
        Plagwitz=0
        Ponttor=0
        Poppelsdorf=0
        Prenzlau=0
        Prenzlauer_Berg_Prenzlauer_Berg=0
        Prohlis_Süd=0
        Pölbitz=0
        Quedlinburg=0
        Radeberg=0
        Radeberger_Vorstadt=0
        Radebeul=0
        Rahlstedt=0
        Ratingen=0
        Recklinghausen=0
        Reick=0
        Reinickendorf_Reinickendorf=0
        Reißiger_Vorstadt=0
        Rendsburg=0
        Reudnitz_Thonberg=0
        Reusa_mit_Sorga=0
        Rheingauviertel_Hollerborn=0
        Rheinhausen_Mitte=0
        Rheydt=0
        Ribnitz_Damgarten=0
        Riedberg=0
        Riesa=0
        Rodgau=0
        Ronsdorf=0
        Rotthausen=0
        Roßlau=0
        Rödelheim=0
        Rüsselsheim_am_Main=0
        Rüttenscheid=0
        Saarbrücken=0
        Saarlouis=0
        Sachsendorf=0
        Sachsenhausen_Nord=0
        Sachsenhausen_Süd=0
        Sandow=0
        Sangerhausen=0
        Schalke=0
        Schkeuditz=0
        Schleswig=0
        Schloßchemnitz=0
        Schmellwitz=0
        Schoppershof=0
        Schreventeich=0
        Schwabing=0
        Schwabing_West=0
        Schwarzenbek=0
        Schwelm=0
        Schwetzingen=0
        Schwetzingerstadt_Oststadt=0
        Schönebeck_Elbe=0
        Schöneberg_Schöneberg=0
        Schönefeld=0
        Schönefeld_Abtnaundorf=0
        Schöningen=0
        Schönwalde_II=0
        Sebnitz=0
        Seesen=0
        Seevetal=0
        Seevorstadt_Ost=0
        Senftenberg=0
        Siedlung_Neundorf=0
        Silberhöhe=0
        Sindelfingen=0
        Sinsheim=0
        Solln=0
        Spandau_Spandau=0
        Spremberger_Vorstadt=0
        Staaken_Spandau=0
        Stade=0
        Stadtfeld_Ost=0
        Stadtfeld_West=0
        Stadtgebiet_Ost=0
        Stadtgebiet_Süd=0
        Stadtmitte=0
        Steglitz_Steglitz=0
        Stendal=0
        Stephanskirchen=0
        Strehlen=0
        Striesen_Ost=0
        Striesen_Süd=0
        Striesen_West=0
        Stötteritz=0
        Sudenburg=0
        Südfriedhof=0
        Südinnenstadt=0
        Südliche_Neustadt=0
        Südost=0
        Südostviertel=0
        Südviertel=0
        Südvorstadt_West=0
        Südwest=0
        Taunusstein=0
        Teltow=0
        Tiergarten_Tiergarten=0
        Toitenwinkel=0
        Tolkewitz_Seidnitz_Nord=0
        Trudering=0
        Uellendahl_Katernberg=0
        Unterbilk=0
        Unterhaching=0
        Untermeiderich=0
        Velbert=0
        Viernheim=0
        Vohwinkel=0
        Volkmarsdorf=0
        Waltrop=0
        Wanheimerort=0
        Wattenscheid_Mitte=0
        Wedding_Wedding=0
        Wedel=0
        Wehringhausen=0
        Weil_am_Rhein=0
        Weinheim=0
        Weitmar_Mitte=0
        Weißenfels=0
        Weißensee_Weißensee=0
        Weißwasser_Oberlausitz=0
        Werdau=0
        Werder_Havel=0
        Werdohl=0
        Wernigerode=0
        Westend_Nord=0
        Westend_Süd=0
        Westenviertel=0
        Westerberg=0
        Westliche_Neustadt=0
        Westliches_Ringgebiet=0
        Wetter_Ruhr=0
        Wiesloch=0
        Wildau=0
        Wilkau_Haßlau=0
        Wilmersdorf_Wilmersdorf=0
        Wilsdruffer_Vorstadt_Seevorstadt_West=0
        Winsen_Luhe=0
        Winterhude=0
        Witten=0
        Wolmirstedt=0
        Wurzen=0
        Wöhrd=0
        Zeitz=0
        Zentrum_Ost=0
        Zentrum_Südost=0
        Zentrum_West=0
        Zeulenroda_Triebes=0
        Zittau=0
        Äußere_Neustadt_Antonstadt=0
        Östliches_Ringgebiet=0
        Ückendorf=0
        
        cities=request.form["city"]
        if (cities=="Adalbertsteinweg"):
        	 Adalbertsteinweg=1
        elif (cities=="Adlershof Treptow"):
        	 Adlershof_Treptow=1
        elif (cities=="Ahrensburg"):
        	 Ahrensburg=1
        elif (cities=="Alfeld Leine"):
        	 Alfeld_Leine=1
        elif (cities=="Alt Hamborn"):
        	 Alt_Hamborn=1
        elif (cities=="Alt Hohenschönhausen Hohenschönhausen"):
        	 Alt_Hohenschönhausen_Hohenschönhausen=1
        elif (cities=="Altena"):
        	 Altena=1
        elif (cities=="Altenburg"):
        	 Altenburg=1
        elif (cities=="Altenessen Süd"):
        	 Altenessen_Süd=1
        elif (cities=="Altenhagen"):
        	 Altenhagen=1
        elif (cities=="Altlindenau"):
        	 Altlindenau=1
        elif (cities=="Altstadt & Neustadt Nord"):
        	 Altstadt_Neustadt_Nord=1
        elif (cities=="Altstadt & Neustadt Süd"):
        	 Altstadt_Neustadt_Süd=1
        elif (cities=="Altstadt / Innenstadt"):
        	 Altstadt_Innenstadt=1
        elif (cities=="Altstadt, St. Sebald"):
        	 Altstadt_St_Sebald=1
        elif (cities=="Andernach"):
        	 Andernach=1
        elif (cities=="Andreasvorstadt"):
        	 Andreasvorstadt=1
        elif (cities=="Annaberg Buchholz"):
        	 Annaberg_Buchholz=1
        elif (cities=="Aschersleben"):
        	 Aschersleben=1
        elif (cities=="Aubing"):
        	 Aubing=1
        elif (cities=="Aue"):
        	 Aue=1
        elif (cities=="Bad"):
        	 Bad=1
        elif (cities=="Bad Aibling"):
        	 Bad_Aibling=1
        elif (cities=="Bad Cannstatt"):
        	 Bad_Cannstatt=1
        elif (cities=="Bad Dürrenberg"):
        	 Bad_Dürrenberg=1
        elif (cities=="Bad Gandersheim"):
        	 Bad_Gandersheim=1
        elif (cities=="Bad Godesberg"):
        	 Bad_Godesberg=1
        elif (cities=="Bad Harzburg"):
        	 Bad_Harzburg=1
        elif (cities=="Bad Homburg vor der Höhe"):
        	 Bad_Homburg_vor_der_Höhe=1
        elif (cities=="Bad Kreuznach"):
        	 Bad_Kreuznach=1
        elif (cities=="Bad Langensalza"):
        	 Bad_Langensalza=1
        elif (cities=="Bad Münster am Stein Ebernburg"):
        	 Bad_Münster_am_Stein_Ebernburg=1
        elif (cities=="Bad Nauheim"):
        	 Bad_Nauheim=1
        elif (cities=="Bad Orb"):
        	 Bad_Orb=1
        elif (cities=="Bad Rappenau"):
        	 Bad_Rappenau=1
        elif (cities=="Bad Soden am Taunus"):
        	 Bad_Soden_am_Taunus=1
        elif (cities=="Bad Vilbel"):
        	 Bad_Vilbel=1
        elif (cities=="Bahnhofsviertel"):
        	 Bahnhofsviertel=1
        elif (cities=="Bahnhofsvorstadt"):
        	 Bahnhofsvorstadt=1
        elif (cities=="Bahnstadt"):
        	 Bahnstadt=1
        elif (cities=="Barmen"):
        	 Barmen=1
        elif (cities=="Barsinghausen"):
        	 Barsinghausen=1
        elif (cities=="Barth"):
        	 Barth=1
        elif (cities=="Bautzen"):
        	 Bautzen=1
        elif (cities=="Beckhausen"):
        	 Beckhausen=1
        elif (cities=="Beeck"):
        	 Beeck=1
        elif (cities=="Bendorf"):
        	 Bendorf=1
        elif (cities=="Bensheim"):
        	 Bensheim=1
        elif (cities=="Bergedorf"):
        	 Bergedorf=1
        elif (cities=="Bergen"):
        	 Bergen=1
        elif (cities=="Bernau am Chiemsee"):
        	 Bernau_am_Chiemsee=1
        elif (cities=="Bernau bei Berlin"):
        	 Bernau_bei_Berlin=1
        elif (cities=="Bessungen"):
        	 Bessungen=1
        elif (cities=="Beuel"):
        	 Beuel=1
        elif (cities=="Biebrich"):
        	 Biebrich=1
        elif (cities=="Biesdorf Marzahn"):
        	 Biesdorf_Marzahn=1
        elif (cities=="Bietigheim Bissingen"):
        	 Bietigheim_Bissingen=1
        elif (cities=="Bilk"):
        	 Bilk=1
        elif (cities=="Bingen am Rhein"):
        	 Bingen_am_Rhein=1
        elif (cities=="Bismarck"):
        	 Bismarck=1
        elif (cities=="Bitterfeld Wolfen"):
        	 Bitterfeld_Wolfen=1
        elif (cities=="Blasewitz"):
        	 Blasewitz=1
        elif (cities=="Bockenheim"):
        	 Bockenheim=1
        elif (cities=="Bockum"):
        	 Bockum=1
        elif (cities=="Bogenhausen"):
        	 Bogenhausen=1
        elif (cities=="Boizenburg/Elbe"):
        	 Boizenburg_Elbe=1
        elif (cities=="Borna"):
        	 Borna=1
        elif (cities=="Braunsbedra"):
        	 Braunsbedra=1
        elif (cities=="Bretten"):
        	 Bretten=1
        elif (cities=="Briesnitz"):
        	 Briesnitz=1
        elif (cities=="Bruchsal"):
        	 Bruchsal=1
        elif (cities=="Bruck"):
        	 Bruck=1
        elif (cities=="Buchholz in der Nordheide"):
        	 Buchholz_in_der_Nordheide=1
        elif (cities=="Buckau"):
        	 Buckau=1
        elif (cities=="Buer"):
        	 Buer=1
        elif (cities=="Bulmke Hüllen"):
        	 Bulmke_Hüllen=1
        elif (cities=="Buxtehude"):
        	 Buxtehude=1
        elif (cities=="Böblingen"):
        	 Böblingen=1
        elif (cities=="Böhlen"):
        	 Böhlen=1
        elif (cities=="Bühlau/Weißer Hirsch"):
        	 Bühlau_Weißer_Hirsch=1
        elif (cities=="Bürgerfelde"):
        	 Bürgerfelde=1
        elif (cities=="Calau"):
        	 Calau=1
        elif (cities=="Castrop Rauxel"):
        	 Castrop_Rauxel=1
        elif (cities=="Celle"):
        	 Celle=1
        elif (cities=="Charlottenburg Charlottenburg"):
        	 Charlottenburg_Charlottenburg=1
        elif (cities=="Chrieschwitz"):
        	 Chrieschwitz=1
        elif (cities=="Clausthal Zellerfeld"):
        	 Clausthal_Zellerfeld=1
        elif (cities=="Connewitz"):
        	 Connewitz=1
        elif (cities=="Coswig"):
        	 Coswig=1
        elif (cities=="Cotta"):
        	 Cotta=1
        elif (cities=="Cracau"):
        	 Cracau=1
        elif (cities=="Crimmitschau"):
        	 Crimmitschau=1
        elif (cities=="Damm"):
        	 Damm=1
        elif (cities=="Darmstadt Mitte"):
        	 Darmstadt_Mitte=1
        elif (cities=="Darmstadt Nord"):
        	 Darmstadt_Nord=1
        elif (cities=="Datteln"):
        	 Datteln=1
        elif (cities=="Datzeviertel"):
        	 Datzeviertel=1
        elif (cities=="Debschwitz"):
        	 Debschwitz=1
        elif (cities=="Delitzsch"):
        	 Delitzsch=1
        elif (cities=="Dellviertel"):
        	 Dellviertel=1
        elif (cities=="Derendorf"):
        	 Derendorf=1
        elif (cities=="Dieburg"):
        	 Dieburg=1
        elif (cities=="Dodesheide"):
        	 Dodesheide=1
        elif (cities=="Dorsten"):
        	 Dorsten=1
        elif (cities=="Dotzheim"):
        	 Dotzheim=1
        elif (cities=="Dreieich"):
        	 Dreieich=1
        elif (cities=="Drewitz"):
        	 Drewitz=1
        elif (cities=="Duissern"):
        	 Duissern=1
        elif (cities=="Durlach"):
        	 Durlach=1
        elif (cities=="Döbeln"):
        	 Döbeln=1
        elif (cities=="Düsseltal"):
        	 Düsseltal=1
        elif (cities=="Eberswalde"):
        	 Eberswalde=1
        elif (cities=="Eckernförde"):
        	 Eckernförde=1
        elif (cities=="Eilenburg"):
        	 Eilenburg=1
        elif (cities=="Einbeck"):
        	 Einbeck=1
        elif (cities=="Elberfeld"):
        	 Elberfeld=1
        elif (cities=="Elberfeld West"):
        	 Elberfeld_West=1
        elif (cities=="Elmshorn"):
        	 Elmshorn=1
        elif (cities=="Ennepetal"):
        	 Ennepetal=1
        elif (cities=="Erkrath"):
        	 Erkrath=1
        elif (cities=="Erle"):
        	 Erle=1
        elif (cities=="Eschborn"):
        	 Eschborn=1
        elif (cities=="Esslingen am Neckar"):
        	 Esslingen_am_Neckar=1
        elif (cities=="Ettlingen"):
        	 Ettlingen=1
        elif (cities=="Eversten"):
        	 Eversten=1
        elif (cities=="Fedderwardergroden"):
        	 Fedderwardergroden=1
        elif (cities=="Fermersleben"):
        	 Fermersleben=1
        elif (cities=="Filderstadt"):
        	 Filderstadt=1
        elif (cities=="Flingern Nord"):
        	 Flingern_Nord=1
        elif (cities=="Frankenberg"):
        	 Frankenberg=1
        elif (cities=="Frankenberg/Sachsen"):
        	 Frankenberg_Sachsen=1
        elif (cities=="Frauenland"):
        	 Frauenland=1
        elif (cities=="Freital"):
        	 Freital=1
        elif (cities=="Friedberg Hessen"):
        	 Friedberg_Hessen=1
        elif (cities=="Friedrichsdorf"):
        	 Friedrichsdorf=1
        elif (cities=="Friedrichsfelde Lichtenberg"):
        	 Friedrichsfelde_Lichtenberg=1
        elif (cities=="Friedrichshain Friedrichshain"):
        	 Friedrichshain_Friedrichshain=1
        elif (cities=="Friedrichstadt"):
        	 Friedrichstadt=1
        elif (cities=="Frohnhausen"):
        	 Frohnhausen=1
        elif (cities=="Gaarden Ost"):
        	 Gaarden_Ost=1
        elif (cities=="Galgenhof"):
        	 Galgenhof=1
        elif (cities=="Gallusviertel"):
        	 Gallusviertel=1
        elif (cities=="Garbsen"):
        	 Garbsen=1
        elif (cities=="Gartenfeld"):
        	 Gartenfeld=1
        elif (cities=="Gebiet Reichenbacher Str./Freiheitssiedlung"):
        	 Gebiet_Reichenbacher_Str_Freiheitssiedlung=1
        elif (cities=="Geestemünde"):
        	 Geestemünde=1
        elif (cities=="Geesthacht"):
        	 Geesthacht=1
        elif (cities=="Gelnhausen"):
        	 Gelnhausen=1
        elif (cities=="Gera Ost"):
        	 Gera_Ost=1
        elif (cities=="Gevelsberg"):
        	 Gevelsberg=1
        elif (cities=="Gießen"):
        	 Gießen=1
        elif (cities=="Gladbach"):
        	 Gladbach=1
        elif (cities=="Gladbeck"):
        	 Gladbeck=1
        elif (cities=="Glauchau"):
        	 Glauchau=1
        elif (cities=="Gleisdreieck"):
        	 Gleisdreieck=1
        elif (cities=="Glockenhof"):
        	 Glockenhof=1
        elif (cities=="Gohlis Mitte"):
        	 Gohlis_Mitte=1
        elif (cities=="Gohlis Nord"):
        	 Gohlis_Nord=1
        elif (cities=="Gohlis Süd"):
        	 Gohlis_Süd=1
        elif (cities=="Golzheim"):
        	 Golzheim=1
        elif (cities=="Gorbitz Süd"):
        	 Gorbitz_Süd=1
        elif (cities=="Goslar"):
        	 Goslar=1
        elif (cities=="Gotha"):
        	 Gotha=1
        elif (cities=="Greiz"):
        	 Greiz=1
        elif (cities=="Grevesmühlen"):
        	 Grevesmühlen=1
        elif (cities=="Grimma"):
        	 Grimma=1
        elif (cities=="Groß Buchholz"):
        	 Groß_Buchholz=1
        elif (cities=="Großenhain"):
        	 Großenhain=1
        elif (cities=="Gruna"):
        	 Gruna=1
        elif (cities=="Göttingen"):
        	 Göttingen=1
        elif (cities=="Haar"):
        	 Haar=1
        elif (cities=="Haidenhof Nord"):
        	 Haidenhof_Nord=1
        elif (cities=="Haidhausen"):
        	 Haidhausen=1
        elif (cities=="Hainichen"):
        	 Hainichen=1
        elif (cities=="Halberstadt"):
        	 Halberstadt=1
        elif (cities=="Hamme"):
        	 Hamme=1
        elif (cities=="Hanau"):
        	 Hanau=1
        elif (cities=="Handelshäfen"):
        	 Handelshäfen=1
        elif (cities=="Hangeweiher"):
        	 Hangeweiher=1
        elif (cities=="Harburg"):
        	 Harburg=1
        elif (cities=="Hartenberg/Münchfeld"):
        	 Hartenberg_Münchfeld=1
        elif (cities=="Haselbrunn"):
        	 Haselbrunn=1
        elif (cities=="Haspe"):
        	 Haspe=1
        elif (cities=="Hassel"):
        	 Hassel=1
        elif (cities=="Hattingen"):
        	 Hattingen=1
        elif (cities=="Heckinghausen"):
        	 Heckinghausen=1
        elif (cities=="Heilbronner Kernstadt"):
        	 Heilbronner_Kernstadt=1
        elif (cities=="Heiligenhaus"):
        	 Heiligenhaus=1
        elif (cities=="Hellersdorf Hellersdorf"):
        	 Hellersdorf_Hellersdorf=1
        elif (cities=="Helmstedt"):
        	 Helmstedt=1
        elif (cities=="Heppenheim Bergstraße"):
        	 Heppenheim_Bergstraße=1
        elif (cities=="Heppens"):
        	 Heppens=1
        elif (cities=="Herten"):
        	 Herten=1
        elif (cities=="Hettstedt"):
        	 Hettstedt=1
        elif (cities=="Hilden"):
        	 Hilden=1
        elif (cities=="Hildesheim"):
        	 Hildesheim=1
        elif (cities=="Hochemmerich"):
        	 Hochemmerich=1
        elif (cities=="Hochheide"):
        	 Hochheide=1
        elif (cities=="Hofheim am Taunus"):
        	 Hofheim_am_Taunus=1
        elif (cities=="Hohenlimburg"):
        	 Hohenlimburg=1
        elif (cities=="Hohenstein Ernstthal"):
        	 Hohenstein_Ernstthal=1
        elif (cities=="Hohenstücken"):
        	 Hohenstücken=1
        elif (cities=="Holsterhausen"):
        	 Holsterhausen=1
        elif (cities=="Homburg"):
        	 Homburg=1
        elif (cities=="Huckarde"):
        	 Huckarde=1
        elif (cities=="Hörde"):
        	 Hörde=1
        elif (cities=="Idstein"):
        	 Idstein=1
        elif (cities=="Ingelheim am Rhein"):
        	 Ingelheim_am_Rhein=1
        elif (cities=="Innenstadt / Jungbusch"):
        	 Innenstadt_Jungbusch=1
        elif (cities=="Innere Altstadt"):
        	 Innere_Altstadt=1
        elif (cities=="Innere Neustadt"):
        	 Innere_Neustadt=1
        elif (cities=="Innerstädtischer Bereich Mitte"):
        	 Innerstädtischer_Bereich_Mitte=1
        elif (cities=="Innerstädtischer Bereich Nord"):
        	 Innerstädtischer_Bereich_Nord=1
        elif (cities=="Innerstädtischer Bereich Süd"):
        	 Innerstädtischer_Bereich_Süd=1
        elif (cities=="Innstadt"):
        	 Innstadt=1
        elif (cities=="Iserlohn"):
        	 Iserlohn=1
        elif (cities=="Johannstadt Nord"):
        	 Johannstadt_Nord=1
        elif (cities=="Johannstadt Süd"):
        	 Johannstadt_Süd=1
        elif (cities=="Kaiserlei"):
        	 Kaiserlei=1
        elif (cities=="Kaltenkirchen"):
        	 Kaltenkirchen=1
        elif (cities=="Kamenz"):
        	 Kamenz=1
        elif (cities=="Katernberg"):
        	 Katernberg=1
        elif (cities=="Katzwang, Reichelsdorf Ost, Reichelsdorfer Keller"):
        	 Katzwang_Reichelsdorf_Ost_Reichelsdorfer_Keller=1
        elif (cities=="Kaßberg"):
        	 Kaßberg=1
        elif (cities=="Kelkheim Taunus"):
        	 Kelkheim_Taunus=1
        elif (cities=="Kirchditmold"):
        	 Kirchditmold=1
        elif (cities=="Kirchrode"):
        	 Kirchrode=1
        elif (cities=="Kitzscher"):
        	 Kitzscher=1
        elif (cities=="Kray"):
        	 Kray=1
        elif (cities=="Kreuzberg Kreuzberg"):
        	 Kreuzberg_Kreuzberg=1
        elif (cities=="Kruppwerke"):
        	 Kruppwerke=1
        elif (cities=="Krämpfervorstadt"):
        	 Krämpfervorstadt=1
        elif (cities=="Kröpeliner Tor Vorstadt"):
        	 Kröpeliner_Tor_Vorstadt=1
        elif (cities=="Käfertal"):
        	 Käfertal=1
        elif (cities=="Königstein im Taunus"):
        	 Königstein_im_Taunus=1
        elif (cities=="Köpenick Köpenick"):
        	 Köpenick_Köpenick=1
        elif (cities=="Köthen Anhalt"):
        	 Köthen_Anhalt=1
        elif (cities=="Langen Hessen"):
        	 Langen_Hessen=1
        elif (cities=="Langenfeld Rheinland"):
        	 Langenfeld_Rheinland=1
        elif (cities=="Langenhagen"):
        	 Langenhagen=1
        elif (cities=="Langenhorn"):
        	 Langenhorn=1
        elif (cities=="Langerfeld Beyenburg"):
        	 Langerfeld_Beyenburg=1
        elif (cities=="Lauchhammer"):
        	 Lauchhammer=1
        elif (cities=="Lausen Grünau"):
        	 Lausen_Grünau=1
        elif (cities=="Lebenstedt"):
        	 Lebenstedt=1
        elif (cities=="Lechhausen"):
        	 Lechhausen=1
        elif (cities=="Leipziger Str."):
        	 Leipziger_Str=1
        elif (cities=="Leipziger Vorstadt"):
        	 Leipziger_Vorstadt=1
        elif (cities=="Leonberg"):
        	 Leonberg=1
        elif (cities=="Leuben"):
        	 Leuben=1
        elif (cities=="Leubnitz Neuostra"):
        	 Leubnitz_Neuostra=1
        elif (cities=="Lichtenberg Lichtenberg"):
        	 Lichtenberg_Lichtenberg=1
        elif (cities=="Lichtenstein/Sachsen"):
        	 Lichtenstein_Sachsen=1
        elif (cities=="Lichterfelde Steglitz"):
        	 Lichterfelde_Steglitz=1
        elif (cities=="Limbach Oberfrohna"):
        	 Limbach_Oberfrohna=1
        elif (cities=="List"):
        	 List=1
        elif (cities=="Loschwitz/Wachwitz"):
        	 Loschwitz_Wachwitz=1
        elif (cities=="Ludwigsburg"):
        	 Ludwigsburg=1
        elif (cities=="Ludwigslust"):
        	 Ludwigslust=1
        elif (cities=="Ludwigsvorstadt Isarvorstadt"):
        	 Ludwigsvorstadt_Isarvorstadt=1
        elif (cities=="Lusan Brüte"):
        	 Lusan_Brüte=1
        elif (cities=="Lusan Laune"):
        	 Lusan_Laune=1
        elif (cities=="Lutherplatz/Thüringer Bahnhof"):
        	 Lutherplatz_Thüringer_Bahnhof=1
        elif (cities=="Lutherstadt Eisleben"):
        	 Lutherstadt_Eisleben=1
        elif (cities=="Lutherviertel"):
        	 Lutherviertel=1
        elif (cities=="Löbau"):
        	 Löbau=1
        elif (cities=="Löbtau Nord"):
        	 Löbtau_Nord=1
        elif (cities=="Löbtau Süd"):
        	 Löbtau_Süd=1
        elif (cities=="Lörrach"):
        	 Lörrach=1
        elif (cities=="Lüdenscheid"):
        	 Lüdenscheid=1
        elif (cities=="Lüneburg"):
        	 Lüneburg=1
        elif (cities=="Maintal"):
        	 Maintal=1
        elif (cities=="Marburg"):
        	 Marburg=1
        elif (cities=="Marienthal Ost"):
        	 Marienthal_Ost=1
        elif (cities=="Markkleeberg"):
        	 Markkleeberg=1
        elif (cities=="Markranstädt"):
        	 Markranstädt=1
        elif (cities=="Marl"):
        	 Marl=1
        elif (cities=="Marxloh"):
        	 Marxloh=1
        elif (cities=="Marzahn Marzahn"):
        	 Marzahn_Marzahn=1
        elif (cities=="Maximin"):
        	 Maximin=1
        elif (cities=="Maxvorstadt"):
        	 Maxvorstadt=1
        elif (cities=="Mayen"):
        	 Mayen=1
        elif (cities=="Meerane"):
        	 Meerane=1
        elif (cities=="Meißen"):
        	 Meißen=1
        elif (cities=="Merseburg"):
        	 Merseburg=1
        elif (cities=="Metternich"):
        	 Metternich=1
        elif (cities=="Mettmann"):
        	 Mettmann=1
        elif (cities=="Meuselwitz"):
        	 Meuselwitz=1
        elif (cities=="Mickten"):
        	 Mickten=1
        elif (cities=="Milbertshofen"):
        	 Milbertshofen=1
        elif (cities=="Mitte Mitte"):
        	 Mitte_Mitte=1
        elif (cities=="Mitte Nord"):
        	 Mitte_Nord=1
        elif (cities=="Mitte West"):
        	 Mitte_West=1
        elif (cities=="Mittelmeiderich"):
        	 Mittelmeiderich=1
        elif (cities=="Mittelstadt"):
        	 Mittelstadt=1
        elif (cities=="Mittweida"):
        	 Mittweida=1
        elif (cities=="Montabaur"):
        	 Montabaur=1
        elif (cities=="Mueßer Holz"):
        	 Mueßer_Holz=1
        elif (cities=="Möckern"):
        	 Möckern=1
        elif (cities=="Mörfelden Walldorf"):
        	 Mörfelden_Walldorf=1
        elif (cities=="Mühlhausen/Thüringen"):
        	 Mühlhausen_Thüringen=1
        elif (cities=="Mülheim"):
        	 Mülheim=1
        elif (cities=="Mürwik"):
        	 Mürwik=1
        elif (cities=="Naumburg Saale"):
        	 Naumburg_Saale=1
        elif (cities=="Naußlitz"):
        	 Naußlitz=1
        elif (cities=="Neckarstadt Ost / Wohlgelegen"):
        	 Neckarstadt_Ost_Wohlgelegen=1
        elif (cities=="Neckarstadt West"):
        	 Neckarstadt_West=1
        elif (cities=="Neckarsulm"):
        	 Neckarsulm=1
        elif (cities=="Nette"):
        	 Nette=1
        elif (cities=="Neu Isenburg"):
        	 Neu_Isenburg=1
        elif (cities=="Neu Olvenstedt"):
        	 Neu_Olvenstedt=1
        elif (cities=="Neue Neustadt"):
        	 Neue_Neustadt=1
        elif (cities=="Neuenheim"):
        	 Neuenheim=1
        elif (cities=="Neuhausen"):
        	 Neuhausen=1
        elif (cities=="Neukölln Neukölln"):
        	 Neukölln_Neukölln=1
        elif (cities=="Neumühl"):
        	 Neumühl=1
        elif (cities=="Neundorfer Vorstadt"):
        	 Neundorfer_Vorstadt=1
        elif (cities=="Neunkirchen"):
        	 Neunkirchen=1
        elif (cities=="Neuplanitz"):
        	 Neuplanitz=1
        elif (cities=="Neustrelitz"):
        	 Neustrelitz=1
        elif (cities=="Niederrad"):
        	 Niederrad=1
        elif (cities=="Nord Holland"):
        	 Nord_Holland=1
        elif (cities=="Nordend Ost"):
        	 Nordend_Ost=1
        elif (cities=="Nordend West"):
        	 Nordend_West=1
        elif (cities=="Norderstedt"):
        	 Norderstedt=1
        elif (cities=="Nordhausen"):
        	 Nordhausen=1
        elif (cities=="Nordost"):
        	 Nordost=1
        elif (cities=="Nordvorstadt"):
        	 Nordvorstadt=1
        elif (cities=="Northeim"):
        	 Northeim=1
        elif (cities=="Nördliche Innenstadt"):
        	 Nördliche_Innenstadt=1
        elif (cities=="Nördliche Neustadt"):
        	 Nördliche_Neustadt=1
        elif (cities=="Oberbarmen"):
        	 Oberbarmen=1
        elif (cities=="Oberbilk"):
        	 Oberbilk=1
        elif (cities=="Obergiesing"):
        	 Obergiesing=1
        elif (cities=="Obermarxloh"):
        	 Obermarxloh=1
        elif (cities=="Obermeiderich"):
        	 Obermeiderich=1
        elif (cities=="Obermenzing"):
        	 Obermenzing=1
        elif (cities=="Oberschöneweide Köpenick"):
        	 Oberschöneweide_Köpenick=1
        elif (cities=="Obersendling"):
        	 Obersendling=1
        elif (cities=="Oberstadt"):
        	 Oberstadt=1
        elif (cities=="Oberursel Taunus"):
        	 Oberursel_Taunus=1
        elif (cities=="Oschatz"):
        	 Oschatz=1
        elif (cities=="Oschersleben Bode"):
        	 Oschersleben_Bode=1
        elif (cities=="Ost"):
        	 Ost=1
        elif (cities=="Ostend"):
        	 Ostend=1
        elif (cities=="Ottobrunn"):
        	 Ottobrunn=1
        elif (cities=="Pankow Pankow"):
        	 Pankow_Pankow=1
        elif (cities=="Pasing"):
        	 Pasing=1
        elif (cities=="Paulsstadt"):
        	 Paulsstadt=1
        elif (cities=="Pempelfort"):
        	 Pempelfort=1
        elif (cities=="Perlach"):
        	 Perlach=1
        elif (cities=="Pieschen Nord/Trachenberge"):
        	 Pieschen_Nord_Trachenberge=1
        elif (cities=="Pieschen Süd"):
        	 Pieschen_Süd=1
        elif (cities=="Pinneberg"):
        	 Pinneberg=1
        elif (cities=="Pirna"):
        	 Pirna=1
        elif (cities=="Plagwitz"):
        	 Plagwitz=1
        elif (cities=="Ponttor"):
        	 Ponttor=1
        elif (cities=="Poppelsdorf"):
        	 Poppelsdorf=1
        elif (cities=="Prenzlau"):
        	 Prenzlau=1
        elif (cities=="Prenzlauer Berg Prenzlauer Berg"):
        	 Prenzlauer_Berg_Prenzlauer_Berg=1
        elif (cities=="Prohlis Süd"):
        	 Prohlis_Süd=1
        elif (cities=="Pölbitz"):
        	 Pölbitz=1
        elif (cities=="Quedlinburg"):
        	 Quedlinburg=1
        elif (cities=="Radeberg"):
        	 Radeberg=1
        elif (cities=="Radeberger Vorstadt"):
        	 Radeberger_Vorstadt=1
        elif (cities=="Radebeul"):
        	 Radebeul=1
        elif (cities=="Rahlstedt"):
        	 Rahlstedt=1
        elif (cities=="Ratingen"):
        	 Ratingen=1
        elif (cities=="Recklinghausen"):
        	 Recklinghausen=1
        elif (cities=="Reick"):
        	 Reick=1
        elif (cities=="Reinickendorf Reinickendorf"):
        	 Reinickendorf_Reinickendorf=1
        elif (cities=="Reißiger Vorstadt"):
        	 Reißiger_Vorstadt=1
        elif (cities=="Rendsburg"):
        	 Rendsburg=1
        elif (cities=="Reudnitz Thonberg"):
        	 Reudnitz_Thonberg=1
        elif (cities=="Reusa mit Sorga"):
        	 Reusa_mit_Sorga=1
        elif (cities=="Rheingauviertel, Hollerborn"):
        	 Rheingauviertel_Hollerborn=1
        elif (cities=="Rheinhausen Mitte"):
        	 Rheinhausen_Mitte=1
        elif (cities=="Rheydt"):
        	 Rheydt=1
        elif (cities=="Ribnitz Damgarten"):
        	 Ribnitz_Damgarten=1
        elif (cities=="Riedberg"):
        	 Riedberg=1
        elif (cities=="Riesa"):
        	 Riesa=1
        elif (cities=="Rodgau"):
        	 Rodgau=1
        elif (cities=="Ronsdorf"):
        	 Ronsdorf=1
        elif (cities=="Rotthausen"):
        	 Rotthausen=1
        elif (cities=="Roßlau"):
        	 Roßlau=1
        elif (cities=="Rödelheim"):
        	 Rödelheim=1
        elif (cities=="Rüsselsheim am Main"):
        	 Rüsselsheim_am_Main=1
        elif (cities=="Rüttenscheid"):
        	 Rüttenscheid=1
        elif (cities=="Saarbrücken"):
        	 Saarbrücken=1
        elif (cities=="Saarlouis"):
        	 Saarlouis=1
        elif (cities=="Sachsendorf"):
        	 Sachsendorf=1
        elif (cities=="Sachsenhausen Nord"):
        	 Sachsenhausen_Nord=1
        elif (cities=="Sachsenhausen Süd"):
        	 Sachsenhausen_Süd=1
        elif (cities=="Sandow"):
        	 Sandow=1
        elif (cities=="Sangerhausen"):
        	 Sangerhausen=1
        elif (cities=="Schalke"):
        	 Schalke=1
        elif (cities=="Schkeuditz"):
        	 Schkeuditz=1
        elif (cities=="Schleswig"):
        	 Schleswig=1
        elif (cities=="Schloßchemnitz"):
        	 Schloßchemnitz=1
        elif (cities=="Schmellwitz"):
        	 Schmellwitz=1
        elif (cities=="Schoppershof"):
        	 Schoppershof=1
        elif (cities=="Schreventeich"):
        	 Schreventeich=1
        elif (cities=="Schwabing"):
        	 Schwabing=1
        elif (cities=="Schwabing West"):
        	 Schwabing_West=1
        elif (cities=="Schwarzenbek"):
        	 Schwarzenbek=1
        elif (cities=="Schwelm"):
        	 Schwelm=1
        elif (cities=="Schwetzingen"):
        	 Schwetzingen=1
        elif (cities=="Schwetzingerstadt / Oststadt"):
        	 Schwetzingerstadt_Oststadt=1
        elif (cities=="Schönebeck Elbe"):
        	 Schönebeck_Elbe=1
        elif (cities=="Schöneberg Schöneberg"):
        	 Schöneberg_Schöneberg=1
        elif (cities=="Schönefeld"):
        	 Schönefeld=1
        elif (cities=="Schönefeld Abtnaundorf"):
        	 Schönefeld_Abtnaundorf=1
        elif (cities=="Schöningen"):
        	 Schöningen=1
        elif (cities=="Schönwalde II"):
        	 Schönwalde_II=1
        elif (cities=="Sebnitz"):
        	 Sebnitz=1
        elif (cities=="Seesen"):
        	 Seesen=1
        elif (cities=="Seevetal"):
        	 Seevetal=1
        elif (cities=="Seevorstadt Ost"):
        	 Seevorstadt_Ost=1
        elif (cities=="Senftenberg"):
        	 Senftenberg=1
        elif (cities=="Siedlung Neundorf"):
        	 Siedlung_Neundorf=1
        elif (cities=="Silberhöhe"):
        	 Silberhöhe=1
        elif (cities=="Sindelfingen"):
        	 Sindelfingen=1
        elif (cities=="Sinsheim"):
        	 Sinsheim=1
        elif (cities=="Solln"):
        	 Solln=1
        elif (cities=="Spandau Spandau"):
        	 Spandau_Spandau=1
        elif (cities=="Spremberger Vorstadt"):
        	 Spremberger_Vorstadt=1
        elif (cities=="Staaken Spandau"):
        	 Staaken_Spandau=1
        elif (cities=="Stade"):
        	 Stade=1
        elif (cities=="Stadtfeld Ost"):
        	 Stadtfeld_Ost=1
        elif (cities=="Stadtfeld West"):
        	 Stadtfeld_West=1
        elif (cities=="Stadtgebiet Ost"):
        	 Stadtgebiet_Ost=1
        elif (cities=="Stadtgebiet Süd"):
        	 Stadtgebiet_Süd=1
        elif (cities=="Stadtmitte"):
        	 Stadtmitte=1
        elif (cities=="Steglitz Steglitz"):
        	 Steglitz_Steglitz=1
        elif (cities=="Stendal"):
        	 Stendal=1
        elif (cities=="Stephanskirchen"):
        	 Stephanskirchen=1
        elif (cities=="Strehlen"):
        	 Strehlen=1
        elif (cities=="Striesen Ost"):
        	 Striesen_Ost=1
        elif (cities=="Striesen Süd"):
        	 Striesen_Süd=1
        elif (cities=="Striesen West"):
        	 Striesen_West=1
        elif (cities=="Stötteritz"):
        	 Stötteritz=1
        elif (cities=="Sudenburg"):
        	 Sudenburg=1
        elif (cities=="Südfriedhof"):
        	 Südfriedhof=1
        elif (cities=="Südinnenstadt"):
        	 Südinnenstadt=1
        elif (cities=="Südliche Neustadt"):
        	 Südliche_Neustadt=1
        elif (cities=="Südost"):
        	 Südost=1
        elif (cities=="Südostviertel"):
        	 Südostviertel=1
        elif (cities=="Südviertel"):
        	 Südviertel=1
        elif (cities=="Südvorstadt West"):
        	 Südvorstadt_West=1
        elif (cities=="Südwest"):
        	 Südwest=1
        elif (cities=="Taunusstein"):
        	 Taunusstein=1
        elif (cities=="Teltow"):
        	 Teltow=1
        elif (cities=="Tiergarten Tiergarten"):
        	 Tiergarten_Tiergarten=1
        elif (cities=="Toitenwinkel"):
        	 Toitenwinkel=1
        elif (cities=="Tolkewitz/Seidnitz Nord"):
        	 Tolkewitz_Seidnitz_Nord=1
        elif (cities=="Trudering"):
        	 Trudering=1
        elif (cities=="Uellendahl Katernberg"):
        	 Uellendahl_Katernberg=1
        elif (cities=="Unterbilk"):
        	 Unterbilk=1
        elif (cities=="Unterhaching"):
        	 Unterhaching=1
        elif (cities=="Untermeiderich"):
        	 Untermeiderich=1
        elif (cities=="Velbert"):
        	 Velbert=1
        elif (cities=="Viernheim"):
        	 Viernheim=1
        elif (cities=="Vohwinkel"):
        	 Vohwinkel=1
        elif (cities=="Volkmarsdorf"):
        	 Volkmarsdorf=1
        elif (cities=="Waltrop"):
        	 Waltrop=1
        elif (cities=="Wanheimerort"):
        	 Wanheimerort=1
        elif (cities=="Wattenscheid Mitte"):
        	 Wattenscheid_Mitte=1
        elif (cities=="Wedding Wedding"):
        	 Wedding_Wedding=1
        elif (cities=="Wedel"):
        	 Wedel=1
        elif (cities=="Wehringhausen"):
        	 Wehringhausen=1
        elif (cities=="Weil am Rhein"):
        	 Weil_am_Rhein=1
        elif (cities=="Weinheim"):
        	 Weinheim=1
        elif (cities=="Weitmar Mitte"):
        	 Weitmar_Mitte=1
        elif (cities=="Weißenfels"):
        	 Weißenfels=1
        elif (cities=="Weißensee Weißensee"):
        	 Weißensee_Weißensee=1
        elif (cities=="Weißwasser/Oberlausitz"):
        	 Weißwasser_Oberlausitz=1
        elif (cities=="Werdau"):
        	 Werdau=1
        elif (cities=="Werder Havel"):
        	 Werder_Havel=1
        elif (cities=="Werdohl"):
        	 Werdohl=1
        elif (cities=="Wernigerode"):
        	 Wernigerode=1
        elif (cities=="Westend Nord"):
        	 Westend_Nord=1
        elif (cities=="Westend Süd"):
        	 Westend_Süd=1
        elif (cities=="Westenviertel"):
        	 Westenviertel=1
        elif (cities=="Westerberg"):
        	 Westerberg=1
        elif (cities=="Westliche Neustadt"):
        	 Westliche_Neustadt=1
        elif (cities=="Westliches Ringgebiet"):
        	 Westliches_Ringgebiet=1
        elif (cities=="Wetter Ruhr"):
        	 Wetter_Ruhr=1
        elif (cities=="Wiesloch"):
        	 Wiesloch=1
        elif (cities=="Wildau"):
        	 Wildau=1
        elif (cities=="Wilkau Haßlau"):
        	 Wilkau_Haßlau=1
        elif (cities=="Wilmersdorf Wilmersdorf"):
        	 Wilmersdorf_Wilmersdorf=1
        elif (cities=="Wilsdruffer Vorstadt/Seevorstadt West"):
        	 Wilsdruffer_Vorstadt_Seevorstadt_West=1
        elif (cities=="Winsen Luhe"):
        	 Winsen_Luhe=1
        elif (cities=="Winterhude"):
        	 Winterhude=1
        elif (cities=="Witten"):
        	 Witten=1
        elif (cities=="Wolmirstedt"):
        	 Wolmirstedt=1
        elif (cities=="Wurzen"):
        	 Wurzen=1
        elif (cities=="Wöhrd"):
        	 Wöhrd=1
        elif (cities=="Zeitz"):
        	 Zeitz=1
        elif (cities=="Zentrum Ost"):
        	 Zentrum_Ost=1
        elif (cities=="Zentrum Südost"):
        	 Zentrum_Südost=1
        elif (cities=="Zentrum West"):
        	 Zentrum_West=1
        elif (cities=="Zeulenroda Triebes"):
        	 Zeulenroda_Triebes=1
        elif (cities=="Zittau"):
        	 Zittau=1
        elif (cities=="Äußere Neustadt Antonstadt"):
        	 Äußere_Neustadt_Antonstadt=1
        elif (cities=="Östliches Ringgebiet"):
        	 Östliches_Ringgebiet=1
        else:
        	   Ückendorf=1
       
        #Balcony
        bal=0
        balcony=request.form["Balcony"]
        if(balcony=="Yes"):
            bal=1
        else:
            bal=0
            
            
    
        
        prediction=model.predict([[
                federal,
                bal,
                living,
                rooms,
                region,
                Adalbertsteinweg,
                Adlershof_Treptow,
                Ahrensburg,
                Alfeld_Leine,
                Alt_Hamborn,
                Alt_Hohenschönhausen_Hohenschönhausen,
                Altena,
                Altenburg,
                Altenessen_Süd,
                Altenhagen,
                Altlindenau,
                Altstadt_Neustadt_Nord,
                Altstadt_Neustadt_Süd,
                Altstadt_Innenstadt,
                Altstadt_St_Sebald,
                Andernach,
                Andreasvorstadt,
                Annaberg_Buchholz,
                Aschersleben,
                Aubing,
                Aue,
                Bad,
                Bad_Aibling,
                Bad_Cannstatt,
                Bad_Dürrenberg,
                Bad_Gandersheim,
                Bad_Godesberg,
                Bad_Harzburg,
                Bad_Homburg_vor_der_Höhe,
                Bad_Kreuznach,
                Bad_Langensalza,
                Bad_Münster_am_Stein_Ebernburg,
                Bad_Nauheim,
                Bad_Orb,
                Bad_Rappenau,
                Bad_Soden_am_Taunus,
                Bad_Vilbel,
                Bahnhofsviertel,
                Bahnhofsvorstadt,
                Bahnstadt,
                Barmen,
                Barsinghausen,
                Barth,
                Bautzen,
                Beckhausen,
                Beeck,
                Bendorf,
                Bensheim,
                Bergedorf,
                Bergen,
                Bernau_am_Chiemsee,
                Bernau_bei_Berlin,
                Bessungen,
                Beuel,
                Biebrich,
                Biesdorf_Marzahn,
                Bietigheim_Bissingen,
                Bilk,
                Bingen_am_Rhein,
                Bismarck,
                Bitterfeld_Wolfen,
                Blasewitz,
                Bockenheim,
                Bockum,
                Bogenhausen,
                Boizenburg_Elbe,
                Borna,
                Braunsbedra,
                Bretten,
                Briesnitz,
                Bruchsal,
                Bruck,
                Buchholz_in_der_Nordheide,
                Buckau,
                Buer,
                Bulmke_Hüllen,
                Buxtehude,
                Böblingen,
                Böhlen,
                Bühlau_Weißer_Hirsch,
                Bürgerfelde,
                Calau,
                Castrop_Rauxel,
                Celle,
                Charlottenburg_Charlottenburg,
                Chrieschwitz,
                Clausthal_Zellerfeld,
                Connewitz,
                Coswig,
                Cotta,
                Cracau,
                Crimmitschau,
                Damm,
                Darmstadt_Mitte,
                Darmstadt_Nord,
                Datteln,
                Datzeviertel,
                Debschwitz,
                Delitzsch,
                Dellviertel,
                Derendorf,
                Dieburg,
                Dodesheide,
                Dorsten,
                Dotzheim,
                Dreieich,
                Drewitz,
                Duissern,
                Durlach,
                Döbeln,
                Düsseltal,
                Eberswalde,
                Eckernförde,
                Eilenburg,
                Einbeck,
                Elberfeld,
                Elberfeld_West,
                Elmshorn,
                Ennepetal,
                Erkrath,
                Erle,
                Eschborn,
                Esslingen_am_Neckar,
                Ettlingen,
                Eversten,
                Fedderwardergroden,
                Fermersleben,
                Filderstadt,
                Flingern_Nord,
                Frankenberg,
                Frankenberg_Sachsen,
                Frauenland,
                Freital,
                Friedberg_Hessen,
                Friedrichsdorf,
                Friedrichsfelde_Lichtenberg,
                Friedrichshain_Friedrichshain,
                Friedrichstadt,
                Frohnhausen,
                Gaarden_Ost,
                Galgenhof,
                Gallusviertel,
                Garbsen,
                Gartenfeld,
                Gebiet_Reichenbacher_Str_Freiheitssiedlung,
                Geestemünde,
                Geesthacht,
                Gelnhausen,
                Gera_Ost,
                Gevelsberg,
                Gießen,
                Gladbach,
                Gladbeck,
                Glauchau,
                Gleisdreieck,
                Glockenhof,
                Gohlis_Mitte,
                Gohlis_Nord,
                Gohlis_Süd,
                Golzheim,
                Gorbitz_Süd,
                Goslar,
                Gotha,
                Greiz,
                Grevesmühlen,
                Grimma,
                Groß_Buchholz,
                Großenhain,
                Gruna,
                Göttingen,
                Haar,
                Haidenhof_Nord,
                Haidhausen,
                Hainichen,
                Halberstadt,
                Hamme,
                Hanau,
                Handelshäfen,
                Hangeweiher,
                Harburg,
                Hartenberg_Münchfeld,
                Haselbrunn,
                Haspe,
                Hassel,
                Hattingen,
                Heckinghausen,
                Heilbronner_Kernstadt,
                Heiligenhaus,
                Hellersdorf_Hellersdorf,
                Helmstedt,
                Heppenheim_Bergstraße,
                Heppens,
                Herten,
                Hettstedt,
                Hilden,
                Hildesheim,
                Hochemmerich,
                Hochheide,
                Hofheim_am_Taunus,
                Hohenlimburg,
                Hohenstein_Ernstthal,
                Hohenstücken,
                Holsterhausen,
                Homburg,
                Huckarde,
                Hörde,
                Idstein,
                Ingelheim_am_Rhein,
                Innenstadt_Jungbusch,
                Innere_Altstadt,
                Innere_Neustadt,
                Innerstädtischer_Bereich_Mitte,
                Innerstädtischer_Bereich_Nord,
                Innerstädtischer_Bereich_Süd,
                Innstadt,
                Iserlohn,
                Johannstadt_Nord,
                Johannstadt_Süd,
                Kaiserlei,
                Kaltenkirchen,
                Kamenz,
                Katernberg,
                Katzwang_Reichelsdorf_Ost_Reichelsdorfer_Keller,
                Kaßberg,
                Kelkheim_Taunus,
                Kirchditmold,
                Kirchrode,
                Kitzscher,
                Kray,
                Kreuzberg_Kreuzberg,
                Kruppwerke,
                Krämpfervorstadt,
                Kröpeliner_Tor_Vorstadt,
                Käfertal,
                Königstein_im_Taunus,
                Köpenick_Köpenick,
                Köthen_Anhalt,
                Langen_Hessen,
                Langenfeld_Rheinland,
                Langenhagen,
                Langenhorn,
                Langerfeld_Beyenburg,
                Lauchhammer,
                Lausen_Grünau,
                Lebenstedt,
                Lechhausen,
                Leipziger_Str,
                Leipziger_Vorstadt,
                Leonberg,
                Leuben,
                Leubnitz_Neuostra,
                Lichtenberg_Lichtenberg,
                Lichtenstein_Sachsen,
                Lichterfelde_Steglitz,
                Limbach_Oberfrohna,
                List,
                Loschwitz_Wachwitz,
                Ludwigsburg,
                Ludwigslust,
                Ludwigsvorstadt_Isarvorstadt,
                Lusan_Brüte,
                Lusan_Laune,
                Lutherplatz_Thüringer_Bahnhof,
                Lutherstadt_Eisleben,
                Lutherviertel,
                Löbau,
                Löbtau_Nord,
                Löbtau_Süd,
                Lörrach,
                Lüdenscheid,
                Lüneburg,
                Maintal,
                Marburg,
                Marienthal_Ost,
                Markkleeberg,
                Markranstädt,
                Marl,
                Marxloh,
                Marzahn_Marzahn,
                Maximin,
                Maxvorstadt,
                Mayen,
                Meerane,
                Meißen,
                Merseburg,
                Metternich,
                Mettmann,
                Meuselwitz,
                Mickten,
                Milbertshofen,
                Mitte_Mitte,
                Mitte_Nord,
                Mitte_West,
                Mittelmeiderich,
                Mittelstadt,
                Mittweida,
                Montabaur,
                Mueßer_Holz,
                Möckern,
                Mörfelden_Walldorf,
                Mühlhausen_Thüringen,
                Mülheim,
                Mürwik,
                Naumburg_Saale,
                Naußlitz,
                Neckarstadt_Ost_Wohlgelegen,
                Neckarstadt_West,
                Neckarsulm,
                Nette,
                Neu_Isenburg,
                Neu_Olvenstedt,
                Neue_Neustadt,
                Neuenheim,
                Neuhausen,
                Neukölln_Neukölln,
                Neumühl,
                Neundorfer_Vorstadt,
                Neunkirchen,
                Neuplanitz,
                Neustrelitz,
                Niederrad,
                Nord_Holland,
                Nordend_Ost,
                Nordend_West,
                Norderstedt,
                Nordhausen,
                Nordost,
                Nordvorstadt,
                Northeim,
                Nördliche_Innenstadt,
                Nördliche_Neustadt,
                Oberbarmen,
                Oberbilk,
                Obergiesing,
                Obermarxloh,
                Obermeiderich,
                Obermenzing,
                Oberschöneweide_Köpenick,
                Obersendling,
                Oberstadt,
                Oberursel_Taunus,
                Oschatz,
                Oschersleben_Bode,
                Ost,
                Ostend,
                Ottobrunn,
                Pankow_Pankow,
                Pasing,
                Paulsstadt,
                Pempelfort,
                Perlach,
                Pieschen_Nord_Trachenberge,
                Pieschen_Süd,
                Pinneberg,
                Pirna,
                Plagwitz,
                Ponttor,
                Poppelsdorf,
                Prenzlau,
                Prenzlauer_Berg_Prenzlauer_Berg,
                Prohlis_Süd,
                Pölbitz,
                Quedlinburg,
                Radeberg,
                Radeberger_Vorstadt,
                Radebeul,
                Rahlstedt,
                Ratingen,
                Recklinghausen,
                Reick,
                Reinickendorf_Reinickendorf,
                Reißiger_Vorstadt,
                Rendsburg,
                Reudnitz_Thonberg,
                Reusa_mit_Sorga,
                Rheingauviertel_Hollerborn,
                Rheinhausen_Mitte,
                Rheydt,
                Ribnitz_Damgarten,
                Riedberg,
                Riesa,
                Rodgau,
                Ronsdorf,
                Rotthausen,
                Roßlau,
                Rödelheim,
                Rüsselsheim_am_Main,
                Rüttenscheid,
                Saarbrücken,
                Saarlouis,
                Sachsendorf,
                Sachsenhausen_Nord,
                Sachsenhausen_Süd,
                Sandow,
                Sangerhausen,
                Schalke,
                Schkeuditz,
                Schleswig,
                Schloßchemnitz,
                Schmellwitz,
                Schoppershof,
                Schreventeich,
                Schwabing,
                Schwabing_West,
                Schwarzenbek,
                Schwelm,
                Schwetzingen,
                Schwetzingerstadt_Oststadt,
                Schönebeck_Elbe,
                Schöneberg_Schöneberg,
                Schönefeld,
                Schönefeld_Abtnaundorf,
                Schöningen,
                Schönwalde_II,
                Sebnitz,
                Seesen,
                Seevetal,
                Seevorstadt_Ost,
                Senftenberg,
                Siedlung_Neundorf,
                Silberhöhe,
                Sindelfingen,
                Sinsheim,
                Solln,
                Spandau_Spandau,
                Spremberger_Vorstadt,
                Staaken_Spandau,
                Stade,
                Stadtfeld_Ost,
                Stadtfeld_West,
                Stadtgebiet_Ost,
                Stadtgebiet_Süd,
                Stadtmitte,
                Steglitz_Steglitz,
                Stendal,
                Stephanskirchen,
                Strehlen,
                Striesen_Ost,
                Striesen_Süd,
                Striesen_West,
                Stötteritz,
                Sudenburg,
                Südfriedhof,
                Südinnenstadt,
                Südliche_Neustadt,
                Südost,
                Südostviertel,
                Südviertel,
                Südvorstadt_West,
                Südwest,
                Taunusstein,
                Teltow,
                Tiergarten_Tiergarten,
                Toitenwinkel,
                Tolkewitz_Seidnitz_Nord,
                Trudering,
                Uellendahl_Katernberg,
                Unterbilk,
                Unterhaching,
                Untermeiderich,
                Velbert,
                Viernheim,
                Vohwinkel,
                Volkmarsdorf,
                Waltrop,
                Wanheimerort,
                Wattenscheid_Mitte,
                Wedding_Wedding,
                Wedel,
                Wehringhausen,
                Weil_am_Rhein,
                Weinheim,
                Weitmar_Mitte,
                Weißenfels,
                Weißensee_Weißensee,
                Weißwasser_Oberlausitz,
                Werdau,
                Werder_Havel,
                Werdohl,
                Wernigerode,
                Westend_Nord,
                Westend_Süd,
                Westenviertel,
                Westerberg,
                Westliche_Neustadt,
                Westliches_Ringgebiet,
                Wetter_Ruhr,
                Wiesloch,
                Wildau,
                Wilkau_Haßlau,
                Wilmersdorf_Wilmersdorf,
                Wilsdruffer_Vorstadt_Seevorstadt_West,
                Winsen_Luhe,
                Winterhude,
                Witten,
                Wolmirstedt,
                Wurzen,
                Wöhrd,
                Zeitz,
                Zentrum_Ost,
                Zentrum_Südost,
                Zentrum_West,
                Zeulenroda_Triebes,
                Zittau,
                Äußere_Neustadt_Antonstadt,
                Östliches_Ringgebiet,
                Ückendorf

            
        ]])

        output=np.exp(round(prediction[0],2))
        out=round(output,0)
        

        return render_template('Prototype3.html',prediction_text="Your Apartment Rental Price is €{}".format(out))


    return render_template("Prototype3.html")




if __name__ == "__main__":
    app.run(debug=True)