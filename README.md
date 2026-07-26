# GitPulse

**An end-to-end GitHub Analytics ETL Pipeline** — extracts live repository data from the GitHub REST API, transforms it into an analytics-ready dimensional model, loads it into PostgreSQL, and visualizes it through interactive Power BI dashboards.

---

## 📌 Overview

GitPulse tracks a set of public GitHub repositories over time and turns raw API responses into a historical, queryable data warehouse. Every ETL run captures a **daily snapshot** of each repository's stats, contributors, commits, issues, pull requests, releases, languages, and topics — so trends (stars, forks, open issues, contributor activity, etc.) can be analyzed over time rather than just as a single point-in-time view.

Currently tracked repositories:

- `microsoft/vscode`
- `apache/airflow`
- `pandas-dev/pandas`
- `numpy/numpy`
- `tensorflow/tensorflow`

## 🧱 Architecture

```
GitHub REST API
      │
      ▼
   Extract   ── src/extract/    (repository, contributor, commit, issue, PR, release data)
      │
      ▼
  Transform  ── src/transform/  (cleaning, standardizing, snapshot-tagging)
      │
      ▼
    Load     ── src/load/       (upsert into PostgreSQL, snapshot_date keyed)
      │
      ▼
 PostgreSQL Data Warehouse (Docker)
      │
      ▼
   Power BI Dashboards ── Executive Overview / Repository Details / Trends
```

The pipeline is orchestrated end-to-end by `src/main.py`, which runs the full extract → transform → load cycle for every tracked repository on each execution.

## 🛠️ Tech Stack

| Layer | Tools |
|---|---|
| Language | Python |
| Extraction | GitHub REST API, `requests` |
| Data processing | `pandas` |
| Database | PostgreSQL (containerized via Docker) |
| ORM / DB access | SQLAlchemy, `psycopg2-binary` |
| Config management | `python-dotenv` (`.env`) |
| Containerization | Docker & Docker Compose |
| BI / Visualization | Power BI (DAX measures, calendar table, cross-filtering model) |
| Orchestration (planned) | Apache Airflow |

## 🗃️ Data Model

Every table is keyed by `snapshot_date`, so each row *is* a historical snapshot — there's no separate "daily snapshot" table. This means trend analysis (stars over time, issue counts over time, etc.) works directly off the base tables.

**Core tables:**
- `repositories` — stars, forks, watchers, open issues, license, visibility, etc.
- `contributors`
- `commits`
- `issues`
- `pull_requests`
- `releases`
- `languages`
- `repository_topics`

**Power BI model:**
- `dim_repository` (one) → fact tables (many): contributors, commits, issues, pull_requests, releases, languages, repository_topics
- A `Calendar` date table synced across all report pages via `snapshot_date`
- Key DAX measures: `Total Stars`, `Total Forks`, `Total Watchers`, `Total Contributors`, `Total Commits`, `Open Issues`, `Closed Issues`, `Avg Commits / Repo`

**Dashboard pages:**
1. **Executive Overview** — KPI cards, repository selector, date slicer, top repositories by stars, language distribution
2. **Repository Details** — contributors, commits, issues, pull requests, releases per repository
3. **Trends** — stars, forks, contributors, and issues over time

## 📂 Project Structure

```
gitpulse/
├── src/
│   ├── extract/
│   │   ├── base_extractor.py
│   │   ├── github_client.py
│   │   ├── repository_extractor.py
│   │   ├── commit_extractor.py
│   │   ├── pull_request_extractor.py
│   │   └── release_extractor.py
│   ├── transform/
│   │   ├── base_transformer.py
│   │   ├── repository_transformer.py
│   │   ├── commit_transformer.py
│   │   └── contributor_transformer.py
│   ├── load/
│   │   ├── repository_loader.py
│   │   └── commit_loader.py
│   ├── pipeline.py
│   └── main.py
├── sql/
│   ├── create_tables.sql
│   ├── views.sql
│   └── metrics.sql
├── airflow/
│   └── dags/
│       └── gitpulse_dag.py        
├── data/
│   └── raw/                       
├── dashboard/
│   └── GitPulse.pbix
├── docker-compose.yml
├── requirements.txt
├── .env                            
└── README.md
```

## ⚙️ Setup

### Prerequisites
- Python 3.x
- Git
- Docker Desktop
- A GitHub personal access token (for higher API rate limits)

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/gitpulse.git
cd gitpulse
```

### 2. Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file in the project root:
```
GITHUB_TOKEN=
DB_HOST=localhost
DB_PORT=5432
DB_NAME=gitpulse
DB_USER=postgres
DB_PASSWORD=
```

### 5. Start PostgreSQL via Docker
```bash
docker compose up -d
```

### 6. Create the database schema
```bash
docker exec -i gitpulse-postgres psql -U postgres -d gitpulse < sql/create_tables.sql
```

### 7. Run the ETL pipeline
```bash
python src/main.py
```

This extracts, transforms, and loads the latest snapshot for all tracked repositories into PostgreSQL, tagged with the current date.

### 8. Explore the data
Connect Power BI (or any PostgreSQL client) to the `gitpulse` database on `localhost:5432` and open `dashboard/GitPulse.pbix` to view the prebuilt reports.

## 🗺️ Roadmap
- [ ] Orchestrate daily runs with **Apache Airflow** instead of manual execution
- [ ] Add data validation / quality checks post-load
- [ ] Paginate all GitHub API calls fully (issues, PRs, contributors) for complete historical accuracy
- [ ] Add incremental/idempotent loading safeguards for repeated snapshot runs
- [ ] Move raw JSON snapshots to cloud storage instead of local disk

## 📄 License
MIT