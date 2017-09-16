import os, time, random, subprocess, json
from subprocess import call
import toolHalfu

def diro(direc=''):
    call(['mkdir','-p',direc])

def date(modde=10,text='-:'):
    a,b,c,d,e,f,g,h,i = time.localtime(time.time())
    j=[]
    for n in [a,b,c,d,e,f]:
        j.append(str(n))
    for n in range(1,6):
        if len(j[n]) == 1 :
            j[n]="0"+j[n]
    if modde == 0 : # output: ["yyyy","mm","dd","hh","mm","ss"]
        return j
    elif modde == 1 : # output: "yyyy-mm-dd" if text = '-'
        return text[0].join(j[0:3])
    elif modde == 2 : # output: "yyyy-mm-dd hh:mm:ss" if text = '-:'
        return text[0].join(j[0:2])+" "+text[1].join(j[3:6])
    elif modde == 3 : # output: "yyyymmddhhmmss"
        return "".join(j)
    elif modde == 4 : # output: "yyyymmddhhmmssrrrrrrrr" rrrr is eight digit random number
        zero = '0000'
        numo = str(random.choice(range(0,10000)))
        return "".join(j)+zero[0:4-len(numo)]+numo
    elif modde == 5 : # output: "yyyy-mm-dd-hh" if text = '-'
        return text[0].join(j[0:4])
    elif modde == 6 : # output: "yyyy-mm" if text = '-'
        return text[0].join(j[0:2])
    elif modde == 10 : # output: yyyymmdd
        return  ''.join( j[0:3] )

def ckfile(usrdir,fille,addi='none'):
    try:
        alla = open(usrdir+'/'+fille,'br')
    except FileNotFoundError:
        temp=open(usrdir+'/'+fille,'w')
        if addi == 'json':
            json.dump({},temp)
        temp.close

def uni(keywo):
    rsstr = ''
    for keno in keywo:
        try:
            keno.encode('latin-1')
            rsstr = rsstr + toolHalfu.fullen(keno)
        except UnicodeEncodeError:
            rsstr = rsstr + keno
    return rsstr

def roundostr(numbe): # round() dos str
    numba = round(float(numbe),2)
    tamba = str(numba).split('.')
    tampa = ''
    if len(tamba[1]) != 2:
        tampa = '0'
    return str(numba)+tampa

def acedate(usrdir,modde,modda='check'):
    filla = modde + '.date'
    ckpath(usrdir,filla,addi='json')
    fillo = open(usrdir + '/' + filla,'r')
    recod = json.load(fillo)

    datte = recod.get('datte','00000000')

    if modda == 'write':
        recod.update({ 'datte' : date() })
        fillo = open(usrdir + '/' + filla,'w')
        json.dump(recod,fillo)
        fillo.close()

    return datte
