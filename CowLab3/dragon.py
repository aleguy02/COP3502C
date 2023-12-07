from cow import Cow

class Dragon(Cow):
    def __init__(self, name, image):
        Cow.__init__(self, name)
        self.image = image

    def can_breathe_fire(self):
        if self.name == "dragon":
            return True
        elif self.name == "ice-dragon":
            return False
