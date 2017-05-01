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

ali_nino = movie.Movie(
    "Ali and Nino",
    "https://trailers.apple.com/trailers/ifcfilms/ali-and-nino/images/poster-large.jpg?lastmod=1",
    "https://www.youtube.com/watch?v=m8-Imlxsqhc",
    "Drama/Romance: Love story of a Muslim Azerbaijani boy and Christian Georgian girl in Baku from 1918 to 1920."
    )
    
assassins = movie.Movie(
    "Assassins Creed",
    "http://cdn2-www.comingsoon.net/assets/uploads/gallery/assassins-creed-movie/asscreedinternational.jpg",
    "https://www.youtube.com/watch?v=4haJD6W136c",
    "When Callum Lynch explores the memories of his ancestor Aguilar and gains the skills of a Master Assassin,"
    +"he discovers he is a descendant of the secret Assassins society."
    )
    
# list of movies
movies=[redemption, dark_song, gump, la_land, ali_nino, assassins]
# render template with list of movies
template.open_movies_page(movies)
