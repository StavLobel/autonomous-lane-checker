# ALC-EP001: Foundation - Implementation Context

This file contains all context needed for implementing the remaining Foundation tasks.
**Note: This file will be deleted after implementation is complete.**

## Overview
ALC-EP001: Foundation (P0) - 8 tasks total
- **Completed**: 1/8 (12.5%)
- **Remaining**: 7 tasks
- **Priority**: P0 (Critical)

## Task Details

### ALC-EP001-M02: FastAPI app bootstrap in src/api/main.py (Major, P0)
*Issue #9 - Status: Open*

**Context**: Create initial FastAPI app and server startup wiring.

**Plan**:
- [ ] Add main.py with app factory
- [ ] Wire basic routes placeholder

**Acceptance**:
- [ ] App starts locally (uvicorn) and responds on /health placeholder

**Links**: Epic: #1

---

### ALC-EP001-M03: Configuration module config.py (Major, P1)  
*Issue #10 - Status: Open*

**Context**: Provide configuration loader with env and sensible defaults.

**Plan**:
- [ ] Implement config.py
- [ ] Validate required envs or provide defaults

**Acceptance**:
- [ ] Config accessible in app; type-hinted

**Links**: Epic: #1

---

### ALC-EP001-M04: Dockerfiles and docker-compose.yml (Major, P0)
*Issue #11 - Status: Open*

**Context**: Create Docker images for app and tests, and compose setup.

**Plan**:
- [ ] Dockerfile.app and Dockerfile.tests
- [ ] docker-compose.yml to run both

**Acceptance**:
- [ ] make docker-up runs app + tests containers

**Links**: Epic: #1

---

### ALC-EP001-M05: Add Python dependencies (Major, P0)
*Issue #12 - Status: Open*

**Context**: Add dependencies: FastAPI, Uvicorn, OpenCV, NumPy, PyTest, Playwright, Allure, Bandit, Black, Flake8.

**Plan**:
- [ ] Define requirements and lock if applicable
- [ ] Verify install in CI

**Acceptance**:
- [ ] Dependencies install cleanly locally and CI

**Links**: Epic: #1

---

### ALC-EP001-m01: Provide config/settings.example.env (Minor, P2)
*Issue #13 - Status: Open*

**Context**: Add example environment file for configuration defaults and documentation.

**Plan**:
- [ ] Create config/settings.example.env
- [ ] Document each key

**Acceptance**:
- [ ] Example file present and referenced in docs

**Links**: Epic: #1

---

### ALC-EP001-m02: Add .gitignore and tooling configs (Minor, P2)
*Issue #14 - Status: Open*

**Context**: Add .gitignore and baseline linter/test configs (pytest.ini, etc.).

**Plan**:
- [ ] Add .gitignore
- [ ] Add pytest.ini and linter configs

**Acceptance**:
- [ ] Tools respect configs locally and CI

**Links**: Epic: #1

---

### ALC-EP001-m03: Seed data/images sample set (Minor, P2)
*Issue #15 - Status: Open*

**Context**: Provide small, diverse sample images for tests.
* Make sure we're fetching online dataset and not storing images locally.

**Plan**:
- [ ] Add happy_path, no_markings, edge samples

**Acceptance**:
- [ ] Tests can reference sample images

**Links**: Epic: #1

## Documentation & References

### FastAPI Documentation
**Source**: `/tiangolo/fastapi` (Trust Score: 9.9)

**Key Patterns for ALC-EP001-M02**:
- **App Factory Pattern**: Use `app = FastAPI()` with lifespan context manager
- **Health Endpoints**: Simple GET endpoints returning JSON responses
- **Lifespan Management**: Use `@asynccontextmanager` for startup/shutdown logic
- **Basic Structure**:
  ```python
  from fastapi import FastAPI
  from contextlib import asynccontextmanager
  
  @asynccontextmanager
  async def lifespan(app: FastAPI):
      # Startup logic
      yield
      # Shutdown logic
  
  app = FastAPI(lifespan=lifespan)
  
  @app.get("/health")
  async def health_check():
      return {"status": "healthy"}
  ```

**Best Practices**:
- Use async endpoints for better performance
- Implement proper startup/shutdown with lifespan
- Keep health endpoints simple and fast
- Use type hints for all parameters and responses

---

### Docker Documentation  
**Source**: `/docker/docs` (Trust Score: 9.9)

**Key Patterns for ALC-EP001-M04**:
- **Multi-stage Builds**: Separate build and runtime environments
- **Base Image Strategy**: Use minimal runtime images (alpine, distroless)
- **Layer Optimization**: Copy only necessary artifacts between stages
- **Security**: Run as non-root user when possible

**Dockerfile Structure**:
```dockerfile
# Build stage
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Runtime stage
FROM python:3.12-alpine AS runtime
WORKDIR /app
COPY --from=builder /app /app
USER nonroot:nonroot
EXPOSE 8000
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0"]
```

**Docker Compose**:
```yaml
services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - ENV=development
  tests:
    build:
      context: .
      target: test
    volumes:
      - .:/app
```

---

### Python Configuration Management
**Source**: `/pydantic/pydantic-settings` (Trust Score: 9.6)

**Key Patterns for ALC-EP001-M03**:
- **BaseSettings Class**: Inherit from `pydantic_settings.BaseSettings`
- **Environment Variables**: Automatic loading with type validation
- **Nested Configuration**: Support for complex nested structures
- **Validation**: Built-in type checking and validation

**Configuration Structure**:
```python
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        case_sensitive=False
    )
    
    # App settings
    app_name: str = "Lane Detection API"
    debug: bool = False
    
    # Server settings
    host: str = "0.0.0.0"
    port: int = Field(8000, ge=1, le=65535)
    
    # OpenCV settings
    max_image_size_mb: int = Field(10, ge=1, le=100)
    
    # Model settings
    confidence_threshold: float = Field(0.5, ge=0.0, le=1.0)
```

**Environment Variable Mapping**:
- `APP_NAME` → `app_name`
- `DEBUG` → `debug`
- `HOST` → `host`
- `PORT` → `port`
- `MAX_IMAGE_SIZE_MB` → `max_image_size_mb`
- `CONFIDENCE_THRESHOLD` → `confidence_threshold`

---

### PyTest Configuration
**Source**: PyTest official documentation patterns

**Key Patterns for ALC-EP001-m02**:
- **pytest.ini**: Central configuration file
- **Markers**: Define custom test markers
- **Options**: Configure test discovery and execution
- **Fixtures**: Shared test setup and teardown

**Configuration Structure**:
```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    -v
    --tb=short
    --strict-markers
    --disable-warnings
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    integration: marks tests as integration tests
    unit: marks tests as unit tests
    api: marks tests as API tests
filterwarnings =
    ignore::DeprecationWarning
    ignore::PendingDeprecationWarning
```

---
*Created: 2025-08-26*
*Purpose: Implementation context for ALC-EP001 Foundation tasks*
*Status: In Progress*
