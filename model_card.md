# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

VibeMatch 1.0

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

VibeMatch takes a short taste profile and returns a top 5 list of songs from a small catalog. It assumes the user already knows what they like: a favorite genre, a favorite mood, a target energy level, and whether they like acoustic songs. It's a classroom project, not a real product — the catalog is tiny and made up.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

Every song has a genre, mood, energy level, tempo, and a few other traits like how acoustic it sounds. You tell VibeMatch your favorite genre, favorite mood, target energy, and whether you like acoustic songs. It checks each song against your answers and hands out points: full points if the genre matches, full points if the mood matches, and partial points for energy and acousticness based on how close they are to what you asked for. It adds up the points and shows you the highest scorers. I built this scoring from scratch — the starter code was just empty stubs.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The catalog has 18 songs. I added 8 of them myself to cover genres and moods the starter file didn't have, like hip hop, classical, folk, reggae, EDM, country, metal, and R&B. Even so, most genres only have one song each — only pop and lofi have more than one. There's no lyrics, no language info, and no real listening history, so a lot of what makes up someone's actual taste just isn't captured here.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

It does well when a user's favorite genre actually has more than one song in the catalog, like pop or lofi — the top picks feel right and the reasons make sense. It's also good at telling high-energy and low-energy tastes apart. My "Chill Lofi" and "High-Energy Pop" test profiles shared zero songs in their top 5, which is exactly what should happen for two opposite vibes.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The biggest weakness I found is a filter-bubble effect caused by how heavily genre and mood are weighted (3.5 of the ~5.5 possible points). When I tested a user whose favorite genre and mood actually exist in the catalog (lofi/chill), the top results were clearly personalized and dominated by that exact genre, scoring 5.19–5.31. But when I tested a user with a favorite genre/mood not present in the catalog (like "trap"/"confident"), every song fell back to scoring almost entirely on energy and acousticness, and the top 5 all landed in a narrow 1.60–1.67 range — basically noise, not a real preference match. So users whose taste matches a well-represented genre get reinforced with more of the same, while users with niche or underrepresented tastes get flat, arbitrary-feeling recommendations instead of an honest "we don't have much for you" signal.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

Profiles tested: "High-Energy Pop" (pop, happy, energy 0.9, not acoustic), "Chill Lofi" (lofi, chill, energy 0.3, acoustic), "Deep Intense Rock" (rock, intense, energy 0.9, not acoustic), plus a "niche" profile with a genre/mood that doesn't exist anywhere in the catalog. For each one I checked whether the top 5 actually matched the vibe the profile was going for, and whether the explanation reasons made sense.

What surprised me: I expected the recommender to basically ignore energy and acousticness whenever genre and mood matched, since those are weighted lower. Instead, the opposite problem showed up — a song can climb near the top even when it doesn't match mood at all, as long as it nails genre, energy, and acousticness. I also didn't expect the "niche" profile (no genre/mood match in the catalog) to produce such a flat, almost random-looking list — every song landed within about 0.07 points of each other, which doesn't feel like a real recommendation, just leftover noise.

High-Energy Pop vs. Chill Lofi: Zero overlap in their top 5s. This makes sense — the two profiles want opposite energy levels (0.9 vs. 0.3) and opposite acoustic preferences, so a song that's great for one is almost automatically bad for the other.

High-Energy Pop vs. Deep Intense Rock: These two share 3 of their top 5 songs ("Gym Hero," "Neon Pulse Rave," "Iron Fury"), even though they want completely different genres. That's because both profiles ask for the same high energy (0.9) and non-acoustic sound — so any loud, high-energy, non-acoustic song scores well for *both* profiles regardless of its genre tag. The genre-matched song still comes out on top for each (Sunrise City for pop, Storm Runner for rock), but the "filler" songs underneath are just generically high-energy tracks.

Chill Lofi vs. Deep Intense Rock Zero overlap, same as the first pair — opposite energy targets pull the rankings in completely different directions, which is the expected, sane behavior.
Matched vs. niche profile: A user whose favorite genre/mood exists in the catalog gets a clearly personalized list (scores in the 5.0+ range, all the same genre). A user whose favorite genre/mood doesn't exist gets a flat list of unrelated songs all scoring around 1.6 — the system quietly falls back to ranking by energy/acousticness alone instead of admitting it has no good match.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

I'd add more songs so every genre has a few options, not just one. I'd also let genres count as "close enough" instead of exact matches only, so "pop" and "indie pop" aren't treated as total strangers. It'd help to mix in a bit of variety on purpose so the top 5 isn't just one genre over and over. Longer term, tracking real listening history would let the system learn from other users too, not just the one profile you type in.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

Building this made me realize a recommender isn't smart, it's just adding up points based on rules someone picked. The weights I chose, genre matters most, then mood, then energy and acoustics, directly decided who gets good recommendations and who doesn't. It was surprising how easily bias creeps in without anyone meaning it to — just having more pop songs than other genres in the catalog was enough to make pop fans happier than everyone else. Now when I use Spotify or YouTube, I think less "the algorithm knows me" and more "the algorithm knows whatever data and weights someone built it with."
