# Lisandro's Portfolio Site

This is the new Resume and Portfolio site, built as a testbed for future AI and web experiments.

## Architecture

- **Frontend**: Vue.js 3 (Vanilla/Standard) with Vite. Located in `client/`.
- **Backend**: Python Flask mid-tier serving static assets and API routes. Located in `server/`.
- **Deployment**: containerized with Docker, ready for AWS Lightsail.

## Directory Structure

- `client/`: Vue.js frontend application.
- `server/`: Flask backend application.
- `Dockerfile`: Multi-stage build for production.
- `docker-compose.yml`: Local development orchestration.
- `_legacy/`: Backup of the previous site.

## Running Locally

### Using Docker Compose (Recommended)
```bash
docker-compose up --build
```
Access the site at `http://localhost:5000`.

### Manual Development
1. **Frontend**:
   ```bash
   cd client
   npm install
   npm run dev
   ```
2. **Backend**:
   ```bash
   cd server
   pip install -r requirements.txt
   python app.py
   ```

## Deployment to AWS Lightsail (Automated)

We use **GitHub Actions** to build the image and **SSH** to deploy it to your Lightsail instance.

### 1. GitHub Repository Setup
Go to your Repository Settings > Secrets and Variables > Actions, and add the following **Repository Secrets**:
- `LIGHTSAIL_HOST`: The Public IP of your instance.
- `LIGHTSAIL_USERNAME`: Usually `ubuntu` or `ec2-user`.
- `LIGHTSAIL_SSH_KEY`: The private SSH key content (open your `.pem` file and copy everything).

### 2. Lightsail Instance Setup (One-time)
**Prerequisite:** When creating your instance, select **OS Only** > **Ubuntu 24.04 LTS**.

SSH into your Lightsail instance (Username: `ubuntu`) and run the following commands to prepare it:

```bash
# 1. Install Docker & Docker Compose
sudo apt-get update
sudo apt-get install -y docker.io docker-compose
sudo usermod -aG docker $USER
# Activate the changes to groups without logging out:
newgrp docker

# 2. Create App Directory
mkdir -p ~/app

# 3. Authenticate with GitHub Container Registry
# You need a GitHub Personal Access Token (Classic) with 'read:packages' scope.
# Create one at: https://github.com/settings/tokens
echo "YOUR_GITHUB_TOKEN" | docker login ghcr.io -u YOUR_GITHUB_USERNAME --password-stdin
```

### 3. Deploying
1. Copy `docker-compose.prod.yml` to the `~/app` folder on your server (you can use scp or creating it manually).
2. **Important**: Edit `docker-compose.prod.yml` on the server to replace the image name with your actual lowercase GitHub username/repo.
   Example: `image: ghcr.io/bluelisandro/bluelisandro.github.io:latest`
3. Push changes to the `develop/v2` or `main` branch. The GitHub Action will automatically build and deploy.

### Manual Verification on Server
```bash
cd ~/app
docker-compose -f docker-compose.prod.yml ps
```


## Security

- Flask-Talisman is configured for Security Headers (CSP, HSTS, etc).
- Docker container runs as a non-root user.
