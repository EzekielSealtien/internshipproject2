import os
import requests
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/blaze999/Medical-NER"
HUGGINGFACE_TOKEN = os.getenv("HF_TOKEN") 



headers = {
    "Authorization": f"Bearer {HUGGINGFACE_TOKEN}"
}

def analyse_text(text):
    payload = {"inputs": text}
    response = requests.post(HUGGINGFACE_API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        return {"error": f"Failed to get prediction: {response.status_code}", "details": response.text}

    result = response.json()

    structured_response = {
        "Patient Demographics": {},
        "Symptoms": [],
        "Duration": [],
        "Medical History": [],
        "Diagnostic Results": [],
        "Biological_structure": [],
        "Therapeutic_procedure": [],
        "Disease_disorder": [],
        "Medications": [],
        "Procedures": [],
        "Status": [],
        "Findings": []
    }

    for entity in result:
        category = entity.get("entity_group", "")
        word = entity.get("word", "")

        if category == "AGE":
            structured_response["Patient Demographics"]["Age"] = word
        elif category == "SEX":
            structured_response["Patient Demographics"]["Sex"] = word
        elif category in ["SIGN_SYMPTOM", "DETAILED_DESCRIPTION"]:
            structured_response["Symptoms"].append(word)
        elif category == "DURATION":
            structured_response["Duration"].append(word)
        elif category == "BIOLOGICAL_STRUCTURE":
            structured_response["Biological_structure"].append(word)
        elif category == "HISTORY":
            structured_response["Medical History"].append(word)
        elif category == "THERAPEUTIC_PROCEDURE":
            structured_response["Therapeutic_procedure"].append(word)
        elif category == "DIAGNOSTIC_PROCEDURE":
            structured_response["Diagnostic Results"].append(word)
        elif category == "MEDICATION":
            structured_response["Medications"].append(word)
        elif category == "NONBIOLOGICAL_LOCATION":
            structured_response["Status"].append(word)
        elif category == "DISEASE_DISORDER":
            structured_response["Findings"].append(word)

    return structured_response
