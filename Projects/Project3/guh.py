from pakuri import Pakuri
from pakudex import Pakudex

pakudex = Pakudex(4)

psygoose = Pakuri('PsyGoose')
pikachu = Pakuri('Pikachu')
chorizo = Pakuri('Chorizo')

pakudex.add_pakuri(psygoose)
pakudex.add_pakuri(pikachu)
pakudex.add_pakuri(chorizo)

print(pakudex.get_size(), '\n""')

# print(pakudex.get_species_array())
# pakudex.sort_pakuri()
# print('""')
#
# print(pakudex.get_species_array())
print(pakudex.get_stats(psygoose))
pakudex.evolve_species(psygoose)
print(pakudex.get_stats(psygoose))
