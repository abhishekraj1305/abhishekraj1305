class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
             The Gothons of Planet Percal #25 have invaded your ship and
             destroyed your entire crew. You are the last surviving
             member and your last mission is to get the neutron destruct
             bomb from the Weapons Armory, put it in the bridge, and
             blow the ship up after getting into an escape pod.

             you're running down the central corridor to the Weapons
             Armory when a Gothon jumps out, red scaly skin, dark grimy
             teeth, and evil clown costume flowing around his hate
             filled body. He's blocking the door to the Armory and
             about to pull a weapon to blast you.
             """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                  Quick on the draw you yank out your blaster and fire
                  it at the Gothon. His clown costume is flowing and
                  moving around his body, which throws off your aim.
                  Your laser hits his costume but misses him entirely.
                  This completely ruins his brand new costume his mother
                  bought him, which makes him fly into an insane rage
                  and blast you repeatedly in the face until you are
                  dead. Then he eats you.
                  """))
            return 'death'   

        elif action == "dodge!":
            print(dedent( """
                  Like a world class boxer you dodge, weave, slip and
                  past your head. In the middle of your artful dodge
                  your foot slips and you bang your head on the metal
                  wall and pass out. You wake up shortly after only to
                  die as the Gothon stomps on your head and eats you.
                  """))

            return 'death'

















