from Friendships import Friendships
from house_choices import get_house_choices
from input import input1
from village import Village

village = Village(input1["village"])
friends = Friendships(input1["wordlist"])



village.show()

#homeless = get_homeless(friends, village)
#possible_houses = get_house_choices(friends, village)

