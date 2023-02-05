movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
def check_IMDB(movie):
    if(movie['imdb']>5.5):
        return True
    else:
        return False

print(check_IMDB(movies[7]))

#2
def sublist_IMDB(movies):
    list=[]
    for i in range(0, len(movies)):
        current_movie=movies[i]
        if current_movie['imdb']>5.5:
            list.append(current_movie)
    return list
print(sublist_IMDB(movies))

#3
def category_movie(movies, cat_name):
    list=[]
    for i in movies:
        cur_cat=i['category']
        if cat_name.lower()==cur_cat.lower():
            list.append(i)
    return list
list=category_movie(movies,'Romance')
#print(list)

#4
def av_imdb_score(movies):
    avg_score=0
    total=len(movies)
    for i in movies:
        avg_score=avg_score+i['imdb']
    avg_score=avg_score/total
    return avg_score
#print(av_imdb_score(movies)) 

#5
def avg_score_of_cat(movies, cat_name):
    cat_movies=category_movie(movies,cat_name)
    avg_score=av_imdb_score(cat_movies)
    return avg_score
print(avg_score_of_cat(movies, 'Thriller'))