FROM python:3.11-slim

WORKDIR /app

RUN pip install uv

# Copy pyproject.toml and uv.lock
COPY pyproject.toml .
COPY uv.lock .

# Install dependencies using uv
RUN uv sync --frozen

# Copy all source files
COPY *.py .

EXPOSE 8100

CMD ["uv", "run", "server.py"] 