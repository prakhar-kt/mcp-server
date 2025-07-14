# MCP Calculator Server

A Model Context Protocol (MCP) server implementation using FastMCP that provides calculator functionality with support for multiple transport methods.

## Features

- **Basic Arithmetic Operations**: add, subtract, multiply, divide
- **Multiple Transport Methods**: stdio, SSE (Server-Sent Events), and streamable HTTP
- **Simple Architecture**: Easy to understand and extend
- **Example Clients**: Includes working client examples for each transport method

## Quick Start

### Prerequisites

#### Local Development
- Python 3.11 or higher
- `uv` package manager

#### Docker
- Docker Engine

### Installation

#### Option 1: Local Installation

```bash
# Clone the repository
git clone <repository-url>
cd mcp-server

# Install dependencies
uv sync
```

#### Option 2: Docker

```bash
# Build the Docker image
docker build -t mcp-calculator .

# Run the container
docker run -p 8100:8100 mcp-calculator
```

### Running the Server

#### Local Development

```bash
uv run server.py
```

#### Using Docker

The Docker container automatically starts the server with streamable HTTP transport on port 8100. The MCP server will be available at:

- Streamable HTTP transport: `http://localhost:8100/mcp`

**Note**: The server doesn't serve a web interface at the root URL (`/`). To test the server, use the provided client scripts or connect with an MCP client to the `/mcp` endpoint.

The server supports three transport configurations (modify `transport` variable in `server.py:48`):

- **stdio**: Direct process communication
- **sse**: HTTP server-sent events on `http://localhost:8100/sse`
- **streamable-http**: HTTP streaming on `http://localhost:8100/mcp`

### Testing with Clients

#### Local Development

Run the appropriate client based on your server's transport configuration:

```bash
# For stdio transport
uv run client-stdio.py

# For SSE transport (server must be running)
uv run client-sse.py

# For streamable HTTP transport (server must be running)
uv run client-streamable.py
```

#### Testing Docker Container

To test the Docker container, run the streamable HTTP client:

```bash
# With Docker container running
uv run client-streamable.py
```

The client will connect to `http://localhost:8100/mcp` and demonstrate the calculator operations.

## API Reference

The calculator server exposes the following tools:

- `add(x: float, y: float)` - Adds two numbers
- `subtract(x: float, y: float)` - Subtracts two numbers
- `multiply(x: float, y: float)` - Multiplies two numbers
- `divide(x: float, y: float)` - Divides two numbers (throws error on division by zero)

## Project Structure

```text
mcp-server/
├── server.py              # Main MCP server implementation
├── main.py                # Simple entry point
├── client-stdio.py        # stdio transport client example
├── client-sse.py          # SSE transport client example
├── client-streamable.py   # Streamable HTTP transport client example
├── pyproject.toml         # Python project configuration
└── README.md              # This file
```

## Development

This project uses `uv` for dependency management. All dependencies are specified in `pyproject.toml`.

### Key Dependencies

- `mcp[cli]>=1.11.0` - Core MCP framework
- `httpx>=0.28.1` - HTTP client library
- `python-dotenv>=1.1.1` - Environment variable management
