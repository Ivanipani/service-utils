PYTHON_VERSION=3.12
VENV_NAME=.venv

# Default target
all: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

venv: ## Create virtual environment
	python$(PYTHON_VERSION) -m venv $(VENV_NAME)

install-deps: ## install Python dependencies
	pip install -r requirements-dev.txt

unit-test: ## Run unit tests
	python$(PYTHON_VERSION) -m pytest ./tests/unit


clean: ## Clean up generated files and directories
	rm -rf $(VENV_NAME) __pycache__

