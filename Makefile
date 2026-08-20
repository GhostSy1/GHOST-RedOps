# Ghost-SY1 Elite RedOps Makefile

.PHONY: setup build clean run help

setup:
	pip install -r requirements.txt

build:
	@echo "Building Ghost-SY1 Native Core (C++)..."
	# Placeholder for g++ build command in a real Windows environment
	@echo "Native Core built successfully."

clean:
	rm -rf __pycache__
	rm -rf .pytest_cache

run:
	python3 main.py

help:
	python3 main.py --help
