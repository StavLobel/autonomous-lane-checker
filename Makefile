# Makefile for Lane Detection API

.PHONY: help install run test docker-up docker-down clean lint format

# Default target
help: ## Show this help message
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-15s %s\n", $$1, $$2}'

install: ## Install Python dependencies
	pip install -r requirements.txt
	pip install -r requirements-test.txt
	playwright install chromium

run: ## Run FastAPI app locally (port 8000)
	uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --reload

test: ## Run all tests locally
	pytest -v

test-functional: ## Run functional tests only
	pytest -v -m functional

test-negative: ## Run negative tests only
	pytest -v -m negative

test-edge: ## Run edge tests only
	pytest -v -m edge

test-performance: ## Run performance tests only
	pytest -v -m performance

docker-build: ## Build Docker images
	docker-compose -f docker/docker-compose.yml build

docker-up: ## Build and start app + tests with Docker Compose
	docker-compose -f docker/docker-compose.yml up --build -d app
	@echo "API running at http://localhost:8000"
	@echo "Health check: http://localhost:8000/health"
	@echo "API docs: http://localhost:8000/docs"

docker-test: ## Run tests in Docker
	docker-compose -f docker/docker-compose.yml --profile testing up --build --abort-on-container-exit tests

docker-down: ## Stop Docker services
	docker-compose -f docker/docker-compose.yml down -v

clean: ## Remove caches and test artifacts
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache
	rm -rf test-results
	rm -rf allure-results
	rm -rf .coverage
	docker-compose -f docker/docker-compose.yml down -v --remove-orphans

lint: ## Run linting checks
	flake8 src/ tests/ --max-line-length=88 --extend-ignore=E203,W503
	bandit -r src/ -ll

format: ## Format code with Black
	black src/ tests/

format-check: ## Check code formatting
	black --check --diff src/ tests/

# Development helpers
dev-setup: install ## Set up development environment
	cp config/settings.example.env config/settings.env
	@echo "Development environment set up!"
	@echo "Edit config/settings.env for local configuration"

logs: ## Show Docker logs
	docker-compose -f docker/docker-compose.yml logs -f

health: ## Check API health
	curl -f http://localhost:8000/health || echo "API not running"
