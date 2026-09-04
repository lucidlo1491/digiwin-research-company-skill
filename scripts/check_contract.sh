#!/bin/zsh
exec python3 "$(dirname "$0")/check_contract.py" "$@"
