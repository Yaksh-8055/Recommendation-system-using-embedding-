import streamlit as st
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer

indexName = "all_movies"
es = None

try:
    es = Elasticsearch(
        "https://localhost:9200",
        basic_auth=("elastic", "4UORufemVQ67-PTLj50o"),
        ca_certs=r"C:\Users\Yaksh\Downloads\elasticsearch-9.4.3-windows-x86_64\elasticsearch-9.4.3\config\certs\http_ca.crt",
        verify_certs=True
    )
    if es.ping():
        print("Successfully connected to Elasticsearch!!")
    else:
        print("Cannot connect to Elasticsearch!")
        es = None
except Exception as e:
    print(f"Connection Error: {e}")
    es = None




def search(input_keyword):
    if es is None:
        st.error("Cannot connect to Elasticsearch! Please ensure Elasticsearch is running.")
        return []

    try:
        model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
        vector_of_input_keyword = model.encode(input_keyword)

        query = {
            "field": "Description_vector",
            "query_vector": vector_of_input_keyword,
            "k": 10,
            "num_candidates": 500
        }

        res = es.search(
            index="all_movies",
            knn={
                "field": "Description_vector",
                "query_vector": vector_of_input_keyword,
                "k": 10,
                "num_candidates": 500
            },
            source=["title", "overview"]
        )
        results = res["hits"]["hits"]
        return results
    except Exception as e:
        st.error(f"Search error: {e}")
        return []

def main():
    st.title("Movie recommendation System")

    # Input: User enters search query
    search_query = st.text_input("Enter your search query")

    # Button: User triggers the search
    if st.button("Search"):
        if search_query:
            # Perform the search and get results
            results = search(search_query)

            # Display search results
            st.subheader("Search Results")
            for result in results:
                with st.container():
                    if '_source' in result:
                        try:
                            st.header(f"{result['_source']['title']}")
                        except Exception as e:
                            print(e)
                        
                        try:
                            st.write(f"overview: {result['_source']['overview']}")
                        except Exception as e:
                            print(e)
                        st.divider()

                    
if __name__ == "__main__":
    main()