# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

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

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

Loading songs from data/songs.csv...

Top 5 Recommendations
=====================

1. Sunrise City  (by Neon Echo)
   Score: 5.30
     - genre match (+2.0)
     - mood match (+1.5)
     - energy closeness (+0.98)
     - acoustic match (+0.82)

2. Gym Hero  (by Max Pulse)
   Score: 3.82
     - genre match (+2.0)
     - energy closeness (+0.87)
     - acoustic match (+0.95)

3. Rooftop Lights  (by Indigo Parade)
   Score: 3.11
     - mood match (+1.5)
     - energy closeness (+0.96)
     - acoustic match (+0.65)

4. City Lights Anthem  (by Bassline Kid)
   Score: 1.87
     - energy closeness (+0.95)
     - acoustic match (+0.92)

5. Neon Pulse Rave  (by DJ Kinetic)
   Score: 1.80
     - energy closeness (+0.83)
     - acoustic match (+0.97)


**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



