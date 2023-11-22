PYTHON_VERSION=3.11
VENV_NAME=.venv

# Default target
all: help

# Install dependencies
install-deps:
	python3.11 -m venv .venv;
	. $(VENV_NAME)/bin/activate; pip install -r requirements-dev.txt

# Run unit tests
unit-test:
	. $(VENV_NAME)/bin/activate; python -m pytest ./tests/unit

# Clean up generated files and directories
clean:
	rm -rf $(VENV_NAME) __pycache__

help:
	@echo "Available commands:"
	@echo "  install-deps: Install dependencies from requirements.txt"
	@echo "  unit-test: Run unit tests"
	@echo "  clean: Clean up generated files and directories"
