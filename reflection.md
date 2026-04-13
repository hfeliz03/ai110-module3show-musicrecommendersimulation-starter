# Reflection on Profile Comparisons

I tested five profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, Adversarial: High Energy But Sad, and Edge Case: Acoustic Metal. Looking at them side by side helped me understand what the recommender is really paying attention to.

High-Energy Pop vs Chill Lofi: The pop profile pushes the list toward louder, more upbeat songs like "Sunrise City" and "Gym Hero," while the lofi profile shifts toward softer and more acoustic songs like "Library Rain" and "Midnight Coding." This makes sense because the lofi user asks for lower energy and more acoustic sound.

High-Energy Pop vs Deep Intense Rock: Both profiles share a preference for high energy, so some energetic songs overlap, but the rock profile moves "Storm Runner" to the top because the genre match becomes more important. This shows why "Gym Hero" can still appear for both users: it matches the energy target even when the genre is not perfect.

High-Energy Pop vs Adversarial: High Energy But Sad: These two profiles are very close because both want pop and high energy, so many of the same songs appear. The interesting part is that the "sad" request does not change much, which tells me the system is not very good at handling emotional contradictions or missing moods in the dataset.

High-Energy Pop vs Edge Case: Acoustic Metal: The pop profile prefers bright, non-acoustic songs, while the acoustic metal profile pulls the results toward quieter and more acoustic tracks. This difference makes sense because the second user is asking for a very unusual mix, so the recommender tries to satisfy acousticness and low energy even when the genre match is weak.

Chill Lofi vs Deep Intense Rock: These two profiles split the catalog in a clear way. Chill Lofi favors calm, acoustic, low-energy songs, while Deep Intense Rock favors louder, more aggressive songs with high energy. The outputs make sense because the two users are asking for opposite listening moods.

Chill Lofi vs Adversarial: High Energy But Sad: The lofi profile leads to gentle songs, but the adversarial profile still gets very energetic songs like "Gym Hero." That makes sense because the second profile asks for high energy, and the current scoring system treats that strong numeric match as more important than the emotional mismatch.

Chill Lofi vs Edge Case: Acoustic Metal: These two profiles overlap more than I expected because both like acoustic songs and lower energy. Even though one asks for lofi and the other asks for metal, their outputs share some quieter tracks, which shows the recommender can be pulled strongly by acousticness and energy.

Deep Intense Rock vs Adversarial: High Energy But Sad: These two profiles both ask for high energy, so they share songs like "Gym Hero," "Storm Runner," and "Iron Anthem." This makes sense numerically, but it also shows a weakness: the system hears "high energy" loudly and does not understand that "sad" should probably push the results in a different emotional direction.

Deep Intense Rock vs Edge Case: Acoustic Metal: Both profiles mention metal or rock-like intensity, but the acoustic metal profile lowers the energy target and asks for acoustic songs, so the results become softer and stranger. This makes sense because the second profile is testing whether the system can handle conflicting signals instead of one clean genre stereotype.

Adversarial: High Energy But Sad vs Edge Case: Acoustic Metal: These are both stress tests, but they stress the model in different ways. The high-energy sad profile proves the model can keep recommending energetic songs even when the mood request is awkward, while the acoustic metal profile proves the model can be split between genre and sound texture. In plain language, this is why "Gym Hero" keeps showing up: the system sees that it is close on energy and not acoustic, so it keeps rewarding it even when the rest of the vibe is questionable.
