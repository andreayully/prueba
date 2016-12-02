import pandas as pd



#pasar nombres de columnas para cada csv y se leen usando pandas
#los nombres de las columnas esta disponibles en readme.txt http://grouplens.org/datasets/movielens/100k/

#leyendo el archivo de usuarios
u_cols=['user_id', 'age', 'sex', 'ocupation', 'zip_code']
users = pd.read_csv('ml-100k/u.user', sep='|', names=u_cols, encoding='latin-1')

#leyendo el archivo de raitings
r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestap']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols, encoding='latin-1')

#leyendo el archivo de items
i_cols=['movie id', 'movie title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
 'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

items = pd.read_csv('ml-100k/u.item', sep='|', names=i_cols, encoding='latin-1')

# print(users.shape)
# users.head()
#(943,5) confirma que hay 943 usuario con 5 caracteristica id, edad, gender, ocupacion, y el zip_code

# print(ratings.shape)
# ratings.head()
#(100000, 4) hay 100mil rating de diferentes usuarios y peliculas. los items cuentan con 4 caracteristicas entre ellas una marce de tiempo

#print(items.shape)
items.head()
#(1682, 24) contiene los atributos de 1682 peliculas 19 de 24 columnas pertenecen al genero
#1 si pertenece al genero, 0 de lo contrario

#se dividen los datos en test y datos de entranamiento para hacer los modelos
r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings_base=pd.read_csv('ml-100k/ua.base', sep='\t', names=r_cols, encoding='latin-1')
ratings_test= pd.read_csv('ml-100k/ua.test', sep='\t', names=r_cols, encoding='latin-1')
print(ratings_base.shape, ratings_test.shape)
