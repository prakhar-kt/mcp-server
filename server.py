from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv(".env")


mcp = FastMCP(
    name="Calculator",
    description="A simple calculator that can perform basic arithmetic operations.",
    version="1.0.0",
    author="PS",
    host="0.0.0.0", # For SSE tranport only (locahost)
    port=8100,
),

#Add a simple calculator tool to the MCP server
@mcp.tool()
def add(x: float, y: float) -> float:
    """Adds two numbers."""
    return x + y

@mcp.tool()
def subtract(x: float, y: float) -> float:
    """Subtracts two numbers."""
    return x - y

@mcp.tool()
def multiply(x: float, y: float) -> float:
    """Multiplies two numbers."""
    return x * y    

@mcp.tool()
def divide(x: float, y: float) -> float:
    """Divides two numbers."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y    

# Run the MCP server
if __name__ == "__main__":
    transport = "stdio"  # Change to "sse" for SSE transport
    if transport == "stdio":
        print("Starting MCP server with stdio transport...")
        mcp.run(transport=transport)
    elif transport == "sse":
        print("Starting MCP server with SSE transport...")
        mcp.run(transport=transport, host="0.0.0.0", port=8100)
    else:
        raise ValueError("Unsupported transport type. Use 'stdio' or 'sse'.")