import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from langchain_deepseek.chat_models import ChatDeepSeek
from langchain_community.vectorstores import Chroma # Using the original import as requested
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

# Load environment variables from the .env file
load_dotenv()

# --- 1. SET UP THE FLASK APP ---
app = Flask(__name__)

# --- 2. LOAD REUSABLE RAG COMPONENTS (Done only once at startup) ---

if 'DEEPSEEK_API_KEY' not in os.environ:
    print("❌ DEEPSEEK_API_KEY not found in .env file or environment variables.")
    exit()

print("Loading RAG components...")
persist_directory = 'chroma_db'
embedding_model_name = "all-MiniLM-L6-v2"

# Load components that don't change per request
embedding_model = HuggingFaceEmbeddings(model_name=embedding_model_name)
vectorstore = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding_model
)
llm = ChatDeepSeek(model="deepseek-chat")

# Define the prompt template, which is also reusable
template = """
You are an expert assistant for answering questions about longevity and anti-aging research.
Use only the following context from the FightAging.org blog to answer the question.
If you don't know the answer from the context provided, just say that you don't know.
Keep the answer concise and based on the provided sources.

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""
prompt = PromptTemplate.from_template(template)
print("✅ Reusable RAG components loaded successfully.")


# --- 3. DEFINE FLASK ROUTES ---

@app.route("/")
def home():
    """This route just serves the HTML page."""
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    """This route handles the question and dynamically builds the RAG chain."""
    data = request.get_json()
    question = data.get("question")
    k_value = int(data.get("k", 5)) # Get k_value from request, default to 5

    if not question:
        return jsonify({"error": "No question provided"}), 400

    print(f"Received question: {question} | Sources to retrieve: {k_value}")

    # Dynamically create the retriever and RAG chain for each request
    retriever = vectorstore.as_retriever(search_kwargs={"k": k_value})
    
    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    # Invoke the chain to get the answer
    answer = rag_chain.invoke(question)
    print(f"Generated answer.")
    
    return jsonify({"answer": answer})

# --- 4. RUN THE APP ---
if __name__ == "__main__":
    app.run(debug=True, port=5001)