import streamlit as st
import pyttsx3
from tempfile import NamedTemporaryFile

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    st.title("Text to Speech Converter")
    st.write("Upload a text file and convert its contents into speech!")

    uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

    if uploaded_file is not None:
        text = uploaded_file.getvalue().decode("utf-8")
        st.write("File content:")
        st.write(text)

        if st.button("Convert to Speech"):
            with NamedTemporaryFile(delete=False, suffix='.txt') as temp_file:
                temp_file.write(text.encode("utf-8"))
                temp_file.seek(0)
                text_to_speech(text)
                st.success("Conversion completed!")

if __name__ == "__main__":
    main()
