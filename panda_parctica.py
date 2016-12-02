import pandas  as pd
from scipy.spatial.distance import cosine

# read the data

data = pd.read_csv('data.csv')

(data.tail(6).ix[1:8,2:10])


# --- Start Item Based Recommendations --- #
# Drop any column named "user"
data_germany = data.drop('user', 1)

# Create a placeholder dataframe listing item vs. item
data_ibs = pd.DataFrame(index=data_germany.columns, columns=data_germany.columns)

#lets fill in those empty spaces with cosine similaries
#loop through the columns
for i in range(0, len(data_ibs.columns)):
    #loop through the columns for each column
    for j in range(0, len(data_ibs.columns)):
        # fill the in place holder with cosine similarities
        data_ibs.ix[i,j] = 1-cosine(data_germany.ix[:, i], data_germany.ix[:,j])

#create a placeholder items  for close neighbours to an item
data_neighbours = pd.DataFrame(index=data_ibs.columns, columns=range(1,11))

#loop trough our similaritie data frame and fill neighbouring items names
for i in range(0, len(data_ibs.columns)):
    data_neighbours.ix[i,:10] = data_ibs.ix[0:,i].sort_values(ascending=False)[:10].index
#-----end item-based  recommendations

data_neighbours.head(6).ix[:6, 1:4] #añadir print() para ver resultado

#-----Recomendaciones basadas en usuarios
#funcion auxiliar para optener los puntajes de similitud
def get_score(history, similarities):
    return sum(history*similarities) / sum(similarities)

#se de be aplicar esta funcion al dataframe de la manera correcta
#se crea una variable para almacenar los datos similares
#basicamente son los mismos datos originales con nada llenado exepto los encabezados
#crear la matrix placeholder para las similitudes y llenar la columna de nombre de usuario
data_sims = pd.DataFrame(index=data.index, columns=data.columns)
data_sims.ix[:, :1]=data.ix[:, :1]

#bucle a traves de todas las columnas, se salta la columna de los usuarios y se llena con las similitudes
for i in range(0, len(data_sims.index)):
    for j in range(1, len(data_sims.columns)):
        user = data_sims.index[i]
        product = data_sims.columns[j]

        if data.ix[i][j] == 1:
            data_sims.ix[i][j] =0 #pone cero en los items que ya fueron consumidos para no recomendarlos de nuevo

        else:
            product_top_names= data_neighbours.ix[product][1:10]
            product_top_sims = data_ibs.ix[product].sort_values(ascending=False)[1:10]
            user_purchases = data_germany.ix[user, product_top_names]

            data_sims.ix[i][j]=get_score(user_purchases, product_top_sims)


#se optiene las top-songs
data_recommend = pd.DataFrame(index=data_sims.index, columns=['user', '1', '2', '3', '4', '5', '6'])
data_recommend.ix[0:,0] = data_sims.ix[:,0]

#para ver los nombres de las canciones
for i in range(0, len(data_sims.index)):
    data_recommend.ix[i,1:] = data_sims.ix[i,:].sort_values(ascending=False).ix[1:7,].index.transpose()

print(data_recommend.ix[:10,:4])
# FutureWarning: order is deprecated, use sort_values(...)




