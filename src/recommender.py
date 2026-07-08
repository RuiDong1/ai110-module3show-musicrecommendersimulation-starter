import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

GENRE_WEIGHT = 2.0
MOOD_WEIGHT = 1.5
ENERGY_WEIGHT = 1.0
ACOUSTIC_WEIGHT = 1.0


def closeness_score(value: float, target: float, max_range: float = 1.0) -> float:
    """Score is 1.0 when value == target, decreasing linearly as distance grows."""
    distance = abs(value - target)
    return max(0.0, 1.0 - (distance / max_range))

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
        """Store the song catalog this recommender will rank."""
        self.songs = songs

    def _score(self, user: UserProfile, song: Song) -> float:
        """Compute a weighted match score between a user and a song."""
        genre_match = 2.0 if song.genre == user.favorite_genre else 0.0
        mood_match = 1.0 if song.mood == user.favorite_mood else 0.0
        energy_match = closeness_score(song.energy, user.target_energy)
        acoustic_match = (
            song.acousticness if user.likes_acoustic else (1.0 - song.acousticness)
        )

        return (
            GENRE_WEIGHT * genre_match
            + MOOD_WEIGHT * mood_match
            + ENERGY_WEIGHT * energy_match
            + ACOUSTIC_WEIGHT * acoustic_match
        )

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top k songs for a user, ranked highest score first."""
        ranked = sorted(self.songs, key=lambda song: self._score(user, song), reverse=True)
        return ranked[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Build a human-readable explanation of why a song scored the way it did."""
        reasons = []
        if song.genre == user.favorite_genre:
            reasons.append(f"genre match (+{GENRE_WEIGHT:.1f})")
        if song.mood == user.favorite_mood:
            reasons.append(f"mood match (+{MOOD_WEIGHT:.1f})")

        energy_points = ENERGY_WEIGHT * closeness_score(song.energy, user.target_energy)
        reasons.append(f"energy closeness (+{energy_points:.2f})")

        acoustic_match = song.acousticness if user.likes_acoustic else (1.0 - song.acousticness)
        acoustic_points = ACOUSTIC_WEIGHT * acoustic_match
        reasons.append(f"acoustic match (+{acoustic_points:.2f})")

        return "Recommended because of: " + ", ".join(reasons) + "."

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    print(f"Loading songs from {csv_path}...")
    numeric_fields = {"energy", "tempo_bpm", "valence", "danceability", "acousticness"}
    songs = []
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            for field in numeric_fields:
                row[field] = float(row[field])
            row["id"] = int(row["id"])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    reasons = []
    score = 0.0

    if song["genre"] == user_prefs.get("favorite_genre"):
        score += GENRE_WEIGHT
        reasons.append(f"genre match (+{GENRE_WEIGHT:.1f})")

    if song["mood"] == user_prefs.get("favorite_mood"):
        score += MOOD_WEIGHT
        reasons.append(f"mood match (+{MOOD_WEIGHT:.1f})")

    target_energy = user_prefs.get("target_energy")
    if target_energy is not None:
        energy_match = closeness_score(song["energy"], target_energy)
        points = ENERGY_WEIGHT * energy_match
        score += points
        reasons.append(f"energy closeness (+{points:.2f})")

    likes_acoustic = user_prefs.get("likes_acoustic")
    if likes_acoustic is not None:
        acoustic_match = song["acousticness"] if likes_acoustic else (1.0 - song["acousticness"])
        points = ACOUSTIC_WEIGHT * acoustic_match
        score += points
        reasons.append(f"acoustic match (+{points:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons) if reasons else "no strong preference match found"
        scored.append((song, score, explanation))

    scored.sort(key=lambda item: item[1], reverse=True)
    return scored[:k]
