################################################################
# Makefile to setup the local development environment
################################################################

#-----------------------------------------------------------------------------------------------
# Shell variables
#-----------------------------------------------------------------------------------------------

# Console text colors :)
BOLD=$(shell tput bold)
GREEN=$(shell tput setaf 2)

# Virtual environment
VENV = venv
PIP = $(VENV)/bin/pip3

#-----------------------------------------------------------------
# Tasks
#-----------------------------------------------------------------
help:
	@echo "$(BOLD)$(GREEN)Unbabel CLI"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: virtualenv
virtualenv: ## Creates a virtual environment
	@virtualenv $(VENV)

.PHONY: local-init
local-init: virtualenv  ## Init the local environment
	@$(PIP) install -r requirements.txt

.PHONY: local-test
local-test:  ## Run local tests
	cd cli; python -m pytest tests

# Default command to help
.DEFAULT_GOAL := help
