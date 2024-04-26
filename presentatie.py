def presenteer(Dict,totaal):
    opgeteld = (sum(Dict.values()))
    print()
    for key,value in Dict.items():
        print(key, ':' , value)
    print('==========================')
    print(f"totaal : {totaal}")