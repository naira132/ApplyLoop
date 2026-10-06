# ApplyLoop

A full-stack application that aggregates tech job listings, analyzes required skills against candidate profiles, and ranks matches in real time.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-009688?logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-18-61DAFB?logo=react&logoColor=black)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?logo=postgresql&logoColor=white)

---

## 🌟 Key Features

* **Job Aggregation Pipeline:** Background tasks scrape and normalize tech postings across public boards.
* **Skill Match Scoring:** Calculates set intersection between user resume skills and job requirements to rank listings ($O(n \log n)$ priority sort).
* **Application Tracker:** Kanban-style board to track job application statuses (`Applied`, `Interviewing`, `Offered`, `Rejected`).
* **Filtering & Search:** Instant search by salary range, remote status, and technology stack keywords.

---

## 🛠️ Tech Stack

* **Backend:** FastAPI, Python 3.12, Pydantic, BeautifulSoup4 / Scrapy
* **Database:** PostgreSQL, SQLAlchemy (ORM), Alembic
* **Frontend:** React, TypeScript, Tailwind CSS
* **DevOps:** Docker Compose, GitHub Actions

---

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/your-username/jobpulse.git
cd jobpulse

# Launch all services
docker compose up -d
```
