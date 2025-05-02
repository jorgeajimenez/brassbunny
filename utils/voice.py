import requests

url = "https://users.rime.ai/v1/rime-tts"

payload = {
    "speaker": "Luna",
    "text": "Citalopram can cause issues.",
    "modelId": "arcana",
    "repetition_penalty": 1.5,
    "temperature": 0.5,
    "top_p": 0.5,
    "max_tokens": 1200
}
headers = {
    "Accept": "audio/mp3",
    "Authorization": "Bearer PqFICVW-eV8x8ZGfi1m-NfhkwRiE4wnCzx_sj9HI4Cw	",
    "Content-Type": "application/json"
}

# Use stream=True to handle streaming response
response = requests.request("POST", url, json=payload, headers=headers, stream=True)

# Check if the request was successful
if response.status_code == 200:
    with open("audio_output.mp3", "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
else:
    print("Error:", response.status_code)

print(response.text)