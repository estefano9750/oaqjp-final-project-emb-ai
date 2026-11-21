import requests

API_URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
MODEL_ID = "emotion_aggregated-workflow_lang_en_stock"


def emotion_detector(text_to_analyze):
    """Return emotion scores and the dominant emotion for the supplied text."""
    empty_result = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }

    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return empty_result

    headers = {"grpc-metadata-mm-model-id": MODEL_ID}
    data = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(API_URL, headers=headers, json=data, timeout=30)
        if response.status_code != 200:
            return empty_result

        result = response.json()
        emotions = result["emotionPredictions"][0]["emotion"]
        scores = {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"]
        }
        scores["dominant_emotion"] = max(scores, key=scores.get)
        return scores

    except (requests.RequestException, ValueError, KeyError, IndexError, TypeError):
        return empty_result
