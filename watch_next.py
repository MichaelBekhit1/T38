import spacy
nlp = spacy.load('en_core_web_md')

movie_list_file = open("movies.txt", "r")
movie_records = movie_list_file.readlines()



def similar_film(synopsis):
    similarity=0
    index = 0
    for key, movie in enumerate(movie_records):
        benchmark = nlp(synopsis)
        synopsis_similarity_to_movie = benchmark.similarity(movie)
        if synopsis_similarity_to_movie > similarity:
            similarity = synopsis_similarity_to_movie
            index = key
    return movie_records[index]
        
    
         

planet_hulk = """Will he save the world or destroy it? When the Hulk becomes
too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch
him into space to a planet where the Hulk can live in peace. Unfortunately,
Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
"""

similar_film(planet_hulk)
