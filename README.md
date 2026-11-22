# JARVIS – AI Desktop Assistant

An AI-powered desktop assistant built using Python that helps automate everyday computer tasks through voice commands, facial authentication, and an interactive web-based interface.

## 🚀 Features

- **Voice Assistant:** Interact with JARVIS using voice commands.
- **Face Authentication:** Facial recognition-based authentication before accessing the assistant.
- **Wake Word Detection:** Activate the assistant using supported wake words such as "Jarvis" and "Alexa".
- **Application Automation:** Open desktop applications and websites using voice commands.
- **YouTube Integration:** Search and play YouTube videos through voice commands.
- **AI-Powered Responses:** Generate responses using Google's Gemini AI.
- **WhatsApp Automation:** Send messages and initiate calls through WhatsApp integration.
- **Mobile Automation:** Perform selected Android actions using ADB.
- **Text-to-Speech:** Receive spoken responses from the assistant.
- **Interactive Interface:** A web-based interface built with HTML, CSS, JavaScript, and Eel.

## 🛠️ Technologies Used

| Category | Technologies |
|---|---|
| Programming | Python |
| Frontend | HTML, CSS, JavaScript |
| Desktop Interface | Eel |
| Speech Recognition | SpeechRecognition |
| Text-to-Speech | pyttsx3 |
| AI Integration | Google Gemini API, HugChat |
| Face Authentication | OpenCV-based authentication module |
| Database | SQLite |
| Automation | PyAutoGUI, PyWhatKit, ADB |
| Wake Word | Porcupine |

## 📁 Project Structure

```text
AI-Desktop-Assistant/
│
├── engine/
│   ├── auth/
│   ├── command.py
│   ├── config.py
│   ├── db.py
│   ├── features.py
│   └── helper.py
│
├── www/
│   ├── assets/
│   ├── controller.js
│   ├── index.html
│   ├── main.js
│   ├── script.js
│   └── style.css
│
├── main.py
├── run.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yuvrajsi1806/AI-Desktop-Assistant.git
```

### 2. Navigate to the project directory

```bash
cd AI-Desktop-Assistant
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API credentials

Configure your Gemini API key securely using environment variables. Do not publish API keys or credentials in the repository.

### 5. Run the assistant

```bash
python run.py
```

**Note:** This project uses Windows-specific automation and may require additional setup for microphone access, Microsoft Edge, Android Debug Bridge (ADB), and authentication components.

## 🎯 Project Objective

The objective of this project is to develop an intelligent desktop assistant that combines voice interaction, artificial intelligence, facial authentication, and task automation to make everyday computer operations easier and more efficient.

## 🔮 Future Enhancements

- Improved natural language understanding.
- More advanced facial recognition and security.
- Additional desktop automation features.
- Enhanced AI chatbot capabilities.
- Sign Language to Audio/Visual Translation integration.

## 👨‍💻 Author

**Yuvraj Singh Rajpurohit**

Computer Science Engineering – Artificial Intelligence and Machine Learning

GitHub: https://github.com/yuvrajsi1806

---

⭐ If you find this project interesting, consider giving it a star!
