## Project Task Catalog (derived from `docs/SRD.md`)

Legend: Priority = P0 (Critical), P1 (High), P2 (Medium), P3 (Low)

### Epics

| ID | Epic | Priority |
| --- | --- | --- |
| ALC-EP001 | Foundation: repo, app skeleton, Docker | P0 |
| ALC-EP002 | Lane detection feature: OpenCV pipeline + `/lanes` endpoint | P0 |
| ALC-EP003 | Functional tests | P0 |
| ALC-EP004 | Negative + edge tests | P1 |
| ALC-EP005 | Performance checks | P1 |
| ALC-EP006 | CI/CD pipelines + reporting | P0 |
| ALC-EP007 | Docs polish + public showcase | P2 |

---

### ALC-EP001 Foundation: repo, app skeleton, Docker (P0)

| ID | Task | Type | Priority |
| --- | --- | --- | --- |
| ALC-EP001-M01 | Scaffold project structure per SRD (`src/api`, `tests`, `config`, `docker`, `.github/workflows`, `Makefile`, `README.md`) | Major | P0 |
| ALC-EP001-M02 | Create FastAPI app bootstrap in `src/api/main.py` with server startup | Major | P0 |
| ALC-EP001-M03 | Add configuration module (`config.py`) with env loading and defaults | Major | P1 |
| ALC-EP001-M04 | Create Dockerfiles (`docker/Dockerfile.app`, `docker/Dockerfile.tests`) and `docker-compose.yml` | Major | P0 |
| ALC-EP001-M05 | Add Python dependencies (FastAPI, Uvicorn, OpenCV, NumPy, PyTest, Playwright, Allure, Bandit, Black, Flake8) | Major | P0 |
| ALC-EP001-m01 | Provide `config/settings.example.env` | Minor | P2 |
| ALC-EP001-m02 | Add `.gitignore`, tooling configs (`pytest.ini`, linter configs) | Minor | P2 |
| ALC-EP001-m03 | Seed `data/images/` with a small sample set | Minor | P2 |

---

### ALC-EP002 Lane detection feature: OpenCV pipeline + `/lanes` endpoint (P0)

| ID | Task | Type | Priority |
| --- | --- | --- | --- |
| ALC-EP002-M01 | Implement OpenCV pipeline: grayscale → Gaussian blur → Canny edges | Major | P0 |
| ALC-EP002-M02 | Implement ROI trapezoid masking | Major | P0 |
| ALC-EP002-M03 | Implement HoughLinesP detection | Major | P0 |
| ALC-EP002-M04 | Separate left/right by slope; average lines | Major | P0 |
| ALC-EP002-M05 | Compute metrics: lane width, center offset, num segments used, processing ms | Major | P0 |
| ALC-EP002-M06 | Implement overlay drawing and optional base64 output | Major | P1 |
| ALC-EP002-M07 | Define pydantic schemas for request/response contract (`schemas.py`) | Major | P0 |
| ALC-EP002-M08 | Implement `POST /lanes` in FastAPI (`lanes.py`), wire into `main.py` | Major | P0 |
| ALC-EP002-M09 | Implement `GET /health` and `GET /version` endpoints | Major | P0 |
| ALC-EP002-m01 | Parameterize thresholds (Canny, Hough, ROI) via config | Minor | P1 |
| ALC-EP002-m02 | Add deterministic seeding/guards to reduce nondeterminism | Minor | P2 |
| ALC-EP002-m03 | Validate image size against `MAX_IMAGE_MB` | Minor | P1 |

---

### ALC-EP003 Functional tests (P0)

| ID | Task | Type | Priority |
| --- | --- | --- | --- |
| ALC-EP003-M01 | Set up PyTest + Playwright API client fixtures | Major | P0 |
| ALC-EP003-M02 | Happy path test: valid road image returns expected structure/metrics | Major | P0 |
| ALC-EP003-M03 | Overlay validation test (when overlay enabled) | Major | P1 |
| ALC-EP003-M04 | No-markings scenario test (graceful response/warnings) | Major | P1 |
| ALC-EP003-M05 | JSON schema/contract validation for response | Major | P0 |
| ALC-EP003-m01 | Test data utilities and fixtures for images | Minor | P2 |
| ALC-EP003-m02 | Allure annotations and attachments (images/overlays) | Minor | P2 |

