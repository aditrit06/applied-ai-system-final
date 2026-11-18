"""VibeMatch AI: recommendation and verification workflow."""

import logging
import math
from pathlib import Path

from .guardrails import validate_preferences, valid_song
from .recommender import load_songs, recommend_songs, score_song

logger = logging.getLogger(__name__)


class VibeMatchAI:
    def __init__(self, songs=None, csv_path=None):
        if songs is not None:
            self.songs = list(songs)
        else:
            path = csv_path or (
                Path(__file__).resolve().parents[1] / "data" / "songs.csv"
            )
            self.songs = load_songs(str(path))

        logger.info("Loaded %d songs", len(self.songs))

    def recommend(self, preferences, k=5, disliked_ids=None):
        # 1. Validate user preferences
        prefs = validate_preferences(preferences)

        if type(k) is not int or not 1 <= k <= 20:
            raise ValueError("k must be between 1 and 20")

        disliked = set(disliked_ids or [])

        # 2. Clean the dataset and remove duplicates
        catalog = []
        seen = set()

        for song in self.songs:
            if not valid_song(song):
                logger.warning("Skipping invalid song")
                continue

            if song["id"] in seen:
                logger.warning("Skipping duplicate song")
                continue

            seen.add(song["id"])

            if song["id"] not in disliked:
                catalog.append(song)

        # 3. Retrieve relevant songs
        matching = [
            song for song in catalog
            if song["genre"].lower() == prefs["genre"]
            or song["mood"].lower() == prefs["mood"]
        ]

        candidates = matching if len(matching) >= k else catalog

        # 4. Rank using the original recommendation algorithm
        ranked = recommend_songs(
            prefs, candidates, k=len(candidates)
        )

        # 5. Verify recommendations before displaying
        results = []
        returned_ids = set()

        for song, score, explanation in ranked:
            expected_score, reasons = score_song(prefs, song)
            expected_explanation = "; ".join(reasons)

            verified = (
                valid_song(song)
                and song["id"] not in returned_ids
                and isinstance(score, (int, float))
                and math.isfinite(score)
                and 0 <= score <= 10
                and abs(score - expected_score) < 0.000001
                and explanation == expected_explanation
            )

            if not verified:
                logger.warning("Rejected invalid recommendation")
                continue

            returned_ids.add(song["id"])

            results.append({
                "id": song["id"],
                "title": song["title"],
                "artist": song["artist"],
                "score": round(score, 2),
                "explanation": explanation
            })

            if len(results) == k:
                break

        logger.info("Verified %d recommendations", len(results))
        return results
