# Automated CI/CD Pipeline Using Jenkins, GitHub, Python Flask, Pytest, and Docker

A beginner-friendly DevOps project that demonstrates how Jenkins can automate Python dependency installation, application testing, and Docker image creation.

## Project Overview

This project contains a simple Flask web application and a Jenkins pipeline. Jenkins retrieves the source code from GitHub, checks the Python environment, installs the required packages, runs automated tests with Pytest, and builds a Docker image when the tests pass.

> **Current scope:** The pipeline automates testing and Docker image building. Starting the Docker container is a separate manual step. A GitHub webhook and automated deployment stage are not configured.

## Technologies Used

- **Python** — application language
- **Flask** — lightweight web framework
- **Pytest** — automated testing
- **Jenkins** — CI pipeline automation
- **GitHub** — source-code hosting and version control
- **Docker** — application containerization

## Project Structure

```text
jenkins-devops-project/
├── app.py
├── requirements.txt
├── test_app.py
├── Dockerfile
├── Jenkinsfile
└── .dockerignore
```

| File | Purpose |
|---|---|
| `app.py` | Flask application with a home page and health-check endpoint |
| `requirements.txt` | Python dependencies required by the project |
| `test_app.py` | Automated tests for the home page and health endpoint |
| `Dockerfile` | Instructions for building the Docker image |
| `Jenkinsfile` | Defines the Jenkins pipeline stages |
| `.dockerignore` | Excludes unnecessary files from the Docker build context |

## Application Endpoints

When the application is running:

- Home page: `http://localhost:5000/`
- Health check: `http://localhost:5000/health`

The health-check endpoint returns:

```json
{
  "status": "healthy"
}
```

## Prerequisites

Install and configure the following tools:

- Python 3
- Git
- Jenkins
- Docker Desktop (or Docker Engine)

Make sure the Docker engine is running before executing Docker commands. The Jenkins agent must have access to Python, pip, Docker, and the project workspace.

## Run Locally

Open a terminal in the project directory.

### 1. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 2. Run automated tests

```powershell
python -m pytest -v
```

The included test suite checks that:
- The home page responds with HTTP 200 and contains the expected welcome message.
- The `/health` endpoint responds with HTTP 200 and reports `healthy`.

Expected result: **2 tests passed**.

### 3. Start the Flask application directly (optional)

```powershell
python app.py
```

Open `http://localhost:5000/` in your browser. Stop the local server with `Ctrl+C`.

## Build and Run with Docker

Run these commands from the project directory.

### 1. Build the image

```powershell
docker build -t jenkins-devops-app .
```

### 2. Start a container

```powershell
docker run -d --name jenkins-devops-app -p 5000:5000 jenkins-devops-app
```

Open the home page at `http://localhost:5000/` and the health check at `http://localhost:5000/health`.

### Useful Docker commands

```powershell
# List images
docker images

# List running containers
docker ps

# List all containers, including stopped containers
docker ps -a

# View application logs
docker logs jenkins-devops-app

# Stop the container
docker stop jenkins-devops-app

# Start the existing container again
docker start jenkins-devops-app
```

If Docker reports that the container name is already in use, the container already exists. Check it with `docker ps -a`, then run `docker start jenkins-devops-app` if it is stopped. To recreate it using the latest image, remove the old container first:

```powershell
docker rm -f jenkins-devops-app
docker run -d --name jenkins-devops-app -p 5000:5000 jenkins-devops-app
```

**Note:** Removing a container does not remove the Docker image, but it does remove that container instance.

## Jenkins Pipeline Setup

1. Open your Jenkins dashboard.
2. Create a **Pipeline** job (or open your existing pipeline job).
3. Configure the job to retrieve its `Jenkinsfile` from source control.
4. Set the repository URL to your GitHub repository.
5. Set the branch to `*/main` and the Script Path to `Jenkinsfile`.
6. Save the job and click **Build Now**.
7. Open the latest build and select **Console Output** to review the logs.

The pipeline used in this project includes these stages:

1. **Checkout** — Jenkins obtains the source code from GitHub through the job's SCM configuration. The named stage in the current Jenkinsfile may only print a message because Jenkins performs the actual checkout automatically.
2. **Check Python** — checks the configured Python and pip executables.
3. **Install Dependencies** — installs packages from `requirements.txt`.
4. **Run Automated Tests** — executes `python -m pytest -v`.
5. **Build Docker Image** — builds the image tagged `jenkins-devops-app`.
6. **Pipeline Complete** — reports successful completion.

If a required stage fails, the pipeline normally stops before later stages run.

### Important configuration note

The Jenkinsfile may contain machine-specific paths to Python and Docker executables. If you use another computer or Jenkins agent, update those paths or configure Python and Docker in a portable way for that environment. Ensure Docker is available to the Jenkins service account.

## Workflow

```text
Developer updates code
        |
        v
       GitHub
        |
        v
      Jenkins
        |
        v
Check Python and install dependencies
        |
        v
 Run automated tests with Pytest
        |
        v
 Build Docker image (if prior stages pass)
        |
        v
Start container manually
        |
        v
Verify the Flask application and health endpoint
```

## What This Project Demonstrates

- CI pipeline automation with Jenkins
- Source-code management using GitHub
- Automated Python testing using Pytest
- Packaging a Flask application into a Docker image
- Running and verifying a containerized web application

## Possible Future Improvements

- Configure a GitHub webhook to trigger builds on new commits.
- Add an automated deployment stage.
- Pin dependency versions for more reproducible builds.
- Use a consistent Python version for testing and the Docker image.
- Add more application tests and a pipeline health-check stage.
- Store credentials securely in Jenkins Credentials rather than in source code.

## Author

**Akhil P**

GitHub: [loopwithakhil](https://github.com/loopwithakhil)

## License

Add a license file if you intend to distribute or reuse this project publicly.
