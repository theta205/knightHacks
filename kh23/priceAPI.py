import json
import aiohttp
import asyncio
import urllib.parse

async def create_job(input):
    create_job_url = "https://api.priceapi.com/v2/jobs"
    data = {
        "token": "NXJUJBSXLZTZEZYMIJNDXMQPNWDGBNATZDXGBJCNJYIDWDMQJBELHJHNYGAKEHZW",
        "country": "us",
        "source": "amazon",
        "topic": "search_results",
        "key": "term",
        "max_age": "43200",
        "max_pages": "1",
        "sort_by": "relevance_descending",
        "values": input,
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(create_job_url, data=data) as response:
            result = await response.json()
            job_id = result["job_id"]
            return job_id

async def check_job_status(job_id):
    while True:
        check_job_url = f"https://api.priceapi.com/v2/jobs/{job_id}?token=NXJUJBSXLZTZEZYMIJNDXMQPNWDGBNATZDXGBJCNJYIDWDMQJBELHJHNYGAKEHZW"
        async with aiohttp.ClientSession() as session:
            async with session.get(check_job_url) as response:
                status = (await response.json())["status"]
                if status in ["finished", "cancelled"]:
                    return

async def download_job_result(job_id):
    download_url = f"https://api.priceapi.com/v2/jobs/{job_id}/download?token=NXJUJBSXLZTZEZYMIJNDXMQPNWDGBNATZDXGBJCNJYIDWDMQJBELHJHNYGAKEHZW"
    async with aiohttp.ClientSession() as session:
        async with session.get(download_url) as response:
            result = await response.json()
            return result

async def main(input):
    input_data = input
    job_id = await create_job(input_data)
    await check_job_status(job_id)
    result = await download_job_result(job_id)
    
    if (
        result['results'][0]['content']['search_results'][0]['min_price'] is None
        or result['results'][0]['content']['search_results'][0]['max_price'] is None
    ):
        print(None)
    else:
        min_price = float(result['results'][0]['content']['search_results'][0]['min_price'])
        max_price = float(result['results'][0]['content']['search_results'][0]['max_price'])
        product = (min_price + max_price) / 2.0
        print(product)

if __name__ == "__main__":
    asyncio.run(main("iRobot Roomba 980")) # change if needed
