# 🧠 Personal AI Assistant

A modular, multimodal AI assistant built in Python that combines voice interaction, conversational intelligence, image generation, real-time web search, and browser automation in a PyQt5-based GUI.

## 🛠️ Features

* 🗣️ Speech-to-Text using Web Speech API (Selenium + Chrome)
* 💬 Conversational AI via Groq, Gemini, and Mistral APIs
* 🧠 Real-Time Web Search with SerpAPI + Google
* 🌿 Image Generation using Replicate (Stable Diffusion models)
* 🔊 Text-to-Speech using Microsoft Edge TTS
* 📃 Modular Python code (Chatbot, STT, TTS, Image, Search, Automation)
* 💡 Extensible architecture for IoT, translation, or AR/VR integration

## 🏐 Tech Stack

| Component            | Technology                       |
| -------------------- | -------------------------------- |
| Programming Language | Python                           |
| GUI Framework        | PyQt5                            |
| Speech Recognition   | Web Speech API + Selenium        |
| Text-to-Speech       | Microsoft Edge TTS               |
| Conversational AI    | Groq API, Gemini, Mistral        |
| Image Generation     | Replicate API (Stable Diffusion) |
| Browser Automation   | Selenium WebDriver               |
| Real-Time Search     | Google Search API via SerpAPI    |

## 📆 Requirements

* Python 3.8+
* Google Chrome
* Microsoft Edge (for TTS)
* API keys:

  * REPLICATE\_API\_KEY
  * SERPAPI\_KEY
  * GROQ / GEMINI API Keys (optional)

## 🚀 Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/Personal-AI-Assistant.git
cd Personal-AI-Assistant
```

2. Set up a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Add your API keys in config.py:

```python
REPLICATE_API_KEY = "your_key"
SERPAPI_KEY = "your_key"
GROQ_API_KEY = "your_key"
```

5. Launch the application:

```bash
python main.py
```

## 📁 Project Structure

```
├── main.py                  # PyQt5 GUI
├── Chatbot.py               # Conversational LLM logic
├── SpeechToText.py          # Speech input (STT)
├── TextToSpeech.py          # Speech output (TTS)
├── ImageGeneration.py       # Text-to-image
├── RealtimeSearchEngine.py  # Real-time web search
├── Automation.py            # Browser automation
├── Model.py                 # API model handler
├── requirements.txt         # Dependencies
```

## 🚀 Future Scope

* Multilingual & regional language support
* IoT device integration (e.g., smart home)
* Calendar, reminders, and email automation
* Offline mode with on-device LLMs
* Emotion detection and AR/VR extensions

