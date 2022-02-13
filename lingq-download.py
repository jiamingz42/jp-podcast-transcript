import requests
import os
import json

from urllib.request import urlretrieve

LINGQ_COOKIES = os.environ['LINGQ_COOKIES']

# Download audio as mp3 and transcript as srt given lesson id
def main():
    # Input Argv
    lesson_id = "7808738"
    lesson_name = "173.ことばの覚え方"

    url = f"https://www.lingq.com/api/v3/ja/lessons/{lesson_id}/"
    response = requests.get(url, headers={"cookie": LINGQ_COOKIES}).json()

    audioUrl = response['audioUrl'] 
    sentences = [t['text'] for text in response['tokenizedText'] for t in text]

    urlretrieve(audioUrl, f"{lesson_name}.mp3")
    print(f"Download {audioUrl} to {lesson_name}.mp3")

    with open(f"{lesson_name}.srt", "w") as f:
        for i, s in enumerate(sentences, 1):
            content = f"{i}\n00:00:00,000 --> 0:00:00,000\n{s}\n\n"
            f.write(content)

main()
