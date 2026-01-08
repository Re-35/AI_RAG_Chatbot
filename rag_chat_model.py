# Import needed libraries:

import numpy as np
import pandas as pd
import os
import faiss
from sentence_transformers import SentenceTransformer
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv() 


# ----  Download Indexes and Dataframe and Embedding Model  ------:

# ----- 512 chunks -------:
index1 = faiss.read_index("ML_ChatBot/Data/faiss_index.bin")
df1 = pd.read_csv("ML_ChatBot/Data/documents.csv", encoding="utf-8")

# ----- 800 chunks -------:
index2 = faiss.read_index("ML_ChatBot/Data/faiss_index_800_chunks.bin")
df2 = pd.read_csv("ML_ChatBot/Data/documents_800_chunks.csv", encoding="utf-8")


# ----  The Chat Model  ------:

MODEL_EMB = SentenceTransformer("intfloat/e5-base-v2")

prompt_tamplate = ChatPromptTemplate([("system", """You're AI assistant that help to learn Machine Learning-ML in specific and other related topic of it.
                                       Take question, and break it, then answer each part, answer in points.
                                       You will give contexts that help you to generate the answer, please follow them and let the answer clear and understandable for person how learn about it as first time. Answer as teacher and just send the answer not contexts"""),
                                       ("human", "Context: {context}, question {question}")])


llm = ChatGroq(model="qwen/qwen3-32b", temperature=0.4, groq_api_key=os.environ.get("GROQ_API_KEY"), max_tokens=2048, reasoning_format="hidden")

def rag_chat(question, k=4, index=index1, df=df1, tamplete=prompt_tamplate, llm=llm):

    # embedding question:
    query = MODEL_EMB.encode(question)
    query_arr = np.array([query]).astype('float32')

    faiss.normalize_L2(query_arr)

    # search:
    destances, indices = index.search(query_arr, k)

    retrived_texts = [df.at[i, "text"] for i in indices[0]]

    # message and prompt:
    message = tamplete.format_messages(context=retrived_texts, question=question)

    # chat model:
    respons = llm.invoke(message)

    return respons.content



while True:

    print("\n\n--- Welcome to ML Teaching ChotBot ---\n\n")

    human_ans = input("Ask your Question or (quit) to exist: ")

    if human_ans.lower() == "quit":
        print("I hope that I helped you, see you soon!")
        break


    try:
        ai_ans = rag_chat(human_ans)
        print('-'* 70)
        print(ai_ans)

    except Exception as e:
        print(f"Error : {e}")
        print("Sorry, error happend.")

        