import numpy as np

# users x songs
# higher number = stronger engagement
R = np.array([
    [5, 4, 0, 0, 1],  # User 0
    [4, 5, 0, 1, 0],  # User 1
    [0, 0, 5, 4, 0],  # User 2
    [0, 1, 4, 5, 0],  # User 3
    [3, 4, 0, 0, 1],  # User 4
])

song_vectors = R.T

def cosine_similarity(a, b):
    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )

target_song = 0

scores = []
for i in range(len(song_vectors)):
    if i != target_song:
        sim = cosine_similarity(
            song_vectors[target_song],
            song_vectors[i]
        )
        scores.append((i, sim))

scores.sort(key=lambda x: x[1], reverse=True)
print(scores)

user_id = 0

# songs user already interacted with
user_history = R[user_id]

# find strongest song they liked
seed_song = np.argmax(user_history)

# recommend similar songs
recommendations = [
    song for song, _ in scores
    if user_history[song] == 0
]

print(recommendations)


"""
Breakdown:

np.dot(a,b) → measures how much the vectors point in the same direction
Big numbers, small numbers, doesn’t matter
If users who liked Song 0 also liked Song 1, dot product is big

np.linalg.norm(a) → length of vector a
Basically: “how big a vector is overall”
Prevents a super-popular song from dominating

Dividing by norms → normalizes vectors
Makes comparison about pattern, not magnitude

Analogy:
Two users both like the same songs but one listens twice as much. Cosine similarity says: “same taste” ignoring total plays.

3️⃣ How it applies to our songs
Song 0 = [5,4,0,0,3]
Song 1 = [4,5,0,1,4]

Look at user-by-user interactions:
User 0: 5 vs 4 → similar
User 1: 4 vs 5 → similar
User 2: 0 vs 0 → same
User 3: 0 vs 1 → small difference
User 4: 3 vs 4 → similar

Dot product = sum of (corresponding users multiplied):

5*4 + 4*5 + 0*0 + 0*1 + 3*4 = 20 + 20 + 0 + 0 + 12 = 52

Norms:
||Song0|| = sqrt(5^2 + 4^2 + 0^2 + 0^2 + 3^2) = sqrt(25+16+0+0+9)=sqrt(50)≈7.07
||Song1|| = sqrt(4^2 +5^2 +0+1+16)=sqrt(16+25+0+1+16)=sqrt(58)≈7.62

Cosine similarity = 52 / (7.07 * 7.62) ≈ 0.96 → very similar
✅ This is your (0,0.98) in the example
"""