import fresh_tomatoes
import media

    # each movie will have four elements (title, plot, picture billboard, movie trailer)

toy_story = media.Movie("Toy Story",
                        "A story of a boy whom all of his toys come to life",
                        "http://img.lum.dolimg.com/v1/images/toy_story_that_time_forgot_keyart_300x450_fc2d5997.jpeg?region=0%2C0%2C300%2C450",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

Avatar=media.Movie("Avatar",
                   "a Marine in Pandora ",
                   "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
                   "https://www.youtube.com/watch?v=d1_JBMrrYw8")

Ironman=media.Movie("IRON MAN",
                    "ME IN THE FUTURE ",
                    "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
                    "https://www.youtube.com/watch?v=8hYlB38asDY")

central_intelligence= media.Movie("Central Intelligence",
                                  "After he reconnects with an awkward pal from high school through Facebook, a mild-mannered accountant is lured into the world of international espionage",
                                  "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA2NzEzNjIwNl5BMl5BanBnXkFtZTgwNzgwMTEzNzE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                                  "https://www.youtube.com/watch?v=MxEw3elSJ8M")


dead_pool=media.Movie("Deadpool",
                      "A fast-talking mercenary with a morbid sense of humor is subjected to a rogue experiment that leaves him with accelerated healing powers and a quest for revenge.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQyODg5Njc4N15BMl5BanBnXkFtZTgwMzExMjE3NzE@._V1_UY268_CR1,0,182,268_AL_.jpg",
                      "https://www.youtube.com/watch?v=ONHBaC-pfsk")

Avengers=media.Movie("The Avengers",
                      "Earth's mightiest heroes must come together and learn to fight as a team if they are to stop the mischievous Loki and his alien army from enslaving humanity.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk2NTI1MTU4N15BMl5BanBnXkFtZTcwODg0OTY0Nw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                      "https://www.youtube.com/watch?v=eOrNdBpGMv8")


    # will make a list of all movies that we have
movies=[dead_pool, Avengers, Ironman, toy_story, Avatar, central_intelligence]
    # movie list will be passed on to fresh_tomatoes to creat the html to play on screen
fresh_tomatoes.open_movies_page(movies)
