from pydantic import BaseModel, field_validator
from src.enums.user_enums import Genders, Statuses, UserErrors

class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Genders
    status: Statuses

    @field_validator('email')
    def check_that_dog_presented_in_email_address(cls, email):
        if '@' in email:
            return email
        else:
            raise ValueError(UserErrors.WRONG_EMAIL.value)




# Если нужно указать необязательность поля,
# то указать, например,
# id: int = 0 или = "" или = None
#

