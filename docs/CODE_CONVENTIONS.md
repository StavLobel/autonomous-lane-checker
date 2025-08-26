# CODE CONVENTIONS & DESIGN PRINCIPLES: OpenCV Lane Detection API - Automation QA Demo

## 1. General Code Style
- Follow **PEP 8** guidelines for Python code.
- Use `black` for formatting (enforced in CI).
- Use `flake8` for linting.
- Limit line length to **88 characters**.
- Use descriptive variable and function names (avoid single letters except for counters).
- Comments should explain **why**, not **what**.

---

## 2. Project Structure
- Source code under `src/`.
- Tests under `tests/` with mirrored structure (`functional`, `negative`, etc.).
- Config under `config/`.
- Keep helper functions in dedicated `utils/` modules.
- Follow separation of concerns: no business logic in FastAPI route handlers, only orchestration.

---

## 3. Object-Oriented Programming (OOP)
- Prefer classes for components with state (e.g., configuration loader, API client wrapper).
- Keep OpenCV pipeline (`lanes.py`) as **pure functions** to simplify testing and determinism.
- Encapsulate drawing/overlay logic in its own module (`draw.py`).
- Use dependency injection via FastAPI for services and configuration.

### Example pattern
```python
class LaneDetector:
    def __init__(self, config: LaneConfig):
        self.config = config

    def process(self, image: np.ndarray) -> LaneResult:
        # run pipeline, return structured result
        ...
```

---

## 4. SOLID Principles

### S - Single Responsibility Principle (SRP)
- Each module/class should have one responsibility.
- Example: `lanes.py` detects lanes; `draw.py` overlays results.

### O - Open/Closed Principle (OCP)
- Core modules should be **open for extension, closed for modification**.
- Example: allow new image preprocessing steps by plugging in a strategy, without modifying core.

### L - Liskov Substitution Principle (LSP)
- Subclasses/implementations should be replaceable without breaking.
- Example: a `BaseDetector` could be extended to `LaneDetector` or `MockDetector` for testing.

### I - Interface Segregation Principle (ISP)
- Keep interfaces small and focused.
- Example: test helpers should provide minimal interfaces (assert schema, assert latency).

### D - Dependency Inversion Principle (DIP)
- High-level modules should depend on abstractions, not concretions.
- Example: route handlers depend on `LaneDetector` interface, not on direct OpenCV calls.

---

## 5. Testing Conventions
- Use **pytest markers** (`functional`, `negative`, `edge`, `performance`).
- Parametrize tests with multiple images instead of duplicating test functions.
- Place fixtures in `conftest.py` for reuse (e.g., API client fixture, image loader fixture).
- Use utility assertions in `tests/utils/assertions.py`.

---

## 6. Documentation & Type Hints
- Use Python **type hints** consistently.
- Docstrings: Google-style or reStructuredText style.
- Example:
```python
def detect_lanes(image: np.ndarray) -> LaneResult:
    """Detect lane lines in an input image.

    Args:
        image: Input road image as numpy array.

    Returns:
        LaneResult: structured lane data with slopes, width, offsets.
    """
```

---

## 7. Error Handling
- Raise HTTPException in FastAPI for invalid inputs.
- Use Pydantic models for schema validation.
- Always return structured error responses with code + message.

---

## 8. Performance & Stability
- Keep image preprocessing efficient.
- Use time measurement utilities to track `processing_ms`.
- Ensure deterministic output for same input image.

---

## 9. Security
- Enforce `MAX_IMAGE_MB` limit for uploads.
- Sanitize inputs before processing.
- Use CI security scanning (`bandit`).

---

By following these conventions, the project stays **clean, testable, and interview-ready**, while also demonstrating adherence to professional software engineering standards.


---

## 10. Test Data Generation with Faker
- Use **Faker** for negative/fuzz testing only.
- Keep functional/edge/performance tests deterministic (no Faker).
- Faker utilities live in `tests/utils/fake_data.py`.
- Purpose: simulate random invalid inputs (URLs, strings, numbers) to validate API robustness.
