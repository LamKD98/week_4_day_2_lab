from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album
from repositories import artist_repository

def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    albums = run_sql(sql,values)
    id = albums[0]['id']
    album.id = id
    return album
    

def select_all():  
    albums = [] 

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist_id = row['artist_id']
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['title'], artist , row['genre'], row['id'])
        albums.append(album)
    return albums 

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

