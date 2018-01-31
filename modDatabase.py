import json, random, pprint, requests
from core import tool
from core import modVariables

def opendb(usrdir):
    print('modDatabase.opendb: '+usrdir)
    try:
        faale = open(usrdir + '/record.json','r')
        record = json.load(faale)
        faale.close()
        return record
    except FileNotFoundError:
        tool.diro(direc=usrdir)
        faale = open(usrdir + '/record.json','w')
        db = {'raw':{},'key':{}}
        json.dump(db,faale,indent=4,sort_keys=True)
        faale.close()
        return db

def openSetting(usrdir):
    print('modDatabase.openSetting: '+usrdir)
    try:
        faale = open(usrdir + '/setting.json','r')
        setting = json.load(faale)
        faale.close()
        return setting
    except FileNotFoundError:
        tool.diro(direc=usrdir)
        faale = open(usrdir + '/setting.json','w')
        argo = modVariables.Argo()
        json.dump(argo.setti,faale,indent=4,sort_keys=True)
        faale.close()
        return setting

def changeSetting(usrdir,libra):
    print('modDatabase.changeSetting: '+usrdir)
    faale = open(usrdir + '/setting.json','w')
    json.dump(libra,faale,indent=4,sort_keys=True)
    faale.close()

def cvKaren(usrdir,orika,tarka,innum):
    print('modDatabase.cvKaren: '+usrdir)
    print('input: '+orika+' '+str(innum))
    tool.ckfile(usrdir,'karen.json',addi='json')
    faale = open(usrdir + '/karen.json',"r")
    try:
        karat = json.load(faale)
    except ValueError:
        karat = {}
    faale.close()

    ratae = karat.get(orika+tarka,0.0)
    outnu = round(innum * ratae,2)

    print('output: '+tarka+' '+str(outnu))
    return outnu

def getKaratio(usrdir,modde='refes'):
    print('modDatabase.getKaratio: '+ usrdir)
    print('modde: '+modde)
    keydb = opendb(usrdir).get('key',{})

    if modde == 'refes':
        karat = openKaratio(usrdir)
        resut = openKaratio(usrdir)
    elif modde == 'reset':
        karat = {}
        resut = {}

    curre = set(list(keydb.get('karen'))+list(keydb.get('tkare')))
    for m in curre:
        for n in curre:
            if m != n:
                urlla = 'https://free.currencyconverterapi.com/api/v5/convert?q='+m+'_'+n+'&compact=y'
                print("URL: "+urlla+" ")
                datta = json.loads(requests.get(urlla).text)
                pprint.pprint(datta)
                resut.update({ m+n : datta.get(m+'_'+n,{}).get('val',0.0) })

    if karat != resut:
        faale = open(usrdir + '/karen.json',"w")
        json.dump(resut,faale,indent=4,sort_keys=True)
        faale.close()
        print("Karat changed \n resut:")
        pprint.pprint(resut)
    else:
        print("Karat remain")

def opencsv(fille,keywo):
    print('modDatabase.opencsv')
    print('keywo: '+keywo)
    result = {}
    numo = 0
    keys = []
    tite = False
    for linne in open(fille,'br').read().decode('utf-8').splitlines():
        if "!" in linne:
            keys = linne.replace("!","").split(keywo)
            if 'uuid' in keys:
                tite = True
        elif linne[0] != "#":
            libo = {}
            word = linne.split(keywo)
            for n in range(0,len(word)):
                libo.update({ keys[n] : word[n] })
            if tite:
                result.update({ libo.pop('uuid','false').replace("uuid-","") : libo  })
            else:
                zero = '9000'
                uri = tool.date(modde=3)
                nama = uri + zero[ 0 : 4-len(str(numo)) ] + str(numo)
                result.update({ nama : libo })
                numo = numo + 1
    return result

def addRaw(usrdir,temra):
    print('modDatabase.addRaw: '+usrdir)
    record = opendb(usrdir)
    timta = tool.date(3) + '0000'
    record.get('raw',{}).update({ timta : temra })
    faale = open(usrdir + '/record.json','w')
    json.dump(record,faale,indent=4,sort_keys=True)
    faale.close()
    return record

