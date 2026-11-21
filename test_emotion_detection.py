import unittest
from unittest.mock import Mock, patch

from emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    @patch("emotion_detection.requests.post")
    def test_successful_detection(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.1,
                    "disgust": 0.2,
                    "fear": 0.05,
                    "joy": 0.6,
                    "sadness": 0.05
                }
            }]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("I am very happy")
        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(result["joy"], 0.6)

    @patch("emotion_detection.requests.post")
    def test_service_error(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 500
        mock_post.return_value = mock_response

        result = emotion_detector("Some text")
        self.assertIsNone(result["dominant_emotion"])

    def test_empty_text(self):
        result = emotion_detector("   ")
        self.assertIsNone(result["dominant_emotion"])

    @patch("emotion_detection.requests.post")
    def test_invalid_response(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}
        mock_post.return_value = mock_response

        result = emotion_detector("Some text")
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
