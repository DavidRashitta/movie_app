import media
import fresh_tomatoes
#there are some inctances of class movie
rush_hour = media.Movie("Rush hour",
                        "When a Chinese diplomat's daughter is kidnapped in Los Angeles, he calls in Hong Kong Detective Inspector Lee ",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAyMzAyNzY5N15BMl5BanBnXkFtZTcwNjU3MTc0MQ@@._V1_SX640_SY720_.jpg",
                        "https://www.youtube.com/watch?v=JMiFsFQcFLE")

fast_and_furious = media.Movie("Fast and furious 8",
	"Some people join cas races for money",
	"http://www.etonline.com/movies/2016/04/24232821/640_furious8_poster.jpg",
	"https://www.youtube.com/watch?v=uisBaTkQAEs")

lucy = media.Movie("Lucy",
	"A woman, accidentally caught in a dark deal, turns the tables on her captors",
	"http://www.impawards.com/intl/france/2014/posters/lucy_ver3.jpg",
	"https://www.youtube.com/watch?v=MVt32qoyhi0")

despicable_me = media.Movie("Despicable Me",
	"It follows the story of Gru, a super-villain who adopts three girls from an orphanage",
	"http://uvchoice.com/wp-content/uploads/2016/05/despicable-me-poster-big.jpg",
	"https://www.youtube.com/watch?v=sUkZFetWYY0")
							 
her = media.Movie("her",
	"Guy falls in love with computer",
	"https://upload.wikimedia.org/wikipedia/en/4/44/Her2013Poster.jpg",
	"https://www.youtube.com/watch?v=WzV6mXIOVl4")
							 

lion_king = media.Movie("Lion King",
	"A lion is a king and his son simba",
	"https://www.movieposter.com/posters/archive/main/108/MPW-54063",
	"https://www.youtube.com/watch?v=4sj1MT05lAA")

#this is list of movie inctances to pass to the open_movies_page method in fresh_tomatoes file
movies = [rush_hour, fast_and_furious, lucy, despicable_me, her, lion_king]
fresh_tomatoes.open_movies_page(movies)

#print(toy_story.storyline)
#lion_king.show_trailer()
