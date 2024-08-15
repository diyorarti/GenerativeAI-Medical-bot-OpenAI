from flask import Flask, render_template, jsonify, request
from src.helper import embedding_model
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import openai
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from src.prompt import *
import os

app = Flask(__name__)

load_dotenv()
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

embedding = embedding_model()

from pinecone import Pinecone
index_name="medical-chatbot"
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(index_name)

from langchain.vectorstores import Pinecone
text_field = "text"
vectorstore = Pinecone(
    index, embedding.embed_query, text_field
)
PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])
chain_type_kwargs={"prompt": PROMPT}

#openai.api_key = OPENAI_API_KEY
llm = OpenAI(
    model_name="gpt-3.5-turbo",  # or "gpt-4"
    temperature=0.8,
    max_tokens=512,
)


qa=RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever=vectorstore.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True, 
    chain_type_kwargs=chain_type_kwargs)

@app.route("/")
def index():
    return render_template('chat.html')



@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result=qa({"query": input})
    print("Response : ", result["result"])
    return str(result["result"])



if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)