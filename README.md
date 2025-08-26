# Lane Detection API

OpenCV-based lane detection service for automotive QA automation demo.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.x-013243?logo=numpy&logoColor=white)
![PyTest](https://img.shields.io/badge/PyTest-7.x-0A9EDC?logo=pytest&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-API%20tests-45ba4b?logo=playwright&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI-2088FF?logo=githubactions&logoColor=white)
![Allure](https://img.shields.io/badge/Allure-Reporting-fc4c02)
![Black](https://img.shields.io/badge/Black-formatter-000000)
![Flake8](https://img.shields.io/badge/flake8-linting-4B8BBE)
![Bandit](https://img.shields.io/badge/Bandit-security-FFC107)

## Overview

A self-contained demo showcasing end-to-end automation skills: OpenCV lane-line detection wrapped by a FastAPI service, tested via PyTest using Playwright’s API client, containerized with Docker, and executed in GitHub Actions. The API returns structured metrics suitable for robust automated tests and reporting.

### Primary goals
- Prove local-to-CI flow: run app locally, in Docker, and in CI with the same commands.
- Exercise OpenCV on a vehicle-adjacent feature: lane-line detection.
- Provide clean, deterministic outputs suitable for robust automated tests.
- Demonstrate professional test structure, fixtures, parametrization, and performance checks.
- Add reporting (Allure) and publish results/docs to GitHub Pages.

### Non-goals
- Full ADAS stack, tracking, or camera calibration.
- Heavy model inference or accuracy benchmarking across large datasets.
- Video streaming or real-time performance.

## Quick Start

### Local Development

1. **Set up environment:**
   ```bash
   make dev-setup
   make install
   ```

2. **Run the API:**
   ```bash
   make run
   ```
   
   API will be available at: http://localhost:8000
   - Health check: http://localhost:8000/health
   - API docs: http://localhost:8000/docs

3. **Run tests:**
   ```bash
   make test
   ```

### Docker

1. **Run with Docker Compose:**
   ```bash
   make docker-up
   ```

2. **Run tests in Docker:**
   ```bash
   make docker-test
   ```

3. **Stop services:**
   ```bash
   make docker-down
   ```

## Project Structure

```
autonomous-lane-checker/
├── src/api/                 # FastAPI application
│   ├── main.py             # Application entry point
│   ├── schemas.py          # Pydantic models
│   ├── lanes.py            # OpenCV lane detection pipeline
│   ├── config.py           # Configuration management
│   └── draw.py             # Overlay drawing utilities
├── tests/                  # Test suite
│   ├── api/                # API tests by category
│   │   ├── functional/     # Happy path tests
│   │   ├── negative/       # Error handling tests
│   │   ├── edge/           # Edge case tests
│   │   └── performance/    # Performance tests
│   ├── conftest.py         # Pytest configuration
│   └── utils/              # Test utilities
├── config/                 # Configuration files
├── docker/                 # Docker configuration
├── data/images/            # Test images
└── .github/workflows/      # CI/CD pipelines
```

## API Endpoints

- `GET /health` - Health check
- `GET /version` - API version and configuration
- `POST /lanes` - Lane detection (TODO: implement in ALC-EP002-M08)

### Response contract (example)

```json
{
  "lanes": {
    "left":  {"x1":120,"y1":720,"x2":300,"y2":420,"slope":-0.92},
    "right": {"x1":980,"y1":720,"x2":760,"y2":420,"slope":0.88}
  },
  "lane_width_px": 640,
  "center_offset_px": -12.5,
  "num_segments_used": 14,
  "processing_ms": 78,
  "warnings": [],
  "overlay_png_b64": null
}
```

### OpenCV Pipeline

- Grayscale → Gaussian blur → Canny edges
- Trapezoid ROI → HoughLinesP
- Separate left/right by slope → average lines
- Compute lane width + center offset

## Development

### Available Make Commands

```bash
make help           # Show all available commands
make install        # Install dependencies
make run            # Run API locally
make test           # Run all tests
make docker-up      # Run with Docker
make lint           # Run code quality checks
make format         # Format code with Black
make clean          # Clean caches and artifacts
```

### Testing Categories

- **Functional**: Happy path scenarios
- **Negative**: Error handling and invalid inputs  
- **Edge**: Boundary conditions and edge cases
- **Performance**: Latency and stability checks

Use pytest markers to run specific test categories:
```bash
pytest -m functional
pytest -m negative
pytest -m edge
pytest -m performance
```

## Configuration

Copy `config/settings.example.env` to `config/settings.env` and modify as needed.

Key settings:
- `MAX_IMAGE_MB`: Maximum image size limit
- `PERF_P95_MS`: Performance threshold (95th percentile)
- OpenCV pipeline parameters

## TODO

This is a scaffolded project structure. Implementation tasks:

- [ ] **ALC-EP001**: Complete foundation setup
- [ ] **ALC-EP002**: Implement lane detection pipeline
- [ ] **ALC-EP003**: Add functional tests
- [ ] **ALC-EP004**: Add negative/edge tests
- [ ] **ALC-EP005**: Add performance tests
- [ ] **ALC-EP006**: Set up CI/CD pipelines
- [ ] **ALC-EP007**: Polish documentation

See `docs/PROGRESS_TRACKING.md` for detailed progress tracking.

## Tooling and Standards

- Python 3.12
- FastAPI, Uvicorn
- OpenCV, NumPy
- PyTest + Playwright API client
- Docker for app + tests
- GitHub Actions for CI/CD
- Allure + GH Pages reporting

## CI/CD Pipelines and Policy

Pipelines:
1. Lint & Security – run `flake8`, `black --check`, `bandit` (on all pushes/PRs)
2. Unit Tests – run `pytest -m unit` (if unit-level tests exist)
3. API Tests (Functional + Negative) – run on PRs
4. Extended Tests (Edge + Performance) – run on merges to `main`
5. Allure Reporting – upload artifacts on all runs, publish static report on `main`
6. Docs Deploy – publish Markdown docs + reports to GitHub Pages

Policy:
- PR → lint, unit, functional, negative
- main → full suite (functional, negative, edge, performance)
- Required checks before merge: lint + functional

## Risks & mitigations

- OpenCV nondeterminism → use stable preprocessing and tolerances
- CI perf variance → small image set, flexible thresholds
- Payload size/memory issues → enforce `MAX_IMAGE_MB`
- Overfitting → diverse but small sample dataset

## Acceptance criteria

- One-command local run (`make docker-up`) runs app + tests
- CI runs full suite with artifacts + report publishing
- All functional/negative/edge/performance tests pass
- README + docs (ARCH, API, TESTING, CI, STP, SRD) complete

## License

This project is for demonstration purposes.
