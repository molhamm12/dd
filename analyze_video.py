import requests

# استبدل بـ مفتاح API الخاص بك من DeepAI
api_key = '76f97ccf-8b48-4fad-b318-1d39ac9a8dc2'

def analyze_video(video_url):
    response = requests.post(
        "https://api.deepai.org/api/video-recognition",
        data={
            'video': video_url,
        },
        headers={'api-key': api_key}
    )
    return response.json()

# استبدل بـ URL للفيديو الخاص بك من Google Drive
video_url = 'https://drive.google.com/uc?id=1M3-XwNSloN5pn3fuXYACEqJlca-9JcXb'
result = analyze_video(video_url)
print(result)
