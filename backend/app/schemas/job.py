from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class JobCreate(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    company: str = Field(min_length=1, max_length=255)
    location: str = Field(min_length=1, max_length=255)
    salary_min: int | None = Field(default=None, ge=0)
    salary_max: int | None = Field(default=None, ge=0)
    required_skills: list[str] = Field(default_factory=list)
    job_url: str = Field(min_length=1, max_length=500)


class JobResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    company: str
    location: str
    salary_min: int | None
    salary_max: int | None
    required_skills: list[str]
    job_url: str
    created_at: datetime
