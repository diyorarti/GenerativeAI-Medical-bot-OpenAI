# Medical Chatbot using OpenAI's Generative AI

## Project Overview
This project is a Medical Chatbot powered by OpenAI's GPT-3.5 and Pinecone, designed to assist users by answering medical-related questions based on the "Gale Encyclopedia of Medicine" by Jacqueline L. Longe Editor. The chatbot retrieves relevant information from the book and provides answers to the user’s queries in a conversational style. It's an innovative application of generative AI in the healthcare domain, with potential to offer real-time information to patients and healthcare professionals.

## Table of Contents
- Project Overview
- Features
- Project Structure
- Technologies Used
- Dataset
- Setup Instructions
- How to Use
- Future Enhancements
- License

## Features
- **Generative AI Responses** : Utilizes OpenAI's GPT-3.5 for generating human-like responses.
- **Medical Knowledge Base**: Integrates information from a comprehensive medical book.
- **Pinecone-powered Retrieval**: Leverages Pinecone for efficient document retrieval and search.
- **Interactive Chat UI**: A responsive, user-friendly chat interface built with Flask.
- **Real-time Question Answering**: Capable of answering medical questions with relevant, precise information.


## Project structure 
```bash
Medical_Chatbot/
│
├── data/
│   └── Medical_book.pdf            # Source medical data
│
├── research/
│   ├── experiment.ipynb            # Experimentation notebook
│
├── src/
│   ├── __init__.py
│   ├── helper.py                   # PDF loading, chunking, and embedding helper functions
│   ├── prompt.py                   # Prompt template for GPT-3 interaction
│
├── static/
│   └── style.css                   # Stylesheet for chat interface
│
├── templates/
│   └── chat.html                   # HTML template for chatbot UI
│
├── app.py                          # Main Flask application
├── store_index.py                  # Script to store and embed data into Pinecone
├── requirements.txt                # Required packages for the project
├── .gitignore
├── LICENSE
└── README.md                       # Project documentation (this file)
```

## Technologies Used
- **OpenAI GPT-3.5**: Provides the core generative AI capabilities for the chatbot.
- **Pinecone**: Used for semantic search and retrieval of medical data.
- **Flask**: Web framework used to create the application and serve the chat interface.
- **LangChain**: For managing the chain of operations for document search and question answering.
- **HTML/CSS/Bootstrap**: For building the chat interface.
- **Docker**: For containerizing the application.

# Dataset
The dataset used for this project is **"The Gale Encyclopedia of Medicine"**, a comprehensive medical reference book.

## Setup Instructions
1. Clone the repository:
```bash
git clone https://github.com/yourusername/medical-chatbot.git
cd medical-chatbot

```
2.  Install dependencies:
Make sure you have Python 3.7+ installed, then install the required packages using pip:
```bash
pip install -r requirements.txt

```
3. Set up environment variables:
Create a .env file in the root directory and add your OpenAI and Pinecone API keys:
```bash
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key

```
4. Store the index to Pinecone:
Run the store_index.py script to process the data and store it into Pinecone:
```bash
python store_index.py
```
5. Run the Flask application:
```bash
python app.py

```

## Future Enhancements
- Multi-Language Support: Integrate multi-language capabilities using OpenAI's language models.
- Voice Integration: Add speech-to-text and text-to-speech features for voice interactions.
- Advanced Medical Datasets: Incorporate more diverse medical datasets for broader medical coverage.


