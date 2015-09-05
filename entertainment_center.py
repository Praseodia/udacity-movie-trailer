import media
import fresh_tomatoes
 
# Create a list of movies from media.py

m_avengers = media.Movie("The Avengers",
    "http://ia.media-imdb.com/images/M/MV5BMTk2NTI1MTU4N15BMl5BanBnXkFtZTcwODg0OTY0Nw@@._V1_SY317_CR0,0,214,317_AL_.jpg", 
    "https://www.youtube.com/watch?v=eOrNdBpGMv8",
    "2012",
    ['Robert Downey Jr.', 'Chris Evans'])
m_dragon = media.Movie("How to Train Your Dragon",
    "https://upload.wikimedia.org/wikipedia/en/9/99/How_to_Train_Your_Dragon_Poster.jpg",
    "https://www.youtube.com/watch?v=oKiYuIsPxYk",
    "2010",
    ['Jay Baruchel', 'Gerard Butler'])
m_insideout = media.Movie("Inside Out",
    "http://ia.media-imdb.com/images/M/MV5BOTgxMDQwMDk0OF5BMl5BanBnXkFtZTgwNjU5OTg2NDE@._V1_SX640_SY720_.jpg",
    "https://www.youtube.com/watch?v=seMwpP0yeu4",
    "2015",
    ['Amy Poehler', 'Phyllis Smith'])
movies = [m_avengers, m_dragon, m_insideout]

fresh_tomatoes.open_movies_page(movies)