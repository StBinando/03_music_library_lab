from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist
import repositories.artist_repository as artist_repository

def save(album):
    sql = f"INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    result = run_sql(sql, values)
    id = result[0]['id']
    album.id = id
    return album


def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    # for row in results:
    #     album = Album(row['title'], row['genre'], row['artist'], row['id'])
    #     albums.append(album)
    # return albums

    for row in results:
        artist = artist_repository.select_1_by_id(row['artist_id'])
        album = Album(row['title'], row['genre'], artist, row['id'] )
        albums.append(album)
    return albums 


def select_1_by_id(id):
    sql = f"SELECT * FROM albums where id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = artist_repository.select_1_by_id(result['artist_id'])
        album = Album(result['title'], result['genre'], artist, result['id'])
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def update_1_by_id(album):
    sql = "UPDATE albums SET (title, genre, artist_id) = (%s, %s, %s) WHERE id = %s"
    values = [album.title, album.genre, album.artist.id, album.id]
    run_sql(sql, values)

def delete_1_by_id(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)