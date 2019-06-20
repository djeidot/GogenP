from Friendships import Friendships
from house_choices import get_house_choices, get_homeless, get_owner_choices, go_shopping
from input import input1, input2
from village import Village

def init_game(input):
    village = Village(input["village"])
    friendships = Friendships(input["wordlist"])
    return village, friendships

village, friendships = init_game(input2)

iter = 1
print("Iter " + str(iter))
village.show()

homeless = get_homeless(friendships, village)
oldlenhomeless = len(homeless) + 1

while len(homeless) > 0 and len(homeless) < oldlenhomeless:
    oldlenhomeless = len(homeless)
    possible_houses = get_house_choices(friendships, homeless, village)
    possible_owners = get_owner_choices(possible_houses)
    
    # print("Homeless: " + str(homeless))
    # print("Possible houses: " + str(possible_houses))
    # print("Possible owners: " + str(possible_owners))

    go_shopping(village, possible_houses, possible_owners)

    iter = iter + 1
    print("\nIter: "+ str(iter))
    village.show()
    homeless = get_homeless(friendships, village)

print()
if len(homeless) == 0:
    print("Solved")
else:
    print("Can't solve any further")
    print("Homeless: " + str(homeless))
    print("Possible houses: " + str(possible_houses))
    print("Possible owners: " + str(possible_owners))
