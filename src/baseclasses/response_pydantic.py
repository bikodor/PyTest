from src.enums.global_enums import GlobalErrorMessages



class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json().get('data') # если юзаем SERVICE_URL_2
        # self.response_json = response.json() # если юзаем SERVICE_URL
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.model_validate(item)
        else:
            schema.model_validate(self.response_json)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, self

    def assert_element_count(self):
        if isinstance(self.response_json, list):
            assert len(self.response_json) == 3, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value # или self чтобы заработал def __str__(self)

        else:
            print("Json is not list")

    def __str__(self):
        return \
        f"\nStatus code: {self.response_status} \n" \
        f"Requested url: {self.response.url} \n" \
        f"Response body: {self.response_json}"

# Если массив из Json объектов приходит, то используем цикл
# [{'id': 1, 'title': 'Post 1'},
# {'id': 2, 'title': 'Post 2'},
# {'id': 3, 'title': 'Post 3'}]
