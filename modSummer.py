from core import modDatabase
from core import modVariables

def sumer(usrdir,dicto):
    print('modSummer.sumer: '+usrdir)
    libra = modDatabase.opendb(usrdir)
    rawdb = libra.get('raw',{})
    keydb = libra.get('key',{})

    dtempo = dicto.get('dtempo','')
    utempo = dicto.get('utempo','')

    tiset = modDatabase.timra(usrdir, dtempo=dtempo, utempo=utempo)

    modee = True

    resut = []
    for rekod in tiset:
        sorse = rawdb.get(rekod,{})
        for keywo in list(sorse.keys()):
            if dicto.get(keywo,'') != '':
                if sorse.get(keywo,'') != dicto.get(keywo,''):
                    modee = False
        if modee:
            resut.append(rekod)
        modee = True
    return resut
