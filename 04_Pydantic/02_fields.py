# %pip install pydantic[email]



from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Dict, Any, List, Literal

class personal_info(BaseModel):

    name: str = Field(..., min_length=3, max_length=20, description="Name of the person")
    age: Optional[int] = Field(..., gt=0, description="Age of person")
    email: EmailStr = Field(..., description="Email address of person")
    gender: Literal['male', 'female', 'other'] = Field(..., description="Gender of person")
    salary: List[int] = Field(..., description="List of salaries of person")

def main(para1:personal_info):

    print("name:", para1.name)
    print("age:", para1.age)
    print("email:", para1.email)
    print("gender:", para1.gender)
    print("salary:", para1.salary)

pydantic_instance = personal_info(**{"name": "John", "age": 30, "email": "john@example.com", "gender": "male", "salary": [1000, 2000, 3000, 4000]})
# print(pydantic_instance)

main(pydantic_instance)




########## Test Code ##########

# from pydantic import BaseModel, Field, EmailStr, constr
# from typing import Optional, List, Literal

# class personal_info(BaseModel):
#     name: constr(min_length=3, max_length=20) = Field(..., description="Name of the person")
#     age: Optional[int] = Field(..., gt=0, description="Age of person")
#     email: EmailStr = Field(..., description="Email address of person")
#     gender: Literal['male', 'female', 'other'] = Field(..., description="Gender of person")
#     salary: List[int] = Field(..., description="List of salaries of person")

# def main(para1: personal_info):
#     print("name:", para1.name)
#     print("age:", para1.age)
#     print("email:", para1.email)
#     print("gender:", para1.gender)

# pydantic_instance = personal_info(
#     **{
#         "name": "John",
#         "age": 30,
#         "email": "john@example.com",
#         "gender": "male",
#         "salary": [1000, 2000, 3000]
#     }
# )
# print(pydantic_instance)