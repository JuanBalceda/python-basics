import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life.",
                        "https://vignette.wikia.nocookie.net/doblaje/images/3/37/5c1f3c2e3e6dc7ae8d7c99e390162049.jpg/revision/latest?cb=20180423154626&path-prefix=es",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A marine on an alien planet.",
                     "https://images-na.ssl-images-amazon.com/images/I/41kTVLeW1CL.jpg",
                     "https://www.youtube.com/watch?v=6ziBFh3V1aM")

star_wars = media.Movie("Star Wars", "Story of Anakin Skywalker childhood.",
                        "https://ae01.alicdn.com/kf/HTB12_AsOpXXXXbaaXXXq6xXFXXXs/Star-Wars-episodio-I-La-Amenaza-Fantasma-Movie-posters-impresi-n-tela-de-seda-impresi-n.jpg_640x640.jpg",
                        "https://www.youtube.com/watch?v=bD7bpG-zDJQ")
# print(avatar.title)
# star_wars.show_trailer()
movies = [toy_story, avatar, star_wars]
# fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
