from pydantic import BaseModel, Field #, computed_field
from typing import Optional, Dict, Any, List, Literal

"""
The import of computed_field, as it is only available in Pydantic v2+, but Databricks currently uses Pydantic v1.x.
"""

class orders(BaseModel):
    id: int = Field(..., description="Unique identifier for the order")
    units: int = Field(..., description="Quantity of the item")
    amount: int = Field(..., description="Amount per unit of the item")

    # @computed_field
    @property
    def total_price(self) -> int:
        return self.units * self.amount

pydantic_instance = orders(id=1, units=10, amount=200)
print(pydantic_instance)
print("\n")
print(pydantic_instance.total_price)