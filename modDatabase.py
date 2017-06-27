import json, random, hashlib, pprint, requests
import tool, mmcDefauV
# fille = __
# mmcdb.writedb(fille,'raw',mmcdb.opencsv(fille,','))

def opendb(usrdir):
    try:
        faale = open(usrdir + '/record.json','r')
        record = json.load(faale)
        faale.close()
        return record
    except FileNotFoundError:
        faale = open(usrdir + '/record.json','w')
        db = {'raw':{},'key':{},'hash':{}}
        json.dump(db,faale)
        faale.close()
        return db

def openSetting(usrdir):
    try:
        faale = open(usrdir + '/setting.json','r')
        setting = json.load(faale)
        faale.close()
        return setting
    except FileNotFoundError:
        faale = open(usrdir + '/setting.json','w')
        setting = mmcDefauV.keywo('setting')
        json.dump(setting,faale)
        faale.close()
        return setting

def changeSetting(usrdir,libra):
    faale = open(usrdir + '/setting.json','w')
    json.dump(libra,faale)
    faale.close()

def openKaratio(usrdir):
    tool.ckfile(usrdir,'karen.json',addi='json')
    faale = open(usrdir + '/karen.json',"r")
    try:
        karatio = json.load(faale)
    except ValueError:
        karatio = {}
    faale.close()
    return karatio

def getKaratio(usrdir,keydb,modde='refes'):
    resut = False
    if int(tool.acedate(usrdir,'karen')) < int(tool.date()):
        if modde == 'refes':
            karatio = openKaratio(usrdir)
        elif modde == 'reset':
            karatio = {}
        curre = set(list(keydb.get('karen'))+list(keydb.get('tkare')))
        kara = []
        for m in curre:
            for n in curre:
                if m != n:
                    kara.append(m+n)
        setta = '\"'+'\",\"'.join(kara)+'\"'
        urlla = 'http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20('+setta+')&format=json&env=store://datatables.org/alltableswithkeys'
        datta = json.loads(requests.get(urlla).text)
        for m in datta['query']['results']['rate']:
            karatio.update({ m['id'] : m['Rate'] })

        faale = open(usrdir + '/karen.json',"w")
        json.dump(karatio,faale)
        tool.acedate(usrdir,'karen',modda='write')
        faale.close()

        resut = True
    return resut

""" mmcdb.opencsv( ,',')"""
def opencsv(fille,keywo):
    result = {}
    numo = 0
    for linne in open(fille).read().splitlines():
        if "!" in linne:
            keys = linne.replace("!","").split(keywo)
        elif linne[0] != "#":
            zero = '9000'
            uri = tool.date(modde=3)
            nama = uri + zero[ 0 : 4-len(str(numo)) ] + str(numo)
            result.update({ nama : {} })
            word = linne.split(keywo)
            for n in range(0,len(word)):
                result.get(nama,{}).update({ keys.get(n,'') : word.get(n,'') })
            numo = numo + 1
    return result

""" record = mmcdb.addRaw(chat_id,self._temra)"""
def addRaw(usrdir,temra):
    record = opendb(usrdir)
    timta = tool.date(3) + '0000'
    record.get('raw',{}).update({ timta : temra })
    faale = open(usrdir + '/record.json','w')
    json.dump(record,faale)
    faale.close()
    return record

""" record = mmcdb.addRaw(chat_id,self._temra)"""
def chRaw(usrdir,uuid,temra):
    record = opendb(usrdir)
    record.get('raw',{}).update( { uuid : temra } )
    faale = open(usrdir + '/record.json','w')
    json.dump(record,faale)
    faale.close()
    return record

def diffdb(a,b):
    for m in a.keys():
        if a.get(m) != b.get(m):
            c=pprint.pformat(a.get(m)).replace('\n', '  ')
            d=pprint.pformat(b.get(m)).replace('\n', '  ')
            print(c+'\n'+d)

def genKey(rawdb):
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

