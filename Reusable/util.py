from friend.models import BuddyList


default_weekdays = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
def turn_QuerySet_to_Json(querySet):


    jsonData = []
    for set in querySet:
        jsonData.append(set)
        
    return jsonData