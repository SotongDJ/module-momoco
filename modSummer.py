from core import modDatabase
from core import modVariables

def sumer(usrdir,dicto):
    print('modSummer.sumer: '+usrdir)
    libra = modDatabase.opendb(usrdir)
    modDatabase.getKaratio(usrdir)
    karatio = modDatabase.openKaratio(usrdir)
    libra = modDatabase.opendb(usrdir)
    rawdb = libra.get('raw',{})
    keydb = libra.get('key',{})

    dtempo = dicto.get('dtempo','')
    utempo = dicto.get('utempo','')
    takas = dicto.get('takas','')
    kekad = dicto.get('kekas','')
    keywo = dicto.get('keywo','')

    tiset = modDatabase.timra(usrdir, dtempo=dtempo, utempo=utempo)

    modee = True

    stagun = []
    for rekod in tiset:
        sorse = rawdb.get(rekod,{})
        for keywo in list(sorse.keys()):
            if dicto.get(keywo,'') != '':
                if sorse.get(keywo,'') != dicto.get(keywo,''):
                    modee = False
        if modee:
            stagun.append(rekod)
        modee = True

    stados = {}
    for rekod in stagun:
        sorse = rawdb.get(rekod,{})
        if sorse.get(kekas,'') == keywo:
            taket = sorse.get(takas,'')
            upvalu = stados.get(taket,0.0)
            stados.update({ taket : upvalu })

    return {'stagun':staguno, 'stados':stados}
