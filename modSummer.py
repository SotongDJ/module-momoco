from core import modDatabase
from core import modVariables

def sumer(usrdir,dicto):
    print('modSummer.sumer: '+usrdir)
    libra = modDatabase.opendb(usrdir)
    rawdb = libra.get('raw',{})
    keydb = libra.get('key',{})

    dtempo = dicto.get('dtempo','')
    utempo = dicto.get('utempo','')
    namma = dicto.get('namma','')
    klass = dicto.get('klass','')
    shoop = dicto.get('shoop','')
    fromm = dicto.get('fromm','')
    karen = dicto.get('karen','')
    price = dicto.get('price','')
    toooo = dicto.get('toooo','')
    tkare = dicto.get('tkare','')
    tpric = dicto.get('tpric','')

    tiset = modDatabase.timra(usrdir, dtempo=dtempo, utempo=utempo)
