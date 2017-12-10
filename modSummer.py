from core import modDatabase

def sumer(usrdir,dicto):
    print('modSummer.sumer: '+usrdir)
    libra = modDatabase.opendb(usrdir)
    karat = modDatabase.openKaratio(usrdir)
    libra = modDatabase.opendb(usrdir)
    rawdb = libra.get('raw',{})
    keydb = libra.get('key',{})

    dtempo = dicto.get('dtempo','')
    utempo = dicto.get('utempo','')
    takas = dicto.get('takas','')
    kekas = dicto.get('kekas','')

    keywo = dicto.get(kekas,'')
    tiset = modDatabase.timra(usrdir, dtempo=dtempo, utempo=utempo)

    modee = True

    stagun = []
    stados = {}

    for rekod in tiset:
        sorse = rawdb.get(rekod,{})
        for keysa in list(sorse.keys()):
            if dicto.get(keywo,'') != '':
                if sorse.get(keysa,'') != dicto.get(keywo,''):
                    modee = False
        if modee:
            stagun.append(rekod)
            print(sorse.get(kekas,'')+' = '+keywo+"?")

            if sorse.get(kekas,'') == keywo:
                taket = sorse.get(takas,'')
                print('kekas:'+kekas+', value:'+sorse.get(kekas,''))
                print('takas:'+takas+', taket:'+taket)
                upvalu = stados.get(taket,0.0) + float(sorse.get('tpric',''))
                stados.update({ taket : upvalu })

        modee = True

    satres = {}
    for itema in stados:
        valus = stados.get(itema,0.0)
        setas = satres.get(valus,[])
        setas.append(itema)
        satres.update({ valus : setas })

    return {'stagun':stagun, 'stados':stados, 'satres':satres}
    #return stados