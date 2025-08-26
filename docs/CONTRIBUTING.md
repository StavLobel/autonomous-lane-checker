# CONTRIBUTING: OpenCV Lane Detection API - Automation QA Demo

## Local Development

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the app locally
```bash
uvicorn src.api.main:app --reload --port 8000
```

### Run tests locally
```bash
pytest -m functional
pytest -m negative
pytest -m edge
pytest -m performance
```

### Run with Docker
```bash
docker compose up --build
```

---

## Branching & CI
- Use feature branches: `feature/...`.
- All PRs trigger GitHub Actions tests.
- Merging to `main` triggers full suite and report publishing.

