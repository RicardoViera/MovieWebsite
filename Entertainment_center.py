import media
import fresh_tomatoes

#Declaring and initializing the different movie objects with respective attributtes
harry_p = media.Movie("Harry Potter and the Sorcerer's Stone","A story of a young magician and his adventures",
                        "https://i.jeded.com/i/harry-potter-and-the-sorcerers-stone.30084.jpg",
                        "https://www.youtube.com/watch?v=VyHV0BRtdxo")

departed = media.Movie("The Departed",
                     "A story about old school gangsters and FBI agents",
                     "https://upload.wikimedia.org/wikipedia/en/5/50/Departed234.jpg",
                     "https://www.youtube.com/watch?v=auYbpnEwBBg")

hobbit =media.Movie("The Hobbit: The Battle of the Five Armies",
                            "The closing chapter of the middle earth saga",
                            "https://upload.wikimedia.org/wikipedia/en/0/0e/The_Hobbit_-_The_Battle_of_the_Five_Armies.jpg",
                            "https://www.youtube.com/watch?v=ZSzeFFsKEt4" )

mr_deeds = media. Movie( "Mr. Deeds" ,
                            "A good man who suddenly becomes rich",
                            "https://upload.wikimedia.org/wikipedia/en/6/63/Mr_deeds_ver2.jpg",
                            "https://www.youtube.com/watch?v=c3sBBRxDAqk")


monster = media. Movie( "Monsters, Inc" ,
                                 "A story about monsters and nightmares",
                                 "https://upload.wikimedia.org/wikipedia/en/6/63/Monsters_Inc.JPG",
                                 "https://www.youtube.com/watch?v=cvOQeozL4S0")

hunger_games = media. Movie("Hunger Games",
                           "A contest for survival amongst youngsters" ,
                           "https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")

#Creating a movie array
movies =[harry_p ,departed, hobbit, mr_deeds, monster, hunger_games]
fresh_tomatoes.open_movies_page(movies)#Passing such movie array to open_movies_page method

#Testing instance and assigned variables

#print(media. Movie.VALID_RATINGS)
#print(media. Movie.__doc__)
#print(media. Movie.__name__)
#print(media. Movie.__module__)
