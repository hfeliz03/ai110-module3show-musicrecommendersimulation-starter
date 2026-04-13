import csv
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

# Reads the CSV catalog and converts numeric fields into Python numbers.
def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    print(f"Loading songs from {csv_path}...")
    songs: List[Dict] = []
    int_fields = {"id"}
    float_fields = {"energy", "tempo_bpm", "valence", "danceability", "acousticness"}
    path = Path(csv_path)

    if not path.is_file():
        project_root = Path(__file__).resolve().parent.parent
        path = project_root / csv_path

    with path.open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        append_song = songs.append
        for row in reader:
            for field in int_fields:
                row[field] = int(row[field])
            for field in float_fields:
                row[field] = float(row[field])
            append_song(row)

    return songs

# Computes a weighted score and explanation list for one song and one user profile.
def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons = []

    # Award points for genre match
    if user_prefs["favorite_genre"].lower() == song["genre"].lower():
        score += 2.0
        reasons.append("genre match (+2.0)")

    # Award points for mood match
    if user_prefs["favorite_mood"].lower() == song["mood"].lower():
        score += 1.5
        reasons.append("mood match (+1.5)")

    # Calculate score for energy preference
    energy_diff = abs(user_prefs["target_energy"] - song["energy"])
    energy_score = max(0, 1.0 - energy_diff)  # Closer energy gets higher score
    score += energy_score
    reasons.append(f"energy match (+{energy_score:.2f})")

    # Award points for acoustic preference
    if user_prefs["likes_acoustic"] and song["acousticness"] > 0.5:
        score += 1.0
        reasons.append("acoustic preference match (+1.0)")
    elif not user_prefs["likes_acoustic"] and song["acousticness"] <= 0.5:
        score += 0.5
        reasons.append("non-acoustic preference match (+0.5)")

    return score, reasons

# Scores every song, sorts the catalog by score, and returns the top matches.
def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    normalized_prefs = {
        "favorite_genre": user_prefs.get("favorite_genre", user_prefs.get("genre", "")),
        "favorite_mood": user_prefs.get("favorite_mood", user_prefs.get("mood", "")),
        "target_energy": user_prefs.get("target_energy", user_prefs.get("energy", 0.0)),
        "likes_acoustic": user_prefs.get("likes_acoustic", False),
    }

    ranked_songs = sorted(
        (
            (song, score, ", ".join(reasons))
            for song in songs
            for score, reasons in [score_song(normalized_prefs, song)]
        ),
        key=lambda recommendation: recommendation[1],
        reverse=True,
    )

    return ranked_songs[:k]
