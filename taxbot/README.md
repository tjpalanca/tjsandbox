# TaxBot 

## Motivation

Simple utility to reset the passwords in Chinabank's tax payment portal, which is required quarterly.

## Instructions

1. Run `make deps` and use the poetry environment and to set up requirements for robotframework.
2. Inject the secret references with the 1password CLI by running `cat config.tpl.yml | op inject >> config.yml`
3. Run the script by running `poetry run python -m taxbot` in the poetry environment.
