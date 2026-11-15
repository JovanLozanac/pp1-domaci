def obradaLinije (unos):
    if ('sorted' in unos or 'reversed' in unos): return unos
    elif ('sort' in unos):
        return ('sorted(' + unos.split('.')[0] + ')')
    elif ('reverse' in unos):
        return ('reversed(' + unos.split('.')[0] + ')')
    else: return unos

while (True):
    unos = input()
    if(';' in unos): break
    if(unos == ""): break
    print (obradaLinije(unos))