# create a list with 10 future clients for sparta
# access at least 4 clients with a nice sentence
# list_of_clients = ['MD PLC', 'Irrigation systems LTD', 'BO', 'Ireland enterprises', 'Earthport', 'Sparta global', 'Crown court justice', 'Google', 'direct line', 'home office']
#
# print(list_of_clients[0] + list_of_clients[1])
# print(f"{list_of_clients[3]} needs additional people and will require Adam to choose another person")
# print(f"{list_of_clients[1]} have pulled out the deal")
# print(f"{list_of_clients[8]} has failed to submit form 10J")
# print(list_of_clients[7] + ' ' + list_of_clients[2])
# print(f"We have had an issue with {list_of_clients[5]} and need to renegotiate contract")
# print(list_of_clients[9] + " have agreed to take 4 spartans")
# print(list_of_clients[1] + "has accepted 4 spartans :)" )
# print("There has been a merger between " + list_of_clients[3] + " and " + list_of_clients[1] + ", they require additional spartans ")

#part 2 create a hash / dictionary that contains a story
#it should have at least 3 sections
#print the story in an orderly fashion

story = {
    'beginning': "Once upon a time there was a DevOps class.",
    'middle': "They were having fun with python.",
    'end':"Then they all got placed to go to Ireland."
}
input1 = input('do you want to hear a story y/n > ')
if input1 == 'y':
    print(story['beginning'])
    input2 = input('do you want to continue y/n > ')
    if input2 == 'y':
        print(story['middle'])
        input3 = input('do you want to continue y/n > ')
        if input3 == 'y':
            print(story['end'])
        else:
            print("we'll finish later then")
    else:
        print("true it probably wasn't an overly long story")
else:
    print('very well, maybe another time')
