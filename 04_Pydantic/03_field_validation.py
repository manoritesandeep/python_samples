from pydantic import BaseModel, Field, validator
from typing import Optional, Dict, Any, List, Literal

# from pydantic import BaseModel, Field, field_validator 
# ## field_validator is only available in Pydantic v2+, but your Databricks environment is using Pydantic v1.x. In Pydantic v1, you should use @validator instead.

class personal_info(BaseModel):

    name: str = Field(..., min_length=3, max_length=20, description="Name of the person")
    age: Optional[int] = Field(..., gt=0, description="Age of person")
    email: str = Field(..., description="Email address of person")

    # Field validator for email
    @validator("email")
    def validate_email(cls, value):
        if "@" not in value:    # or ".com" not in value:
            raise ValueError("Invalid email address")
        elif ".com" not in value:   ## Adds .com to the value
            return value + ".com"
        else:
            return value

# pydantic_schema = personal_info.schema()
# print(pydantic_schema)      

pydantic_instance = personal_info(**{"name":"John", "age":30, "email":"john.doe@gmail"})
print(pydantic_instance)      