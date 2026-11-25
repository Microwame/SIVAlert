from uvicorn import Config, Server

config = Config(
    "api_main:app",
    host="0.0.0.0",
    port=80,
    log_level="info"
)
server = Server(config)
server.run()