from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """Show the emotion detection page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """Analyze the text received from the browser."""
    text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze.strip():
        return "Please enter some text to analyze.", 400

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Emotion analysis is unavailable. Please try again later.", 502

    response = (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response, 200


@app.errorhandler(404)
def page_not_found(error):
    """Return a simple message for unknown pages."""
    return "Page not found.", 404


@app.errorhandler(500)
def internal_error(error):
    """Return a simple message for server errors."""
    return "An internal server error occurred.", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
