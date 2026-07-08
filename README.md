# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

This version (VibeMatch) takes a short taste profile — favorite genre, favorite mood, target energy, and whether you like acoustic songs — and scores every song in a small catalog against it. It returns the top 5 matches with a plain-English reason for each one, so you can see exactly why a song got picked.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

Each Song has a genre, mood, energy, tempo, valence, danceability, and acousticness. The UserProfile stores a favorite genre, a favorite mood, a target energy level, and whether the user likes acoustic tracks.

To score a song, the Recommender checks it against those preferences one feature at a time and adds up points: full points if the genre matches, full points if the mood matches, points for energy based on how *close* it is to the user's target (not just how high it is), and points for acousticness depending on whether the user likes acoustic songs or not. Genre and mood count for more than energy and acousticness since they're stronger taste signals. All the songs get sorted by their total score, and the top k many are returned as recommendations, each with a short explanation of why it was picked.

recipe: `score = 2.0*genre_match + 1.5*mood_match + 1.0*energy_closeness + 1.0*acoustic_match`, where genre matches are 2 or 0, mood matches are 1 or 0, and energy/acoustic are 0-1 depending on how close they are to the user's preference.

potential biases: since genre is weighted the heaviest, this system might over-prioritize genre and pass over a song that's a great match on mood and energy but happens to be tagged with a different genre.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Ran `python -m src.main` against three distinct taste profiles defined in `src/main.py`:

**High-Energy Pop** (`favorite_genre=pop, favorite_mood=happy, target_energy=0.9, likes_acoustic=False`)

```
Top 5 Recommendations — High-Energy Pop
=======================================

1. Sunrise City  (by Neon Echo)
   Score: 5.24
     - genre match (+2.0)
     - mood match (+1.5)
     - energy closeness (+0.92)
     - acoustic match (+0.82)

2. Gym Hero  (by Max Pulse)
   Score: 3.92
     - genre match (+2.0)
     - energy closeness (+0.97)
     - acoustic match (+0.95)

3. Rooftop Lights  (by Indigo Parade)
   Score: 3.01
     - mood match (+1.5)
     - energy closeness (+0.86)
     - acoustic match (+0.65)

4. Neon Pulse Rave  (by DJ Kinetic)
   Score: 1.90
     - energy closeness (+0.93)
     - acoustic match (+0.97)

5. Iron Fury  (by Blacksteel)
   Score: 1.90
     - energy closeness (+0.92)
     - acoustic match (+0.98)
```

**Chill Lofi** (`favorite_genre=lofi, favorite_mood=chill, target_energy=0.3, likes_acoustic=True`)

```
Top 5 Recommendations — Chill Lofi
==================================

1. Library Rain  (by Paper Lanterns)
   Score: 5.31
     - genre match (+2.0)
     - mood match (+1.5)
     - energy closeness (+0.95)
     - acoustic match (+0.86)

2. Midnight Coding  (by LoRoom)
   Score: 5.09
     - genre match (+2.0)
     - mood match (+1.5)
     - energy closeness (+0.88)
     - acoustic match (+0.71)

3. Focus Flow  (by LoRoom)
   Score: 3.68
     - genre match (+2.0)
     - energy closeness (+0.90)
     - acoustic match (+0.78)

4. Spacewalk Thoughts  (by Orbit Bloom)
   Score: 3.40
     - mood match (+1.5)
     - energy closeness (+0.98)
     - acoustic match (+0.92)

5. Old Porch Stories  (by Willow Creek)
   Score: 1.88
     - energy closeness (+1.00)
     - acoustic match (+0.88)
```

**Deep Intense Rock** (`favorite_genre=rock, favorite_mood=intense, target_energy=0.9, likes_acoustic=False`)

```
Top 5 Recommendations — Deep Intense Rock
=========================================

1. Storm Runner  (by Voltline)
   Score: 5.39
     - genre match (+2.0)
     - mood match (+1.5)
     - energy closeness (+0.99)
     - acoustic match (+0.90)

2. Gym Hero  (by Max Pulse)
   Score: 3.42
     - mood match (+1.5)
     - energy closeness (+0.97)
     - acoustic match (+0.95)

3. Neon Pulse Rave  (by DJ Kinetic)
   Score: 1.90
     - energy closeness (+0.93)
     - acoustic match (+0.97)

4. Iron Fury  (by Blacksteel)
   Score: 1.90
     - energy closeness (+0.92)
     - acoustic match (+0.98)

5. City Lights Anthem  (by Bassline Kid)
   Score: 1.87
     - energy closeness (+0.95)
     - acoustic match (+0.92)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

I ran three very different profiles (High-Energy Pop, Chill Lofi, Deep Intense Rock) and a "niche" profile with a genre/mood that isn't in the catalog at all. The opposite-vibe profiles (pop vs lofi) shared zero songs in their top 5, which felt right. The niche profile was the interesting one — with no genre/mood to match, every song scored about the same, so the "recommendations" were basically noise instead of a real match. I also noticed the same song ("Gym Hero") kept showing up across different genre profiles just because it's high energy and not acoustic — it was getting partial credit even when the genre or mood didn't fully match.

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

Only 18 songs total, and most genres only have one song each, so there's not much to actually choose from once you narrow by genre. It can't tell "pop" and "indie pop" are related — exact match only, so close-but-not-exact genres get zero credit. Genre and mood are weighted the heaviest, so a song that nails those two can beat out one that's a much better overall fit. Users with a favorite genre/mood not in the catalog basically get random-feeling picks instead of an honest "nothing really matches" answer.

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

Building this showed me a recommender is really just a math formula, it's adding up points based on weights someone picked, and whichever song has the most points wins. There's no real "understanding" of the music happening, just comparisons on a handful of numbers and labels.

Bias exist too. It's not that the code is unfair on purpose, it's that the catalog has way more pop and lofi songs than anything else, and genre happens to be weighted the heaviest. So people who like popular genres get well-matched picks, and people with niche taste get leftovers. The same thing probably happens on real apps: whatever's most common in the data and whatever the engineers decided to weight most ends up shaping what you see, whether that was the intent or not.



