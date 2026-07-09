# 📚 AI Powered Study Assistant

An AI-powered Study Assistant built with **Python** and **Google Gemini 2.5 Flash**. It explains complex topics in a simple and interactive way while allowing users to choose different response styles.

## ✨ Features

- 🤖 Powered by Google Gemini 2.5 Flash
- 😊 Multiple AI personalities:
  - Friendly
  - Academic
- 📖 Beginner-friendly explanations
- 🎯 Customizable response generation
- 🔐 Secure API key management using `.env`

## 🛠️ Tech Stack

- Python
- Google GenAI SDK
- Python Dotenv

## 📂 Project Structure

```
Ai_Powered_Study_Assistant/
│── assistant.py
│── .env
│── .gitignore
├── requirements.txt
└── venv/
```

## ⚙️ Installation

1. Clone the repository

```bash
git clone <repository-url>
cd Ai_Powered_Study_Assistant
```

2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Create a `.env` file

```env
GENAI_API_KEY=your_api_key_here
```

## ▶️ Run

```bash
python assistant.py
```

## 📌 Example

**Input**

```
Explain Generative AI in simple terms.
```

**Output**

```
Generative AI is like a creative assistant that learns patterns from existing data and uses them to generate new content such as text, images, or code...
```

## 📄 License

This project is for educational purposes.