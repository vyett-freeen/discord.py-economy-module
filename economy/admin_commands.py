import json

#! MONEY MANIPULATION


def addbal(amount,player):
    amount=int(amount)

    with open('economy_data.json') as eco_data:
        moneydata=json.load(eco_data)

        for line in moneydata:
            if line["name"]==player:
                line["balance"]=amount+line["balance"]
                break
    
    with open('economy_data.json','w') as eco_data:
        json.dump(moneydata,eco_data,indent=4)


def removebal(amount,player):
    amount=int(amount)

    with open('economy_data.json') as eco_data:
        moneydata=json.load(eco_data)

        for line in moneydata:
            if line["name"]==player:
                if (line["balance"]-amount)<0:
                    return False
                
                else:
                    line["balance"]=line["balance"]-amount
                
                break
    with open('economy_data.json','w') as eco_data:
        json.dump(moneydata,eco_data,indent=4)


#! ACCOUNT CREATION


def create_account(player):
    with open('economy_data.json') as eco_data:
        moneydata=json.load(eco_data)

        new_account={
            "name": player,
            "balance": 0
        }
    moneydata.append(new_account)
    with open('economy_data.json','w') as eco_data:
        json.dump(moneydata,eco_data,indent=4)