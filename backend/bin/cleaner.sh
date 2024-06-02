#! /usr/bin/env bash
rm -rf db.sqlite3
find . -path "*/migration/*.py" -not -name "--init--.py" -delete

#-not -path "./.venv/*"