---

### ALC-EP004 Negative + edge tests (P1)

| ID | Task | Type | Priority |
| --- | --- | --- | --- |
| ALC-EP004-M01 | Negative: missing input, corrupt bytes, invalid params | Major | P1 |
| ALC-EP004-M02 | Negative: oversized file (enforce `MAX_IMAGE_MB`) | Major | P1 |
| ALC-EP004-M03 | Edge: small/large images, grayscale, night, extreme aspect ratios | Major | P1 |
| ALC-EP004-M04 | Fuzz: random invalid strings/URLs with Faker | Major | P2 |
| ALC-EP004-m01 | Validate error shapes and helpful messages | Minor | P2 |

---

### ALC-EP005 Performance checks (P1)

| ID | Task | Type | Priority |
| --- | --- | --- | --- |
| ALC-EP005-M01 | Latency: enforce p95 threshold on `/lanes` | Major | P1 |
| ALC-EP005-M02 | Stability: repeated-call test without memory bloat | Major | P2 |
| ALC-EP005-m01 | Payload size checks (request/response/overlay) | Minor | P2 |

---

### ALC-EP006 CI/CD pipelines + reporting (P0)

| ID | Task | Type | Priority |
| --- | --- | --- | --- |
| ALC-EP006-M01 | Workflow: Lint & Security (flake8, black --check, bandit) on pushes/PRs | Major | P0 |
| ALC-EP006-M02 | Workflow: Unit tests (if any) | Major | P1 |
| ALC-EP006-M03 | Workflow: API tests (functional + negative) on PRs | Major | P0 |
| ALC-EP006-M04 | Workflow: Extended tests (edge + performance) on merges to `main` | Major | P1 |
| ALC-EP006-M05 | Workflow: Allure reporting – upload artifacts; publish static report on `main` | Major | P1 |
| ALC-EP006-M06 | Workflow: Docs deploy to GitHub Pages | Major | P1 |
| ALC-EP006-M07 | Configure required checks before merge: lint + functional | Major | P0 |
| ALC-EP006-m01 | Cache pip and Docker layers for faster CI | Minor | P2 |
| ALC-EP006-m02 | Makefile targets used in CI jobs for parity | Minor | P2 |

---

### ALC-EP007 Docs polish + public showcase (P2)

| ID | Task | Type | Priority |
| --- | --- | --- | --- |
| ALC-EP007-M01 | Finalize docs: ARCH, API, TESTING, CI, STP, SRD alignment | Major | P2 |
| ALC-EP007-M02 | README: project overview, quickstart, badges, links to reports | Major | P2 |
| ALC-EP007-M03 | Publish docs and Allure to GitHub Pages | Major | P2 |
| ALC-EP007-m01 | Add screenshots/diagrams (pipeline, ROI, overlays) | Minor | P3 |
| ALC-EP007-m02 | Release notes / changelog entry | Minor | P3 |

---

### Cross-cutting risk mitigations (distributed across epics)

| ID | Task | Type | Priority |
| --- | --- | --- | --- |
| ALC-RISK-m01 | Stabilize preprocessing to reduce OpenCV nondeterminism | Minor | P2 |
| ALC-RISK-m02 | Keep small, diverse image set to reduce CI variance | Minor | P2 |
| ALC-RISK-m03 | Enforce `MAX_IMAGE_MB` and validate inputs strictly | Minor | P1 |

---

### Acceptance criteria checklist

- [ ] ALC-ACC-01 (P0): `make docker-up` runs app + tests locally
- [ ] ALC-ACC-02 (P0): CI runs full suite with artifacts + report publishing
- [ ] ALC-ACC-03 (P0): All functional/negative/edge/performance tests pass
- [ ] ALC-ACC-04 (P1): Docs complete and published; README highlights features and links


