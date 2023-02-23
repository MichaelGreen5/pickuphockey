from pickuphockey.models import Invitation
#player data will be name and email from my_players list
active_host = 'Lauren.Ciccarelli'
current_event = 'Event at The Edge Bedford'
player_data = [ {'field1': 'value1', 'field2': 'value2'},
    {'field1': 'value3', 'field2': 'value4'},
    {'field1': 'value5', 'field2': 'value6'},]
def GenerateInvites(active_host, current_event, guest_contact):
    guest_data = [ {'field1': 'value1', 'field2': 'value2'},
    {'field1': 'value3', 'field2': 'value4'},
    {'field1': 'value5', 'field2': 'value6'},]

    for item in guest_data :
        instance = Invitation(**item)
        instance.save()



        