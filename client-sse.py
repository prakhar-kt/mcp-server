import asyncio
import nest_asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

nest_asyncio.apply()

"""
Make sure:
1. The server is running before running this script
2. The server is configured to use SSE transport
3. The server is listening on port 8100

To run the server:
uv run server.py
"""


async def main():
    # Connect to the mcp server using SSE
    async with sse_client("http://localhost:8100/sse") as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()

            # List availabale tools
            tools_result = await session.list_tools()
            print("Available tools:")
            for tool in tools_result.tools:
                print(f" - {tool.name}: {tool.description}")

            # Call our calculator tool
            result = await session.call_tool("add", arguments={"x": 8, "y": 4})
            print(f"8 + 4 = {result.content[0].text}")

            result = await session.call_tool("subtract", arguments={"x": 8, "y": 4})
            print(f"8 - 4 = {result.content[0].text}")

            result = await session.call_tool("multiply", arguments={"x": 8, "y": 4})
            print(f"8 * 4 = {result.content[0].text}")

            result = await session.call_tool("divide", arguments={"x": 8, "y": 4})
            print(f"8 / 4 = {result.content[0].text}")


if __name__ == "__main__":
    asyncio.run(main())
