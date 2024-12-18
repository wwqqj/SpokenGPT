import json
import os
import uuid

import azure.cognitiveservices.speech as speechsdk


def recognize(file_path):
    speech_config = speechsdk.SpeechConfig(
        subscription=os.getenv('azure_key'),
        region='eastasia',
    )
    speech_config.speech_recognition_language = "en-US"

    audio_config = speechsdk.AudioConfig(filename=file_path)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    result = speech_recognizer.recognize_once_async().get()

    return result.text


def pronuciation_assessment(filename):
    speech_config = speechsdk.SpeechConfig(
        subscription=os.getenv('azure_key'),
        region='eastasia',
    )
    pronunciation_assessment_config = speechsdk.PronunciationAssessmentConfig(
        json_string='{"referenceText":"","gradingSystem":"HundredMark","granularity":"Phoneme","EnableMiscue":true}'
    )
    audio_config = speechsdk.audio.AudioConfig(
        filename=filename
    )
    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config, audio_config=audio_config
    )

    pronunciation_assessment_config.apply_to(speech_recognizer)
    speech_recognition_result = speech_recognizer.recognize_once_async().get()
    # The pronunciation assessment result as a JSON string
    pronunciation_assessment_result_json = speech_recognition_result.properties.get(
        speechsdk.PropertyId.SpeechServiceResponse_JsonResult
    )
    print('打分', pronunciation_assessment_result_json)
    return json.loads(pronunciation_assessment_result_json)["NBest"][0][
            "PronunciationAssessment"
    ]


def speech_synthesis(text, voice='en-US-JaneNeural'):
    speech_config = speechsdk.SpeechConfig(
        subscription=os.getenv('azure_key'),
        region='eastasia',
    )
    path = 'audio/' + uuid.uuid4().hex + '.wav'
    audio_config = speechsdk.audio.AudioOutputConfig(filename=path)
    # The language of the voice that speaks.
    speech_config.speech_synthesis_voice_name = voice
    speech_synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config, audio_config=audio_config
    )
    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()
    return path


