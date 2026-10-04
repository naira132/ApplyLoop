from datetime import date
from enum import Enum

from sqlalchemy import Date, Enum as SqlEnum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class ApplicationStatus(str, Enum):
    APPLIED = "APPLIED"
    INTERVIEWING = "INTERVIEWING"
    OFFERED = "OFFERED"
    REJECTED = "REJECTED"


class Application(Base):
    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, index=True)
    job_id: Mapped[int] = mapped_column(ForeignKey("jobs.id"), nullable=False, index=True)
    status: Mapped[ApplicationStatus] = mapped_column(SqlEnum(ApplicationStatus), nullable=False, default=ApplicationStatus.APPLIED)
    applied_date: Mapped[date] = mapped_column(Date, nullable=False)

    user = relationship("User", back_populates="applications")
    job = relationship("Job", back_populates="applications")
