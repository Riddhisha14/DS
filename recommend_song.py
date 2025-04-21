import pandas as pd
import random
import os
from PIL import Image

df = pd.read_csv("tamil_music_recommendations.csv")

emoji_map = {
    "倀": "😊",
    "倔": "💪",
    "倓": "😃",
    "倘": "🎷",
    "倖": "😌",
    "候": "🌙",
    "倜": "😢"
}
df['mood'] = df['mood'].replace(emoji_map)

df.to_csv("tamil_music_fixed.csv", index=False)

def recommend_music(emoji, listening_time):
    filtered_songs = df[(df['mood'] == emoji) & (df['time'] == listening_time.lower())]
    if not filtered_songs.empty:
        recommendation = filtered_songs.sample(n=1).iloc[0]
        print("\n🎵 Recommended Tamil Song 🎵")
        print(f"Song: {recommendation['song']}")
        print(f"Genre: {recommendation['genre']}")
        print(f"Time: {recommendation['time']}")
    else:    
        print("❌ No recommendations found for this mood and time. Try another combination.")

print("🎧 Tamil Song Recommender")
user_emoji = input("Enter your mood emoji (😊, 😌, 😃, 😢, 💪, 🌙, 🎷): ").strip()
listening_time = input("Enter time of day (morning/afternoon/evening/night): ").strip()

recommend_music(user_emoji, listening_time)
