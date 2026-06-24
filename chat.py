import requests
import ollama
from configuration import Configuration
from chat_box_utilities import ChatBoxUtilities

class FaithChat:
    def __init__(self):
        self._config = Configuration()
        self.introduction = self._config["introduction"]   
        self._utilits = ChatBoxUtilities()
        self._init_chat()
    
    def _init_chat(self):
        self.chat = []
        self.chat.append({
            "role": "assistant",
            "content": self.introduction
        })
    
    def _add_user_message(self, message):
        self.chat.append({
            "role": "user",
            "content": message
        })
        
    def _add_faith_message(self, message):
        self.chat.append({
            "role": "assistant",
            "content": message
        })

    def send_message(self, message):
        self._add_user_message(message)
        response = ollama.chat(
                model="llama3.1:8b",
                messages=self.chat,
                options={"temperature": 0.7}
            )
        return response['message']['content']
        

    def chat_loop(self):
        while True:
            user_input = input("\nTu: ")
            
            if user_input.lower() == 'esci':
                break
            
            context = self._utilits.find_context(user_input)
            if(context != None):
                user_input =  f"""Use the following documents to answer the question. 

                    Context:
                    {context}

                    Question: {user_input}"""
            
            model_response = self.send_message(user_input)
            
            print(f"Faith: {model_response}")

            self.chat.append({
                "role": "assistant",
                "content": model_response
            })


