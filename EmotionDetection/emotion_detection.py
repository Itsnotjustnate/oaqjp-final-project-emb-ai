import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    myobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = myobj, headers = headers)

    formatted_response = json.loads(response.text)

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
      
    return { 'anger': anger_score, 
     'disgust': disgust_score, 
     'fear': fear_score, 'joy': joy_score,
     'sadness': sadness_score,
     'dominant_emotion': dominant_emotion
    }