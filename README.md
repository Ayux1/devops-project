# Flask Application — DevOps CI/CD Project

A containerized Python Flask application with an automated CI/CD pipeline using GitHub Actions, Docker Hub, and Azure Container Apps.

## Project Overview

This project demonstrates how to build, test, package, and deploy a web application through an automated DevOps workflow. Code changes pushed to the `main` branch trigger the pipeline, which runs tests, builds a Docker image, validates the running container, publishes the image to Docker Hub, and updates the Azure Container App.

## Architecture

```text
Developer
   |
   v
GitHub Repository (main)
   |
   v
GitHub Actions
   |
   +--> Install Python dependencies
   |
   +--> Run application tests
   |
   +--> Build Docker image
   |
   +--> Run container and verify HTTP response
   |
   +--> Push versioned image and latest tag
   |       |
   |       v
   |    Docker Hub
   |
   +--> Authenticate to Azure using OIDC
           |
           v
      Azure Container Apps
           |
           v
      Live Flask Application
```

## Technologies Used

- **Python & Flask** — Web application
- **pytest / unittest** — Automated testing
- **Docker** — Application containerization
- **Git & GitHub** — Version control and source code hosting
- **GitHub Actions** — CI/CD automation
- **Docker Hub** — Container image registry
- **Azure Container Apps** — Application deployment
- **Azure OpenID Connect (OIDC)** — Passwordless authentication from GitHub Actions to Azure

## Repository Structure

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml
├── tests/
│   └── test_app.py
├── app.py
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
```

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Ayux1/devops-project.git
cd devops-project
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
python app.py
```

Open `http://localhost:5000` in your browser.

## Run Tests

Run the automated tests locally:

```bash
python -m pytest -q
```

The CI workflow also runs the test suite using Python's `unittest` discovery.

## Build and Run with Docker

Build the image:

```bash
docker build -t devops-project .
```

Run the container:

```bash
docker run -d --name devops-app -p 5000:5000 devops-project
```

Verify the HTTP response:

```bash
curl http://localhost:5000/
```

Stop and remove the container:

```bash
docker rm -f devops-app
```

## CI/CD Pipeline

The GitHub Actions workflow is configured to run on pushes and pull requests targeting `main`.

1. Checks out the repository.
2. Sets up Python and installs dependencies.
3. Runs automated application tests.
4. Builds the Docker image.
5. Starts the container and checks its HTTP response.
6. Removes the test container, including during cleanup after a failed step.
7. On pushes to `main`, logs in to Docker Hub and pushes a commit-specific image tag and `latest`.
8. Authenticates to Azure through OIDC.
9. Updates the Azure Container App to use the commit-specific image.

Docker Hub publishing and Azure deployment are restricted to pushes to `main`; pull requests run the validation stages without deploying.

## Deployment and Security

- The application is deployed to Azure Container Apps.
- Container images are published to Docker Hub.
- The workflow uses GitHub repository secrets for credentials and Azure identifiers.
- Azure authentication uses OpenID Connect (OIDC), avoiding a long-lived Azure client secret in GitHub.
- A commit-specific Docker image tag helps identify the version selected for deployment.
- `.gitignore` and `.dockerignore` exclude development and unnecessary files from version control and the Docker build context.

## Future Improvements

- Add linting and code-quality checks.
- Add dependency and container vulnerability scanning.
- Add environment-specific deployments and health checks.
- Add monitoring, logging, and deployment rollback procedures.

## Author

**Ayush**
GitHub: https://github.com/Ayux1
