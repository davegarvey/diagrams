Guidance for MacOS.

### Pre-requisites:

- Homebrew
- Docker
- Python 3





notes


- add sub-directory in `diagrams` for the provider e.g. `tyk`
- add `__init__.py` file in provider directory - copy from other provider and adjust as needed
- update `config.py` to add provider name to `PROVIDERS` object and other objects as needed
- add a 'cleaner definition' for provider to `scripts/resource.py` - copy from other provider and adjust as needed, then add cleaner to `cleaners` object