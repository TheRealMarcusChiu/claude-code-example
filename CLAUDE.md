# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a minimal Python project with a single HTTP server (`server.py`) that uses Python's built-in `http.server` module to serve files on port 8000.

## Setup

This project uses [uv](https://docs.astral.sh/uv/) for Python environment and dependency management.

```bash
uv sync
```

## Running the server

```bash
uv run python server.py
```

The server will be available at `http://localhost:8000`.

## Running tests

```bash
uv run python -m unittest test_server.py
```
