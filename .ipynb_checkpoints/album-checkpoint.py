"""8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Use None to add an optional parameter to make_album() that allows you to
store the number of songs on an album. If the calling line includes a value for
the number of songs, add that value to the album’s dictionary. Make at least
one new function call that includes the number of songs on an album.
"""

# define a function called make_album(),take in artist name and an album title as arguments
def make_album(artist_name,album_title,num_songs = None):
    # contains dictionary for music album
    music_album = {
        'artist_name': artist_name,
        'title': album_title
    }
    # use an if conditon to add the value to the album's dictionary
    if num_songs :
        music_album['num_songs'] = num_songs
    return music_album
