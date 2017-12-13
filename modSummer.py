from core import modDatabase

def sumer(usrdir,dicto):
    print('modSummer.sumer: '+usrdir)
    libra = modDatabase.opendb(usrdir)
    libra = modDatabase.opendb(usrdir)
    rawdb = libra.get('raw',{})
    keydb = libra.get('key',{})

    dtempo = dicto.get('dtempo','')
    utempo = dicto.get('utempo','')
    takas = dicto.get('takas','')
    kekas = dicto.get('kekas','')
    karen = dicto.get('karen','')

    keywo = dicto.get(kekas,'')
    tiset = modDatabase.timra(usrdir, dtempo=dtempo, utempo=utempo)

    modee = True

    stagun = []
    stados = {}
    stacua = {}

    for rekod in tiset:
        sorse = rawdb.get(rekod,{})
        for keysa in list(sorse.keys()):
            if dicto.get(keywo,'') != '':
                if sorse.get(keysa,'') != dicto.get(keywo,''):
                    modee = False

        valus = 0.0
        if modee:
            stagun.append(rekod)
            #print(sorse.get(kekas,'')+' = '+keywo+"?")

            if sorse.get(kekas,'') == keywo:
                taket = sorse.get(takas,'')
                tkare = sorse.get('tkare','')
                tpric = sorse.get('tpric','')
                valus = 0.0
                upvalu = 0.0
                valis = []
                print('kekas:'+kekas+', value:'+sorse.get(kekas,''))
                print('takas:'+takas+', taket:'+taket)

                if tkare != karen:
                    valus = modDatabase.cvKaren(usrdir,tkare,karen,float(tpric))
                else:
                    valus = float(tpric)

                upvalu = round(stados.get(taket,0.0) + valus,2)
                stados.update({ taket : upvalu })

                valis = stacua.get(taket,[])
                valis.append(rekod)
                stacua.update({ taket : valis })

        modee = True

    satres = {}
    for itema in stados:
        valus = 0.0
        setas = []
        valus = stados.get(itema,0.0)
        setas = satres.get(valus,[])
        setas.append(itema)
        satres.update({ valus : setas })

    return {'stagun':stagun, 'stados':stados, 'satres':satres, 'stacua':stacua}
    #return stados
