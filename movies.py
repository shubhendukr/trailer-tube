import media
import trailer_tube

# Movie 1 : Theory of Everything
theory_of_everything = media.Movie(
    "Theory of Everything",
    "Biograpghy of Dr. Stephen Hawking",
    "https://goo.gl/dvyQmT",
    "https://www.youtube.com/watch?v=Salz7uGp72c&t=21s")

# Movie 2 : 12 Strong
_12_strong = media.Movie(
    "12 Strong",
    "Special Forces team deployed to Afghanistan after 9/11",
    "https://goo.gl/Cj8Ci1",
    "https://www.youtube.com/watch?v=ouAf90EILnE")

# Movie 3 : Interstellar
interstellar = media.Movie(
    "Interstellar",
    "A search for mankind's new home beyond Earth",
    "https://goo.gl/nf8Fhz",
    "https://www.youtube.com/watch?v=zSWdZVtXT7E")

# Movie 4 : Avatar
avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "http://bit.ly/2phPEyO",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY&t=12s")

# Movie 5 : Dunkirk
dunkirk = media.Movie(
    "Dunkirk",
    "A fierce battle in World War II",
    "https://goo.gl/5Vv7ro",
    "https://www.youtube.com/watch?v=F-eMt3SrfFU")

# Movie 6 : 300
_300 = media.Movie(
    "300",
    "A fictionalized retellings of the Battle of Thermopylae",
    "http://bit.ly/2piEvOf",
    "https://www.youtube.com/watch?v=UrIbxk7idYA")

# Movie 7 : Kung Fu Panda
kung_fu_panda = media.Movie(
    "Kung Fu Panda 3",
    "Another adventure of PO, the awesome Panda",
    "https://goo.gl/14aQcA",
    "https://www.youtube.com/watch?v=-pyPwjy_5qE")

# Movie 8 : The Man who knew Infinity
the_man_who_knew_infinity = media.Movie(
    "The Man who knew Infinity",
    "Ramanujan travels to England to work with professor G.H. Hardy",
    "https://goo.gl/m5oL3z",
    "https://www.youtube.com/watch?v=NP0lUqNAw3k&t=15s")

# Movie 9 : Me Before You
me_before_you = media.Movie(
    "Me Before You",
    "A girl forms an unlikely bond with a paralyzed man she's taking care of",
    "https://goo.gl/FbePR7",
    "https://www.youtube.com/watch?v=eR_T_HhkL0A")


# Creating array of the above movies details
movies = [theory_of_everything, _12_strong, interstellar,
          avatar, dunkirk, _300, kung_fu_panda,
          the_man_who_knew_infinity, me_before_you]

trailer_tube.open_movies_page(movies)
