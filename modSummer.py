from core import modDatabase
from core import tool

def help():
    print("""
    sumer(usrdir,parao,dicto,vebo=False):
        usrdir: path for user's data (end without '/')
            'database'

        parao: parametre
            {
                'btempo':'2017-10', #Begin of time range
                'ftempo':'2017-12', #End of time range
                'takas':'shoop', # Target category
                'kekas':'klass', # Base category
                'karen':'TWD' # Target currency
            }

        dicto: filter for each category
            {'klass':'食物','toooo':'支出'}

        vebo: view more detail
            True or False
    """)

def vebosa(msg="",vebo=False):
    if vebo:
        print(msg)

def sumer(usrdir,parao,dicto,vebo=False):
    print('modSummer.sumer: '+usrdir)
    libra = modDatabase.opendb(usrdir)
    rawdb = libra.get('raw',{})
    keydb = libra.get('key',{})
    btempo = parao.get('btempo','')
    ftempo = parao.get('ftempo','')

    resut = {}
    tiset = modDatabase.timra(usrdir, btempo=btempo, ftempo=ftempo)

    stagun = samuno(usrdir,tiset,dicto,vebo=vebo)
    resut.update({'stagun':stagun})
    resut.update(dotres(usrdir,stagun,parao,dicto,vebo=vebo))

    return resut

def samuno(usrdir,ulist,dicto,vebo=False):
    print('modSummer.samuno: '+usrdir)
    libra = modDatabase.opendb(usrdir)
    rawdb = libra.get('raw',{})
    keydb = libra.get('key',{})

    modee = True
    stagun = []

    for rekod in ulist:
        sorse = rawdb.get(rekod,{})
        for keysa in list(sorse.keys()):
            if dicto.get(keysa,'') != '':
                if sorse.get(keysa,'') != dicto.get(keysa,''):
                    vebosa(msg="[remove]keysa:"+sorse.get(keysa,'')+"!="+dicto.get(keysa,''),vebo=vebo)
                    modee = False
        if modee:
            stagun.append(rekod)
        modee = True
    return stagun

def dotres(usrdir,ulist,parao,dicto,vebo=False):
    print('modSummer.dotres: '+usrdir)
    libra = modDatabase.opendb(usrdir)
    rawdb = libra.get('raw',{})
    keydb = libra.get('key',{})

    takas = parao.get('takas','')
    kekas = parao.get('kekas','')
    karen = parao.get('karen','')
    keywo = dicto.get(kekas,'')

    stados = {}
    satres = {}
    stacua = {}

    for rekod in ulist:
        sorse = rawdb.get(rekod,{})

        if sorse.get(kekas,'') == keywo:
            taket = sorse.get(takas,'')
            tkare = sorse.get('tkare','')
            tpric = sorse.get('tpric','')
            valus = 0.0
            upvalu = 0.0
            valis = []
            vebosa(msg='[accept]kekas:'+kekas+', takas:'+takas,vebo=vebo)
            print('[accept]value:'+sorse.get(kekas,'')+', taket:'+taket)

            if tkare != karen:
                valus = modDatabase.cvKaren(usrdir,tkare,karen,float(tpric))
            else:
                valus = float(tpric)

            upvalu = round(stados.get(taket,0.0) + valus,2)
            stados.update({ taket : upvalu })

            valis = stacua.get(taket,[])
            valis.append(rekod)
            stacua.update({ taket : valis })

    for itema in stados:
        valus = 0.0
        setas = []
        valus = stados.get(itema,0.0)
        setas = satres.get(valus,[])
        setas.append(itema)
        satres.update({ valus : setas })

    return {'stados':stados, 'satres':satres, 'stacua':stacua}
