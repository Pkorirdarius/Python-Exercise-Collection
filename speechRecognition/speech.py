# fuction transcribes users words into text
import streamlit as st
import speech_recognition as sr
import time

# Define a dictionary to map API names to their corresponding functions
API_FUNCTIONS = {
    "Google Speech Recognition": sr.Recognizer().recognize_google,
    "Microsoft Azure Speech Services": sr.Recognizer().recognize_azure,
    "IBM Speech to Text": sr.Recognizer().recognize_ibm,
    "Houndify Speech Recognition": sr.Recognizer().recognize_houndify,
    "Bing Speech Recognition": sr.Recognizer().recognize_bing,
    "Deepgram Speech Recognition": sr.Recognizer().recognize_google,
}

def transcribe_speech(recognizer, microphone, api_function, language):
    """
    Transcribes speech from the microphone using the given recognizer and API.

    Args:
        recognizer (sr.Recognizer): The speech recognition engine.
        microphone (sr.Microphone): The microphone to use for recording.
        api_function (function): The API function to use for speech recognition.
        language (str): The language to use for speech recognition.

    Returns:
        str: The transcribed text.
    """
    with microphone as source:
        st.info("Speak now...")
        audio_text = recognizer.listen(source)
        st.info("Transcribing...")

        try:
            text = api_function(audio_text, language=language)
            return text
        except sr.UnknownValueError:
            return "Sorry, I did not understand what you said."
        except sr.RequestError as e:
            return f"Error: {e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"

def main():
    st.title("Speech Recognition App")
    st.write("Click on the microphone to start speaking:")

    # Initialize recognizer and microphone
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # Add a selectbox to choose the API
    api_names = list(API_FUNCTIONS.keys())
    api_name = st.selectbox("Choose a speech recognition API", api_names)
    api_function = API_FUNCTIONS[api_name]

    # Add a selectbox to choose the language
    languages = ["en-US", "fr-FR", "es-ES", "de-DE", "it-IT", "pt-PT"]
    language = st.selectbox("Choose a language", languages)

    # Add a button to trigger speech recognition
    if st.button("Start Recording"):
        text = transcribe_speech(recognizer, microphone, api_function, language)
        st.write("Transcription:", text)

    # Add a button to save the transcribed text to a file
    if st.button("Save to File"):
        filename = st.text_input("Enter a filename")
        with open(filename, "w") as f:
            f.write(text)
        st.success("Text saved to file")

    # Add a button to pause and resume the speech recognition process
    pause_button = st.button("Pause")
    resume_button = st.button("Resume")
    if pause_button:
        st.info("Speech recognition paused")
        # Add a timer to pause the speech recognition process for 5 seconds
        time.sleep(5)
        st.info("Speech recognition resumed")
    if resume_button:
        st.info("Speech recognition resumed")

if __name__ == "__main__":
    main()