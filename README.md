
# Movie Ratings Scraper

## Overview

This repository contains Python code that scrapes IMDb ratings for a specified set of movies, using their IMDb IDs. It leverages asynchronous requests to efficiently fetch ratings for multiple movies concurrently.

## Datasets

The code relies on two datasets, which should be placed in the same directory as the `scraper.py` file:

1. **links.csv:** Contains movie IDs and corresponding IMDb IDs.
2. **ratings.csv:** Contains user ratings for movies.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Thirupy/Movie-Ratings-Scrape.git
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure the datasets are in the same directory as `scraper.py`.
2. Run the script:
   ```bash
   python scraper.py
   ```

## Output

The script will create a DataFrame with the following columns:

- `imdbId`: The IMDb ID of the movie.
- `movieId`: The internal movie ID (from the `links.csv` dataset).
- `Imdb_ratings`: The scraped IMDb rating.

## Code Structure

- **`scraper.py`:** Main Python script containing the scraping logic.
- **`requirements.txt`:** Lists required Python libraries.
- **`links.csv` and `ratings.csv`:** Datasets.
- **`webScrapping.ipynb`:** Sample output.

## Key Features

- Asynchronous requests for efficient scraping.
- Retries for failed requests.
- Data cleaning and filtering.
- Integration with Pandas DataFrames.

## Additional Notes

- The code filters movies with fewer than 50 ratings and those with ratings below 5.0.
- You can adjust filtering criteria and dataset paths within the `scraper.py` file.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Feel free to contribute to this project by submitting issues or pull requests!
