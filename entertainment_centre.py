import media
import trailer_tube

# Movie 1 : Theory of Everything
theory_of_everything = media.Movie("Theory of Everything",
								   "Biograpghy of Dr. Stephen Hawking",
								   "http://kulttura.rs/wp-content/uploads/2015/03/27.11.2014_13_36_38_teorija_svega.jpg",
								   "https://www.youtube.com/watch?v=Salz7uGp72c&t=21s")

# Movie 2 : 12 Strong
_12_strong = media.Movie("12 Strong",
					     "Story of the first Special Forces team deployed to Afghanistan after 9/11",
					     "https://www.dvdsreleasedates.com/posters/800/0/12-Strong-2018-movie-poster.jpg",
					     "https://www.youtube.com/watch?v=ouAf90EILnE")

# Movie 3 : Interstellar
interstellar = media.Movie("Interstellar",
	                       "Former NASA pilot Cooper and a team of researchers travel across the galaxy to find out mankind's new home.",
	                       "https://www.ilcinemainsegna.it/wp-content/uploads/2017/07/interstellar-locandina.jpg",
	                       "https://www.youtube.com/watch?v=zSWdZVtXT7E")

# Movie 4 : Avatar
avatar = media.Movie("Avatar",
					 "A marine on an alien planet",
					 "http://www.writingfordesigners.com/wp-content/uploads/2014/09/Avatar-Poster-blue-people.jpg",
					 "https://www.youtube.com/watch?v=5PSNL1qE6VY&t=12s")

# Movie 5 : Dunkirk
dunkirk = media.Movie("Dunkirk",
	                  "Allied soldiers from Belgium, the British Empire and France are surrounded by the German Army, and evacuated during a fierce battle in World War II",
	                  "https://images-na.ssl-images-amazon.com/images/I/410yY%2BU925L.jpg",
	                  "https://www.youtube.com/watch?v=F-eMt3SrfFU")

# Movie 6 : 300
_300 = media.Movie("300",
			"A fictionalized retellings of the Battle of Thermopylae within the Persian Wars",
			"https://i.pinimg.com/originals/d7/a8/81/d7a8813bf2cd115540ccffe96d75cb9f.png",
			"https://www.youtube.com/watch?v=UrIbxk7idYA")

# Movie 7 : Kung Fu Panda
kung_fu_panda = media.Movie("Kung Fu Panda 3",
			  "Continuing his legendary adventures of awesomeness, Po must face two hugely epic, but different threats: one supernatural and the other a little closer to his home",
			  "https://vignette.wikia.nocookie.net/kungfupanda/images/5/51/Kung-Fu-Panda-3-Poster-2-UK.jpg/revision/latest?cb=20151122162126",
			  "https://www.youtube.com/watch?v=-pyPwjy_5qE")

# Movie 8 : The Man who knew Infinity
the_man_who_knew_infinity = media.Movie("The Man who knew Infinity",
	 									"A brilliant South Indian mathematician Srinivasa Ramanujan travels to Trinity College in England to work with professor G.H. Hardy",
	 									"https://mediafiles.cineplex.com/Central/Film/Posters/24887_320_470.jpg",
	 									"https://www.youtube.com/watch?v=NP0lUqNAw3k&t=15s")

# Movie 9 : Me Before You
me_before_you = media.Movie("Me Before You",
							"A girl in a small town forms an unlikely bond with a recently-paralyzed man she's taking care of",
							"http://img.moviepostershop.com/me-before-you-movie-poster-2016-1020773860.jpg",
							"https://www.youtube.com/watch?v=eR_T_HhkL0A")


movies = [theory_of_everything, _12_strong, interstellar, avatar, dunkirk, _300, kung_fu_panda, the_man_who_knew_infinity, me_before_you]
trailer_tube.open_movies_page(movies)