""" genHash(rawdb)"""
def genHash(rawdb):
    hashdb = {}
    for uuid in list(rawdb.keys()):
        hasa = hashlib.sha512()
        if rawdb.get(uuid,{}) != {}:
            hasa.update((",".join(set(list(rawdb.get(uuid,{}).values())))).encode("utf-8"))
            hashdb.update( { uuid : hasa.hexdigest() } )
    return hashdb

def ckrpt(h):
    l={}
    for n in h.keys():
        if '' in h[n].values():
            for m in h[n].keys():
                if m != 'desci':
                    if h[n][m] == '':
                        l.update( { n : m } )
    return l

def ckdb(a,b):
    l={}
    for m in a:
        for n in a[m]:
            if n != '':
                if sorted(a[m][n]) !=  sorted(b[m][n]):
                    l.update( { m+' '+n  : [sorted(b[m][n]) , sorted(a[m][n])] } )
    return l

""" fixAcc(libra[raw],usrid)"""
def fixAcc(usrdir,rawdb):
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
            ndb.update( {'tpric' : ndb.get('price','') })
            ndb.update( {'tkare' : ndb.get('karen','') })
            if ndb.get('fromm','') == '':
                ndb.update( {'fromm' : dexpe })
            if ndb.get('toooo','') == '':
                ndb.update( {'toooo' : ovede })
        rawdb.update({ n : ndb })
    return rawdb

""" mmcdb.refesdb(chat_id)"""
def refesdb(usrdir):
    libra = {}
    rawdb = opendb(usrdir).get('raw',{})
    rawdb = fixAcc(usrdir,rawdb)
    libra.update( {'raw' : rawdb})
    keydb = genKey(rawdb)
    libra.update( {'key' : keydb})
    hashdb = genHash(rawdb)
    libra.update( {'hash' : hashdb})
    faale = open(usrdir + '/record.json','w')
    json.dump(libra,faale)
    faale.close()

""" mmcdb.upgradeSetting(self._setting,chat_id)"""
def upgradeSetting(usrdir,lib):
    libra = openSetting(usrdir)
    if set(libra.keys()) == set(lib.keys()):
        return libra
    else:
        for keywo in libra.keys():
            lib[keywo]=libra[keywo]
        changeSetting(usrdir,lib)
        return lib

""" importRaw(usrid,lib)"""
def importRaw(usrdir,lib):
    refesdb(usrdir)
    lib=fixAcc(usrdir,lib)
    source = opendb(usrdir)
    for uuid in list(lib.keys()):
        hasa = hashlib.sha512()
        if lib[uuid] != {}:
            hasa.update((",".join(set(list(lib[uuid].values())))).encode("utf-8"))
            if hasa.hexdigest() not in list(source['hash'].values()):
                source['raw'][uuid]=lib[uuid]
    filla = open(usrdir + '/record.json','w')
    json.dump(source,filla)
    filla.close()

""" recomc(self._keys,self._keywo,knolib,unoset,usrid) """
def recomc(usrdir,srckey,veluo,knolib,unoset):
    #refesdb(usrid)
    rawdb = opendb(usrdir).get('raw',{})
    keydb = opendb(usrdir).get('key',{})
    rslib = {}
    for uuid in keydb.get(srckey,{}).get(veluo,[]):
        mdlib = {}
        for rawkey in rawdb.get(uuid,{}):
            if rawkey in unoset:
                mdlib.update({ rawkey : rawdb.get(uuid,{}).get(rawkey,'') })
            elif rawkey in knolib.keys():
                if rawdb.get(uuid,{}).get(rawkey,'') != knolib.get(rawkey,''):
                    mdlib.update({ 'mismo' : 'no' })
        if mdlib.get('mismo','') != 'no':
            for mdkey in mdlib.keys():
                mdlist = rslib.get(mdkey,[])
                mdlist.append(mdlib.get(mdkey,''))
                rslib.update({ mdkey : [x for x in mdlist if x != ''] })
    for rskey in rslib:
        lista = []
        listo = rslib.get(rskey,[])
        setto = set(listo)
        for n in [1,2,3,4,5]:
            try:
                dan = max(setto,key=listo.count)
                lista.append(dan)
                setto.remove(dan)
            except ValueError:
                print('finish listing')
        rslib.update({ rskey : lista })
    return rslib

