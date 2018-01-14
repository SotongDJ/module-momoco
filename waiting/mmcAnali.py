import pprint, np
import mmcdb, tool, mmcDefauV

def abratio(usrid,dicto):
    saita = mmcdb.openSetting(usrid)
    karen = saita['karen']
    lim = saita['screen']

    btempo=dicto.get('btempo')
    ftempo=dicto.get('ftempo')
    targe=dicto.get('targe')
    cokas=dicto.get('cokas')
    cokey=dicto.get('cokey')

    karatio = mmcdb.openKaratio()

    libra = mmcdb.opendb(usrid)
    timon = mmcdb.timra(usrid,btempo,ftempo)
    pintosum = 0

    tarTpinto = {}
        # { targe : price'int'total}
    tarTpinpos = {}
        # { targe : (price'int'total/sum)*(lim^2) }
    pintoTtarset = {}
        # { price'int'total : [targe1,targe2...] }
    pindiTtarset = {}
        # { price'int'indi : [targe1,targe2...] }
    tarTpinpec = {}
        # { targe : (price'int'total/sum)*100 }
    tarTpinsiset = {}
        # { targe : [price1'str'indi,price2'str'indi...] }
    lenpinsiTtarset = {}
        # { len([price1'str'indi,price2'str'indi...])'int': [targe1, targe2] }

    rawdb = libra['raw']
    keydb = libra['key']

    for uuid in timon:
        if libra['raw'][uuid][cokas] == cokey:
            if libra['raw'][uuid]['karen'] == karen:
                price = round(float(libra['raw'][uuid]['price']),2)
            else:
                rate = float(karatio[libra['raw'][uuid]['karen']+karen])
                price = round(float(libra['raw'][uuid]['price']) * rate,2)

            pinsiset = tarTpinsiset.get(libra['raw'][uuid][targe],[])
            pinsiset.append(str(price))
            tarTpinsiset.update( { libra['raw'][uuid][targe] : pinsiset } )

            tarset = lenpinsiTtarset.get(len(pinsiset),[])
            tarset.append(libra['raw'][uuid][targe])
            lenpinsiTtarset.update( { len(pinsiset) : tarset } )

            pinto = tarTpinto.get(libra['raw'][uuid][targe],0.00)
            pinto = round(pinto + price,2)
            tarTpinto.update( { libra['raw'][uuid][targe] : pinto } )

            tarset = pindiTtarset.get(price,[])
            tarset.append(libra['raw'][uuid][targe])
            pindiTtarset.update( { price : tarset } )

    print('tarTpinsiset : '+pprint.pformat(tarTpinsiset,compact=True))
    print('lenpinsiTtarset : '+pprint.pformat(lenpinsiTtarset,compact=True))
    print('tarTpinto : '+pprint.pformat(tarTpinto,compact=True))
    print('pindiTtarset : '+pprint.pformat(pindiTtarset,compact=True))

    pintosum = round(sum(list(tarTpinto.values())),2)
    if round(pintosum,2) == 0.00:
        return {'pri':['No Data','Maybe using wrong combination']}
    pintoSumsi = str(pintosum)
    print(' pintosum : '+pprint.pformat(pintosum))

    for tarto in list(tarTpinto):

        pinpos = round((tarTpinto[tarto]/pintosum)*(lim*lim))
        tarTpinpos.update( { tarto : pinpos } )

        pinpec = round((tarTpinto[tarto]/pintosum)*(100),2)
        tarTpinpec.update( { tarto : pinpec } )
        #print(' loto : '+pprint.pformat(loto))

        tarset = pintoTtarset.get(tarTpinto[tarto],[])
        tarset.append(tarto)
        pintoTtarset.update( { tarTpinto[tarto] : tarset } )


    print('tarTpinpos : '+pprint.pformat(tarTpinpos,compact=True))
    print('tarTpinpec : '+pprint.pformat(tarTpinpec,compact=True))
    print('pintoTtarset : '+pprint.pformat(pintoTtarset,compact=True))
    pinpecSumsi = str(round(sum(list(tarTpinpec.values())),2))
    pinposSumsi = str(sum(list(tarTpinpos.values())))

    sotPinto = sorted( pintoTtarset , reverse = True)
    print('sotPinto : '+pprint.pformat(sotPinto,compact=True))

    statik = {}
    sotPindi = sorted(pindiTtarset)
    statik.update({ 'max' : pprint.pformat( set( pindiTtarset.get( sotPindi[-1],'' ) ) ).replace('{','').replace('}','') })
    statik.update({ 'maxPc' : str(sotPindi[-1]) })
    statik.update({ 'min' : pprint.pformat( set( pindiTtarset.get( sotPindi[0],'' ) ) ).replace('{','').replace('}','') })
    statik.update({ 'minPc' : str(sotPindi[0]) })

    sotLenpinsi = sorted(lenpinsiTtarset)
    dafro = ''
    for tar in lenpinsiTtarset.get(sotLenpinsi[-1],''):
        dafro = dafro + '－'+tar+' '+karen+' '+pprint.pformat(tarTpinto.get(tar),compact=True).replace('[','').replace(']','')+'\n'
        dafro = dafro + '　'+pprint.pformat(tarTpinsiset.get(tar),compact=True).replace('[','( ').replace(']',' )')+'\n'
    statik.update({ 'time' : str(sotLenpinsi[-1]) })
    statik.update({ 'dafro' : dafro })

    pri = []
    for pinto in sotPinto:
        print('nume : '+pprint.pformat(pinto))
        for tarit in pintoTtarset[pinto]:
            #print('tarit : '+pprint.pformat(tarit))
            pinos = tarTpinpos[tarit]
            #print('pinos : '+pprint.pformat(pinos))
            fisTar = tool.uni(tarit[0])
            try:
                reclinum = len(pri[-1])
            except IndexError:
                pri = ['']
                reclinum = 0
            pprint.pprint([tarit,pinos,reclinum,lim],compact=True)
            if pinos + reclinum >lim:
                if reclinum < lim:
                    pri[-1]=pri[-1]+fisTar*(lim-reclinum)
                    pinos = pinos + reclinum - lim
                if pinos > lim:
                    tik = int(pinos/lim)
                    tok = pinos % lim
                    for n in range(0,tik):
                        pri.append(fisTar*lim)
                    pri.append(fisTar*tok)
                    pprint.pprint([tarit,pinos,reclinum,lim],compact=True)
                elif pinos <= lim:
                    pri.append(fisTar*pinos)
                    pprint.pprint([tarit,pinos,reclinum,lim],compact=True)
            elif pinos + reclinum <= lim:
                pri[-1]=pri[-1]+fisTar*pinos
                print('[tarit,pinos,reclinum,lim]')
                pprint.pprint([tarit,pinos,reclinum,lim],compact=True)

    des=""
    for pinto in sotPinto:
        for taran in pintoTtarset[pinto]:
            des=des+taran[0]+'　'+taran+'\n　　'+karen+' '+str(tarTpinto[taran])+' ('+str(tarTpinpec[taran])+'%, '+str(tarTpinpos[taran])+')\n'
    resut={}

    resut.update({'btempo': btempo })
    resut.update({'ftempo': ftempo })
    resut.update({'cokas': cokas })
    resut.update({'cokey': cokey })
    resut.update({'targe': targe })
    resut.update({'pri': pri })
    resut.update({'des': des })
    resut.update({'karen': karen })
    resut.update({'sam': pintoSumsi })
    resut.update({'par': pinpecSumsi })
    resut.update({'kub': pinposSumsi })
    resut.update({'statik': statik })

    return resut

