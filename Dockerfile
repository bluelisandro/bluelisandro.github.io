# Stage 1: Build Vue app
FROM node:22-alpine as build-stage
WORKDIR /app
COPY client/package*.json ./
RUN npm install
COPY client/ ./
RUN npm run build

# Stage 2: Serve with Flask
FROM python:3.11-slim
WORKDIR /app

# Install dependencies
COPY server/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy server code
COPY server/ ./server

# Copy built frontend
COPY --from=build-stage /app/dist ./client/dist

# Create a non-root user for security
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 5000

# Run Gunicorn
# --chdir ./server points to the directory containing app.py
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "--chdir", "./server", "app:app"]
