import os
from googleapiclient.discovery import build
from dotenv import load_dotenv
def ytSearch(input):
    load_dotenv()

    api_key = os.getenv('YT_API_KEY')

    youtube = build("youtube", "v3", developerKey=api_key)

    # Define the search query
    search_query = input

    # Initialize variables to store video information and total view count
    video_data = []
    total_view_count = 0

    # Make a search request to get the videos
    search_response = youtube.search().list(
        q=search_query,
        type="video",
        part="id",
        maxResults=20  # Limit the results to 20 videos
    ).execute()

    # Retrieve video IDs from the search results
    video_ids = [item["id"]["videoId"] for item in search_response.get("items", [])]

    # Get video statistics for the retrieved video IDs
    video_stats_response = youtube.videos().list(
        id=",".join(video_ids),  # Comma-separated list of video IDs
        part="statistics"
    ).execute()

    # Calculate the sum of view counts for the top 20 videos
    for video in video_stats_response.get("items", []):
        view_count = int(video["statistics"]["viewCount"])
        total_view_count += view_count

    print(f"Total view count for the top 20 videos with '{search_query}' in the title: {total_view_count}")
