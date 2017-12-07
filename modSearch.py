from core import modDatabase
from core import modVariables

def sachi(usrdir,dicto):
    print('modSearch.sachi: '+usrdir)
    libra = modDatabase.opendb(usrdir)
    rawdb = libra.get('raw',{})
    keydb = libra.get('key',{})

    keywo = dicto.get('keywo','')
    dtempo = dicto.get('dtempo','')
    utempo = dicto.get('utempo','')
    cokas = dicto.get('cokas','')

    tiset = modDatabase.timra(usrdir, dtempo=dtempo, utempo=utempo)

    if cokas == '':
        kaset = keydb.keys()
    else:
        kaset = [cokas]

    ralib = {}
    keyra = {}
    for keyo in kaset:
        for valo in keydb.get(keyo,{}).keys():
            vakey = ralib.get(valo,[])
            nonom = len(vakey)
            vaset = keydb.get(keyo).get(valo)
            vakey.extend([x for x in vaset if x in tiset])
            nonam = len(vakey)
            if nonam > nonom:
                ralib.update({ valo : vakey })

                kekey = keyra.get(valo,[])
                kekey.extend([keyo])
                keyra.update({ valo : kekey })

    kelib = {} # searchresut : uuid
    keyto = {} # searchresut : class
    for valo in ralib.keys():
        if keywo in valo:
            kelib.update({ valo : ralib.get(valo,[]) })
            keyto.update({ valo : keyra.get(valo,[]) })

    return { 'kelib': kelib , 'keyto': keyto }

def listSachi(usrdir,libto,lingua='enMY'):
    libra = modDatabase.opendb(usrdir)
    rawdb = libra.get('raw',{})

    kelib = libto.get('kelib',{})
    keyto = libto.get('keyto',{})

    transle = modVariables.keywo('transle',lingua=lingua)
    resut = {'resut':{},'lenam':1,'lenes':1}

    lenam = 1
    lenes = 1
    for keyo in kelib.keys():
        conto = {}
        namma = keyo + '\n'
        lenna = len(namma)
        if lenam < lenna:
            lenam = lenna
        otnoc = [transle.get(x,'') for x in keyto.get(keyo,[]) ]
        namma = namma +'(' + ',\n'.join(otnoc)+ ')'
        for uuid in set(kelib.get(keyo,[])):
            testa = '　' + rawdb.get(uuid,{}).get('datte','')+'　'
            testa = testa + rawdb.get(uuid,{}).get('namma','')+'\n'
            testa = testa + '　' + rawdb.get(uuid,{}).get('klass','')+'　'
            testa = testa + rawdb.get(uuid,{}).get('shoop','')+'\n'
            testa = testa + '　' + rawdb.get(uuid,{}).get('fromm','')+' '
            testa = testa + rawdb.get(uuid,{}).get('karen','')+' '
            testa = testa + rawdb.get(uuid,{}).get('price','')+'\n'
            testa = testa + '　' + rawdb.get(uuid,{}).get('toooo','')+' '
            testa = testa + rawdb.get(uuid,{}).get('tkare','')+' '
            testa = testa + rawdb.get(uuid,{}).get('tpric','')+'\n'
            conto.update({ uuid : testa })
        resut.get('resut').update({ namma : conto })

    return resut
