set dotenv-load

# List available recipes
default:
    @just --list

# Start both frontend and backend
dev:
    #!/usr/bin/env bash
    trap 'kill 0' EXIT
    just backend &
    just frontend &
    wait

# Start frontend dev server
frontend:
    npm run dev

# Start backend dev server
backend:
    cd backend && uv run uvicorn main:app --reload --port 8321

# Type-check frontend
check:
    npx svelte-check --tsconfig ./tsconfig.json

# Build frontend for production
build:
    npm run build

# Install all dependencies
install:
    npm install
    cd backend && uv sync
