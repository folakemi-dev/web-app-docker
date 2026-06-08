# Dockerized Python Web App

Containerized Python web application with Docker Compose, environment-based configuration, Postgres service wiring, and a GitHub Actions workflow that builds and publishes the image to GitHub Container Registry.

## What This Project Demonstrates

- Building a lightweight Python application image with Docker.
- Running a local multi-service stack with Docker Compose.
- Managing application and database settings through environment variables.
- Publishing container images with GitHub Actions and GHCR.
- Keeping local configuration out of source control with `.env`.

## Architecture

```text
Browser
   |
   v
Python HTTP server container
   |
   v
Postgres container

GitHub push -> GitHub Actions -> Docker build -> GHCR image
```

## Repository Structure

```text
.
|-- .github/workflows/docker-push.yml
|-- app.py
|-- docker-compose.yml
|-- Dockerfile
|-- .env.example
|-- .gitignore
`-- README.md
```

## Local Setup

Copy the example environment file:

```bash
cp .env.example .env
```

Start the stack:

```bash
docker compose up --build
```

Open the application:

```text
http://localhost:8000
```

Stop the stack:

```bash
docker compose down
```

Remove volumes when you want a clean database:

```bash
docker compose down -v
```

## Environment Variables

| Variable | Purpose |
|---|---|
| `APP_PORT` | Port exposed by the Python web application |
| `APP_MESSAGE` | Message rendered by the application |
| `POSTGRES_USER` | Local Postgres username |
| `POSTGRES_PASSWORD` | Local Postgres password |
| `POSTGRES_DB` | Local Postgres database name |

## CI/CD

The GitHub Actions workflow in `.github/workflows/docker-push.yml`:

1. Checks out the repository.
2. Sets up Docker Buildx.
3. Authenticates to GitHub Container Registry.
4. Builds and pushes the container image.

## Recruiter Notes

This project shows container basics, local service orchestration, environment configuration, and image publishing. It pairs well with the larger Kubernetes and CI/CD projects in this portfolio.
