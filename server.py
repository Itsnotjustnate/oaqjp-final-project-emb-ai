''' Executing this function initiates the application of
    emotion detection to be executed and deployed on
    localhost:5000
'''
from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    ''' This function receives the text from the HTML interface 
        and runs the emotional detector. The output returned shows
        the emotions, anger, disgust, fear, joy, and sadness, while
        also displaying the dominant emotion.
    '''
    text_to_detect = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_detect)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return {f"For the given statement, the system response is 'anger': {anger}, 'disgust':" +
            f"{disgust}, 'fear': {fear}, 'joy': {joy}, " +
            f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}"}

@app.route("/")
def render_index_page():
    ''' This function renders the index page for the root URL ("/"). '''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
