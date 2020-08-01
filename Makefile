.PHONY: help clean clean-pyc clean-build lint

help:
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "lint - check style with flake8"

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

lint:
	flake8 yaml-lint-to-junit-xml test

dist: clean
	python3 setup.py sdist bdist_wheel
	python3 -m twine check dist/*

release: dist
	python3 -m twine upload --non-interactive dist/*
