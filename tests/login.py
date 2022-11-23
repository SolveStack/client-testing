
import os
from dotenv import load_dotenv


load_dotenv()

JIVE_CLIENT_ID = os.getenv("JIVE_CLIENT_ID")
JIVE_CLIENT_SECRET = os.getenv("JIVE_CLIENT_SECRET")
STARTING_REFRESH_TOKEN = os.getenv("STARTING_REFRESH_TOKEN")

# Instantiate client

from jive_client.client import JiveClient
# from ..jive_integration.jive_client.client import JiveClient


jive_client = JiveClient(client_id=JIVE_CLIENT_ID, client_secret=JIVE_CLIENT_SECRET, refresh_token=STARTING_REFRESH_TOKEN)


print(jive_client.access_token)