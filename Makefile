# ----- Cross-platform Makefile for local dev -----
# Usage:
#   make dev     # create .venv and install deps
#   make fis     # run scripts/fetch_fis.py (writes _data/fis_results.json)
#   make news    # run scripts/fetch_news.py (writes _data/news.json)
#   make run     # run both
#   make clean   # remove .venv + caches (posix only)

ifeq ($(OS),Windows_NT)
  PY       ?= python
  VENV_BIN := .venv/Scripts
  RM       := rmdir /S /Q
else
  PY       ?= python3
  VENV_BIN := .venv/bin
  RM       := rm -rf
endif

PIP     := $(VENV_BIN)/pip
PYTHON  := $(VENV_BIN)/python
REQ     := requirements.txt

.PHONY: dev fis news run clean

dev: .venv/.created
	@echo
	@echo "✓ Virtualenv ready at .venv"
	@echo "→ VS Code: Command Palette › Python: Select Interpreter › $(PYTHON)"

.venv/.created:
	$(PY) -m venv .venv
	$(PIP) -q install -U pip
	@if [ -f $(REQ) ]; then \
		$(PIP) -q install -r $(REQ); \
	else \
		$(PIP) -q install requests beautifulsoup4 lxml feedparser pyyaml; \
	fi
	@echo "created" > .venv/.created

fis: dev
	$(PYTHON) scripts/fetch_fis.py

news: dev
	$(PYTHON) scripts/fetch_news.py

run: fis news

clean:
	-$(RM) .venv
	-$(RM) **/__pycache__ __pycache__ 2> NUL || true
