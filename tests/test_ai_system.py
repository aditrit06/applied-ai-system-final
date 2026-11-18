"""Reliability tests for VibeMatch AI."""

import pytest
from src.ai_system import VibeMatchAI


@pytest.fixture
def songs():
    return [
        {"id": 1, "title": "Bright Day", "artist": "A",
         "genre": "pop", "mood": "happy",
         "energy": 0.8, "valence": 0.9},
        {"id": 2, "title": "Soft Rain", "artist": "B",
         "genre": "lofi", "mood": "chill",
         "energy": 0.3, "valence": 0.5},
        {"id": 3, "title": "Golden Hour", "artist": "C",
         "genre": "pop", "mood": "happy",
         "energy": 0.7, "valence": 0.8},
        {"id": 4, "title": "Fast Lane", "artist": "D",
         "genre": "rock", "mood": "intense",
         "energy": 0.95, "valence": 0.4}
    ]


@pytest.fixture
def prefs():
    return {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "valence": 0.9
    }


def test_recommendations_work(songs, prefs):
    results = VibeMatchAI(songs=songs).recommend(prefs, k=2)
    assert len(results) == 2
    assert results[0]["id"] == 1


def test_explanations_exist(songs, prefs):
    results = VibeMatchAI(songs=songs).recommend(prefs)
    assert all(r["explanation"] for r in results)


def test_scores_are_valid(songs, prefs):
    results = VibeMatchAI(songs=songs).recommend(prefs)
    assert all(0 <= r["score"] <= 10 for r in results)


@pytest.mark.parametrize("energy", [-1, 2, "high", True])
def test_invalid_energy(songs, prefs, energy):
    with pytest.raises(ValueError):
        VibeMatchAI(songs=songs).recommend(
            {**prefs, "energy": energy}
        )


def test_feedback_removes_disliked_song(songs, prefs):
    app = VibeMatchAI(songs=songs)
    results = app.recommend(prefs, disliked_ids={1})
    assert 1 not in [r["id"] for r in results]


def test_duplicate_songs_removed(songs, prefs):
    app = VibeMatchAI(songs=songs + [songs[0]])
    results = app.recommend(prefs)
    ids = [r["id"] for r in results]
    assert len(ids) == len(set(ids))


def test_empty_catalog(songs, prefs):
    app = VibeMatchAI(songs=[])
    assert app.recommend(prefs) == []


def test_invalid_number_of_recommendations(songs, prefs):
    with pytest.raises(ValueError):
        VibeMatchAI(songs=songs).recommend(prefs, k=0)


def test_consistent_results(songs, prefs):
    app = VibeMatchAI(songs=songs)
    first = app.recommend(prefs)
    second = app.recommend(prefs)
    assert first == second


def test_recommendations_are_ranked(songs, prefs):
    results = VibeMatchAI(songs=songs).recommend(prefs)
    scores = [r["score"] for r in results]
    assert scores == sorted(scores, reverse=True)
