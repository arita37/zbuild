import numpy as np

import hnswlib        
dim = 50
elements = 10_000

hnsw = hnswlib.Index(space='cosine', dim=dim)


                     
