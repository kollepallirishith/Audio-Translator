# Live Speech Translation Application

## Overview
This application is a Python-based tool for real-time speech translation. It captures audio input through a microphone, translates it into a selected target language, and provides audio feedback of the translated text. It leverages libraries such as `speech_recognition`, `googletrans`, and `gTTS` for speech-to-text, translation, and text-to-speech functionalities respectively.

---

## Features
1. **Real-Time Speech Recognition**:
   - Captures spoken words through a microphone.
2. **Language Translation**:
   - Translates spoken input from one language to another.
3. **Audio Feedback**:
   - Plays back the translated text in the target language.
4. **Customizable Languages**:
   - Allows users to select both source and target languages from a predefined list.
5. **Dynamic Listening**:
   - Continuously listens for user input until interrupted.

---

## Prerequisites
1. **Python (3.x)**
2. **Required Libraries**:
   - `playsound`
   - `speech_recognition`
   - `googletrans==4.0.0-rc1`
   - `gTTS`
3. **Microphone**:
   - Ensure a working microphone is connected to your system.

---

## Installation
1. Clone or download the repository.
2. Install the required Python libraries:
   ```bash
   pip install playsound speechrecognition googletrans==4.0.0-rc1 gtts
   ```
3. Run the Python script:
   ```bash
   python live_translate.py
   ```

---

## Usage
### Steps:
1. **Language Selection**:
   - Input the source language (e.g., `English`, `Hindi`).
   - Input the destination language (e.g., `Spanish`, `French`).
2. **Speak into the Microphone**:
   - The program will capture and recognize your speech.
3. **Translation**:
   - The recognized text is translated into the selected target language.
4. **Audio Playback**:
   - The translated text is converted into speech and played back.

### Stopping the Program:
- Use `Ctrl+C` to terminate the application.

---

## Supported Languages
The application supports a wide range of languages. Some examples include:
- English (`en`)
- Hindi (`hi`)
- Tamil (`ta`)
- Telugu (`te`)
- French (`fr`)
- German (`de`)

Refer to the `dic` dictionary in the code for the complete list of supported languages and their codes.

---

## Code Explanation
1. **`takecommand` Function**:
   - Captures audio from the microphone and converts it to text using Google Speech Recognition.
2. **`language_input` Function**:
   - Prompts the user to input the source and target languages.
3. **Translation**:
   - Uses `googletrans.Translator` to translate text from the source language to the target language.
4. **Text-to-Speech**:
   - Converts the translated text into speech using `gTTS` and plays it back using `playsound`.
5. **Dynamic Listening**:
   - Continuously listens and processes audio until manually stopped.

---

## Known Limitations
1. **Internet Connection**:
   - Requires an active internet connection for translation and text-to-speech.
2. **Language Support**:
   - Limited to languages supported by `googletrans` and `gTTS`.
3. **Accuracy**:
   - Speech recognition and translation accuracy depend on clarity, accent, and background noise.

---

## Future Enhancements
- Add support for offline translation and text-to-speech.
- Include a graphical user interface (GUI) for easier interaction.
- Expand the dictionary for more language options.

---

## License
This project is open-source and available under the [MIT License](LICENSE).

---

## Acknowledgments
- Google Speech Recognition
- Google Translator API
- Google Text-to-Speech (gTTS)

