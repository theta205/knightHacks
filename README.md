![image](https://github.com/yukinoyuu/finalKnightHacks/assets/56956339/6917b13a-3f5a-49ee-966f-6d81c60a9c87)

# VIDEO DEMO: https://youtu.be/i2df1ZLSMAc


# Inspiration

In choosing a project fitting RBC's theme, we wanted to address the fact that not everyone enjoys the process of researching before they buy. With AI, we aim to accelerate and take the tediousness out of finding reputable products by utilizing AI recommendations and automatic detection of online user sentiment.

# What it does

Using Semantic Kernel, GPT-3.5 is prompted to list popular products in a category chosen by the user. Next, the LLM determines what subreddit would be the best fit for a consumer looking to research a product in that category. Using Reddit's PRAW rapper and Google's YouTube data API, the number of mentions of the item in the most appropriate subreddit as well as the number of recent video views about the product are collected. Using these data points, a popularity score is applied to the product and the recommendations are displayed on a page with prices and links.

# How we built it

We used MS Semantic Kernel to generate recommendations using GPT-3.5. Using Reddit and YouTube API's we determined each recommendation's user popularity score. With additional API's, we automatically pulled links, prices, and images from the internet for each product. We used React to create a UI and route user search queries to the backend APIs.

# Challenges we ran into

Trying to connect as many moving parts as we were working with caused friction at times. Precise prompt engineering took a while, as OpenAI's models have a tendency to insert unwanted data at times.

# Accomplishments that we're proud of

Using an LLM to automatically determine the "subreddit of best fit" for researching a particular product turned out quite well. We feel that we have a good foundation for a great user experience and we're all quite happy with nothing going catastrophically wrong.

# What we learned

Building frontend and backend separately and attempting to connect them towards the end of the allotted time was not the optimal workflow. In future projects, we will develop frontend and backend more stepwise and concurrently.

What's next for Knight Market
First, we want to improve the generation speed of new recommendations and improve the ruggedness of the app through strict prompt structuring. Additionally, we want to add user filter options like price range and release date. We anticipate OpenAI's models having access to current online data in the near future will allow us to take the project in new directions.
