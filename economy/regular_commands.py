from economy import admin_commands as admin
import json

#! BALANCE


def get_balance(player):
    
    with open('economy_data.json') as eco_data:
        moneydata=json.load(eco_data)

        for line in moneydata:
            if line["name"]==player:
                return line["balance"]

    admin.create_account(player)

    with open('economy_data.json') as eco_data:
        moneydata=json.load(eco_data)

        for line in moneydata:
            if line["name"]==player:
                return line["balance"]
    

#! TRANSFER


def transfer_balance(from_player, to_player, amount):
    amount=int(amount)

    with open('economy_data.json') as eco_data:
        moneydata=json.load(eco_data)

        for line in moneydata:
            if line["name"]==from_player:
                if (line["balance"]-amount)<0:
                    return False
                
                else:
                    line["balance"]=line["balance"]-amount
                
                break

    with open('economy_data.json','w') as eco_data:
        json.dump(moneydata,eco_data,indent=4)
    
    with open('economy_data.json') as eco_data:
        moneydata=json.load(eco_data)

        for line in moneydata:
            if line["name"]==to_player:
                line["balance"]=amount+line["balance"]
                break
    
    with open('economy_data.json','w') as eco_data:
        json.dump(moneydata,eco_data,indent=4)