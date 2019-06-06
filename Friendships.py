class Friendships:

    def __init__(self, wordlist):
        self._build_connections(wordlist)
    
    def _build_connections(self, wordlist):
        self.friendships = {}

        for word in wordlist:
            prev = ''
            for letter in word:
                self._add_connection(letter, prev)
                prev = letter

    def _add_connection(self, letter, prev):
        if letter not in self.friendships:
            self.friendships[letter] = set()

        if prev != '':
            self.friendships[letter].add(prev)
            self.friendships[prev].add(letter)

    def get_friends(self, letter):
        return self.friendships[letter]