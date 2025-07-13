import asyncio
import nest_asyncio
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

nest_asyncio.apply()


async def main():
    # Define the server parameters
    server_params = StdioServerParameters(
        command=sys.executable,  # Use the current Python interpreter for cross-platform compatibility
        args=["server.py"],
    )

    # Connect to the MCP server using stdio transport
    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            # Example usage of the calculator tools
            await session.initialize()
            # list available tools
            tools_result = await session.list_tools()
            print("Available Tools:")
            for tool in tools_result.tools:
                print(f" - {tool.name}: {tool.description}")

            result = await session.call_tool("add", arguments={"x": 6, "y": 2})
            print(f"6 + 2 = {result.content[0].text}")

            result = await session.call_tool("subtract", arguments={"x": 6, "y": 2})
            print(f"6 - 2 = {result.content[0].text}")

            result = await session.call_tool("multiply", arguments={"x": 6, "y": 2})
            print(f"6 * 2 = {result.content[0].text}")

            result = await session.call_tool("divide", arguments={"x": 6, "y": 2})
            print(f"6 / 2 = {result.content[0].text}")


if __name__ == "__main__":
    asyncio.run(main())
