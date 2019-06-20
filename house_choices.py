def get_homeless(friendships, village):
    homeless = []
    for friend in friendships.get_people():
        if village.get_house(friend) == None:
            homeless.append(friend)
    return homeless

def get_house_choices(friendships, homeless, village):
    house_choices = {}
    for letter in homeless:
        houses = village.get_all_empty_houses()
        
        friends = friendships.get_friends(letter)
        for friend in friends:
            empty_neighbours = village.get_empty_neighbours(friend)
            houses = list(set(houses) & set(empty_neighbours))

        house_choices[letter] = houses
        
    return house_choices

def get_owner_choices(house_choices):
    owner_choices = {}
    for letter in house_choices:
        for house in house_choices[letter]:
            if house not in owner_choices:
                owner_choices[house] = set(letter)
            else:
                owner_choices[house].add(letter)
    
    return owner_choices

def go_shopping(village, possible_houses, possible_owners):
    for owner, houses in possible_houses.items():
        if len(houses) == 0:
            print("Owner " + owner + " has no possible house - something went wrong")
            exit()
        elif len(houses) == 1:
            village.buy_house(houses[0], owner)
    for house, owners in possible_owners.items():
        if len(owners) == 0:
            print("House " + house + " has no possible owner - something went wrong")
            exit()
        elif len(owners) == 1:
            village.buy_house(house, owners.pop())
