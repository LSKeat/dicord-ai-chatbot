import google.generativeai as genai

# Replace your Gemini api token
GEMINI_TOKEN = 'GEMINI_TOKEN'

def get_response(user_input):
    # Gemini 1.0 pro model
    prompt = "You are a helpful ai assistant. Answer the user question."

    genai.configure(api_key=GEMINI_TOKEN)
    # Gemini 1.0 pro
    model = genai.GenerativeModel(model_name="gemini-1.0-pro")

    # generate response
    response = model.generate_content(prompt + user_input)
    return(response.text)

