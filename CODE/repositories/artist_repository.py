from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album

def save(artist):
    sql = f"INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    result = run_sql(sql, values)
    id = result[0]['id']
    artist.id = id
    return artist


def select_all():
    artists = []

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['name'], row['id'])
        artists.append(artist)
    return artists 


def select_1_by_id(id):
    sql = f"SELECT * FROM artists where id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = Artist(result['name'], result['id'])
    return artist

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def list_albums_by_artist(artist):
    albums = []
    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist.id]
    results = run_sql(sql, values)
    for row in results:
        album = Album(row['title'], row['genre'], artist, row['id'])
        albums.append(album)
    return albums