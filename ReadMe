# DevOps Home Assignment – F5

This project demonstrates a containerized Nginx service with automated testing and a CI pipeline.

The goal of the assignment is to show basic DevOps skills:
- Running services with Docker
- Configuring Nginx
- Writing automated tests
- Using Docker Compose and GitHub Actions

---

## Project Overview

The project includes two main components:

### Nginx Service
The Nginx container exposes three endpoints:
- **HTTP OK (8080)** – serves a static HTML page
- **HTTP Error (8081)** – always returns HTTP 500
- **HTTPS (8443)** – serves the same page over HTTPS using a self-signed certificate

Rate limiting is configured on the HTTP OK endpoint using Nginx `limit_req`.

### Test Service
A separate test container runs automated Python tests that verify:
- HTTP OK response on port 8080
- HTTP 500 error on port 8081
- HTTPS response on port 8443
- Rate limiting configuration is active

Tests exit with a non-zero code if any check fails.

---

## Project Structure

