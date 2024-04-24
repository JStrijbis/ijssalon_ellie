def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print (lengte * "*")
    print (f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag,personen):
    bedrag_pp = bedrag/personen
    return f'De fooi per persoon bedraagt {bedrag_pp}'

def onderstreep(tekst=""):
    uit = []
    regel ="=-" * len(tekst)
    uit.append(tekst)
    uit.append (regel)
    return uit

def som(dictonary):
    totaal = (sum(dictonary.values()))
    return totaal



    