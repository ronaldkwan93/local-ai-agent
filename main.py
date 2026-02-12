from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import PromptTemplate
from vector import retriever

model = OllamaLLM(model='llama3.2')

template = """
You are an expert in answering questions about buying property in Sydney, Australia, especially close to Lidcombe 2141 region.

Here are the relevant information {information}

Here is the question to answer: {question}
"""

prompt = PromptTemplate.from_template(template)

chain = prompt | model

while True:
    print("\n\n------------------------------------")
    question = input("Ask your question (q to quit):")
    if question == 'q':
        break
    information = retriever.invoke(question)
    result = chain.invoke({"information": information, "question": question})
    print(result)
