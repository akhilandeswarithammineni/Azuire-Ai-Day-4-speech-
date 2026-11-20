
import azure.cognitiveservices.speech as speechsdk

# Azure Speech configuration
speech_key = " our speech key"
endpoint_url = "our end point URL"

speech_config = speechsdk.SpeechConfig(
    subscription=speech_key,
    endpoint=endpoint_url
)

# Select voice
speech_config.speech_synthesis_voice_name = "en-US-AvaMultilingualNeural"

# Create speech synthesizer
speech_synthesizer = speechsdk.SpeechSynthesizer(
    speech_config=speech_config
)

# Text to speak
text = "hello everyone"

# Generate speech
result = speech_synthesizer.speak_text_async(text).get()

# Check result
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized successfully!")

elif result.reason == speechsdk.ResultReason.Canceled:
    details = result.cancellation_details
    print("Speech synthesis canceled:", details.reason)
    print("Error details:", details.error_details)
