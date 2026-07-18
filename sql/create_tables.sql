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


-- Repositories

CREATE TABLE repositories (

    id BIGSERIAL PRIMARY KEY,

    github_repo_id BIGINT UNIQUE NOT NULL,

    owner VARCHAR(100) NOT NULL,

    name VARCHAR(200) NOT NULL,

    full_name VARCHAR(250) UNIQUE NOT NULL,

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

    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Contributors

CREATE TABLE contributors (

    id BIGSERIAL PRIMARY KEY,

    github_contributor_id BIGINT NOT NULL,

    github_repo_id BIGINT NOT NULL,

    login VARCHAR(200),

    contributions INTEGER,

    account_type VARCHAR(50),

    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Commits

CREATE TABLE commits (

    id BIGSERIAL PRIMARY KEY,

    github_repo_id BIGINT NOT NULL,

    sha VARCHAR(50) NOT NULL,

    author_name VARCHAR(200),

    author_email VARCHAR(250),

    commit_message TEXT,

    commit_date TIMESTAMP,

    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Issues

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

    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Pull Requests

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

    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Releases

CREATE TABLE releases (

    id BIGSERIAL PRIMARY KEY,

    github_release_id BIGINT NOT NULL,

    github_repo_id BIGINT NOT NULL,

    tag_name VARCHAR(100),

    name VARCHAR(300),

    draft BOOLEAN,

    prerelease BOOLEAN,

    published_at TIMESTAMP,

    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Languages

CREATE TABLE languages (

    id BIGSERIAL PRIMARY KEY,

    github_repo_id BIGINT NOT NULL,

    language VARCHAR(100),

    bytes_of_code BIGINT,

    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Repository Topics

CREATE TABLE repository_topics (

    id BIGSERIAL PRIMARY KEY,

    github_repo_id BIGINT NOT NULL,

    topic VARCHAR(100) NOT NULL,

    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);