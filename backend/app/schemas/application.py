from datetime import date

from pydantic import BaseModel

from app.models.application import ApplicationStatus


class ApplicationCreate(BaseModel):
    user_id: int
    job_id: int
    status: ApplicationStatus = ApplicationStatus.APPLIED
    applied_date: date


class ApplicationUpdate(BaseModel):
    status: ApplicationStatus
