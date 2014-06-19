#format [Name,Description,startlocation,endlocation,reward]
from items import declareitems
from rooms import declarerooms
rooms = declarerooms()
items = declareitems()
def declarequests(items,rooms):
    quests = [ ["Get a sword","Get a sword from the weapons master","Null",rooms["weaponsroom"],items["Training Sword"]]  ]
    return quests
