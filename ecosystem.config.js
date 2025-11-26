module.exports = {
  apps: [
    {
      name: "fastapi-backend-minecraft",
      script: "./venv/bin/uvicorn",
      args: "app.main:app --host 0.0.0.0 --port 8005",
      interpreter: "none",   // <- ESTO ES CLAVE
      autorestart: true,
      watch: false,
      max_memory_restart: "500M",
      env: {
        ENV: "production"
      }
    }
  ]
};
