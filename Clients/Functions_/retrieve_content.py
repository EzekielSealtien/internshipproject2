import streamlit as st
from .readFunctions import lire_docx,lire_pdf

def retrieve_content_file_uploaded(file_uploaded):
    if file_uploaded is not None:
        extension_fichier = file_uploaded.name.split('.')[-1].lower()

        if extension_fichier in ["pdf", "docx"]:
            st.markdown("---")
                    
            if extension_fichier == "pdf":
                file_content = lire_pdf(file_uploaded)
                return file_content
            
            else:
                file_content = lire_docx(file_uploaded)
                return file_content
         
        else:
            st.markdown("---")
            st.error("⚠️ Seuls les fichiers PDF, DOCX, et PPTX sont acceptés.")