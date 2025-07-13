import asyncio
import nest_asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

nest_asyncio.apply()

"""
Make sure:
1. The server is running before running this script.
2. The server is configured to use streamable-http transport.
3. The server is listening on port 8100.

To run the server:
uv run server.py
"""


async def main():
    async with streamablehttp_client("http://localhost:8100/mcp") as (
        read_stream,
        write_stream,
        get_session_id,
    ):
        async with ClientSession(read_stream, write_stream) as session:

            await session.initialize()

            tools_result = await session.list_tools()
            print("Available Tools:")
            for tool in tools_result.tools:
                print(f" - {tool.name}: {tool.description}")

            result = await session.call_tool("add", arguments={"x": 10, "y": 5})
            print(f" 10 + 5 = {result.content[0].text}")

            result = await session.call_tool("subtract", arguments={"x": 10, "y": 5})
            print(f" 10 - 5 = {result.content[0].text}")

            result = await session.call_tool("multiply", arguments={"x": 10, "y": 5})
            print(f" 10 * 5 = {result.content[0].text}")

            result = await session.call_tool("divide", arguments={"x": 10, "y": 5})
            print(f" 10 / 5 = {result.content[0].text}")


if __name__ == "__main__":
    asyncio.run(main())
