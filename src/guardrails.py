"""Safety checks for VibeMatch AI."""

import math


def validate_preferences(prefs):
    if not isinstance(prefs, dict):
        raise ValueError("Preferences must be a dictionary.")

    cleaned = {}

    for key in ("genre", "mood"):
        value = prefs.get(key)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Invalid {key}")
        cleaned[key] = value.strip().lower()

    for key in ("energy", "valence"):
        value = prefs.get(key, 0.6 if key == "valence" else None)
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(f"Invalid {key}")
        if not math.isfinite(value) or not 0 <= value <= 1:
            raise ValueError(f"{key} must be between 0 and 1")
        cleaned[key] = float(value)

    return cleaned


def valid_song(song):
    if not isinstance(song, dict):
        return False

    if type(song.get("id")) is not int:
        return False

    for key in ("title", "artist", "genre", "mood"):
        if not isinstance(song.get(key), str) or not song[key].strip():
            return False

    for key in ("energy", "valence"):
        value = song.get(key)
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            return False
        if not math.isfinite(value) or not 0 <= value <= 1:
            return False

    return True
