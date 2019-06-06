def get_homeless(friendships, village):
    homeless = []
    for friend in friendships:
        if village.get_house(friend) == None:
            homeless.append(friend)
    return homeless

def get_house_choices(friendships, village):
    house_choices = {}
    for letter in friendships:
        house_choices[letter] = []
        
        friends = friendships.get_friends(letter)
        for friend in friends:
            friend_neighbours = village.get_neighbours(friend)

        