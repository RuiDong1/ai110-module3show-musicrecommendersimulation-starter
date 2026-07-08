# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agentic Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I asked Claude to implement the actual scoring logic (the TODOs in `recommender.py`), get the CLI running end to end, clean up the terminal output, and then help me test it against a few different taste profiles and write up what I found in the README and model card.

**Prompts used:**

"Walk me through the tradeoffs between linear  and Gaussian for scoring numerical features like energy"
"If I wanted to let related genres (like 'pop' and 'indie pop') partially match instead of requiring an exact string match, how would I redesign the genre scoring?"

**What did the agent generate or change?**

It filled in `load_songs`, `score_song`, `recommend_songs`, and the `Recommender` class in `src/recommender.py`; added three test profiles to `src/main.py` and reformatted the terminal output;

**What did you verify or fix manually?**

I actually ran `python -m src.main` and `pytest` myself rather than trusting the agent's word that things worked. That's how we caught two real bugs: `main.py` was importing `recommender` instead of `src.recommender` so the documented run command crashed, and plain `pytest` failed with a `ModuleNotFoundError` because it wasn't adding the project root to the path (fixed with a `pytest.ini`). I also had it re-run the bias analysis with real numbers pulled from the catalog instead of a made-up example.

---

## Design Pattern (SF10)

> Document how AI helped you choose or implement a design pattern.

**Which design pattern did you use?**

<!-- e.g., Strategy, Factory, Observer, etc. -->

**How did AI help you brainstorm or implement it?**

<!-- Describe the conversation or suggestions that led to your decision -->

**How does the pattern appear in your final code?**

<!-- Point to the relevant class or method -->
