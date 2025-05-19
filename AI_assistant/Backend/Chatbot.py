from   groq import Groq
from json import load , dump
import datetime
from dotenv import dotenv_values

env_vars = dotenv_values(".env")

username = env_vars.get("Username")
Assistantname = env_vars.get("Assistantname")
GroqAPIKey = env_vars.get("GroqAPIKey")

client = Groq(api_key=GroqAPIKey)

messages = []

System = f"""Hello, I am {username}, You are a very accurate and advanced AI chatbot named {Assistantname} which also has real-time up-to-date information from the internet.
*** Do not tell time until I ask, do not talk too much, just answer the question.***
*** Reply in only English, even if the question is in Hindi, reply in English.***
*** Do not provide notes in the output, just answer the question and never mention your training data. ***
"""

SystemChatBot = [
    {"role":"system","content":System}
]

try:
    with open(r"Data\ChatLog.json","r") as f:
        messages = load(f)
except FileNotFoundError:
    with open(r"Data\ChatLog.json","w") as f:
        dump([],f)

def RealtimeInformation():
    current_date_time = datetime.datetime.now()
    day = current_date_time.strftime("%A")
    date = current_date_time.strftime("%d")
    month = current_date_time.strftime("%B")
    year = current_date_time.strftime("%Y")
    hour = current_date_time.strftime("%H")
    minute = current_date_time.strftime("%M")
    second = current_date_time.strftime("%S")

    #formate the info in a string.
    data = f"PLease use the real-time information if needed,\n"
    data += f"Day:{day}\nDate: {date}\nMonth: {month}\nYear: {year}\n"
    data += f"Time:{hour}hours :{minute}minutes :{second}seconds.\n"
    return data

def AnswerModifier(Answer):
    lines = Answer.split("\n")
    non_empty_lines = [line for line in lines if line.strip()]#removes empty lines
    modified_answer = "\n".join(non_empty_lines)
    return modified_answer

#main chat bot function to handle user query
def ChatBot(Query):
    """This function sends the user's query to the chatbot and return the AI's response. """
    try:
        #load the existing chat from chatbot json
        with open(r"Data\ChatLog.json","r") as f:
            messages=load(f)
        #approved the user's query to the messages and list.
        messages.append({"role":"user","content":Query})
        full_messages = SystemChatBot + [{"role": "system", "content": RealtimeInformation()}] + messages

        #make a request to the groq API
        completion = client.chat.completions.create(
            model="llama3-70b-8192",#specify the AI model to use.
            messages=full_messages,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None
        )

        Answer = "" #empty string to store Ai response
        for chunk in completion:
            if chunk.choices[0].delta.content:
                Answer += chunk.choices[0].delta.content
        Answer = Answer.replace("</s>","")#clean up any unwanted tocken from the response

        #append the chat bot response to the messages list
        messages.append({"role":"assistant","content":Answer})

        #save the uploade chat log to the json file
        with open(r"Data\ChatLog.json","w") as f:
            dump(messages,f,indent=4)
        
        #reutn the formatted response
        return AnswerModifier(Answer=Answer)
    except Exception as e:
        print(f"error: {e}")
        with open(r"Data\ChatLog.json","w") as f:
            dump([],f,indent=4)
        return ChatBot(Query)

if __name__ == "__main__":
    while True:
        user_input = input("enter your Question == > ")
        print(ChatBot(user_input))