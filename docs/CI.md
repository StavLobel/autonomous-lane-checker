# CI/CD: OpenCV Lane Detection API - Automation QA Demo

## Workflow Overview
The project uses **GitHub Actions** for CI/CD, designed to validate code quality, run automated tests, generate reports, and publish documentation. Pipelines are split into multiple jobs for clarity and maintainability.

---

## Pipelines

### 1. Lint & Security
- **Trigger:** On every push and PR
- **Steps:**
  1. Checkout code
  2. Install Python dependencies
  3. Run `flake8` and `black --check` for style
  4. Run `bandit` for security scanning
- **Outcome:** Fast feedback on code quality

---

### 2. Unit Tests (FastAPI service)
- **Trigger:** On every push and PR
- **Steps:**
  1. Build app Docker image (`Dockerfile.app`)
  2. Run `pytest -m "unit"` if unit-level tests exist (pure functions, OpenCV pipeline logic)
- **Outcome:** Ensures core functions work independently

---

### 3. API Tests (Functional + Negative)
- **Trigger:** On PR
- **Steps:**
  1. Start app container
  2. Run test runner container (`Dockerfile.tests`)
  3. Execute `pytest -m "functional or negative"`
- **Outcome:** Validates correctness and robustness on critical scenarios

---

### 4. Extended Tests (Edge + Performance)
- **Trigger:** On push/merge to `main`
- **Steps:**
  1. Start app container
  2. Run full suite `pytest -m "functional or negative or edge or performance"`
  3. Collect metrics (latency, stability)
- **Outcome:** Full validation on main branch

---

### 5. Allure Reporting
- **Trigger:** After tests in all jobs
- **Steps:**
  1. Upload `allure-results` as artifact for each run
  2. On `main`, generate Allure static HTML
  3. Publish to `gh-pages` branch via GitHub Pages
- **Outcome:** Human-readable reports accessible via public link

---

### 6. Documentation Deploy
- **Trigger:** On push to `main`
- **Steps:**
  1. Build docs (README + Markdown files + auto-generated diagrams if any)
  2. Deploy to GitHub Pages or artifact
- **Outcome:** Always up-to-date docs visible to candidates/interviewers

---

## Test Markers in CI
The test suite defines four markers:
- `functional` - core scenarios (always run)
- `negative` - invalid inputs, error handling
- `edge` - small/large images, grayscale, night scenes
- `performance` - latency, stability

---

## PR Policy
- On PR: Run `lint`, `unit`, `functional`, and `negative`
- On `main`: Run all pipelines including `edge` and `performance`
- Required checks: lint + functional must pass before merge

---

## Secrets & Env
- `MAX_IMAGE_MB` - max image size
- `PERF_P95_MS` - perf threshold (default 300 ms)
- All stored in GitHub Secrets and loaded into workflows

---

## Future Enhancements
- Add Docker image publish to GitHub Container Registry
- Add Slack/Teams notification integration
- Add scheduled nightly runs with extended edge dataset
