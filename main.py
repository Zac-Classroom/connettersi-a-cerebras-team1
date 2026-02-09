import langchain
from langchain.chat_models import init_chat_model

from dotenv import dotenv_values

config = dotenv_values(".env")
print(config)
llm = init_chat_model(config['MODEL']
                      , temperature=config['TEMPERATURE']
                      , api_key=config['CK']
                      , verbose=True
                      , base_url="https://api.cerebras.ai/v1/")

response= llm.invoke("Chi è mira murati e perché è importante")

print(response.content)