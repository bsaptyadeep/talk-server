from pydantic import BaseModel
from typing import Optional

class WaitList(BaseModel):
    emailId: str