import uvicorn

config = uvicorn.Config("api_main:app", host="0.0.0.0", port=8000, log_level="info")
server = uvicorn.Server(config)
server.run()