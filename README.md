# Movies Scraper

The project uses **Scrapy** to gather IMDb movie IDs, which are then used in the OMDb API fetcher to retrieve detailed movie information.
The data is stored in a **MongoDB Atlas cloud database**. 

## Installation

To set up the project, install the dependencies listed in `requirements.txt`:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/brankowss/Movies-Scraper
    cd Movies-Scraper
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/Mac
    venv\Scripts\activate     # On Windows
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Start program**:
    ```bash
    python3 main.py
    ```

## Setup

Before running the project, you need to sign up for certain services and configure your API keys.

### 1. Setting Up the OMDb API Key

To use the OMDb API, create an account at [OMDb API](https://www.omdbapi.com/) and obtain your API key:

- Visit [OMDb API Key](https://www.omdbapi.com/apikey.aspx).
- Sign up and get your free API key.

### 2. Setting Up MongoDB Atlas

To connect to a MongoDB Atlas database, sign up at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) and set up your database:

1. Visit [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/register).
2. Create a free account and set up a new database.
3. Retrieve the `MongoDB URI` to use later in the `.env` file.

### 3. Creating the `.env` File

In the root of the project, create a file named `.env` and add the following environment variables:

```dotenv
API_KEY=your-omdb-api-key
MONGO_URI=your-mongodb-atlas-uri
MONGO_DATABASE=your-database-name
```

