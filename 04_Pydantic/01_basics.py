# %pip install pydantic

from pydantic import BaseModel, Field, StrictInt

class input(BaseModel):
    x: StrictInt = Field(..., description="x is required. StrictInt")
    # x: int = Field(..., description="x is required. Int")
    y: str = Field(default="Hello")
    # y: str = Field(..., description="y is required. String")

pyd_input = input(**{"x": 10})
# pyd_input = input(**{"x": 10, "y": "Sandeep"})
# pyd_input = input(x=10, y="Sandeep")

# pyd_input = input(x="10", y="Sandeep") '''## this will fail as x is not int in StrictInt: ValidationError: 1 validation error for input x  value is not a valid integer (type=type_error.integer)'''

print(pyd_input)

def main(para1: input):
    print("Welcome to main class!")

main(pyd_input)
