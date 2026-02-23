.PHONY: all build sdist wheel install install-dev check clean deps

all: build

# Install build and check dependencies
deps:
	pip install --upgrade build twine

# Build both sdist and wheel
build: deps
	python -m build

# Build source distribution only
sdist: deps
	python -m build --sdist

# Build wheel only
wheel: deps
	python -m build --wheel

# Check the built distributions for common packaging issues
check: build
	twine check dist/*

# Install the package in editable/development mode
install-dev:
	pip install -e .

# Install the built wheel
install: wheel
	pip install dist/*.whl

# Remove build artifacts
clean:
	rm -rf build/ dist/ *.egg-info/ favicon_generator/*.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
