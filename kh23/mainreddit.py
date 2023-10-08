import semantic_kernel as sk
import json
#import boto3
import time
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion, AzureChatCompletion

kernel = sk.Kernel()

# Prepare OpenAI service using credentials stored in the `.env` file
api_key, org_id = sk.openai_settings_from_dot_env()
kernel.add_chat_service("chat-gpt", OpenAIChatCompletion("gpt-3.5-turbo", api_key, org_id))

# Alternative using Azure:
# deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
# kernel.add_chat_service("dv", AzureChatCompletion(deployment, endpoint, api_key))

product = input("Seach a product: ")

# Wrap your prompt in a function

subreddit_prompt = kernel.create_semantic_function(f"""Name the best subreddit to check for researching what {product} to buy. Output the subreddit name as only its name without a URL or an "r/". For example, headphones might result in an output of "audiophile" sans quotation marks.""", max_tokens=200, temperature=0.2, top_p=0.5)

subreddit_name = str(subreddit_prompt())

print(subreddit_name)

prompt1 = kernel.create_semantic_function(f""" Consider important factors when researching a {product} to purchase and list 25 popular options 
for {product} with these factors in mind. Do not insert number the items in the list. Insert the raw product names into a JSON array. REPLY STRICTLY IN JSON FORMAT. Do not insert numbers before product names. Set the key to {product}""", max_tokens=2000, temperature=0.2, top_p=0.5)

print(prompt1()) 

# list = kernel.create_semantic_function(f"""Output a list of the five product names you just generated in the format of a JSON array. REPLY STRICTLY IN JSON FORMAT""", max_tokens=2000, temperature=0.2, top_p=0.5)
# print(list())

list_string = str(prompt1())

json_list = json.loads(list_string)

print(json_list)


from reddit import count_mentions_in_subreddit

for item in json_list[f"{product}"]:
    print(item)
    count = count_mentions_in_subreddit(item, subreddit_name)
    print(count)
        # print(f"Title: {result['Title']}")
        # print(f"URL: {result['URL']}")
        # print(f"Body: {result['Body']}")
        # print("\n" + "-" * 50 + "\n")

# chosen_keyword = 'your_chosen_keyword'
# search_results = search_reddit_for_product(chosen_keyword)

# for result in search_results:
#     print(f"Title: {result['Title']}")
#     print(f"URL: {result['URL']}")
#     print(f"Body: {result['Body']}")
#     print("\n" + "-" * 50 + "\n")


#prompt2 = kernel.create_semantic_function(""" Create a list of important factors, maximum of three words per factor. List only the most important factors.""")
#prompt3 = kernel.create_semantic_function(f""" Do all of these factors actually make sense for a {product}? If not, remove the factors that don't make sense and rewrite the list. Do not elaborate on the factors, just list them.""")

# Run your prompt

#print(prompt3()) 
