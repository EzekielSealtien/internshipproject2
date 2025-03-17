 An intelligent medical application designed to streamline medical report analysis and assist healthcare professionals in clinical decision-making using state-of-the-art AI technologies.

---

This application leverages artificial intelligence to automate the extraction of key medical entities from patient reports and provide personalized recommendations via an intelligent chatbot.  
The goal is to save physicians valuable time and support better, faster clinical decisions.

---

- Automated medical report analysis (NER-based)
- Extraction of clinical entities (symptoms, medications, diagnostics, etc.)
- Conversational chatbot for interpreting reports and assisting decisions
- Semantic search based on existing medical reports
- Personalized suggestions based on patient context

---

- **Frontend**: Streamlit  
- **Backend**: FastAPI  
- **NER Model**: Medical-NER (Hugging Face)  
- **Text Embedding**: OpenAI Embeddings (`text-embedding-ada-002`)  
- **Semantic Search**: Pinecone  
- **Conversational Model**: GPT-4  
- **Orchestration Layer**: Langchain  
- **Database**: PostgreSQL (AWS RDS)  
- **CI/CD**: GitHub Actions  
- **Deployment**: Heroku

---

1. Upload or write a medical report  
2. The AI model extracts key clinical information (NER)  
3. A chatbot interprets the report and provides context-aware recommendations  
4. Physicians can interact with the chatbot for further analysis or guidance

---
Here is the link to the application: https://ezekieltene-97b5db30cb69.herokuapp.com/
