from flask import Flask, request, jsonify
import openai
import logging
import requests

app = Flask(__name__)

# إعداد مفاتيح API مباشرة في الكود
openai.api_key = "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"
deepai_api_key = "76f97ccf-8b48-4fad-b318-1d39ac9a8dc2"

# رابط الفيديو (تأكد من أن هذا الرابط صحيح ويمكن الوصول إليه)
video_url = 'https://drive.google.com/uc?id=1M3-XwNSloN5pn3fuXYACEqJlca-9JcXb'

def analyze_video(video_url):
    response = requests.post(
        "https://api.deepai.org/api/video-recognition",
        data={
            'video': video_url,
        },
        headers={'api-key': deepai_api_key}
    )
    return response.json()

@app.route("/chat", methods=['POST'])
def chat():
    try:
        if request.content_type != 'application/json':
            return jsonify({"response": "Unsupported Media Type: Content-Type must be application/json"}), 415

        incoming_msg = request.json.get('message', '').strip()
        app.logger.debug(f"Received message: {incoming_msg}")

        if not incoming_msg:
            return jsonify({"response": "The message is empty. Please provide a valid message."}), 400

        # تحليل الفيديو باستخدام DeepAI
        analysis_result = analyze_video(video_url)
        app.logger.debug(f"Analysis result: {analysis_result}")

        # معالجة النتائج وإعداد الرد
        if 'output' in analysis_result:
            labels = analysis_result['output']
            if labels:
                answer = "The video contains: " + ", ".join(labels)
            else:
                answer = "No recognizable objects found in the video."
        else:
            answer = "Error analyzing the video. Please try again with a different video."

        app.logger.debug(f"Sending response: {answer}")
        return jsonify({"response": answer})
    except Exception as e:
        app.logger.error(f"Error: {str(e)}", exc_info=True)
        return jsonify({"response": "Sorry, an error occurred. Please try again later."}), 500

if __name__ == "__main__":
    app.run(debug=True)
