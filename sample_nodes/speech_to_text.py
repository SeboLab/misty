from misty_ros.msg import CaptureSpeech, AssetRequest, AudioFile
import rospy


# Example translating speech to text using the Google API
# https://cloud.google.com/speech-to-text/docs/libraries#client-libraries-install-python

def main():
    speech_pub = Publisher("/audio/speech/capture", CaptureSpeech)
    speech_pub.publish(False, True, 7500, 5000)

    Subscriber("/audio/get/results", AudioFile, translate_to_text)
    audio_get_pub = Publisher("/audio/get", AssetRequest)
    audio_get_pub.publish("capture_Dialogue.wav", True)

def translate_to_text(params):

    from google.cloud import speech
    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(params.data["base64"])
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))

if __name__ == "__main__":
    rospy.init_node("misty_demo")

    main()