def atren(usrid,dicto):
    btempo=dicto.get('btempo')
    ftempo=dicto.get('ftempo')
    leve=dicto.get('leve')
    cokas=dicto.get('cokas')
    cokey=dicto.get('cokey')
    karatio = mmcdb.openKaratio()

    saita = mmcdb.openSetting(usrid)
    karen = saita['karen']
    lim = saita['screen'] -3

    libra = mmcdb.opendb(usrid)
    timon = mmcdb.timra(usrid,btempo,ftempo)
    makprin = 0.00
    rawdb = libra['raw']
    keydb = libra['key']
    fisTar = tool.uni(cokey[0])

    daTprinsum = {}
        # { datte : price'int'sum}
    prinsumTdaset = {}
        # { price'int'sum : [datte]}
    daTprinset = {}
        # { datte : [price'int'indi]}
    prinTdaset = {}
        # { price'int'indi : [datte] }
    lenprinsetTdaset = {}
        # { len([price'int'indi]) : [datte] }
    daTprinpos = {}
        # { datte : (price'int'sum)/makprin*lim}
    diaTda = {}
        # { num : datte}

    for uuid in timon:
        datte = rawdb[uuid]['datte'][0:leve]
        if rawdb[uuid][cokas] == cokey:
            if libra['raw'][uuid]['karen'] == karen:
                price = round(float(libra['raw'][uuid]['price']),2)
            else:
                rate = float(karatio[libra['raw'][uuid]['karen']+karen])
                price = round(float(libra['raw'][uuid]['price']) * rate,2)

            prinsum = daTprinsum.get(datte,0)
            prinsum = round(prinsum + price,2)
            daTprinsum.update( { datte : prinsum } )

            prinset = daTprinset.get(datte,[])
            prinset.append(str(price))
            daTprinset.update( { datte : prinset } )

            daset = prinTdaset.get(price,[])
            daset.append(datte)
            prinTdaset.update( { price : daset } )

            if prinsum > makprin:
                makprin = prinsum
        else:
            prinsum = daTprinsum.get(datte,0)
            daTprinsum.update( { datte : prinsum } )

            prinset = daTprinset.get(datte,[])
            daTprinset.update( { datte : prinset } )

    print('daTprinsum : '+pprint.pformat(daTprinsum,compact=True))
    print('daTprinset : '+pprint.pformat(daTprinset,compact=True))
    print('prinTdaset : '+pprint.pformat(prinTdaset,compact=True))
    das = sorted(daTprinsum)
    print('das : '+pprint.pformat(das,compact=True))
    if round(makprin,2) == 0.00:
        return {'graf':['No Data','Maybe using wrong combination']}
    makprin = round(makprin,2)
    print('makprin : '+pprint.pformat(makprin))
    dia = 1
    for da in das:
        prinpos = round((daTprinsum.get(da,0) / makprin) * lim)
        daTprinpos.update( { da : prinpos } )
        diaTda.update( { dia : da } )
        dia = dia + 1

    print('daTprinpos : '+pprint.pformat(daTprinpos,compact=True))
    print('diaTda : '+pprint.pformat(diaTda,compact=True))

    # x against y
    nugra = len(tool.uni(str(sorted(diaTda)[-1])))
    print('nugra : '+pprint.pformat(nugra))

    graf = []
    for dia in sorted(diaTda):
        da = diaTda.get(dia)
        prinpos = daTprinpos.get(da,0)
        unidia = tool.uni(str(dia))
        if len(unidia) < nugra:
            unidia = ('　' * (nugra-len(unidia))) + unidia
        lina = unidia + '｜' + (fisTar * prinpos)# + ' ' + str(daTprinsum.get(m))
        graf.append(lina)

    desta=[]
    for dia in sorted(diaTda):
        unidia = tool.uni(str(dia))
        if len(unidia) < nugra:
            unidia = ('　' * (nugra-len(unidia))) + unidia
        da = diaTda.get(dia)
        prinsuka = karen+' '+str(round(daTprinsum.get(da),2))
        prinsefo = pprint.pformat(daTprinset.get(da))#.replace('[','').replace(']','').replace('\'','')
        desta.append(unidia+'：')
        desta.append('　'*(nugra-1) + da )
        desta.append('　'*(nugra-1) + prinsuka + '\n' )
        #desta.append('　'+ofe)
    des='\n'.join(desta)

    prinsum = [x for x in list(daTprinsum.values())]
    prinsuSum = round(sum(prinsum),2)
    prinsumVa = round(prinsuSum/len(prinsum),2)
    firinsu = [x for x in list(daTprinsum.values()) if abs(x - np.mean(prinsum)) <= (np.std(prinsum)*1)]
    firinsuSum = round(sum(firinsu),2)
    firinsumVa = round(firinsuSum/len(firinsu),2)

    statik = {}
    for da in daTprinsum.keys():
        prinsum = daTprinsum.get(da)
        daset = prinsumTdaset.get(prinsum,[])
        daset.append(da)
        prinsumTdaset.update( { prinsum : daset } )
    print('prinsumTdaset : '+pprint.pformat(prinsumTdaset, compact=True))

    for da in daTprinset.keys():
        lenprinset = len(daTprinset.get(da))
        daset = lenprinsetTdaset.get(lenprinset,[])
        daset.append(da)
        lenprinsetTdaset.update( { lenprinset : daset } )
    print('lenprinsetTdaset : '+pprint.pformat(lenprinsetTdaset, compact=True))

    prinset = sorted(prinTdaset)
    statik.update({ 'sinMax' : pprint.pformat( set( prinTdaset.get( prinset[-1],'' ) ) ).replace('}, {',' ; ').replace('{','').replace('}','') })
    statik.update({ 'sinMaxPc' : str(prinset[-1]) })
    statik.update({ 'sinMin' : pprint.pformat( set( prinTdaset.get( prinset[0],'' ) ) ).replace('}, {',' ; ').replace('{','').replace('}','') })
    statik.update({ 'sinMinPc' : str(prinset[0]) })

    prinsumSet = sorted(prinsumTdaset)
    oveMaxDat=''
    for daf in prinsumTdaset.get( prinsumSet[-1],[''] ):
        oveMaxDat = oveMaxDat+'－'+daf+' '+pprint.pformat(daTprinset.get(daf),compact=True).replace('[','（').replace(']','）')+'\n'
    statik.update({ 'oveMaxPc' : str(prinsumSet[-1]) })
    statik.update({ 'oveMaxDat' : oveMaxDat })

    oveMinDat=''
    if prinsumSet[0] != 0:
        mino = prinsumSet[0]
    else:
        try:
            mino = prinsumSet[1]
        except KeyError:
            mino = prinsumSet[0]
    for daf in prinsumTdaset.get( mino,[''] ):
        oveMinDat = oveMinDat+'－'+daf+' '+pprint.pformat(daTprinset.get(daf),compact=True).replace('[','（').replace(']','）')+'\n'
    statik.update({ 'oveMinPc' : str(mino) })
    statik.update({ 'oveMinDat' : oveMinDat })

    lenprinseSet = sorted(lenprinsetTdaset)
    modeDat=''
    for daf in lenprinsetTdaset.get(lenprinseSet[-1],''):
        modeDat = modeDat+'－'+daf+' '+karen+' '+pprint.pformat(daTprinsum.get(daf),compact=True).replace('[','').replace(']','')+'\n'
        modeDat = modeDat+'　'+pprint.pformat(daTprinset.get(daf),compact=True).replace('[','（').replace(']','）')+'\n'
    statik.update({ 'time' : str(lenprinseSet[-1]) })
    statik.update({ 'modeDat' : modeDat })

    resut={}

    resut.update({'btempo': btempo })
    resut.update({'ftempo': ftempo })
    resut.update({'cokas': cokas })
    resut.update({'cokey': cokey })
    resut.update({'graf': graf })
    resut.update({'des': des })
    resut.update({'karen': karen })
    resut.update({'sam': prinsuSum })
    resut.update({'vam': prinsumVa })
    resut.update({'san': firinsuSum })
    resut.update({'van': firinsumVa })
    resut.update({'statik': statik })

    return resut

