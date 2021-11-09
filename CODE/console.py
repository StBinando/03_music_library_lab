import pdb
# from os???
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository




# --------------------------------------------------
# -------------- TEST FOR ARTISTS ------------------
# --------------------------------------------------

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
print("ALL ARTISTS--------------------------")
for row in result:
    print(row.__dict__)


# calls artist_repository SELECT 1 by id
result = artist_repository.select_1_by_id(1)
print("ARTIST id = 1 --------------------------")
print(result.__dict__)


# calls artist_repository DELETE ALL
# artist_repository.delete_all()
# result = artist_repository.select_all()
# print("ALL ARTISTS (after DELETE ALL)------------------")
# for row in result:
#     print(row.__dict__)



# --------------------------------------------------
# -------------- TEST FOR ALBULMS ------------------
# --------------------------------------------------

# creates some albums objects from Album class for tests
album_1 = Album("Hunky Dory", "Pop Rock", artist_1)
album_2 = Album("The Rise and Fall of Ziggy Stardust and the Spiders from Mars", "Glam Rock", artist_1)
album_3 = Album("Fresh Fruit for Rotting Vegetables", "Hardcore Punk", artist_2)
album_4 = Album("Plastic Surgery Disasters", "Hardcore Punk", artist_2)
album_5 = Album('"Heroes"', "Experimental Rock", artist_1)
album_6 = Album("1. Outside (The Nathan Adler Diaries: A Hyper-cycle)", "Industrial Rock", artist_1)
album_7 = Album("Other Directions", "Jazz", artist_3)
album_8 = Album("The Next Day", "Rock", artist_1)
album_9 = Album("Bedtime for Democracy", "Hardcore Punk", artist_2)


# calls album_repository SAVE -- 9 albums
album_repository.save(album_1)
album_repository.save(album_2)
album_repository.save(album_3)
album_repository.save(album_4)
album_repository.save(album_5)
album_repository.save(album_6)
album_repository.save(album_7)
album_repository.save(album_8)
album_repository.save(album_9)


# calls album_repository SELECT ALL -- 9 albums
result = album_repository.select_all()
print("ALL ALBUMS--------------------------")
for row in result:
    print(row.__dict__)


# calls album_repository SELECT 1 by id
result = album_repository.select_1_by_id(1)
print("ALBUM id = 1 --------------------------")
print(result.__dict__)


# calls album_repository DELETE ALL
# album_repository.delete_all()
# result = album_repository.select_all()
# print("ALL ALBUMS (after DELETE ALL)------------------")
# for row in result:
#     print(row.__dict__)







pdb.set_trace()