import requests
import pymongo
import os
from dotenv import load_dotenv
import re
import json

load_dotenv()


def connect_to_atlas(mongo_uri, mongo_db):
    # Connection to the Atlas Cloud database
    client = pymongo.MongoClient(mongo_uri)
    db = client[mongo_db]
    collection = db["movies"]  
    return collection


def clean_runtime(runtime):
        # A function that clears the runtime in minutes and converts it to hours and minutes.
        match = re.match(r"(\d+)\s*min", runtime)
        if match:
            minutes = int(match.group(1)) 
            hours = minutes // 60  
            remaining_minutes = minutes % 60  
            return f"{hours} hours {remaining_minutes} minutes"
        else:
            return runtime  


def fetch_movie_data(imdb_id):
    API_KEY = os.getenv('API_KEY')
    MONGO_URI = os.getenv('MONGO_URI')
    MONGO_DATABASE = os.getenv('MONGO_DATABASE')

    if not API_KEY:
        raise ValueError("API_KEY not found in .env file")

    url = f"http://www.omdbapi.com/?i={imdb_id}&apikey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get("Response") == "True":
            movie_data = {
                "name": data.get("Title"),
                "year": data.get("Year"),
                "released": data.get("Released"),
                "country": data.get("Country"),
                "director": data.get("Director"),
                "actors": data.get("Actors"),
                "genre": data.get("Genre"),
                "box_office": data.get("BoxOffice", "N/A"),
                "awards": data.get("Awards"),
                "imdbRating": data.get("imdbRating", "N/A"),
                "imdbVotes": data.get("imdbVotes"),
                "plot": data.get("Plot"),
                "runtime": clean_runtime(data.get("Runtime"))
            }

            # Connect to MongoDB Atlas 
            collection = connect_to_atlas(mongo_uri=MONGO_URI, mongo_db=MONGO_DATABASE)

            # Insert data into Atlas Cloud
            collection.insert_one(movie_data)

            return movie_data

        else:
            print(f"Error for IMDb ID {imdb_id}: {data.get('Error')}")
            return None
    else:
        raise Exception(f"Error with API call: {response.status_code}")


def main():
    with open("data/id.json", "r") as file:
        imdb_ids = json.load(file)

    movies = []
    for imdb_id in imdb_ids:
        movie_data = fetch_movie_data(imdb_id)
        if movie_data:
            movies.append(movie_data)

if __name__ == "__main__":
    main()



