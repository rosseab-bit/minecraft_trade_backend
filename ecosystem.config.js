module.exports = {
  apps: [
    {
      name: "fastapi-backend-minecraft",
      script: "uvicorn",
      args: "main:app --host 0.0.0.0 --port 8005",
      interpreter: "python3",
      watch: false,
      autorestart: true,
      max_memory_restart: "500M",
      env: {
        ENV: "production"
      }
    }
  ]
};
