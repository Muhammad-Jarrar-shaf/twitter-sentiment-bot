# Twitter Sentiment Bot

A Twitter-inspired Sentiment Analysis application built with Python, FastAPI, TextBlob, and Pandas. The project analyzes social media text, classifies sentiment as Positive, Negative, or Neutral, stores processed results, and exposes them through REST API endpoints.

## Features

* Sentiment Analysis using TextBlob
* Simulated Tweet Streaming Pipeline
* FastAPI REST API
* CSV-based Data Persistence
* Swagger/OpenAPI Documentation
* Health Check Endpoint
* Automated Unit Tests with Pytest
* Modular Project Structure

## Project Structure

```text
twitter-sentiment-bot/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── services/
│   └── utils/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── scripts/
├── tests/
│
├── main.py
├── requirements.txt
├── README.md
└── .env.example
```

## Tech Stack

* Python
* FastAPI
* TextBlob
* Pandas
* Pytest
* Uvicorn

## Installation

### Clone Repository

```bash
git clone https://github.com/Muhammad-Jarrar-shaf/twitter-sentiment-bot.git
cd twitter-sentiment-bot
```

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Download TextBlob Resources

```bash
python -m textblob.download_corpora
```

## Run Sentiment Pipeline

```bash
python -m scripts.run_pipeline
```

Processed results are stored in:

```text
data/processed/sentiment_results.csv
```

## Run API Server

```bash
uvicorn main:app --reload
```

API available at:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### Home

```http
GET /
```

### Health Check

```http
GET /health
```

### Sentiment Results

```http
GET /sentiments
```

### Summary Statistics

```http
GET /summary
```

## Testing

Run all tests:

```bash
pytest -v
```

## Sample Output

```json
{
  "total_tweets": 10,
  "positive": 4,
  "negative": 6,
  "neutral": 0
}
```

## Learning Outcomes

* NLP Fundamentals
* Sentiment Analysis
* Data Processing Pipelines
* FastAPI Development
* API Testing
* Software Project Structure
* Git and GitHub Workflow

## Author

Muhammad Jarrar Shaf

## License

This project is intended for educational and portfolio purposes.
