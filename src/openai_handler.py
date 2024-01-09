import os

import openai
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)

openai.api_key = os.environ["OPENAI_API_KEY"]

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def call_openai_api(prompt: str) -> dict:
    return openai.Completion.create(
        prompt=prompt,
        engine="text-davinci-003",
        max_tokens=0,
        temperature=1,
        n=1,
        logprobs=1,
        echo=True,
        presence_penalty=0,
        frequency_penalty=0,
        stop=None
    )
