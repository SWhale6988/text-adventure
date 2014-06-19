def declarerooms():
    entrancegate = ['Entrance Gate','An open area which has a large gate that can let people in and out of the castle']
    weaponsroom = ['Weapons Room','A small room stocked with weapons of all kinds']
    mainhall = ['Main Hall','A large open hall with several passages leading off']
    throneroom = ['Throne Room','A long and brightly lit room with a currently empty throne']
    nebattlements = ['North East Battlement','A battlement looking over the sea']                    #Defines Room Information
    sebattlements = ['South East Battlement','A battlement looking over a small jungle']  
    swbattlements = ['South West Battlement','A battlement looking over vast plains']
    nwbattlements = ['North West Battlement','A battlement looking over some farmland']
    northcorridoor = ['North Corridoor','A busy corridoor leading to the north battlements']
    southcorridoor = ['South Corridoor','A quiet corridoor leading to the south battlements']
    castletown = ['Castle Town','A trading town overlooked by the castle']


    #locations

    entrancegate.append([mainhall,southcorridoor,castletown])
    weaponsroom.append([mainhall,northcorridoor])
    mainhall.append([weaponsroom,entrancegate,northcorridoor,southcorridoor,throneroom])
    throneroom.append([mainhall])
    nebattlements.append([northcorridoor])
    sebattlements.append([southcorridoor])                       #defines room options
    swbattlements.append([southcorridoor])
    nwbattlements.append([northcorridoor])
    northcorridoor.append([nebattlements,nwbattlements,weaponsroom,mainhall])
    southcorridoor.append([swbattlements,sebattlements,entrancegate,mainhall])
    castletown.append([entrancegate])

    rooms = {"entrancegate": entrancegate,
             "weaponsroom": weaponsroom,
             "mainhall": mainhall,
             "throneroom": throneroom,
             "nebattlements": nebattlements,
             "sebattlements": sebattlements,
             "swbattlements": swbattlements,
             "nwbattlements": nwbattlements,
             "northcorridoor": northcorridoor,
             "southcorridoor": southcorridoor,
             "castletown": castletown,}
    return rooms
