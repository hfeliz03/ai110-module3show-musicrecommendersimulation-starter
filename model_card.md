# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeFinder 1.0**

---

## 2. Intended Use  

This recommender suggests songs from a small class dataset. It tries to match a user's favorite genre, mood, energy level, and acoustic preference. It is made for classroom exploration and learning. It is not meant for real music streaming users or high-stakes decisions.

---

## 3. How the Model Works  

The model looks at each song one by one. It gives points if the genre matches and if the song is close to the user's target energy. It also gives points when the acousticness matches the user's preference. In one experiment, I turned off the mood bonus to see how much mood affected the rankings. After scoring every song, the system sorts the list and returns the top matches.

---

## 4. Data  

The dataset has 18 songs. Each song has a title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness. The catalog includes styles like pop, lofi, rock, metal, ambient, jazz, hip hop, house, and folk. The dataset is very small, so many kinds of music taste are missing. Some moods and genre combinations are also underrepresented.

---

## 5. Strengths  

The system works best for simple profiles with clear preferences. It did a good job for High-Energy Pop, Chill Lofi, and Deep Intense Rock. In those cases, the top songs mostly matched the expected vibe. The scoring is also easy to explain because each recommendation has a reason.

---

## 6. Limitations and Bias 

The system can over-focus on genre and energy. That can create a small filter bubble where the same songs keep showing up. "Gym Hero" appeared often because it matches high energy well, even when the rest of the vibe was not right. The dataset is also small, so users with unusual tastes do not get many good options. This means the system may feel repetitive or unfair for people whose preferences do not fit the catalog.

---

## 7. Evaluation  

I tested five profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, Adversarial: High Energy But Sad, and Edge Case: Acoustic Metal. I compared the top five songs for each profile and checked whether the results matched the user's vibe. I also tried an experiment where I removed the mood bonus from scoring. The biggest surprise was that "Gym Hero" kept showing up for profiles that only partly matched it. That showed me the system can reward one strong feature too much.

---

## 8. Future Work  

I would add more songs and more kinds of moods. I would tune the weights so one feature does not dominate the whole result. I would also add a diversity rule so the top five songs are less repetitive.

---

## 9. Personal Reflection  

My biggest learning moment was seeing how one small scoring rule could change the whole feel of the recommender. When I removed the mood bonus, the results became less personal and more repetitive. That helped me understand that building a system is not just about making it run. It is also about checking whether the logic matches what a real person means.

AI tools helped me move faster when I was writing code, fixing imports, and organizing my files. They were especially helpful for turning ideas into working steps. But I still had to double-check the outputs and think about whether the recommendations actually made sense. The code could run and still give results that felt wrong for the user.

What surprised me most is that a simple algorithm can still feel like a recommendation system. Even a few scoring rules can create results that look thoughtful at first. At the same time, that feeling can be misleading, because the system may only be matching one or two features really well.

If I extended this project, I would add more user preference types and a larger song catalog. I would also test ways to increase diversity so the same songs do not appear too often. I would want the recommender to balance accuracy with variety, so it feels both useful and less repetitive.
