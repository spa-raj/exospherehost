from pydantic import BaseModel, Field
from typing import Optional

class TokenRequest(BaseModel):
    identifier: str = Field(..., description="Identifier of the user, could be an email, phone, username, etc.")

    credential: str = Field(..., description="Credential of the user, could be a password, api secret, etc.")
    
    project: Optional[str] = Field(None, description="Project id against which the token is being requested.")
    
    satellites: Optional[list[str]] = Field(None, description="Satellites against which the token is being requested.")