def akaun(usrid,dicto):
    libra = mmcdb.opendb(usrid)
    rawdb = libra.get('raw',{})
    keydb = libra.get('key',{})
    rslib = {} # rs = result

    karatio = mmcdb.openKaratio()
    saita = mmcdb.openSetting(usrid)
    karen = saita.get('karen','')

    btempo = dicto.get('btempo')
    ftempo = dicto.get('ftempo')
    rslib.update({ 'btempo' : btempo })
    rslib.update({ 'ftempo' : ftempo })

    acuno = dicto.get('acuno','')
    rslib.update({ 'acuno' : acuno })
    cokas = dicto.get('cokas','')
    rslib.update({ 'cokas' : cokas })
    balan = float(dicto.get('balan','0.0'))

    idsrc = [] # uuid set (related with cokas)
    tiset = mmcdb.timra(usrid,btempo,ftempo) # uuid set (related with tempo)
    coset = [] # cokey set
    transle = mmcDefauV.keywo('transle')

    if acuno in keydb.get('fromm',{}).keys():
        print(acuno + ' in fromm')
        idsrc.extend(keydb.get('fromm',{}).get(acuno,[]))

    if acuno in keydb.get('toooo',{}).keys():
        print(acuno + ' in toooo')
        idsrc.extend(keydb.get('toooo',{}).get(acuno,[]))

    idset = sorted(list( set(idsrc) - ( set(idsrc)-set(tiset) )))
    # uuid set ( final )

    uilib = {} # ui = uuid
    colib = {} # co = cokey
    folib = {} # fo = fromm
    tolib = {} # to = toooo
    inval = 0.0
    outva = 0.0

    for uuid in idset:
        idlib = rawdb.get(uuid,{})
        fromm = ''
        toooo = ''

        if idlib.get('fromm','') == acuno :

            if idlib.get('karen','') == karen:
                price = round(float(idlib.get('price','')),2)
            else:
                kaset = idlib.get('karen','')+karen
                rate = float(karatio[kaset])
                price = round((float(idlib.get('price','')) * rate),2)

            fromm = tool.roundostr(price)
            outva = outva + price

        elif idlib.get('toooo','') == acuno :

            if idlib.get('tkare','') == karen:
                price = round(float(idlib.get('tpric','')),2)
            else:
                kaset = idlib.get('tkare','')+karen
                rate = float(karatio[kaset])
                price = round((float(idlib.get('tpric','')) * rate),2)

            toooo = tool.roundostr(price)
            inval = inval + price

        cokey = idlib.get(cokas,'')

        if cokey not in coset:
            uilib.update({ uuid : cokey })
            coset.append(cokey)

        mdlis = colib.get(cokey,[])
        mdlis.append(uuid)
        colib.update({ cokey : mdlis })

        mdlis = folib.get(cokey,[])
        mdlis.append(fromm)
        folib.update({ cokey : mdlis })

        mdlis = tolib.get(cokey,[])
        mdlis.append(toooo)
        tolib.update({ cokey : mdlis })

    pebal = balan - inval + outva
    pesum = tool.roundostr(pebal)
    otsum = tool.roundostr(outva)
    insum = tool.roundostr(inval)
    basum = tool.roundostr(balan)
    rslib.update({ 'otsum' : otsum })
    rslib.update({ 'insum' : insum })
    rslib.update({ 'basum' : basum })

    rslib.update({ 'uilib' : uilib })
    rslib.update({ 'colib' : colib })
    rslib.update({ 'folib' : folib })
    rslib.update({ 'tolib' : tolib })

    nummo = 0
    pilib = {} # pi = price
    lelib = {'nummo':0, 'tosum':0, 'fosum':0, 'cokey':0}

    for uuid in uilib.keys():
        nummo = nummo + 1
        cokey = uilib.get(uuid,'')

        foset = [float(x) for x in folib.get(cokey) if x != '']
        if sum(foset) != 0.0:
            fosum = tool.roundostr(sum(foset))
        else:
            fosum = ''

        toset = [float(x) for x in tolib.get(cokey) if x != '']
        if sum(toset) != 0.0:
            tosum = tool.roundostr(sum(toset))
        else:
            tosum = ''

        mdlib = {
            'cokey' : cokey,
            'fosum' : fosum,
            'tosum' : tosum,
        }
        pilib.update({ nummo : mdlib })

        for keyo in mdlib.keys():
            if len(mdlib.get(keyo,'')) > lelib.get(keyo,0):
                lelib.update({ keyo : len(mdlib.get(keyo,'')) })

        for sumwo,sumke in [['tosum',insum],['fosum',otsum]]:
            if len(sumke) > lelib.get(sumwo,0):
                lelib.update({ sumwo : len(sumke) })

        lelib.update({ 'nummo' : len(str(nummo))})

    rslib.update({ 'lelib' : lelib })
    rslib.update({ 'pilib' : pilib })

    pides = '' # pi = price

    lingua = mmcdb.openSetting(usrid).get('lingua')
    transle = mmcDefauV.keywo('transle',lingua=lingua)
    namcokas = transle.get(cokas,'')

    a = '　'*lelib.get('nummo',0)
    b = round((lelib.get('tosum',0) - 2)/2)
    bb = '　'*b
    c = '　'*(lelib.get('tosum',0) - 2 - b)
    d = round((lelib.get('fosum',0) - 3)/2)
    dd = '　'*d
    e = lelib.get('fosum',0) - 3 - d

    f = a +'　'+bb+'ＩＮ'+c+'　'+dd+'ＯＵＴ'
    g = len(f)+e
    pides = f + '\n' + '—'*g + '\n'

    for nummo in sorted(list(pilib.keys())):
        fosum = pilib.get(nummo,{}).get('fosum')
        tosum = pilib.get(nummo,{}).get('tosum')

        if len(str(nummo)) < lelib.get('nummo',0):
            a = '　'*(lelib.get('nummo',0) - len(str(nummo)))
        else:
            a = ''

        if len(tosum) < lelib.get('tosum',0):
            b = '　'*(lelib.get('tosum',0) - len(tosum))
        else:
            b = ''

        if len(fosum) < lelib.get('fosum',0):
            c = '　'*(lelib.get('fosum',0) - len(fosum))
        else:
            c = ''
        d = a + str(nummo) + '　'  + b + tosum + '　'  + c + fosum
        pides = pides + tool.uni(d) + '\n'

    pides = pides + '—'*g + '\n'

    a = '　'*lelib.get('nummo',0)

    if len(insum) < lelib.get('tosum',0):
        b = '　'*(lelib.get('tosum',0) - len(insum))
    else:
        b = ''

    if len(otsum) < lelib.get('fosum',0):
        c = '　'*(lelib.get('fosum',0) - len(otsum))
    else:
        c = ''

    e = a + '　'  + b + insum + '　'  + c + otsum
    pides = pides + tool.uni(e) + '\n'
    pides = pides + '—'*g + '\n' + f

    codes = '' # co = cokey

    for nummo in sorted(list(pilib.keys())):
        cokey = pilib.get(nummo,{}).get('cokey')

        if len(str(nummo)) < lelib.get('nummo',0):
            a = '　'*(lelib.get('nummo',0) - len(str(nummo)))
        else:
            a = ''

        d = a + str(nummo) + '：'
        codes = codes + tool.uni(d) + cokey + '\n'

    rslib.update({ 'pides' : pides })
    rslib.update({ 'codes' : codes })

    lefin = 0

    if lelib.get('fosum',0) > lelib.get('tosum',0):
        lefin = lelib.get('fosum',0)
    else:
        lefin = lelib.get('tosum',0)

    if len(basum) > lefin:
        lefin = len(basum)
    elif len(pesum) > lefin:
        lefin = len(pesum)

    blanc = '　'*lefin
    pefin = '　'*(lefin-len(pesum)) + tool.uni(pesum)
    infin = '　'*(lefin-len(insum)) + tool.uni(insum)
    otfin = '　'*(lefin-len(otsum)) + tool.uni(otsum)
    linec = '—'*lefin
    bafin = '　'*(lefin-len(basum)) + tool.uni(basum)

    rslib.update({ 'blanc' : blanc })
    rslib.update({ 'pefin' : pefin })
    rslib.update({ 'infin' : infin })
    rslib.update({ 'otfin' : otfin })
    rslib.update({ 'linec' : linec })
    rslib.update({ 'bafin' : bafin })

    return rslib

def listClass(keywo,lingua='enMY'):
    finno = ""
    skdic = mmcDefauV.keywo('transle',lingua=lingua)
    listo = sorted(list(mmcDefauV.keywo('temra')))
    for intta in listo:
        finno = finno + '/set_'+keywo+'_as_'+intta+'\n' +'＞　'+skdic.get(intta)+'\n\n'
    return finno

def check(keset):
    modda = keset.get('mode','')
    resut = False
    for keyo in mmcDefauV.keywo('staset').get(modda,[]):
        if keset.get(keyo,'') == '':
            resut = True
    return resut
