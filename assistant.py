import os
from google import genai
from dotenv import load_dotenv
from google.genai import types

import gradio as gr

load_dotenv()

api_key = os.getenv("GENAI_API_KEY")

client = genai.Client(api_key=api_key)


personalities = {
  "Friendly":
  "You are a friendly, enthusiastic, and highly encouraging Study Assistant. Your goal is to break down complex concepts into simple, beginner-friendly explanations. Use analogies and real-world examples that beginners can relate to. Always ask a follow-up question to check understanding",
  "Academic":
  "You are a strictly academic, highly detailed, and professional university Professor. Use precise, formal terminology, cite key concepts and structure your response. Your goal is to break down complex concepts into simple, beginner-friendly explanations. Use analogies and real-world examples that beginners can relate to. Always ask a follow-up question to check understanding"
}

def study_assistant(user_question, persona):
    system_prompt= personalities[persona]
    user_prompt = f"You are my smart Study Assistant. Your goal is to break down complex concepts into simple, beginner-friendly explanations. Use analogies and real-world examples that beginners can relate to. Always ask a follow-up question to check understanding. Here is my question: {user_question}"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config= types.GenerateContentConfig(
            system_instruction= system_prompt,
            temperature=0.4,
            max_output_tokens= 1000
        ),        
        contents=user_prompt,
    )
    return response.text


demo=gr.Interface(
    fn = study_assistant,
    inputs=[
        gr.Textbox(lines=4, placeholder="Enter your question here...", label="Question"),
        gr.Radio(choices=list(personalities.keys()), label="Personality", value="Friendly")
    ],

    outputs=gr.Textbox(lines=10, label="Response"),
    title="AI-Powered Study Assistant",
    description="Ask any question and get a detailed, beginner-friendly explanation from your AI Study Assistant. Choose between a Friendly or Academic personality for the response."
    )

demo.launch(debug=True)

user_question = "Explain Generative AI in simple terms ."
personality= "Academic"

output = study_assistant(user_question, personality)
print(output)

