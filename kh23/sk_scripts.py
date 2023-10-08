import semantic_kernel as sk
import json
import re
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from yt import ytSearch

def blackbox(product_type):
    kernel = sk.Kernel()

    product_dict = { }
    # Prepare OpenAI service using credentials stored in the `.env` file
    api_key, org_id = sk.openai_settings_from_dot_env()
    kernel.add_chat_service("chat-gpt", OpenAIChatCompletion("gpt-3.5-turbo", api_key, org_id))

    product = product_type

    # Wrap your prompt in a function

    subreddit_prompt = kernel.create_semantic_function(f"""Name the best subreddit to check for researching what {product} to buy. Output the subreddit name as only its name without a URL or an "r/". For example, headphones might result in an output of "audiophile" sans quotation marks.""", max_tokens=200, temperature=0.2, top_p=0.5)


    #remove non-alphanumeric characters from the generated subreddit name
    subreddit_name = re.sub('[\W_]+', '', str(subreddit_prompt()))

    print(subreddit_name)

    #prompt for list of products
    prompt1 = kernel.create_semantic_function(f""" Consider important factors when researching a {product} to purchase and list the six most popular and best options 
    for {product} with these factors in mind. LIST ONLY BRANDED PRODUCTS- DO NOT NAME GENERIC PRODUCTS. IF YOU CANNOT NAME PRODUCTS, DO NOT USE GENERIC PLACEHOLDERS. Do not insert number the items in the list. Insert the raw product names into a JSON array. REPLY STRICTLY IN JSON FORMAT. Do not insert numbers before product names. Set the key to {product}""", max_tokens=2000, temperature=0.2, top_p=0.5)

    #print(prompt1()) 

    list_string = str(prompt1())

    json_list = json.loads(list_string)

    print(json_list)


    from reddit import count_mentions_in_subreddit

    #check relevant subreddit for mentions of product including alternate names
    item_list = []
    for item in json_list[f"{product}"]:
        try:
            item_list.append(item)
            total_count = 0
            print(item)
            altname = kernel.create_semantic_function(f"""List a few (at most five) alternative names for {item} that are commonly used by consumers. Output the alternative names as a JSON array. REPLY STRICTLY IN JSON FORMAT. DO NOT ATTACH A KEY.""", max_tokens=100, temperature=0.2, top_p=0.5)
            altname_string = str(altname())
            altname_list = json.loads(altname_string)

            for altname in altname_list:
                try:
                    count = count_mentions_in_subreddit(altname, subreddit_name)
                    total_count += count
                except Exception as e:
                    count = 0
                    print(f"An error occurred while processing {item}: {e}")
                print(total_count)
                product_dict[item_list.index(item)] = {'name': (f'{item}'), 'views': 0, 'mentions': total_count, 'subreddit': subreddit_name}
                print(product_dict)
                
        except Exception as e:
            continue

        #retrieve number of viewers for top 20 videos on YouTube for each product
        try:
            product_dict[item_list.index(item)]['views'] = ytSearch(item)
        except Exception as e:
            print("An error occurred invoking the YouTube API: {e}""")
        print(product_dict)
    
    json_dict = json.dumps(product_dict, indent=1)
    print(json_dict)
    return json_dict
