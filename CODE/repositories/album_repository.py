from db.run_sql import run_sql

from models.album import Album

def save(album):
    sql = f"INSERT INTO albums (title, genre, artist) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist]
    result = run_sql(sql, values)
    id = result[0]['id']
    album.id = id
    return album


def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        album = Album(row['title'], row['genre'], row['artist'], row['id'])
        albums.append(album)
    return albums 


def select_1_by_id(id):
    sql = f"SELECT * FROM albums where id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        album = Album(result['title'], result['genre'], result['artist'], result['id'])
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)
