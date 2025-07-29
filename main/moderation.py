import os
from openai import OpenAI, RateLimitError, APIError
import logging

from django.conf import settings

# Ensure the OpenAI API key is set in the environment
openai_api_key = settings.OPENAI_API_KEY
if not openai_api_key:
    raise ValueError("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")

client = OpenAI(api_key=openai_api_key)


def is_inappropriate(text: str) -> bool:
    """
    Uses OpenAI's moderation endpoint to check if the text is inappropriate.
    Returns True if flagged, False otherwise.
    """
    if not text:
        return False
    try:
        response = client.moderations.create(input=text)
        return response.results[0].flagged
    except (RateLimitError, APIError) as e:
        # Log the error and fail open to avoid blocking users due to API issues.
        logging.error(f"OpenAI Moderation API error: {e}")
        return False
