# Note: "make test" won't halt if linting and coverage fail.
# Note: .egg and .egg-info folders aren't removed on "clean"
#       This is so that many make commands don't download
#       dependencies over and over again.
# Note: All these tasks are simply _recommendations_ meant to
# 		make your life easier. Change what you will but please
#		*keep the names of the tasks the same*!

# Nikhil Anand <mail@nikhil.io>
# Mon Jun 13 16:00:12 CDT 2016


.PHONY: help
help:
	@echo ""
	@echo " help"
	@echo "     Display this message"
	@echo " all"
	@echo "     Clean build artifacts, run tests, build wheel & documentation"
	@echo " build"
	@echo "     Run tests and build a wheel"
	@echo " bump"
	@echo "     Increment patch number and push tags to remote"
	@echo " clean"
	@echo "     Remove all build artifacts"
	@echo " coverage"
	@echo "     Run and display coverage report"
	@echo " dev_install"
	@echo "     Install editable version of package into virtualenv"
	@echo " doc"
	@echo "     Build HTML documentation"
	@echo " doc_serve"
	@echo "     Serve documentation on localhost:8888 and watch source for changes"
	@echo " install"
	@echo "     Install package into virtualenv"
	@echo " lint"
	@echo "     Run linter and display report"
	@echo " publish"
	@echo "     Run tests, make wheel, push to PyPI"
	@echo " sdist"
	@echo "     Build source distribution"
	@echo " test"
	@echo "     Run linter, coverage reporter, and all tests"
	@echo ""
	@echo " > To bootstrap dependencies, run 'make dev_install'"
	@echo ""

.PHONY: check_venv
check_venv:

ifndef VIRTUAL_ENV
	$(error "! You don't appear to be in a virtual environment.")
endif


.PHONY: all
all: check_venv clean test build doc


.PHONY: build
build: check_venv test
	python setup.py sdist
	python setup.py bdist_wheel
	python setup.py bdist_egg


.PHONY: bump
bump:
ifneq ($(shell bash -c 'bumpversion' >/dev/null 2>&1; echo $$?), 1)
	$(warning "! Could not find bumpversion; attempting install")
	pip install bumpversion
endif
	bumpversion patch
	git push --follow-tags


.PHONY: clean
clean: check_venv
	rm -rf dist build .cache*
	rm -rf docs/build
	find . -type f -iname "*.pyc" | xargs rm -rf {}
	find . -type d -iname "__pycache__" | xargs rm -rf {}


.PHONY: coverage
coverage: check_venv
	-python setup.py -q test --addopts --cov=laueagle


.PHONY: dev_install
dev_install: check_venv
	pip install -e .


.PHONY: doc
doc: check_venv
ifneq ($(shell bash -c 'sphinx-build' >/dev/null 2>&1; echo $$?), 1)
	$(warning "! Could not find Sphinx; attempting install")
	pip install sphinx sphinx_rtd_theme
endif
	cd docs && make clean && make html


.PHONY: doc_serve
doc_serve: doc
ifneq ($(shell bash -c 'livereload --version' >/dev/null 2>&1; echo $$?), 2)
	$(warning "! Could not find live-reloader; attempting install")
	pip install livereload
endif
	python -c "from livereload import Server, shell; server = Server(); server.watch('docs/source/*.rst', shell('make html',   cwd='docs')); server.serve(port=8888, host='localhost', root='docs/build/html')"


.PHONY: install
install: check_venv
	pip install .


.PHONY: lint
lint: check_venv
	-python setup.py -q test --addopts --flake8


.PHONY: publish
publish: check_venv build
	python setup.py sdist upload
	python setup.py bdist_wheel upload


.PHONY: sdist
sdist: check_venv
	python setup.py sdist


.PHONY: test
test: check_venv clean lint coverage
	python setup.py -q test
