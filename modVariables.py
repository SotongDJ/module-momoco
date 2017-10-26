def keywo(text,lingua='enMY'):
    resut = {}
    genar = {
        'sf' : {
            "dt":"datte",
            "nm":"namma", "kl":"klass", "sh":"shoop",
            "fr":"fromm", "pr":"price", "kr":"karen",
            "to":"toooo", "tp":"tpric", "tk":"tkare",

            "in":"dinco", "ex":"dexpe",
            "gi":"genis", "oe":"ovede",
            "tf":"tanfe", "ic":"incom",
        },
        'fs' : {
            "datte":"dt",
            "namma":"nm", "klass":"kl", "shoop":"sh",
            "fromm":"fr", "price":"pr", "karen":"kr",
            "toooo":"to", "tpric":"tp", "tkare":"tk",

            "dinco":"in", "dexpe":"ex",
            "genis":"gi", "ovede":"oe",
            "tanfe":"tf", "incom":"ic",
        },
        'klass' : {
            'Acc':['fr','to','in','ex','gi','oe'],
            'Kas':['kl','tf','ic'],
            'Ken':['kr','tk'],
            'Pis':['pr','tp'],
        },
        'lingua':['enMY','hanT'],
        'leve':{
            10:'Day',
            7:'Month',
            4:'Year',
            'Day':10,
            'Month':7,
            'Year':4,
        },
        'recset':['namma', 'klass', 'shoop', 'price'],
        'staset':{
            'abratio':['dtempo','utempo','cokey','cokas','targe'],
            'atren':['dtempo','utempo','cokey','cokas','leve'],
            'akaun':['dtempo','utempo','cokas','acuno','balan'],
            'sachi':['dtempo','utempo','keywo']
        }
    }
    woood = {
        'enMY' : {
            'transle' : {
                "datte":"Date",
                "namma":"Item/Remind", "shoop":"Seller/Agent",
                'aconu':'Account','fromm':'Account[General/From]','toooo':'Account[To]',
                'dinco':'Account[income]','dexpe':'Account[expense]',
                'genis':'Account[G.I.S.]','ovede':'Account[O.E.D.]',
                'klass':'Category','tanfe':'Category','incom':'Category',
                'karen':'Currency[General/From]','tkare':'Currency[To]',
                'price':'Price[General/From]','tpric':'Price[To]',
                'cokas':'Top Class (Set)', 'cokey':'Class (Object)',
                'targe':'Target Class', 'desci':'Description',
                'lingua':'Language',
                'Day':'Day',
                'Month':'Month',
                'Year':'Year',
            },
        },
        'hanT' : {
            'transle' : {
                "datte":"日期",
                "namma":"品名／品項", "shoop":"商家／中介",
                'aconu':'賬戶','fromm':'賬戶［通用/來源］','toooo':'賬戶［目標］',
                'dinco':'賬戶［收入］','dexpe':'賬戶［支出］',
                'genis':'收入賬戶［分析］','ovede':'支出賬戶［分析］',
                'klass':'收支類型','tanfe':'轉賬名目［收支類型］','incom':'收入名目［收支類型］',
                'karen':'幣種［通用/來源］','tkare':'幣種［目標］',
                'price':'價格［通用/來源］','tpric':'價格［目標］',
                'cokas':'類型［集合］', 'cokey':'類別［物件］',
                'targe':'類型［目標］', 'desci':'明細',
                'lingua':'語言',
                'Day':'天數',
                'Month':'月數',
                'Year':'年數',
            },
        },
    }
    if text in genar.keys():
        resut = genar.get(text,{})
    elif text in woood[lingua].keys():
        resut = woood[lingua].get(text,{})
    return resut

class Argo:
    def __init__(self):
        super(Argo, self).__init__()
        self.usrdir = ''
        self.primo = []
        self.submo = ''
        self.keywo = ''
        self.kasso = ''
        self.recom = {}

        #'rawdb' : {},
        #'keydb' : {},
        #'karat' : {},

        self.veces = 0

        self.setti = {
            'dinco':'Bank', 'dexpe':'Cash',
            'genis':'Income', 'ovede':'Expense',
            'tanfe':'Transfer', 'incom':'Income',
            'karen':'MYR',
            'defSettWarn':0,
            'screen':13,
            'limit':'',
            'krset':{},
            'lingua':'enMY',
            'natio':'',
        }
        self.temra = {
            "datte":"",
            "namma":"", "klass":"", "shoop":"",
            "fromm":"", "price":"", "karen":"",
            "toooo":"", "tpric":"", "tkare":"",
            "desci":"",
        }
        self.stati = {
            'mode':'',
            'leve':10,
            'dtempo':'','utempo':'',
            'cokas':'','cokey':'',
            'targe':'','keywo':'',
            'acuno':'','balan':'0',
        }
        self.listi = {
            'datte': '',
            'uuid' : '',
        }

        self.catid = 0
        self.catyp = ''
        self.cotyp = ''