def chRaw(usrdir,uuid,temra):
    print('modDatabase.chRaw: '+usrdir)
    print('uuid: '+uuid)
    record = opendb(usrdir)
    record.get('raw',{}).update( { uuid : temra } )
    faale = open(usrdir + '/record.json','w')
    json.dump(record,faale,indent=4,sort_keys=True)
    faale.close()
    return record

def rmRaw(usrdir,uuid):
    print('modDatabase.rmRaw: '+usrdir)
    print('uuid: '+uuid)
    record = opendb(usrdir)
    ra = record.get('raw',{}).pop(uuid,'')
    if ra == '':
        print('rmRaw failed, no record')
    faale = open(usrdir + '/record.json','w')
    json.dump(record,faale,indent=4,sort_keys=True)
    faale.close()
    return record

def diffdb(a,b):
    print('modDatabase.diffdb')
    resut=[]
    for m in a.keys():
        if a.get(m,{}) != b.get(m,{}):
            c=a.get(m,{})
            d=b.get(m,{})
            resut.append([c,d])
    return resut

def genKey(rawdb):
    print('modDatabase.genKey')
    keydb = {}
    eledb = {}
    valudb = {}
    for uuid in rawdb.keys():
        for eleme in rawdb.get(uuid,{}):
            valuh = rawdb.get(uuid,{}).get(eleme,'')
            if valuh != '':
                tadd = eledb.get(eleme,{})

                mobb = tadd.get(valuh,[])
                mobb.append(uuid)
                mobb = sorted(list(set(mobb)))

                tadd.update( { valuh : mobb } )
                eledb.update({ eleme : tadd })
    return eledb

def ckrpt(h):
    print('modDatabase.ckrpt')
    l={}
    for n in h.keys():
        if '' in h[n].values():
            for m in h[n].keys():
                if m != 'desci':
                    if h[n][m] == '':
                        l.update( { n : m } )
    return l

def ckdb(a,b):
    print('modDatabase.ckdb')
    l={}
    for uuid in a:
        for n in a[uuid]:
            if n != '':
                if a[uuid][n] !=  b.get(uuid,{}).get(n,''):
                    l.update( { uuid+' '+n  : [a[uuid][n], b.get(uuid,{}).get(n,'')] } )
    return l

def fixAcc(usrdir,rawdb):
    print('modDatabase.fixAcc: '+usrdir)
    setti = openSetting(usrdir)
    #rawdb = opendb(usrid).get('raw',{})

    tanfe = setti.get('tanfe','Transfer')
    incom = setti.get('incom','Income')

    dinco = setti.get('dinco','Bank')
    dexpe = setti.get('dexpe','Cash')
    genis = setti.get('genis','Income')
    ovede = setti.get('ovede','Expense')

    karen = setti.get('karen','')

    for n in list(rawdb):
        ndb = rawdb.get(n,{})
        if ndb.get('klass','') == incom:
            if ndb.get('price','') == '':
                ndb.update( {'price' : ndb.get('tpric','') })
            if ndb.get('karen','') == '':
                ndb.update( {'karen' : ndb.get('tkare','') })
            if ndb.get('fromm','') == '':
                ndb.update( {'fromm' : genis })
            if ndb.get('toooo','') == '':
                ndb.update( {'toooo' : dinco })
        elif ndb.get('klass','') in tanfe:
            if ndb.get('tpric','') == '':
                ndb.update( {'tpric' : ndb.get('price','') })
            if ndb.get('tkare','') == '':
                ndb.update( {'tkare' : ndb.get('karen','') })
            if ndb.get('fromm','') == '':
                ndb.update( {'fromm' : dinco })
            if ndb.get('toooo','') == '':
                ndb.update( {'toooo' : dexpe })
        else:
            if ndb.get('fromm','') == '':
                ndb.update( {'fromm' : dexpe })
            if ndb.get('toooo','') == '':
                ndb.update( {'toooo' : ovede })
        rawdb.update({ n : ndb })
    return rawdb