""" mmcdb.recomtxt(self._temra,self._keys,self._keywo,['namma','klass','shoop','price'],chat_id) """
def recomtxt(usrdir,temra,vetco,keysa,keywo,deset):
    fsdic = mmcDefauV.keywo('fs')
    skdic = mmcDefauV.keywo('transle')

    finno = ""
    conta = vetco.get(2,{})
    numme = str(random.choice(range(10,100)))
    nodda = 0

    knolib = {}
    knoset = [ x for x in deset if temra.get(x,'') != '' ]
    unoset = set(deset) - set(knoset)

    for knokey in knoset:
        knolib.update({ knokey : temra.get(knokey,'') })

    rslib = recomc(usrdir,keysa,keywo,knolib,unoset)
    for rskey in rslib:
        for itema in rslib.get(rskey,[]):
            try:
                itema.encode('latin-1')
                finno = finno + "    /rg_"+fsdic[rskey]+"_"+itema+" "+itema+" ("+skdic[rskey]+")\n\n"
            except UnicodeEncodeError:
                conta.update({ numme+str(nodda) : itema })
                finno = finno + "    /rgs_"+fsdic[rskey]+"_"+numme+str(nodda)+" "+itema+" ("+skdic[rskey]+")\n\n"
                nodda = nodda + 1

    return { 1:finno , 2:conta}

""" mmcdb.listAcc('ch','chu',keywo,chat_id)"""
def listAcc(usrdir,pref,prefs,keywo):
    skdic = mmcDefauV.keywo('transle')
    sfdic = mmcDefauV.keywo('sf')
    listo = []
    finno = ""
    conta = {}
    numme = str(random.choice(range(100,1000)))
    nodda = 0
    libro = opendb(usrdir)
    keydb = libro.get('key',{})
    frodb = keydb.get('fromm',{})
    toodb = keydb.get('toooo',{})
    listo = set(list(frodb.keys())+list(toodb.keys()))
    for intta in listo:
        if intta != '':
            try:
                intta.encode('latin-1')
                finno = finno + "    /"+pref+"_"+keywo+"_"+intta+" "+intta+" ("+skdic.get(keywo, skdic.get(sfdic.get(keywo,''),'') )+")\n\n"
            except UnicodeEncodeError:
                conta[numme+str(nodda)]=intta
                finno = finno + "    /"+prefs+"_"+keywo+"_"+numme+str(nodda)+" "+intta+" ("+skdic.get(keywo, skdic.get(sfdic.get(keywo,''),'') )+")\n\n"
                nodda = nodda + 1
    return {1:finno,2:conta}

""" mmcdb.listSeller(self._temra.get('klass',''),'rg','rgs',keywo,chat_id)"""
def listSeller(usrdir,klass,pref,prefs,keywo):
    skdic = mmcDefauV.keywo('transle')
    sfdic = mmcDefauV.keywo('sf')
    listo = []
    finno = ""
    conta = {}
    numme = str(random.choice(range(100,1000)))
    nodda = 0

    rawdb = opendb(usrdir).get('raw',{})
    keydb = opendb(usrdir).get('key',{})
    listo = []
    for uuid in keydb.get('klass',{}).get(klass,[]):
        listo.append(rawdb.get(uuid,{}).get('shoop',''))
    lists = set(listo)

    for intta in lists:
        if intta != '':
            try:
                intta.encode('latin-1')
                finno = finno + "    /"+pref+"_"+keywo+"_"+intta+" "+intta+" ("+skdic.get(keywo, skdic.get(sfdic.get(keywo,''),'') )+")\n\n"
            except UnicodeEncodeError:
                conta.update( { numme+str(nodda) : intta })
                finno = finno + "    /"+prefs+"_"+keywo+"_"+numme+str(nodda)+" "+intta+" ("+skdic.get(keywo, skdic.get(sfdic.get(keywo,''),'') )+")\n\n"
                nodda = nodda + 1
    return {1:finno,2:conta}

