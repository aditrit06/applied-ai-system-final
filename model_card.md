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

## Reflection: AI Collaboration

I used ChatGPT to help me extend my original Module 3
music recommender into a complete applied AI system.

ChatGPT helped me organize my Python modules, develop
guardrails, create reliability tests, and improve my
documentation.

I copied the suggested code into VS Code and tested it
myself. When the initial terminal paste failed, I had
to troubleshoot the issue and create the files separately.

I also manually tested the recommendation system and
confirmed that disliking a song changed the playlist.

AI was useful for speeding up development, but I still
needed to run the code, review the results, and verify
that the application behaved as expected.

## Reflection: Bias and Responsible AI

My system has some limitations related to dataset bias.

Because I only have 18 songs, certain genres and moods
may be represented more than others. The scoring system
also assigns more weight to genre and mood matching,
which may not reflect every user's preferences.

I tried to make the system more transparent by including
explanations for each recommendation.

The application also validates inputs and verifies
recommendations before displaying them.

## Reflection: Testing and Results

I used pytest to evaluate recommendation behavior,
input validation, score accuracy, duplicate prevention,
feedback handling, and consistency.

My earlier local evaluation passed 15 tests.

I also manually entered different preferences and
confirmed that the application generated recommendations
and updated them when I disliked a song.

These tests help establish reliability for the tested
scenarios. However, they do not prove that users will
always enjoy the recommended songs.

## Reflection: What I Learned

This project taught me that building a useful AI-related
application involves more than generating an answer.

I learned how important it is to validate information,
explain system decisions, test edge cases, and involve
users in the process.

If I continued improving this project, I would focus
on expanding the dataset and developing more advanced
personalization features.
