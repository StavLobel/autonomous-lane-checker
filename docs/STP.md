# STP: OpenCV Lane Detection API - Automation QA Demo

## 1) Overview
This test plan defines the strategy, scope, and test cases for verifying the FastAPI-based Lane Detection service built on OpenCV. The API accepts images of roads and returns lane-line metrics (lane width, offset, slopes, etc.). Tests are automated with PyTest + Playwright API client, run in Docker, and validated in CI/CD.

---

## 2) Objectives
- Validate functional correctness of API endpoints.
- Ensure robustness against invalid/missing inputs.
- Validate handling of edge cases (small/large images, grayscale, night scenes).
- Verify performance meets defined thresholds.
- Provide structured, repeatable tests with Allure reporting.

---

## 3) Scope
### In scope
- `GET /health`, `GET /version`
- `POST /lanes` with multipart or base64 image input
- Functional, negative, edge, and performance tests
- CI/CD execution via GitHub Actions

### Out of scope
- Accuracy benchmarking against large datasets
- Real-time or video lane tracking
- Full ADAS validation

---

## 4) Test categories

### 4.1 Functional Tests
| ID | Title | Description | Expected Result |
|----|-------|-------------|-----------------|
| LANE-FUNC-001 | Health Check | Call `GET /health` | Returns 200 with `{"status":"ok"}` |
| LANE-FUNC-002 | Version Check | Call `GET /version` | Returns 200 with version JSON |
| LANE-FUNC-003 | Happy Path Detection | Submit clear highway image | 200, both left/right lanes detected, lane_width_px in [300,1200], offset < 40 |
| LANE-FUNC-004 | Urban Lane | Submit urban road with markings | 200, one or both lanes detected, valid metrics |
| LANE-FUNC-005 | No Markings | Submit gravel/parking lot image | 200, lanes null or empty, warnings contain `"insufficient segments"` |
| LANE-FUNC-006 | Overlay Response | Submit with `return_overlay=true` | Response includes `overlay_png_b64` field with base64 image |

---

### 4.2 Negative Tests
| ID | Title | Description | Expected Result |
|----|-------|-------------|-----------------|
| LANE-NEG-001 | Missing File | Call `POST /lanes` with no file | 422 with validation error |
| LANE-NEG-002 | Corrupt Image Bytes | Submit broken image payload | 400 or 415 with error JSON |
| LANE-NEG-003 | Unsupported Type | Submit `.txt` file | 415 unsupported media type |
| LANE-NEG-004 | Invalid Params | Send `roi_top_ratio=0.9, roi_bottom_ratio=0.5` | 422 validation error |
| LANE-NEG-005 | Oversized Image | Submit > `MAX_IMAGE_MB` | 413 Payload Too Large |

---

### 4.3 Edge Case Tests
| ID | Title | Description | Expected Result |
|----|-------|-------------|-----------------|
| LANE-EDGE-001 | Very Small Image | 160x120 px input | 200, no lanes detected, warnings contain `small_image` |
| LANE-EDGE-002 | Very Large Image | >4K resolution input | 200 within perf budget or 413 with size error |
| LANE-EDGE-003 | Grayscale Image | Submit grayscale PNG | 200, detections valid if lanes visible |
| LANE-EDGE-004 | Extreme Aspect Ratio | Panoramic image (4000x500) | 200, may detect partial lanes, warnings optional |
| LANE-EDGE-005 | Night Scene | Submit dark/low-light road image | 200, detections possible, warnings if low confidence |

---

### 4.4 Performance Tests
| ID | Title | Description | Expected Result |
|----|-------|-------------|-----------------|
| LANE-PERF-001 | Latency p95 | Run canonical test set of 3 images | p95 processing_ms < `PERF_P95_MS` (default 300 ms) |
| LANE-PERF-002 | Stability - Repeatability | Submit same image 5 times | Output lane coordinates consistent within ±5 px |
| LANE-PERF-003 | Response Size | Verify JSON payload size | < 1 MB including overlay |

---

## 5) Test data
- `data/images/happy_path/*.jpg` - clear highway images
- `data/images/no_markings/*.jpg` - gravel/parking lot
- `data/images/edge/*.jpg` - small, large, grayscale, night, aspect-ratio samples

---

## 6) Entry/Exit criteria
- **Entry:** API builds successfully, `/health` returns 200.
- **Exit:** All functional/negative/edge tests pass, performance thresholds met, report generated.

---

## 7) Reporting
- PyTest with markers (`functional`, `negative`, `edge`, `performance`)
- Allure reports (later milestone)
- Artifacts uploaded in GitHub Actions

---

## 8) Risks
- Variance in OpenCV detection on edge cases
- Performance variance in CI runners
- Test flakiness from nondeterminism

---

## 9) Deliverables
- Automated test suite in `tests/`
- Test data set in `data/images/`
- CI pipeline with artifacts
- Allure report (future milestone)
