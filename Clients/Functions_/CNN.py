# Use a pipeline as a high-level helper
from transformers import pipeline
import streamlit as st

def analyse_text(text):
    pipe = pipeline("token-classification", model="Clinical-AI-Apollo/Medical-NER", aggregation_strategy='simple')
    result = pipe(text)
    
    structured_response = {
        "Patient Demographics": {},
        "Symptoms": [],
        "Duration":[],
        "Medical History": [],
        "Diagnostic Results": [],
        "Biological_structure":[],
        "Therapeutic_procedure":[],
        "Disease_disorder":[],
        "Medications": [],
        "Procedures": [],
        "Status": [],
        "Findings": []
    }
    
    
    for entity in result:
        category = entity["entity_group"]
        word = entity["word"]

        # Group entities into meaningful categories
        if category == "AGE":
            structured_response["Patient Demographics"]["Age"] = word
        elif category == "SEX":
            structured_response["Patient Demographics"]["Sex"] = word
        elif category in ["SIGN_SYMPTOM", "DETAILED_DESCRIPTION"]:
            structured_response["Symptoms"].append(word)
        elif category in ["DURATION"]:
            structured_response["Duration"].append(word)
        elif category in ["BIOLOGICAL_STRUCTURE"]:
            structured_response["Biological_structure"].append(word)
        elif category == "HISTORY":
            structured_response["Medical History"].append(word)
        elif category == "THERAPEUTIC_PROCEDURE":
            structured_response["Therapeutic_procedure"].append(word)
        elif category in ["DIAGNOSTIC_PROCEDURE"]:
            structured_response["Diagnostic Results"].append(word)
        elif category == "MEDICATION":
            structured_response["Medications"].append(word)
        elif category == "NONBIOLOGICAL_LOCATION":
            structured_response["Status"].append(word)
        elif category == "DISEASE_DISORDER":
            structured_response["Findings"].append(word)

    return structured_response
