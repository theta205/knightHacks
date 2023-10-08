# import semantic_kernel as sk
# #import boto3
# import time
# from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion, AzureChatCompletion

# kernel = sk.Kernel()

# # Prepare OpenAI service using credentials stored in the `.env` file
# api_key, org_id = sk.openai_settings_from_dot_env()
# kernel.add_chat_service("chat-gpt", OpenAIChatCompletion("gpt-3.5-turbo", api_key, org_id))

# # Alternative using Azure:
# # deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
# # kernel.add_chat_service("dv", AzureChatCompletion(deployment, endpoint, api_key))

# product = input("Seach a product: ")

# # Wrap your prompt in a function
# prompt1 = kernel.create_semantic_function(f""" Consider important factors when researching a {product} to purchase and list five good options 
# for {product} with these factors in mind. """, max_tokens=2000, temperature=0.2, top_p=0.5)

# print(prompt1()) 

# #prompt2 = kernel.create_semantic_function(""" Create a list of important factors, maximum of three words per factor. List only the most important factors.""")
# #prompt3 = kernel.create_semantic_function(f""" Do all of these factors actually make sense for a {product}? If not, remove the factors that don't make sense and rewrite the list. Do not elaborate on the factors, just list them.""")

# # Run your prompt

# #print(prompt3()) 

from fastapi import FastAPI
from sk_scripts import blackbox

app = FastAPI()

# @app.get("/")
# async def root():
#     return "Error: no input" 

@app.get("/{input}")
async def root(input: str):
    return blackbox(input)
