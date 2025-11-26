module.exports = {
  apps: [
    {
      name: "fastapi-backend-minecraft",
      script: "./venv/bin/uvicorn",
      args: "app.main:app --host 0.0.0.0 --port 8005",
      watch: false,
      autorestart: true,
      max_memory_restart: "500M",
      env: {
        ENV: "production"
      }
    }
  ]
};
