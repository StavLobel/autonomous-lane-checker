# SRD: OpenCV Lane Detection API - Automation QA Demo

## 1) Project overview
A self-contained, interview-ready demo that showcases end-to-end automation skills: OpenCV logic wrapped by a FastAPI service, tested via PyTest using Playwright’s API client, containerized with Docker, and executed in GitHub Actions. The API performs classic lane-line detection on road images and returns structured metrics useful for automotive-type discussions.

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

---

## 2) System under test

### 2.1 FastAPI endpoints
- `GET /health` → returns `{"status":"ok"}` for liveness.
- `GET /version` → API + config info.
- `POST /lanes` → accepts image (multipart or base64), optional params, returns detections + metrics.

### 2.2 Response contract (example)
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

### 2.3 OpenCV pipeline
- Grayscale → Gaussian blur → Canny edges
- Trapezoid ROI → HoughLinesP
- Separate left/right by slope → average lines
- Compute lane width + center offset

---

## 3) Test strategy
- **Functional**: happy path, no-markings, overlay checks
- **Negative**: missing input, corrupt bytes, invalid params, oversized file
- **Edge**: small/large images, grayscale, night, extreme aspect ratios
- **Performance**: latency (p95 < threshold), stability, payload size

---

## 4) Tooling and standards
- Python 3.12
- FastAPI, Uvicorn
- OpenCV, NumPy
- PyTest + Playwright API client
- Docker for app + tests
- GitHub Actions for CI/CD
- Allure + GH Pages reporting

---

## 5) Repository layout (proposed)
```
repo-root/
  src/
    api/
      main.py
      schemas.py
      lanes.py
      config.py
      draw.py
  tests/
    api/
      functional/
      negative/
      edge/
      performance/
    conftest.py
    utils/
  data/images/
  config/
    pytest.ini
    settings.example.env
  docker/
    Dockerfile.app
    Dockerfile.tests
    docker-compose.yml
  .github/workflows/
    ci.yml
  Makefile
  README.md
```

---

## 6) CI/CD pipelines
The CI/CD setup is split into multiple pipelines for clarity and speed:

1. **Lint & Security** – run `flake8`, `black --check`, `bandit` (on all pushes/PRs)  
2. **Unit Tests** – run `pytest -m unit` (if unit-level tests exist)  
3. **API Tests (Functional + Negative)** – run on PRs  
4. **Extended Tests (Edge + Performance)** – run on merges to `main`  
5. **Allure Reporting** – upload artifacts on all runs, publish static report on `main`  
6. **Docs Deploy** – publish Markdown docs + reports to GitHub Pages  

**Policy:**  
- PR → lint, unit, functional, negative  
- main → full suite (functional, negative, edge, performance)  
- Required checks before merge: lint + functional

---

## 7) Makefile usage
The project provides a `Makefile` for common developer tasks:

- `make install` → install dependencies  
- `make run` → run FastAPI app locally (port 8000)  
- `make test` → run all tests locally (`pytest`)  
- `make docker-up` → build & start app + tests with Docker Compose  
- `make docker-down` → stop services  
- `make clean` → remove caches + test artifacts  

---

## 8) Milestones and epics
1. Foundation: repo + app skeleton + Docker  
2. Lane detection feature: OpenCV pipeline, `/lanes` endpoint  
3. Functional tests: happy path, overlay, no-markings  
4. Negative + edge tests  
5. Performance checks  
6. CI/CD with pipelines and reporting  
7. Docs polish + public showcase  

---

## 9) Risks & mitigations
- OpenCV nondeterminism → use stable preprocessing, tolerances  
- CI perf variance → small image set, flexible thresholds  
- Payload size/memory issues → enforce `MAX_IMAGE_MB`  
- Overfitting → diverse but small sample dataset  

---

## 10) Acceptance criteria
- One-command local run (`make docker-up`) runs app + tests  
- CI runs full suite with artifacts + report publishing  
- All functional/negative/edge/performance tests pass  
- README + docs (ARCH, API, TESTING, CI, STP, SRD) complete  
