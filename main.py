import subprocess
import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

def run_spider():
    subprocess.run(["scrapy", "crawl", "imdbmoviesidscraper"], check=True)

def run_postprocessing():
    subprocess.run(["python3", "scripts/format_json.py"], check=True)

def run_omdb_fetcher():
    subprocess.run(["python3", "scripts/omdb_api_data_fetcher.py"], check=True)

if __name__ == "__main__":
    print("Start Scrapy spider...")
    run_spider()

    print("Format json data...")
    run_postprocessing()

    print("Start OMDb API fetch data...")
    run_omdb_fetcher()

    print("All done as expected!")





   

