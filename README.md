# callama

`callama` is a small API experiment for sending a user query through an API endpoint to an Ollama model and returning the model response.

The goal is simple: test how a prompt travels from a client request, into an API route, through the model layer, and back to the user as a response.

## What It Does

- Starts a FastAPI app.
- Returns a random default response from the root endpoint.
- Accepts a query at `/model/ask`.
- Sends that query to an Ollama model.
- Returns the original query, selected model name, and model response.

## Project Structure

```text
callama/
|-- Dockerfile              # Docker image for the FastAPI app
|-- docker-compose.yaml     # App + Ollama Docker Compose setup
|-- main.py                 # FastAPI app entry point
|-- model.py                # Ollama model call wrapper
|-- default_respones.py     # Random default root responses
|-- router/
|   `-- askmodel.py         # /model/ask endpoint
|-- example.env             # Example environment variables
|-- .dockerignore           # Files excluded from Docker builds
|-- pyproject.toml          # Project metadata and uv dependencies
|-- requirements.txt        # Pinned dependency list
`-- README.md
```

## Requirements

- Python 3.13 or newer
- Ollama access configured for the model you want to use
- `uv` or `pip`
- Docker and Docker Compose, if you want to run it in containers

## Setup

Clone the project and enter the folder:

```bash
git clone https://github.com/Pulsedude/callama.git
cd callama
```

Create a `.env` file from the example:

```bash
cp example.env .env
```

Edit `.env` and set the model:

```env
OLLAMA_CLOUD_API_KEY=
MODEL=gpt-oss:120b-cloud
OLLAMA_HOST=http://localhost:11434
```

Use any Ollama model name that is available in your environment.

## Install Dependencies

Using `uv`:

```bash
uv sync
```

Or using `pip`:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run The API

For local development:

```bash
uvicorn main:app --reload --port 8000
```

The API will run at:

```text
http://127.0.0.1:8000
```

## Run With Docker

The project includes a `Dockerfile` and `docker-compose.yaml`.

### Docker Compose

Start the API and an Ollama container together:

```bash
docker compose up
```

The API will run at:

```text
http://127.0.0.1:3000
```

The Ollama service will be available to the app at:

```text
http://ollama:11434
```

The Compose file sets these environment variables for the app:

```yaml
OLLAMA_HOST: http://ollama:11434
MODEL: gpt-oss:120b-cloud
```

Change `MODEL` in `docker-compose.yaml` if you want to use a different Ollama model.

### Build Locally

The Compose file currently uses the published image:

```yaml
image: raunaksharma/callama:latest
```

To build the image locally instead, change the app service to use:

```yaml
build: .
```

Then run:

```bash
docker compose up --build
```

You can also build and run only the app container manually:

```bash
docker build -t callama .
docker run --env-file .env -p 3000:3000 callama
```

When running only the app container, make sure `OLLAMA_HOST` points to an Ollama server that the container can reach.

## Endpoints

### Root

```http
GET /
```

Returns a random default response.

Example:

```bash
curl http://127.0.0.1:8000/
```

For Docker:

```bash
curl http://127.0.0.1:3000/
```

### Ask The Model

```http
GET /model/ask?query=<your-query>
```

Sends your query to the configured Ollama model.

Example:

```bash
curl "http://127.0.0.1:8000/model/ask?query=What%20is%20FastAPI?"
```

For Docker:

```bash
curl "http://127.0.0.1:3000/model/ask?query=What%20is%20FastAPI?"
```

Example response:

```json
{
  "query": "What is FastAPI?",
  "model": "gpt-oss:120b-cloud",
  "response": "FastAPI is a modern Python web framework..."
}
```

## API Docs

After starting the server, open:

```text
http://127.0.0.1:8000/docs
```

For Docker:

```text
http://127.0.0.1:3000/docs
```

The OpenAPI schema is available at:

```text
http://127.0.0.1:8000/openapi.json
```

For Docker:

```text
http://127.0.0.1:3000/openapi.json
```

## Notes

- This is an experiment, not a production-ready API.
- The model name comes from the `MODEL` environment variable.
- The Ollama host comes from the `OLLAMA_HOST` environment variable.
- Make sure your Ollama setup can access the selected model before calling `/model/ask`.
- Docker Compose stores Ollama data in the `ollama_data` volume.
- Error handling is intentionally simple for now.

## Free To Use

This experiment is free to use, copy, modify, and learn from.

If you use it in your own project, attribution is appreciated but not required. For clearer legal reuse, consider adding a formal open source license file such as MIT.
