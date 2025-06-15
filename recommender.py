import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def __int__(self,csv_path="movies.csv")
    self.movies=pd.read_csv(csv_path)
    self.movies['genres']=self.movie['genres'].fillna('').str.replace('|','',regex=FALSE)
    