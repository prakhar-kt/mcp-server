# MCP Calculator Server

A Model Context Protocol (MCP) server implementation using FastMCP that provides calculator functionality with support for multiple transport methods.

## Features

- **Basic Arithmetic Operations**: add, subtract, multiply, divide
- **Multiple Transport Methods**: stdio, SSE (Server-Sent Events), and streamable HTTP
- **Simple Architecture**: Easy to understand and extend
- **Example Clients**: Includes working client examples for each transport method

## Quick Start

### Prerequisites

- Python 3.13 or higher
- `uv` package manager

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd mcp-server

# Install dependencies
uv sync
```

### Running the Server

```bash
uv run server.py
```

The server supports three transport configurations (modify `transport` variable in `server.py:48`):

- **stdio**: Direct process communication
- **sse**: HTTP server-sent events on `http://localhost:8100/sse`
- **streamable-http**: HTTP streaming on `http://localhost:8100/mcp`

### Testing with Clients

Run the appropriate client based on your server's transport configuration:

```bash
# For stdio transport
uv run client-stdio.py

# For SSE transport (server must be running)
uv run client-sse.py

# For streamable HTTP transport (server must be running)
uv run client-streamable.py
```

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
