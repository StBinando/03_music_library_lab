import pdb
# from os???
from models.artist import Artist

import repositories.artist_repository as artist_repository

# creates some artist objects from Artist class for tests
artist_1 = Artist("David Bowie")
artist_2 = Artist("Dead Kennedys")
artist_3 = Artist("Nicola Conte")


# calls artist_repository SAVE -- 3 artists
artist_repository.save(artist_1)
artist_repository.save(artist_2)
artist_repository.save(artist_3)

# calls artist_repository SELECT ALL -- 3 artists
result = artist_repository.select_all()
for row in result:
    print(row.__dict__)

pdb.set_trace()