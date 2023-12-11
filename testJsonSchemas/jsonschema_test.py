import requests
from configuration import SERVICE_URL
from src.baseclasses.response_jsonschemas import Response
from src.jsonschemas.post import POST_SCHEMA


def test_get_request():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)
    response.validate(POST_SCHEMA)
    response.assert_status_code(200)
    response.assert_element_count()



