class song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = song(["happy birthday to you",
                  "i don't want to get sued",
                  "so I'll stop right there"])            

bulls_on_parade = song(["The rally around tha family",
                       "with pocket full of shells"])

happy_bday.sing_me_a_song()                                         

bulls_on_parade.sing_me_a_song()