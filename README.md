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
<<<<<<< HEAD

## 📄 License

This project is for educational purposes.
=======
## 🚨 Troubleshooting

### Installation issues

If you encounter errors while installing dependencies (such as `tiktoken` requiring a Rust compiler), first upgrade `pip`, `setuptools`, and `wheel`:

```bash
python -m pip install --upgrade pip setuptools wheel
```

Then reinstall the dependencies:

```bash
pip install -r requirements.txt
```

If the issue persists, ensure you are using a supported Python version (Python 3.10–3.12) and an up-to-date version of `pip`.

## 📄 License

This project is for educational purposes.
>>>>>>> 31bbac4c6d9a28ba76be64c6ead2cc7fdfbd1e9d
