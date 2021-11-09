import pdb

from models.artist import Artist

import repositories.artist_repository as artist_repository

# creates some artist objects from Artist class for tests
artist_1 = Artist("David Bowie")


# calls artist_repository SAVE
print(artist_1.id)
artist_repository.save(artist_1)
print(artist_1.id)

pdb.set_trace()