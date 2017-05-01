import movie
import template

redemption = movie.Movie(
    "The Shawshank Redemption",
    "https://s-media-cache-ak0.pinimg.com/736x/93/fe/0f/93fe0ff5efd5812671803fb75a12e0b5.jpg",
    "https://www.youtube.com/watch?v=6hB3S9bIaco",
    "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
    )

dark_song = movie.Movie(
    "A Dark Song",
    "http://kaleidoscope-admin.piggy.co.uk/site/assets/files/1726/a_dark_song_one_sheet_approved.jpg",
    "https://www.youtube.com/watch?v=vvQ2ClKbRcU",
    "Drama: A determined young woman and a damaged occultist risk their lives and souls to perform a dangerous ritual that will grant them what they want."
    )

gump = movie.Movie(
    "Forrest Gump",
    "http://2.bp.blogspot.com/-i03dWHqsKuY/Ucw2YpUKlOI/AAAAAAAAAFQ/NqfUh7pHZZQ/s1456/forrest-gump-poster-1994-tom-hanks.png",
    "https://www.youtube.com/watch?v=uPIEn0M8su0",
    "Comedy: While not intelligent, Forrest Gump has accidentally been present at many historic moments, but his true love, Jenny Curran, eludes him."
    )

la_land = movie.Movie(
    "La La Land",
    "http://www.impawards.com/2016/posters/la_la_land_ver8_xxlg.jpg",
    "https://www.youtube.com/watch?v=0pdqf4P9MB8",
    "A jazz pianist falls for an aspiring actress in Los Angeles."
    )
    
# list of movies
movies=[redemption, dark_song, gump, la_land]
# render template with list of movies
template.open_movies_page(movies)
