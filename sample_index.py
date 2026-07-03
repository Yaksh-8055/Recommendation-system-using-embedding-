index_mappings = {
    "properties": {
        "budget	": {"type":"long"},
        "genres": {"type":"text"},
        "homepage": {"type":"text"},
        "id": {"type":"long"},
        "keywords": {"type":"text"},
        "original_language": {"type":"text"},
        "original_title": {"type":"text"},
        "overview": {"type":"text"},
        "popularity": {"type":"float"},
        "production_companies": {"type":"text"},
        "production_countries": {"type":"text"},
        "release_date": {"type":"date"},
        "revenue": {"type":"long"},
        "runtime": {"type":"float"},
        "spoken_languages": {"type":"text"},
        "status": {"type":"text"},
        "tagline": {"type":"text"},
        "title": {"type":"text"},
        "vote_average": {"type":"float"},
        "vote_count": {"type":"long"},
        "Description_vector": {"type":"dense_vector", "dims": 768 ,
                               "index" :True,
                               "similarity": "l2_norm"


                               }
    }

}