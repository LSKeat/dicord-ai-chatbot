from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
  
def get_response(user_input):
    # llama2 model local host with ollama
    # Change any model available in ollama
    model_name = "llama2"
    chat = Ollama(model=model_name, temperature=0)
    
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful ai assistant. Answer the user's questions."),
            ("human", "{input}")
        ]
    )
    
    chain = prompt | chat

    result = chain.invoke({"input": user_input})

    return result