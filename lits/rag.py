import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import warnings
from pathlib import Path as p
from pprint import pprint
import pandas as pd
import os
from langchain_core.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
warnings.filterwarnings("ignore")
os.environ["GOOGLE_API_KEY"] = "AIzaSyAf5yg3UKOhVfXxPDU4oa4WRi3wylhaU5M"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model2 = ChatGoogleGenerativeAI(model="gemini-2.0-flash",
                             temperature=1)

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
pdf_file = "rr.pdf"
pdf_loader = PyPDFLoader(pdf_file)
pages = pdf_loader.load_and_split()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=0)
context = "\n\n".join(str(p.page_content) for p in pages)
texts = text_splitter.split_text(context)
prompt_template = """Answer the question as precise as possible using the provided context. If the answer is
                    not contained in the context, say "answer not available in context" \n\n
                    Context: \n {context}?\n
                    Question: \n {question} \n
                    Answer:
                  """

prompt = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)
vector_index = Chroma.from_texts(texts, embeddings).as_retriever()
def ask(question):
    docs = vector_index.get_relevant_documents(question)
    stuff_chain = load_qa_chain(model2, chain_type="stuff", prompt=prompt)
    stuff_answer = stuff_chain(
        {"input_documents": docs, "question": question}, return_only_outputs=True
    )
    return(stuff_answer['output_text'])
