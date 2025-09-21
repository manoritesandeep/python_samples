from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List, Literal

class input(BaseModel):

    query: str = Field(..., description="The SQL query to be executed")

class output(BaseModel):

    query: str = Field(..., description="The SQL query to be executed")
    result: str = Field(..., description="The result of the query")

def process_data(p_input: input) -> output:
    
    input_query = p_input.query
    result = "Hello there"
    
    pydantic_output = output(**{"query": input_query, "result": result})
    return pydantic_output

input_query = input(**{"query": "How are you?"})
response = process_data(input_query)
print(response)

print("--------Serialization to Dictionary---------")
# Serialization to Dictionary
"""
 Pydantic v1.x, which does not have the model_dump or model_dump_json methods. Use .dict() and .json() instead.
"""
# print(response.model_dump())
print(response.dict())
print("-----------------------------------------------")
print(response.json())
print("-----------------------------------------------")


