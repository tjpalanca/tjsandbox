# TaxBot 

## Motivation

Simple utility to reset the passwords in Chinabank's tax payment portal, which is required quarterly.

## Instructions

1. Run `poetry install` and use the poetry environment.
2. Run `rfbrowser init` to set up requirements for robotframework
3. Inject the secret references with the 1password CLI by running `cat config.tpl.yml | op inject >> config.yml`
4. Run the script by running `python -m taxbot` in the poetry environment.
