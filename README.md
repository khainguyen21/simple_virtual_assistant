# Voice Assistant using Python

## Overview
This is a simple voice assistant built using Python. It utilizes speech recognition and text-to-speech (TTS) capabilities to interact with the user. The assistant can perform tasks such as greeting the user, providing the current date and time, searching Wikipedia, and responding to basic commands.

## Features
- **Speech Recognition**: Converts spoken input into text using Google's `recognize_google` function.
- **Text-to-Speech**: Responds with synthesized speech using `pyttsx3`.
- **Date and Time Retrieval**: Provides the current date and time upon request.
- **Wikipedia Search**: Fetches summaries from Wikipedia.
- **Interactive Conversation**: Responds to basic greetings and farewells.

## Installation
To run this voice assistant, you need to install the required libraries. Use the following command:

```sh
pip install SpeechRecognition pyttsx3 wikipedia
```

## Usage
Run the script using Python:

```sh
python voice_assistant.py
```

The assistant will start listening and responding to voice commands.

## Commands
- "Hello" → Responds with a greeting.
- "What is the date today?" → Provides the current date.
- "What time is it?" → Provides the current time.
- "Search [topic]" or "Wikipedia [topic]" → Fetches a short summary from Wikipedia.
- "Bye" → Ends the program.

## Dependencies
- `speech_recognition`
- `pyttsx3`
- `wikipedia`
- `datetime` (built-in Python module)
- `re` (built-in Python module)

## Contributing
Feel free to fork this repository, open issues, or submit pull requests to improve the assistant.

## License
This project is licensed under the MIT License.

## Author
Khai Nguyen

