import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class movierecommender:
 def __intit__(self,csv_path="movies.csv"):
        self.movies=pd.read_csv(csv_path)
        self.movies['genres']=self.movies['genres'].fillna('').str.replace('|','',regex=False)
        tfidf=TfidfVectorizer(stop_words="english")
        genre_vector=tfidf.fit_transform(self.movies['genres'])
        self.similarity=cosine_similarity(genre_vector)
        self.title_index = pd.Series(self.movies.index , index=self.movies['titles']).drop_duplicates()


 def recommend(self,movie_title,top_n=5):
    index=self.title_index.get(movie_title)
    similar_movies=list(enumerate(self.similarity[index]))
    similar_movies=sorted(similar_movies , key=lambda x:x[1] , reverse=True)[1:top_n+1]
    recommend=[i[0] for i in similar_movies]
    return self.movies['title'].iloc[recommend].tolist()

 def get_all_titles(self):
        return self.movies['title'].sort_values().tolist()
