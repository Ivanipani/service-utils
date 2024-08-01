PYTHON_VERSION=3.12
VENV_NAME=.venv

# Default target
all: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

clean: ## Clean up generated files and directories
	rm -rf $(VENV_NAME) __pycache__

