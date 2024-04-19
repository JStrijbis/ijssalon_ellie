from algemene_functies import mijn_functie_2
#5
def aanbieding_1(smaak,prijs,korting):
    aanbieding = prijs * korting
    return(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak} van {prijs} euro voor {aanbieding} euro")
    
#6+7
def inkomsten_totaal(inkomsten,btw):
    totaal = 0
    for i in inkomsten: 
        totaal += i
    btwteruggave = totaal * btw
    return(f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btwteruggave} euro btw betaald dient te worden.")

#8
def laag_en_hoog(mijn_lijst):
    Min = min(mijn_lijst)
    Max = max(mijn_lijst)
    return [Max,Min]

#9
def gemiddelde(mijn_lijst):
    aantal = len(mijn_lijst)
    totaal = 0
    for a in mijn_lijst:
        totaal +=a
    gemiddelde = totaal / aantal
    return(f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro.")

#10
def meervoudig(invoer_lijst):
    uitkomst = (laag_en_hoog (invoer_lijst)[1], laag_en_hoog(invoer_lijst)[0])
    return uitkomst

#12
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    print(korte_lijst)
    return uitvoer