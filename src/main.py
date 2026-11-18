"""Interactive VibeMatch AI music recommender."""

import logging
from .ai_system import VibeMatchAI


def show_recommendations(results):
    if not results:
        print("\nNo songs found. Try different preferences.")
        return

    for number, song in enumerate(results, 1):
        print(f"\n{number}. {song['title']} by {song['artist']}")
        print(f"   Song ID: {song['id']}")
        print(f"   Match Score: {song['score']:.2f}/10")
        print(f"   Why: {song['explanation']}")


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s"
    )

    print("\n================================")
    print("       VIBEMATCH AI")
    print("  Your Personal Music Assistant")
    print("================================\n")

    try:
        app = VibeMatchAI()

        genre = input("Favorite genre (pop, rock, lofi, etc.): ")
        mood = input("Current mood (happy, chill, intense, etc.): ")
        energy = float(input("Energy level (0 to 1): "))

        valence_input = input(
            "Positivity level (0 to 1, Enter for 0.6): "
        )
        valence = float(valence_input) if valence_input else 0.6

        preferences = {
            "genre": genre,
            "mood": mood,
            "energy": energy,
            "valence": valence
        }

        results = app.recommend(preferences, k=5)

        print("\nYOUR PERSONALIZED PLAYLIST")
        show_recommendations(results)

        if results:
            feedback = input(
                "\nEnter song IDs you dislike "
                "(separated by commas), or press Enter to skip: "
            )

            if feedback.strip():
                disliked_ids = {
                    int(item.strip())
                    for item in feedback.split(",")
                }

                updated = app.recommend(
                    preferences,
                    k=5,
                    disliked_ids=disliked_ids
                )

                print("\nYOUR UPDATED PLAYLIST")
                show_recommendations(updated)

        print("\nThank you for using VibeMatch AI!")

    except (ValueError, FileNotFoundError) as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()
