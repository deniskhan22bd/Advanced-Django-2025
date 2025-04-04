import os
import docx
from pdfminer.high_level import extract_text
import re
import json
from mistralai import Mistral
from dotenv import load_dotenv
load_dotenv()

def extract_text_from_pdf(file_path):
    try:
        text = extract_text(file_path)
        return text
    except Exception as e:
        print("Error extracting PDF text:", e)
        return ""

def extract_text_from_docx(file_path):
    try:
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        print("Error extracting DOCX text:", e)
        return ""

def parse_resume(file_path):
    # Determine file type by extension
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.pdf':
        text = extract_text_from_pdf(file_path)
    elif ext in ['.docx', '.doc']:
        text = extract_text_from_docx(file_path)
    else:
        text = ""
    api_key = os.getenv('AI_API_KEY')
    model = "mistral-large-latest"

    client = Mistral(api_key=api_key)
    text = "I have a resume provided as text (extracted from either a PDF or DOCX file). Your task is to analyze the text and extract the following information:Name: The candidates full name.Email: The candidates email address.Skills: A list of technical and/or soft skills mentioned.Education: Details about the candidates educational background if available. Please output the extracted information in JSON format with the keys name, email, skills, and education(place_of_learning, degree, in array of objects). If any of the details are not found, leave the corresponding value empty or null" + text
    chat_response = client.chat.complete(
        model= model,
        messages = [
            {
                "role": "user",
                "content": text,
            },
        ]
    )
    data = chat_response.choices[0].message.content.strip()
    print(data)
    match = re.search(r"```json\s*(\{.*\})\s*```", data, re.DOTALL)
    if match:
        json_str = match.group(1)
        try:
            data_dict = json.loads(json_str)
            return data_dict
        except json.JSONDecodeError as e:
            return("Error decoding JSON")
    else:
        return("No valid JSON found in the response.")

    


