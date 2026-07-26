-- GitPulse Data Warehouse
-- PostgreSQL Schema

DROP TABLE IF EXISTS repository_topics CASCADE;
DROP TABLE IF EXISTS languages CASCADE;
DROP TABLE IF EXISTS releases CASCADE;
DROP TABLE IF EXISTS pull_requests CASCADE;
DROP TABLE IF EXISTS issues CASCADE;
DROP TABLE IF EXISTS commits CASCADE;
DROP TABLE IF EXISTS contributors CASCADE;
DROP TABLE IF EXISTS repositories CASCADE;


-- Repositories (Daily Snapshot)

CREATE TABLE repositories (

    id BIGSERIAL PRIMARY KEY,

    github_repo_id BIGINT NOT NULL,

    owner VARCHAR(100) NOT NULL,

    name VARCHAR(200) NOT NULL,

    full_name VARCHAR(250) NOT NULL,

    description TEXT,

    language VARCHAR(100),

    stars INTEGER,

    forks INTEGER,

    watchers INTEGER,

    open_issues INTEGER,

    default_branch VARCHAR(100),

    visibility VARCHAR(20),

    license VARCHAR(150),

    created_at TIMESTAMP,

    updated_at TIMESTAMP,

    snapshot_date DATE NOT NULL DEFAULT CURRENT_DATE,

    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    UNIQUE (snapshot_date, github_repo_id)

);


-- Contributors (Daily Snapshot)

CREATE TABLE contributors (

    id BIGSERIAL PRIMARY KEY,

    github_contributor_id BIGINT NOT NULL,

    github_repo_id BIGINT NOT NULL,

    login VARCHAR(200),

    contributions INTEGER,

    account_type VARCHAR(50),

    snapshot_date DATE NOT NULL DEFAULT CURRENT_DATE,

    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    UNIQUE (

        snapshot_date,
        github_repo_id,
        github_contributor_id

    )

);


-- Commits (Daily Snapshot)

CREATE TABLE commits (

    id BIGSERIAL PRIMARY KEY,

    github_repo_id BIGINT NOT NULL,

    sha VARCHAR(50) NOT NULL,

    author_name VARCHAR(200),

    author_email VARCHAR(250),

    commit_message TEXT,

    commit_date TIMESTAMP,

    snapshot_date DATE NOT NULL DEFAULT CURRENT_DATE,

    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    UNIQUE (

        snapshot_date,
        sha

    )

);


-- Issues (Daily Snapshot)

CREATE TABLE issues (

    id BIGSERIAL PRIMARY KEY,

    github_issue_id BIGINT NOT NULL,

    github_repo_id BIGINT NOT NULL,

    title TEXT,

    state VARCHAR(20),

    comments INTEGER,

    created_at TIMESTAMP,

    updated_at TIMESTAMP,

    closed_at TIMESTAMP,

    snapshot_date DATE NOT NULL DEFAULT CURRENT_DATE,

    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    UNIQUE (

        snapshot_date,
        github_issue_id

    )

);


-- Pull Requests (Daily Snapshot)

CREATE TABLE pull_requests (

    id BIGSERIAL PRIMARY KEY,

    github_pr_id BIGINT NOT NULL,

    github_repo_id BIGINT NOT NULL,

    title TEXT,

    state VARCHAR(20),

    merged BOOLEAN,

    created_at TIMESTAMP,

    updated_at TIMESTAMP,

    closed_at TIMESTAMP,

    snapshot_date DATE NOT NULL DEFAULT CURRENT_DATE,

    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    UNIQUE (

        snapshot_date,
        github_pr_id

    )

);


-- Releases (Daily Snapshot)

CREATE TABLE releases (

    id BIGSERIAL PRIMARY KEY,

    github_release_id BIGINT NOT NULL,

    github_repo_id BIGINT NOT NULL,

    tag_name VARCHAR(100),

    name VARCHAR(300),

    draft BOOLEAN,

    prerelease BOOLEAN,

    published_at TIMESTAMP,

    snapshot_date DATE NOT NULL DEFAULT CURRENT_DATE,

    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    UNIQUE (

        snapshot_date,
        github_release_id

    )

);


-- Languages (Daily Snapshot)

CREATE TABLE languages (

    id BIGSERIAL PRIMARY KEY,

    github_repo_id BIGINT NOT NULL,

    language VARCHAR(100),

    bytes_of_code BIGINT,

    snapshot_date DATE NOT NULL DEFAULT CURRENT_DATE,

    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    UNIQUE (

        snapshot_date,
        github_repo_id,
        language

    )

);


-- Repository Topics (Daily Snapshot)

CREATE TABLE repository_topics (

    id BIGSERIAL PRIMARY KEY,

    github_repo_id BIGINT NOT NULL,

    topic VARCHAR(100) NOT NULL,

    snapshot_date DATE NOT NULL DEFAULT CURRENT_DATE,

    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    UNIQUE (

        snapshot_date,
        github_repo_id,
        topic

    )

);