# Bayard Vacations Chatbot 🤖✈️

An AI-powered chatbot built to assist customers with basic travel-related queries
such as tour packages, destinations, pricing, and booking process.

This project was developed as part of a technical assignment for the
Machine Learning Engineer position at Bayard Vacations.

---

## Tech Stack

- Python
- Streamlit (Frontend UI)
- Flask (Backend API)
- Rule-based NLP (Keyword Matching)

---

## Features

- Answers queries related to:
  - Travel packages
  - Destinations
  - Pricing
  - Booking process
- Web UI using Streamlit
- REST API using Flask
- JSON-based intent system for easy extension

---

## Project Structure

- `app.py` – Flask backend server
- `streamlit_app.py` – Streamlit frontend UI
- `chatbot.py` – Chatbot logic
- `intents.json` – Intent configuration
- `requirements.txt` – Dependencies

---

## How It Works

1. Flask server handles chatbot logic and API requests
2. Streamlit UI sends user queries to Flask API
3. Input is processed using keyword-based intent matching
4. Response is returned to the UI
5. Fallback message is shown if no intent matches

---

## Limitations

- Rule-based logic only
- No context or memory handling
- Limited to predefined intents

---

## Future Improvements

- ML-based intent classification
- Greeting and small-talk support
- Context-aware conversations
- Database-backed booking workflow
- Deployment on cloud (AWS / GCP)

---

## Run Locally

Follow the steps below to run the chatbot locally:

```bash
git clone <your-github-repo-link>
cd bayard-vacations-chatbot
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
streamlit run streamlit_app.py