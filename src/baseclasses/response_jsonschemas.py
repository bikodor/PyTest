from jsonschema import validate
from src.enums.global_enums import GlobalErrorMessages


class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                validate(item, schema)
        else:
            validate(self.response_json, schema)

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value

    def assert_element_count(self):
        if isinstance(self.response_json, list):
            assert len(self.response_json) == 3, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value
        else:
            print("Json is not list")


# Если массив из Json объектов приходит, то используем цикл
# [{'id': 1, 'title': 'Post 1'},
# {'id': 2, 'title': 'Post 2'},
# {'id': 3, 'title': 'Post 3'}]
