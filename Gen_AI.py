from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Ask interview questions. 

Here is the conversation history:{context}

Question:{question}

Answer:
"""

# Initialize the model and prompt
model = OllamaLLM(model="llama3.1")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("Hello, Introduce yourself")
    while True:
        user_input = input("you: ")
        if user_input.lower() == "exit":
            break
        elif user_input:  # If the input is not empty
            result = chain.invoke({"context": context, "question": user_input})
            print("Bot: ", result)
            context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_conversation()