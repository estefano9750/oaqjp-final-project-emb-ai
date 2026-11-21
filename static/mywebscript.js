async function RunSentimentAnalysis() {
    const textToAnalyze = document.getElementById("textToAnalyze").value.trim();
    const responseArea = document.getElementById("system_response");
    const button = document.getElementById("analyzeButton");

    if (!textToAnalyze) {
        responseArea.textContent = "Please enter some text to analyze.";
        return;
    }

    button.disabled = true;
    responseArea.textContent = "Analyzing...";

    try {
        const params = new URLSearchParams({ textToAnalyze: textToAnalyze });
        const response = await fetch("/emotionDetector?" + params.toString());
        const message = await response.text();

        if (!response.ok) {
            responseArea.textContent = message;
        } else {
            responseArea.textContent = message;
        }
    } catch (error) {
        responseArea.textContent = "Could not connect to the application. Please try again.";
    } finally {
        button.disabled = false;
    }
}