def refesdb(usrdir):
    print('modDatabase.refesdb: '+usrdir)
    libra = {}
    rawdb = opendb(usrdir).get('raw',{})
    rawdb = fixAcc(usrdir,rawdb)
    libra.update( {'raw' : rawdb})
    keydb = genKey(rawdb)
    libra.update( {'key' : keydb})
    faale = open(usrdir + '/record.json','w')
    json.dump(libra,faale,indent=4,sort_keys=True)
    faale.close()

def upgradeSetting(usrdir,lib):
    print('modDatabase.upgradeSetting: '+usrdir)
    libra = openSetting(usrdir)
    if set(libra.keys()) == set(lib.keys()):
        return libra
    else:
        for keywo in libra.keys():
            lib[keywo]=libra[keywo]
        changeSetting(usrdir,lib)
        return lib

def importRaw(usrdir,lib):
    print('modDatabase.importRaw: '+usrdir)
    refesdb(usrdir)
    lib=fixAcc(usrdir,lib)
    source = opendb(usrdir)
    for uuid in list(lib.keys()):
        source.get('raw',{}).update({ uuid : lib.get(uuid,{}) })

    filla = open(usrdir + '/record.json','w')
    json.dump(source,filla,indent=4,sort_keys=True)
    filla.close()

def expocsv(usrdir,keywo):
    print('modDatabase.opencsv')
    result = {}
    numo = 0
    temla = usrdir + '/template.csv'
    resuf = open(usrdir + '/result-' + tool.date(3) + '.csv','w')
    rawdb = opendb(usrdir).get('raw')
    for linne in open(temla,'br').read().decode('utf-8').splitlines():
        if "!" in linne:
            keys = linne.replace("!","").split(keywo)
        resuf.write(linne + '\n')
    for uuid in sorted(list(rawdb.keys())):
        linno = ''
        temra = rawdb.get(uuid,{})
        temra.update({ 'uuid' : "uuid-"+uuid })
        for keyso in keys:
            linno = linno + temra.get(keyso,'').replace('\n',' ').replace(keywo,'-') + keywo
        resuf.write(linno+'\n')
    resuf.close()

def timra(usrdir, btempo='',ftempo='', modde='uuid'):
    print('modDatabase.timra: '+usrdir)
    print('modde: '+modde)
    libra = opendb(usrdir)
    rawdb = libra.get('raw',{})
    keydb = libra.get('key',{})

    if btempo == '':
        btempo = tool.date(modde=1)[0:7]
    if ftempo == '':
        ftempo = tool.date(modde=1)[0:7]

    ddalit = '0000-00-00'
    udalit = '9999-99-99'
    btempo = btempo + ddalit[len(btempo):len(ddalit)+1]
    ftempo = ftempo + udalit[len(ftempo):len(udalit)+1]
    print('btempo: '+btempo)
    print('ftempo: '+ftempo)

    tok = []
    tak = list(keydb.get('datte',{}).keys())
    tak.append(btempo)
    tak.append(ftempo)
    tik = sorted(set(tak))
    print('datte : '+pprint.pformat(tik,compact=True))

    if tik.index(ftempo)-tik.index(btempo) < 0:
        dlit = ftempo
        ulit = btempo
    else:
        dlit = btempo
        ulit = ftempo

    tuk = tik[tik.index(dlit):tik.index(ulit)+1]

    datui = []
    for datte in tuk:
        datui.extend(keydb.get('datte',{}).get(datte,[]))

    if modde == 'datte':
        return tuk
    elif modde == 'uuid':
        return datui


def listKeywo(usrdir):
    print('modDatabase.listKeywo: '+usrdir)
    keydb = opendb(usrdir).get('key',{})
    resut = {}
    for kas in keydb.keys():
        if kas not in ['datte','price','tpric','desci','karen','tkare']:
            for keywo in keydb.get(kas,{}).keys():
                numon = 0
                metdi = {}
                metse = []

                metdi = resut.get(keywo,{})
                metse = metdi.get(kas,[])
                metse.extend(keydb.get(kas,{}).get(keywo,[]))
                metdi.update({ kas : metse })
                resut.update({ keywo : metdi })
    return resut
