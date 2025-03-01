import pandas as pd
import numpy as np
import spacy
import ast

def preprocess_input(title: str):
    
    nlp = spacy.load('en_core_web_sm')
    
    return nlp(title).vector


def cosine(a: np.array, b: np.array):
    
    return a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))


def find(title):
    
    vector = preprocess_input(title)
    data = pd.read_csv('data/movies.csv')
    
    lst = []
    
    for i, row in data.iterrows():
        vector_ = np.fromstring(row['vector'].strip('[]'), sep=' ')
        
        cos = cosine(vector_, vector)
        if cos<0.99:
            lst.append( [ cos, row['title'], row['plot'], row['type'], row['genre'] , row['runtime']]  )
        
    lst.sort(reverse=True)
    
    return lst[:10]