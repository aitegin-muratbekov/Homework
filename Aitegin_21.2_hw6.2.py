movies = {
    "Django Unchained": {
        "John": 10,
        "Jack": 9
    },

    "Акыркы Сабак": {}
}

def add_movie(movie):
    if movie not in movies.keys():
        print("Movie added successfully")
        movies[movie] = {}
        return movies
    print("This movie already exist!")

add_movie('Брат')
add_movie('Брат')
add_movie('Spider-Man')


def add_rate(movie , name, rate):
    if movie in movies.keys():
        movies[movie][name] = rate
        print(f'A rating has been added for {movie}: {name} rated it {rate}')
        return movies
    print("This movie doesn't exist")

add_rate('Акыркы Сабак', 'aitegin', 10)
add_rate('Акыркы Сабак', 'alan', 4)
add_rate('МАМА', 'aibek', 3)
add_rate('Брат', 'cholpon', 7)

def get_average():
    average = 0
    for movie in movies.keys():
        if len(movies[movie]) > 0 :
            for key , value in movies[movie].items():
                average = average + value
            average = average / len(movies[movie].items())
            print(f'{movie} is rated {average}')
        else:
            print(f'Rating is not yet available for {movie}')
    return


get_average()





