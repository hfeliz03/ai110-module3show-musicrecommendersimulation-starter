"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    user_profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.8,
            "likes_acoustic": False,
        },
        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.35,
            "likes_acoustic": True,
        },
        "Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.95,
            "likes_acoustic": False,
        },
        "Adversarial: High Energy But Sad": {
            "genre": "pop",
            "mood": "sad",
            "energy": 0.9,
            "likes_acoustic": False,
        },
        "Edge Case: Acoustic Metal": {
            "genre": "metal",
            "mood": "dreamy",
            "energy": 0.2,
            "likes_acoustic": True,
        },
    }

    for profile_name, user_prefs in user_profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\n=== {profile_name} ===")
        print(f"Preferences: {user_prefs}\n")
        print("Top Recommendations:\n")
        print(f"{'Title':<30} {'Score':<10} {'Reason'}")
        print("-" * 60)

        for song, score, explanation in recommendations:
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()
