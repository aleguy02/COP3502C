from cow import Cow
import os

class FileCow(Cow):
    def __init__(self, name, filename):
        super().__init__(name)
        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                lines = f.read()
                self.image = lines
        else:
            raise RuntimeError('MOOOOO!!!!!!')

    def set_image(self, image):
        raise RuntimeError('Cannot reset FileCow Image')