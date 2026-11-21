# Emotion Detection Application

A Flask web application that analyzes text with the IBM Watson NLP emotion prediction service.

## Features

- Detects anger, disgust, fear, joy, and sadness.
- Reports the dominant emotion.
- Provides a browser interface.
- Handles empty input and service errors.
- Includes automated unit tests and static analysis.

## Install and run

Python 3.9 or newer and internet access to the Watson NLP service are required.

\`\`\`bash
python3 -m pip install -r requirements.txt
python3 server.py
\`\`\`

Open http://127.0.0.1:5000 in your browser.

## Run tests

\`\`\`bash
python3 -m unittest -v
\`\`\`

## Install as a Python package

\`\`\`bash
python3 -m pip install .
\`\`\`

The detector is packaged in \`EmotionDetection\` and can be imported with:

\`\`\`python
from EmotionDetection import emotion_detector
\`\`\`

## Static code analysis

\`\`\`bash
python3 -m pip install pylint
python3 -m pylint --errors-only EmotionDetection server.py
\`\`\`

A GitHub Actions workflow runs unit tests and Pylint on pushes and pull requests to \`main\`.

## Deployment

The \`Procfile\` starts the application with Gunicorn:

\`\`\`text
web: gunicorn server:app
\`\`\`

Configure a Python hosting platform to install dependencies from \`requirements.txt\` and use the Procfile start command.

## Watson NLP service

The application sends text to the Watson NLP EmotionPredict endpoint using the \`emotion_aggregated-workflow_lang_en_stock\` model. Live predictions require the service to be reachable.
