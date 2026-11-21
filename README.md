# Emotion Detection Application

A small Flask web application that analyzes a sentence with the IBM Watson NLP emotion prediction service.

## Features

- Detects anger, disgust, fear, joy, and sadness.
- Reports the dominant emotion.
- Provides a browser interface.
- Handles empty input and service errors.
- Includes automated unit tests.

## Requirements

Python 3.9 or newer and an internet connection to reach the Watson NLP service.

## Install and run

\`\`\`bash
python3 -m pip install -r requirements.txt
python3 server.py
\`\`\`

Open http://127.0.0.1:5000 in your browser.

## Run tests

\`\`\`bash
python3 -m unittest -v
\`\`\`

## Static code analysis

Install and run Pylint:

\`\`\`bash
python3 -m pip install pylint
python3 -m pylint emotion_detection.py server.py
\`\`\`

## Deployment

The included Procfile starts the Flask application with Gunicorn:

\`\`\`text
web: gunicorn server:app
\`\`\`

Configure the deployment platform to install dependencies from \`requirements.txt\`.

## Watson NLP service

The application sends the input text to the Watson NLP EmotionPredict endpoint using the model identifier \`emotion_aggregated-workflow_lang_en_stock\`. The service must be reachable for live emotion predictions.
