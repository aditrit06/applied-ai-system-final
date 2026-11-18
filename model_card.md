# VibeMatch AI — Model Card

## System Overview
VibeMatch AI is an explainable, rule-based music recommendation system developed for the CodePath AI110 final project.

It extends my Module 3 Music Recommender Simulation with integrated guardrails, verification, logging, automated reliability testing, and user feedback.

## How It Works
The system uses content-based filtering to recommend songs based on four preferences:

- Genre match: up to 4 points
- Mood match: up to 3 points
- Energy similarity: up to 2 points
- Valence similarity: up to 1 point

The total possible score is 10.

This is a deterministic scoring system, not a trained machine-learning model or generative AI model.

## Intended Use
The system is intended for personal music exploration, educational demonstrations, and explainable recommendation experiments.

## Data
The application currently uses a sample CSV dataset containing 18 songs.

## Reliability and Safety
The application includes:
- Input validation
- Song metadata verification
- Duplicate prevention
- Score and explanation verification
- Logging and error handling
- Feedback-based song exclusion

## Testing
The latest local evaluation reported 15 passing automated tests and zero failures.

Manual testing confirmed that disliked songs were excluded when generating updated recommendations.

## Human-in-the-Loop
Users can identify songs they dislike and request an updated playlist. Feedback changes the recommendations during the current session.

## Limitations
The dataset is small and may not represent every genre or mood. Recommendations depend on manually assigned song metadata and fixed scoring rules.

The application does not learn from feedback or store user preferences permanently.

Passing automated tests demonstrates correctness for tested cases, not guaranteed listener satisfaction.

## Future Improvements
Future work could include a larger dataset, persistent preferences, natural-language requests, and learned recommendation models.

## Responsible Design
VibeMatch AI prioritizes understandable explanations, input validation, transparent limitations, and user control.
