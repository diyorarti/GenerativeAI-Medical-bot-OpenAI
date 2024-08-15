from src.helper import load_pdf, text_split, embedding_model
from pinecone import Pinecone
import pinecone
from dotenv import load_dotenv
import os

# load pinecone api key
load_dotenv()
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')

# extracting data
extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
chunks = text_chunks[:200]

# embedding model
embed = embedding_model()

# embedding the data and prepaiong for upserting to Pinecone
page_contents = [t.page_content for t in chunks]
embeddinged_chunks = [embed.embed_query(content) for content in page_contents]
ids = [f"id-{i}" for i in range(len(embeddinged_chunks))]
upsert_data = [
    {
        "id":ids[i],
        "values":embeddinged_chunks[i],
        "metadata":{"text":page_contents[i]}
    }
    for i in range(len(embeddinged_chunks))
]

# initializing Pineocne
index_name="medical-chatbot"
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(index_name)

# upserting to pineocne
index.upsert(upsert_data)