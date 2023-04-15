# 'Voodoo' is a terminal-focused, text-based-adventure game engine for python #
# It is currently being developed for use exclusively as a python package, but #
# the end vision is to have an intuitive, standalone text-based-adventure game creator #

# The 'Game' class holds all content relevant to game #
# functionality such as game objects and algorithms #
class Game:

    # The 'Entity' class is a non-descript object base class containing #
    # most functionality required for game objects #
    class Entity:
        def __init__(self,
                     name="",
                     parent=None,
                     children=None,
                     desc="",
                     can_take=False):

            # This is necessary due to lists being mutable #
            if children is None:
                children = []

            self.name = name
            self.parent = parent
            self.children = children
            self.desc = desc
            self.can_take = can_take

        # ToString just returns 'desc' #
        def __repr__(self):
            return self.desc

    # The 'Room' class is used to represent sections of space that #
    # are connected to one or more other sections of space #
    class Room(Entity):
        def __init__(self,
                     name,
                     parent,
                     children,
                     desc,
                     can_take,
                     connections=None):

            super().__init__(name, parent, children, desc, can_take)

            # This is necessary due to lists being mutable #
            if connections is None:
                connections = []

            self.connections = connections

        # ToString handled by ancestor #
        def __repr__(self):
            super().__repr__()

    # The 'Player' class represents the player character and is automatically #
    # given an 'inventory' attribute (empty list) #
    # ^^^ 'inventory' is purely conventional and may be deprecated in future updates ^^^ #
    class Player(Entity):

        # 'inventory' attribute may be deprecated in future updates #
        inventory = []

        def __init__(self,
                     name,
                     parent,
                     children,
                     desc,
                     can_take):

            super().__init__(name, parent, children, desc, can_take)

        # ToString handled by ancestor #
        def __repr__(self):
            super().__repr__()
