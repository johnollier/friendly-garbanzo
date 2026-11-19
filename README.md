# friendly-garbanzo

A simple Flask web app that renders and handles a text-based contact form.
Form submissions are saved in PostgreSQL.

## Run in Codespaces

The Codespaces dev container starts PostgreSQL automatically. Its data is kept
in a Docker volume while the Codespace exists.

```bash
python app.py
```

Open the forwarded port 5000 to use the app. PostgreSQL is available to the app
at `db:5432`; the development connection URL is configured in the Compose file.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
docker compose -f .devcontainer/docker-compose.yml up -d db
export DATABASE_URL=postgresql://friendly_garbanzo:friendly_garbanzo@localhost:5432/friendly_garbanzo
python app.py
```

Open <http://127.0.0.1:5000> to submit the form. The app does not accept or
save file uploads. The Compose database credentials are for development only.
