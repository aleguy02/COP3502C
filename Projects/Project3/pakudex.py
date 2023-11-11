class Pakudex:
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.size = 0
        self.species_array = []

    def get_size(self):
        return self.size

    def get_capacity(self):
        return self.capacity

    def get_species_array(self):  # gets a named list of species
        if self.size == 0:
            return None
        else:
            species_array_named = []
            for species_obj in self.species_array:
                species_array_named.append(species_obj.species)
            return species_array_named

    def get_stats(self, species_obj):
        if species_obj not in self.species_array:
            return None
        else:
            return [species_obj.attack, species_obj.defense, species_obj.speed]

    def sort_pakuri(self):  # least should be to the left, most should be to the right
        if len(self.species_array) > 0:
            species_name_list = self.get_species_array()
            species_name_list.sort()  # 2. order the speciesname list

            sorted_species_array = []
            # 3. reposition the object of species name to in species array to match the position of its name in the name list
            for species_name in species_name_list:
                for species_obj in self.species_array:
                    if species_obj.species == species_name:
                        sorted_species_array.append(species_obj)
            self.species_array = sorted_species_array

    def add_pakuri(self, species_obj: object):
        named_list = [] if self.get_species_array() is None else self.get_species_array()
        if self.size >= self.capacity:  # Don't add if the pakudex is full
            return False
        elif species_obj.species in named_list:  # Don't add if the pakudex already has this pokemon
            print('Error: Pakudex already contains this species!')
            return False
        else:                                # Add species to species array, increment pakudex size
            self.species_array.append(species_obj)
            self.size += 1
            print(f'Pakuri species {species_obj.get_species()} successfully added!')
            return True

    def evolve_species(self, species_obj: object):
        species_obj.evolve()
