import pdb
from models.artist import Artist
from models.album import Album
from repositories import artist_repository
from repositories import album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist('Deftones')
artist_repository.save(artist_1)

artists = artist_repository.select_all()
for artist in artists:
    print(artist.__dict__)

album_1 = Album('Adrenaline', ' New Metal', artist_1)
album_repository.save(album_1)

album_2 = Album('Gore', 'New Metal', artist_1)
album_repository.save(album_2)

albums = album_repository.select_all()
for album in albums:
    print(album.__dict__)
