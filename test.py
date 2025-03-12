import streamlit as st

dictionnary={"Patient Demographics":{"Age":"32-year-old","Sex":"woman"},
 "Symptoms":["persistent","cough","generalized","fatigue","heaviness","fever","occasional","chills","progressive","loss of appetite","tachypnea","crackles","right-sided","pallor","rest","mod","erate","opacity","abnormalities","adequate"],
 "Duration":["past 3 weeks"],
 "Medical History":["no prior hospitalizations or known chronic illnesses"],
 "Diagnostic Results":["Physical examination","auscultation","Oxygen saturation","radiograph","CT","Blood tests","C-reactive protein","CRP","eosinophils","Bronchoscopy","biopsy","auscultation"],
 "Biological_structure":["chest","lung","skin","chest","right middle lobe","mediastinal","pulmonary"],
 "Therapeutic_procedure":["Supportive care","hydration"],
 "Disease_disorder":[],
 "Medications":["cough suppressants"],
 "Procedures":[],
 "Status":[],"Findings":["iron deficiency anemia","iron deficiency anemia","lymphadenopathy"]}

b=""
for key in dictionnary.keys():
    a=f'{key}: {dictionnary[key]} \n'
    b=b+a+"\n"
st.write(b)