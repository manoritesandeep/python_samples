from pydantic import BaseModel, Field, root_validator
from typing import Optional, Dict, Any, List, Literal

# from pydantic import BaseModel, Field, model_validator
# ## The @model_validator decorator is only available in Pydantic v2+. In Pydantic v1.x (which is used in Databricks as of early 2024), you should use the @root_validator decorator for model-level validation.

class API_auth(BaseModel):
    email: str = Field(..., description="This is email address")
    password: str = Field(..., description="This is password")
    confirm_password: str = Field(..., description="This is confirm password")
    
    @root_validator #(mode="after")
    def validate_password(cls, values):
        if values["password"] != values["confirm_password"]:
            raise ValueError("Passwords do not match")
        return values

api_auth = API_auth(email="test@test.com", password="test", confirm_password="test")
print(api_auth)