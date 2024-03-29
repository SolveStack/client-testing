import os
from dotenv import load_dotenv
import pytest

from jive_integration.models import JiveAPICredentials

load_dotenv()


JIVE_ACCOUNT_KEY = os.getenv("JIVE_ACCOUNT_KEY")
JIVE_CLIENT_ID = os.getenv("JIVE_CLIENT_ID")
JIVE_CLIENT_SECRET = os.getenv("JIVE_CLIENT_SECRET")
STARTING_ACCESS_TOKEN = os.getenv("STARTING_ACCESS_TOKEN")
STARTING_REFRESH_TOKEN = os.getenv("STARTING_REFRESH_TOKEN")

# Instantiate client

from jive_integration.jive_client.client import JiveClient


def test_jive_access_token():
    jive_api_credentials = JiveAPICredentials(
        access_token=STARTING_ACCESS_TOKEN, refresh_token=STARTING_REFRESH_TOKEN
    )

    jive_client = JiveClient(
        client_id=JIVE_CLIENT_ID,
        client_secret=JIVE_CLIENT_SECRET,
        jive_api_credentials=jive_api_credentials,
    )
    assert bool(jive_client.access_token)


@pytest.mark.django_db
def test_list_voicemail_boxes():
    jive_api_credentials = JiveAPICredentials(
        access_token=STARTING_ACCESS_TOKEN, refresh_token=STARTING_REFRESH_TOKEN
    )

    jive_client = JiveClient(
        client_id=JIVE_CLIENT_ID,
        client_secret=JIVE_CLIENT_SECRET,
        jive_api_credentials=jive_api_credentials,
    )
    jive_client.list_extensions(account_key=JIVE_ACCOUNT_KEY)
    assert False