""" mmcdb.listKas('ch','chu',keywo,chat_id)"""
def listKas(usrdir,pref,prefs,keywo):
    listo = []
    finno = ""
    conta = {}
    numme = str(random.choice(range(100,1000)))
    nodda = 0
    libro = opendb(usrdir)
    keydb = libro.get('key',{})
    kladb = keydb.get('klass',{})
    listo = set(list(kladb.keys()))
    for intta in listo:
        if intta != '':
            try:
                intta.encode('latin-1')
                finno = finno + "    /"+pref+"_"+keywo+"_"+intta+" "+intta+"\n\n"
            except UnicodeEncodeError:
                conta[numme+str(nodda)]=intta
                finno = finno + "    /"+prefs+"_"+keywo+"_"+numme+str(nodda)+" "+intta+"\n\n"
                nodda = nodda + 1
    return {1:finno,2:conta}

""" mmcdb.listKen('ch','chu',keywo,chat_id)"""
def listKen(usrdir,pref,prefs,keywo):
    listo = []
    finno = ""
    conta = {}
    numme = str(random.choice(range(10,100)))
    nodda = 0
    libro = opendb(usrdir)
    keydb = libro.get('key',{})
    kardb = keydb.get('karen',{})
    takdb = keydb.get('tkare',{})
    listo = set(list(kardb.keys())+list(takdb.keys()))
    for intta in listo:
        if intta != '':
            try:
                intta.encode('latin-1')
                finno = finno + "    /"+pref+"_"+keywo+"_"+intta+" "+intta+"\n\n"
            except UnicodeEncodeError:
                conta[numme+str(nodda)]=intta
                finno = finno + "    /"+prefs+"_"+keywo+"_"+numme+str(nodda)+" "+intta+"\n\n"
                nodda = nodda + 1
    return {1:finno,2:conta}

def listLigua(pref,keywo):
    finno = ""
    listo = mmcDefauV.keywo('lingua')
    for intta in listo:
        finno = finno + "    /"+pref+"_"+keywo+"_"+intta+" "+intta+"\n\n"
    return {1:finno,2:{}}

def listList(usrdir,datte):
    tasta=""
    try:
        libron = opendb(usrdir)
        rauron = libron.get('raw',{})
        datron = libron.get('key',{}).get('datte',{}).get(datte,{})
        for n in datron:
            nron = rauron.get(n,{})
            tasta = tasta + '/uuid_'+n+'\n    '
            tasta = tasta + nron.get('datte','') +'  '
            tasta = tasta + nron.get('namma','') +'  '
            tasta = tasta + nron.get('klass','') +'  '
            tasta = tasta + nron.get('karen','') +' '
            tasta = tasta + nron.get('price','') +'\n'
        return tasta
    except IndexError :
        return ''

def timra(usrdir, dtempo='',utempo='', modde='uuid'):
    libra = opendb(usrdir)
    rawdb = libra.get('raw',{})
    keydb = libra.get('key',{})

    if dtempo == '':
        dtempo = tool.date(modde=1)[0:8]
    if utempo == '':
        utempo = tool.date(modde=1)[0:8]

    tok = []
    tik = sorted(set(keydb.get('datte',{}).keys()))
    print('tik : '+pprint.pformat(tik,compact=True))
    toka = 0
    toko = len(tik)
    try:
        toka = tik.index(dtempo)
    except ValueError:
        ck = 0
        for n in sorted(tik, reverse=True):
            if dtempo[0:8] in n:
                toka = tik.index(n)
                ck = 1

        if ck == 0:
            for n in sorted(tik, reverse=True):
                if dtempo[0:4] in n:
                    toka = tik.index(n)
                    ck = 1

    try:
        toko = tik.index(utempo)
    except ValueError:
        ck = 0
        for n in tik:
            if utempo[0:8] in n:
                toko = tik.index(n)
                ck = 1

        if ck == 0:
            for n in tik:
                if utempo[0:4] in n:
                    toko = tik.index(n)
                    ck = 1

    tok = tik[toka:toko+1]
    print('tok : '+pprint.pformat(tok,compact=True))

    datui = []
    for datte in tok:
        datui.extend(keydb.get('datte',{}).get(datte,[]))

    if modde == 'datte':
        return tok
    elif modde == 'uuid':
        return datui