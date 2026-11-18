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

<!-- DEMO EVIDENCE START -->
## Reproducible Demo Examples

These examples were captured by running the application.

### Example 1: Recommendations and feedback

**Reproduction command:**
```bash
printf 'pop\nchill\n1\n0.6\n5\n' | python -u -m src.main 2>&1
```

**Actual output:**
```text
================================
       VIBEMATCH AI
  Your Personal Music Assistant
================================

INFO: Loaded 18 songs
Favorite genre (pop, rock, lofi, etc.): Current mood (happy, chill, intense, etc.): Energy level (0 to 1): Positivity level (0 to 1, Enter for 0.6): INFO: Verified 5 recommendations

YOUR PERSONALIZED PLAYLIST

1. Gym Hero by Max Pulse
   Song ID: 5
   Match Score: 6.69/10
   Why: genre match (+4.00); mood does not match (+0.00); energy similarity (+1.86); valence similarity (+0.83)

2. Sunrise City by Neon Echo
   Song ID: 1
   Match Score: 6.40/10
   Why: genre match (+4.00); mood does not match (+0.00); energy similarity (+1.64); valence similarity (+0.76)

3. Midnight Coding by LoRoom
   Song ID: 2
   Match Score: 4.80/10
   Why: genre does not match (+0.00); mood match (+3.00); energy similarity (+0.84); valence similarity (+0.96)

4. Library Rain by Paper Lanterns
   Song ID: 4
   Match Score: 4.70/10
   Why: genre does not match (+0.00); mood match (+3.00); energy similarity (+0.70); valence similarity (+1.00)

5. Spacewalk Thoughts by Orbit Bloom
   Song ID: 6
   Match Score: 4.51/10
   Why: genre does not match (+0.00); mood match (+3.00); energy similarity (+0.56); valence similarity (+0.95)

Enter song IDs you dislike (separated by commas), or press Enter to skip: INFO: Verified 5 recommendations

YOUR UPDATED PLAYLIST

1. Sunrise City by Neon Echo
   Song ID: 1
   Match Score: 6.40/10
   Why: genre match (+4.00); mood does not match (+0.00); energy similarity (+1.64); valence similarity (+0.76)

2. Midnight Coding by LoRoom
   Song ID: 2
   Match Score: 4.80/10
   Why: genre does not match (+0.00); mood match (+3.00); energy similarity (+0.84); valence similarity (+0.96)

3. Library Rain by Paper Lanterns
   Song ID: 4
   Match Score: 4.70/10
   Why: genre does not match (+0.00); mood match (+3.00); energy similarity (+0.70); valence similarity (+1.00)

4. Spacewalk Thoughts by Orbit Bloom
   Song ID: 6
   Match Score: 4.51/10
   Why: genre does not match (+0.00); mood match (+3.00); energy similarity (+0.56); valence similarity (+0.95)

5. Storm Runner by Voltline
   Song ID: 3
   Match Score: 2.70/10
   Why: genre does not match (+0.00); mood does not match (+0.00); energy similarity (+1.82); valence similarity (+0.88)

Thank you for using VibeMatch AI!
```


### Example 2: Different music preferences

**Reproduction command:**
```bash
printf 'rock\nintense\n0.9\n0.4\n\n' | python -u -m src.main 2>&1
```

**Actual output:**
```text
================================
       VIBEMATCH AI
  Your Personal Music Assistant
================================

INFO: Loaded 18 songs
Favorite genre (pop, rock, lofi, etc.): Current mood (happy, chill, intense, etc.): Energy level (0 to 1): Positivity level (0 to 1, Enter for 0.6): INFO: Verified 5 recommendations

YOUR PERSONALIZED PLAYLIST

1. Storm Runner by Voltline
   Song ID: 3
   Match Score: 9.90/10
   Why: genre match (+4.00); mood match (+3.00); energy similarity (+1.98); valence similarity (+0.92)

2. Gym Hero by Max Pulse
   Song ID: 5
   Match Score: 5.57/10
   Why: genre does not match (+0.00); mood match (+3.00); energy similarity (+1.94); valence similarity (+0.63)

3. Iron Echoes by Ash Engine
   Song ID: 18
   Match Score: 2.75/10
   Why: genre does not match (+0.00); mood does not match (+0.00); energy similarity (+1.84); valence similarity (+0.91)

4. Night Drive Loop by Neon Echo
   Song ID: 8
   Match Score: 2.61/10
   Why: genre does not match (+0.00); mood does not match (+0.00); energy similarity (+1.70); valence similarity (+0.91)

5. Concrete Dreams by Metro Verse
   Song ID: 12
   Match Score: 2.48/10
   Why: genre does not match (+0.00); mood does not match (+0.00); energy similarity (+1.78); valence similarity (+0.70)

Enter song IDs you dislike (separated by commas), or press Enter to skip: 
Thank you for using VibeMatch AI!
```


### Example 3: Invalid input guardrail

**Reproduction command:**
```bash
printf 'pop\nhappy\n1.5\n0.6\n' | python -u -m src.main 2>&1
```

**Actual output:**
```text
================================
       VIBEMATCH AI
  Your Personal Music Assistant
================================

INFO: Loaded 18 songs
Favorite genre (pop, rock, lofi, etc.): Current mood (happy, chill, intense, etc.): Energy level (0 to 1): Positivity level (0 to 1, Enter for 0.6): 
Error: energy must be between 0 and 1
```

Full test evidence is in [assets/EXECUTION_LOG.md](assets/EXECUTION_LOG.md).
<!-- DEMO EVIDENCE END -->

## Original Project Attribution

This project extends the CodePath AI110 Module 3
Music Recommender Simulation starter project.

Original repository:
https://github.com/aditrit06/ai110-module3show-musicrecommendersimulation-starter

The original recommender and dataset provided the foundation
for VibeMatch AI. The final project adds an integrated
recommendation workflow, guardrails, verification, feedback,
automated tests, and documentation.

The starter project's original contributors are credited
through the linked source repository.
