''' This function is used in the server.py file
    and is used to find the emotion scores of
    anger, disgust, fear, joy, and sadness. It
    is also used to find the most dominant emotion.
'''
import json
import requests

def emotion_detector(text_to_analyze):
    ''' This function uses the text_to_analyze parameter to
        return the emotion scores of anger, disgust, fear,
        joy, and sadness. It also decides which emotion is the
        most dominant and returns that as well
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    myobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = myobj, headers = headers)

    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        dominant_emotion = 'anger'
        dominant_emotion_score = anger_score
        if dominant_emotion_score < disgust_score:
            dominant_emotion_score = disgust_score
            dominant_emotion = 'disgust'
        if dominant_emotion_score < fear_score:
            dominant_emotion_score = fear_score
            dominant_emotion = 'fear'
        if dominant_emotion_score < joy_score:
            dominant_emotion_score = joy_score
            dominant_emotion = 'joy'
        if dominant_emotion_score < sadness_score:
            dominant_emotion_score = sadness_score
            dominant_emotion = 'sadness'
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

    return { 'anger': anger_score,
     'disgust': disgust_score, 
     'fear': fear_score, 'joy': joy_score,
     'sadness': sadness_score,
     'dominant_emotion': dominant_emotion
    }
