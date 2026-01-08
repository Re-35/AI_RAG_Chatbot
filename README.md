# (RAG Chatbot) AI Assistant for Machine Learning (ML)
AI assistant coded to help students, learners, teachers, or anyone interested in Machine Learning (ML). You want to understand something related to ML? Just ask the assistant and it’ll give you almost comprehensive answer.

<br>
---
<br>

## Structure of RAG Chatbot:
The project is based on three main concepts: speed, accuracy, and free-based:
-	**Speed:** Not many unwanted structures or functions, just include what the chatbot needs, and use FAISS to accelerate the retrieval of related documents with no more space to store the database.
-	**Accuracy:** The RAG chatbot based on trusted and papular documents are Hands on Machine Learning, Practical Statistics for Data Science, and Andrew NG notes about ML.
-	**Free-Based:** The LLM API used as free trial of Groq, and other components are also free like database. Also, the deploy of project in public by HuggingFace space and Github.

<br>

### **Why I used free components in project?**
In summarized answer, to prove that can deploy his/her AI agent with some customization to what you need.

<br>

### **Other choices for LLM:**
You can use Ollama local host to save your data and privacy. It was my first choice but because I want to deploy for public I changed to Groq.

<br>

### **The components:**
Based on three concepts that I focused on them, and benchmark results, the main components of RAG chatbot:

1. **Vector Database:** FAISS, for speed and flexibility.

2.	**LLM:** From Groq, used Qwen/Qwen3-32b. Qwen3-32B is a large language model from Alibaba's Qwen3 series. It features 32.8 billion parameters, a 128k token context window, support for 119 languages, and hybrid thinking modes allowing switching between deep reasoning and fast responses. It demonstrates strong performance in reasoning, instruction-following, and agent capabilities. For more detailes: [paper of Qwen3-32b](https://arxiv.org/pdf/2505.09388).

3.	**Embedding Model:** Used E5-base-v2. The E5 series based on weakly-supervised contrastive pre-training for embedding. Also used for its accuracy and no need too strong hardware. For more detailes: [paper of  E5-base-v2](https://arxiv.org/pdf/2212.03533). [Benchmark article](https://supermemory.ai/blog/best-open-source-embedding-models-benchmarked-and-ranked/) .

<br>

### **The Chunks and Tokens:**
For splits data of documents, used “RecursiveCharacterTextSplitter” with 512 chunks and 800 chunks, after embedding I found the 512 chunks is better than 800 chunks especially with capability of the project (Used CPU, and limited tokens because free trial of API of LLM).
About the max tokens of the answer of LLM, used 512, 1024, and 2048. After testing I found the best max tokens is 2048 to can LLM complete its answer.

<br>

### **Prompt:**
Used prompt to lead LLM to write a comprehensive, clear, and understandable answer for learners or person who read it at first time. The structure of answer is written in points.

<br>

> **Warning:** The components I choose based on what my needs and goals are, they may not be suitable for your needs.
> 
<br>

---
<br>

## Environments:
Used three environments to create the project, Google Colab for split documents embedding process – used GPU T4. VScode for entire process of project, and HuggingFace space for deployment.

<br>

---

<br>

## Strategies:
-	Convert Documents from PDF to TXT for faster processing and avoid no need computing process.
-	Used Claude AI as helper during code and requirements analysis.
-	Used Streamlit for UI design of application chatbot.

<br>

---

<br>

## The Accuracy of RAG Chatbot:
The developer checks from chatbot and gives good answers, but be careful, it may be mistaken and inaccurate.

<br>

---

<br>

## The URL of RAG Chatbot:
I hope to be interested in AI ❤️
<br>
[Link of RAG Chatbot](https://huggingface.co/spaces/Re-35/AI_Learning_ML) 

--- 

Developer:
Developed by [Re-35].

