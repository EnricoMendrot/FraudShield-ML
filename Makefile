.PHONY: install run test lint format clean help

PYTHON = python
PIP = pip

install:
	$(PIP) install -r requirements.txt

run:
	docker compose up -d

test:
	$(PYTHON) -m pytest tests/

lint:
	$(PYTHON) -m ruff check .

format:
	$(PYTHON) -m ruff format .
	$(PYTHON) -m ruff check --fix .

clean:
	$(PYTHON) -c "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.pyc')]"
	$(PYTHON) -c "import pathlib, shutil; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('__pycache__')]"
	$(PYTHON) -c "import pathlib, shutil; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('.pytest_cache')]"

help:
	@echo "Comandos disponíveis:"
	@echo "  make install  - Instala dependências"
	@echo "  make run      - Roda a aplicação (Docker)"
	@echo "  make test     - Executa os testes (Pytest)"
	@echo "  make lint     - Verifica o código (Ruff)"
	@echo "  make format   - Formata o código (Ruff)"
	@echo "  make clean    - Remove arquivos de cache"