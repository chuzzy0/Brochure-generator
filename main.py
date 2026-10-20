import os
from dotenv import load_dotenv
from scraper import fetch_website_contents
from openai import OpenAI

# Load environment variables
load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

system_prompt = """
You are an AI assistant that analyzes the contents of a website,
and provides a short summary. Respond in markdown.
Do not wrap the markdown in a code block - respond just with the markdown.
"""

user_prompt_prefix = """
Here are the contents of a website. Provide a short summary of this website:

"""


def message_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_prefix + website},
    ]


def summarize(url):
    website = fetch_website_contents(url)
    response = client.chat.completions.create(
        model="gpt-4o-mini", messages=message_for(website), temperature=0.7
    )
    return response.choices[0].message.content


def display_summary(url):
    print(f"--- Summary for {url} ---\n")
    summary = summarize(url)
    print(summary)


if __name__ == "__main__":
    target_url = "https://edwarddonner.com"
    display_summary(target_url)