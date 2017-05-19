import media
import fresh_tomatoes

#Declaring and Initializing the different move objects with respective attributtes
toy_story = media.Movie("Toy Story","A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien Planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

school_of_rock =media.Movie("School of Rock",
                            "A school for kids to learn rock",
                            "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                            "https://www.youtube.com/watch?v=XCwy6lW5Ixc" )

ratatouille = media. Movie( "Ratatouille" ,
                            "A rat that wants to be a chef",
                            "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                            "https://www.youtube.com/watch?v=c3sBBRxDAqk")


midnight_in_paris = media. Movie( "Midnight in Paris " ,
                                 "A guy who parties at night in Paris hiddden from his wife",
                                 "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                 "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media. Movie("Hunger Games",
                           "A contest for survival amongst youngsters" ,
                           "https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")

#Creating a movie array
movies =[toy_story ,avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)#Passing such movie array to open_movies_page method

#Testing instance and assigned variables

#print(media. Movie.VALID_RATINGS)
#print(media. Movie.__doc__)
#print(media. Movie.__name__)
#print(media. Movie.__module__)
