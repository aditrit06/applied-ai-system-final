# VibeMatch AI 🎵
### An Explainable and Reliable Music Recommendation System

## Project Overview

VibeMatch AI is a personalized music recommendation system
that helps users discover songs based on their preferences.

The application recommends music based on genre, mood,
energy, and valence (musical positivity).

Unlike a basic recommendation system, VibeMatch AI also
verifies its recommendations, explains its scoring decisions,
and allows users to improve their playlist through feedback.

This project extends my original CodePath AI110 Module 3
Music Recommender Simulation.

## Features

- Personalized music recommendations
- Genre and mood matching
- Energy and valence similarity scoring
- Explainable recommendation scores
- Feedback-based playlist updates
- Input validation and safety guardrails
- Automatic recommendation verification
- Logging and error handling
- Automated reliability testing

## How It Works

1. The user enters their music preferences.
2. The system validates the inputs.
3. Songs are loaded and checked for invalid data.
4. Relevant songs are retrieved from the dataset.
5. The recommendation engine calculates match scores.
6. Songs are ranked by compatibility.
7. Recommendations are verified before being displayed.
8. The user can dislike songs and receive an updated playlist.

## Recommendation Algorithm

The system uses a specialized, rule-based recommendation
algorithm to evaluate how closely each song matches
the user's preferences.

The scoring system considers:

- Genre match: up to 4 points
- Mood match: up to 3 points
- Energy similarity: up to 2 points
- Valence similarity: up to 1 point

Each recommendation receives a score between 0 and 10.

The application also provides an explanation describing
how the score was calculated.

This is a deterministic recommendation system, not a
generative language model.

## Advanced AI Feature: Reliability Testing

VibeMatch AI integrates reliability checks directly
into the recommendation workflow.

The system checks that:

- User preferences are valid.
- Energy and valence values fall between 0 and 1.
- Song data contains required information.
- Duplicate song IDs are excluded.
- Recommendation scores are valid.
- Explanations match the scoring calculations.
- Disliked songs are excluded from updated results.

The system uses Python logging to record processing
information and warnings.

## Technologies Used

- Python
- pytest
- CSV datasets
- Git and GitHub
- Mermaid architecture diagrams

## Installation

Clone this repository:

    git clone https://github.com/aditrit06/applied-ai-system-final.git

Navigate into the project:

    cd applied-ai-system-final

Create a virtual environment:

    python3 -m venv .venv

Activate it on macOS or Linux:

    source .venv/bin/activate

Install dependencies:

    python -m pip install -r requirements.txt

Install pytest if needed:

    python -m pip install pytest

## Running the Application

Run:

    python -m src.main

Example input:

    Genre: pop
    Mood: chill
    Energy: 1.0
    Valence: 0.6

The system returns ranked song recommendations
with scores and explanations.

Users can enter disliked song IDs to generate
an updated playlist.

## Testing

Run the automated test suite:

    python -m pytest -q

Latest local test result:

    15 passed

The tests evaluate recommendation functionality,
validation, score ranges, duplicate prevention,
feedback handling, consistency, and ranking.

See EVALUATION.md for detailed evaluation results.

## System Architecture

The system follows this workflow:

User Input
    |
Input Validation
    |
Song Retrieval
    |
Recommendation Engine
    |
Ranking and Scoring
    |
Result Verification
    |
Personalized Playlist
    |
User Feedback
    |
Updated Recommendations

The Mermaid source file is located at:

    diagrams/architecture.mmd

## Responsible AI Design

VibeMatch AI focuses on transparency and reliability.

Recommendations include explanations so users can
understand why particular songs were selected.

Input validation and verification help prevent
incorrect or inconsistent outputs.

The application does not claim to understand users'
emotions or guarantee musical satisfaction.

## Limitations

- The current dataset includes 18 songs.
- The recommendation algorithm is rule-based.
- Recommendations depend on available song metadata.
- Feedback is not permanently stored.
- The application does not use a generative AI model.
- Recommendation quality has not been evaluated
  through a large-scale user study.

## Future Improvements

- Expand the song dataset
- Add Spotify API integration
- Support natural-language preferences
- Build an interactive web interface
- Save user preferences
- Improve personalization using machine learning

## Conclusion

VibeMatch AI demonstrates how a simple recommendation
prototype can be extended into a more reliable,
explainable, and interactive applied AI system.

The project integrates retrieval, recommendation logic,
guardrails, verification, logging, and reliability
testing into one functional application.

## Author

Aditri Tangeti
CodePath AI110 — Applied AI System Final Project
