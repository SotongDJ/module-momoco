class MsgSetti:
    def main(self,setti):
        """will replace by Start Card after finished Account Card and Currency Card"""
        if self.lingua == "enMY":
            final = """Setting Card
——————————
Account:
　Default Income: """+setti.get('dinco',"____")+"""
　Default Expense: """+setti.get('dexpe',"____")+"""
　General Income Source: """+setti.get('genis',"____")+"""
　Overall Expense Destination: """+setti.get('ovede',"____")+"""
　　——————　　
Category:
　Default Income: """+setti.get('tanfe',"____")+"""
　Default Transfer: """+setti.get('incom',"____")+"""
　　　——————　　
Curency:
　Default Currency: """+setti.get('karen',"____")+"""
　　　——————　　
Language:
　Default Language: """+setti.get('lingua',"____")+"""
——————————
　/modify_Setting　/whats_now
Remind:
　Use whats_now to check status of current work
"""
            return final

        elif self.lingua == "hanT":
            final = """Setting Card
——————————
Account:
　Default Income: """+setti.get('dinco',"____")+"""
　Default Expense: """+setti.get('dexpe',"____")+"""
　General Income Source: """+setti.get('genis',"____")+"""
　Overall Expense Destination: """+setti.get('ovede',"____")+"""
　　——————　　
Category:
　Default Income: """+setti.get('tanfe',"____")+"""
　Default Transfer: """+setti.get('incom',"____")+"""
　　　——————　　
Curency:
　Default Currency: """+setti.get('karen',"____")+"""
　　　——————　　
Language:
　Default Language: """+setti.get('lingua',"____")+"""
——————————
　/modify_Setting　/whats_now
Remind:
　Use whats_now to check status of current work
"""
            return final

    def warn():
        final="""
——————————
Normal Income:
　G.I.S. ---> Bank A , Category: Income
Normal Expense:
　Cash ---> O.E.D. , Category: Expense
Withdrawal:
　Bank A ---> Cash , Category: Transfer
Deposit:
　Cash ---> Bank A , Category: Transfer
Tranfer:
　Bank A ---> Bank B , Category: Transfer
——————————
Notes:
　Chatbot are using G.I.S. and O.E.D. for Analystic Purpose
"""
        return final

""" self.sender.sendMessage(mmcmsg.defSettList(self._setting)) """
    def lista(self,setti):
        """will replace by Start Card after finished Account Card and Currency Card"""
        if self.lingua == "enMY":
            final = """Account Setting Card
————— Account —————
Default Income: (E.g. Bank A)
　"""+setti.get('dinco',"____")+"""　/change_in
Default Expense: (E.g. Cash)
　"""+setti.get('dexpe',"____")+"""　/change_ex
　　——————　　
General Income Source:(E.g. "Income")
　"""+setti.get('genis',"____")+"""　/change_gi
Overall Expense Destination: (E.g. "Expense")
　"""+setti.get('ovede',"____")+"""　/change_oe
————— Category —————
Default Income:(E.g. "Income")
　"""+setti.get('incom',"____")+"""　/change_ic
Default Transfer:(E.g. "Transfer")
　"""+setti.get('tanfe',"____")+"""　/change_tf
————— Curency —————
Default Currency: (For Expense)
　"""+setti.get('karen',"____")+"""　/change_kr
————— Curency —————
Default Language:
　"""+setti.get('lingua',"____")+"""　/change_lingua
——————————
　/Discard　/Save　/Explain
Note:
　Changing setting now
"""
            return final
        elif self.lingua == "hanT":
            final = """Account Setting Card
————— Account —————
Default Income: (E.g. Bank A)
　"""+setti.get('dinco',"____")+"""　/change_in
Default Expense: (E.g. Cash)
　"""+setti.get('dexpe',"____")+"""　/change_ex
　　——————　　
General Income Source:(E.g. "Income")
　"""+setti.get('genis',"____")+"""　/change_gi
Overall Expense Destination: (E.g. "Expense")
　"""+setti.get('ovede',"____")+"""　/change_oe
————— Category —————
Default Income:(E.g. "Income")
　"""+setti.get('incom',"____")+"""　/change_ic
Default Transfer:(E.g. "Transfer")
　"""+setti.get('tanfe',"____")+"""　/change_tf
————— Curency —————
Default Currency: (For Expense)
　"""+setti.get('karen',"____")+"""　/change_kr
————— Curency —————
Default Language:
　"""+setti.get('lingua',"____")+"""　/change_lingua
——————————
　/Discard　/Save　/Explain
Note:
　Changing setting now
"""
            return final

    def setup(self,keywo,teksi):
        if self.lingua == "enMY":
            final = """Select Position
——————————
Keyword: """+keywo+"""
　　——————　　
Account:
　Default Income
　( /set_as_dinco )
　Default Expense
　( /set_as_dexpe )
　General Income Source
　( /set_as_genis )
　Overall Expense Destination
　( /set_as_ovede )
　　——————　　
Category:
　Default Income
　( /set_as_incom )
　Default Transfer
　( /set_as_tanfe )
　　——————　　
Curency:
　Default Currency
　( /set_as_karen )
——————————
　/Discard　/Save　/Back
"""
            return final

        elif self.lingua == "hanT":
            final = """Select Position
——————————
Keyword: """+keywo+"""
　　——————　　
Account:
　Default Income
　( /set_as_dinco )
　Default Expense
　( /set_as_dexpe )
　General Income Source
　( /set_as_genis )
　Overall Expense Destination
　( /set_as_ovede )
　　——————　　
Category:
　Default Income
　( /set_as_incom )
　Default Transfer
　( /set_as_tanfe )
　　——————　　
Curency:
　Default Currency
　( /set_as_karen )
——————————
　/Discard　/Save　/Back
"""
            return final

    def fins(setting):
        if self.lingua == "enMY":
            final = """Account Setting #Saved
——————————
Default Income: """+setti.get('dinco',"____")+"""
Default Expense: """+setti.get('dexpe',"____")+"""
General Income Source: """+setti.get('genis',"____")+"""
Overall Expense Destination: """+setti.get('ovede',"____")+"""
　　——————　　
Default Income: """+setti.get('tanfe',"____")+"""
Default Transfer: """+setti.get('incom',"____")+"""
　　——————　　
Default Currency: """+setti.get('karen',"____")+"""
　　——————　　
Default Language: """+setti.get('lingua',"____")+"""
——————————
　/setting　/help　/whats_now
Note:
　Changing setting now
"""
            return final

        elif self.lingua == "enMY":
            final = """Account Setting #Saved
——————————
Default Income: """+setti.get('dinco',"____")+"""
Default Expense: """+setti.get('dexpe',"____")+"""
General Income Source: """+setti.get('genis',"____")+"""
Overall Expense Destination: """+setti.get('ovede',"____")+"""
　　——————　　
Default Income: """+setti.get('tanfe',"____")+"""
Default Transfer: """+setti.get('incom',"____")+"""
　　——————　　
Default Currency: """+setti.get('karen',"____")+"""
　　——————　　
Default Language: """+setti.get('lingua',"____")+"""
——————————
　/setting　/help　/whats_now
Note:
　Changing setting now
"""
            return final

""" self.sender.sendMessage(mmcmsg.defSettDis()) """
def discard():
    final="""¡ Discard !
——————————

　Closed Account Setting Card

——————————
　/whats_now　/setting　/help
"""
    return final
