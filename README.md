# ERPNext AST-Based Code Explainer

This project is a static code analysis tool built using Python AST to help
developers and interns understand ERPNext modules faster.

## What it does
- Analyzes ERPNext Python source files without executing them
- Extracts function names, inputs, behavior, and result type
- Works with DocType and utility modules
- Safe, fast, and deterministic

## Why AST
- No runtime execution
- No hallucination
- Accurate structural analysis

## Project Structure
- `main.py` – entry point
- `module_reader.py` – locates ERPNext source files
- `ast_parser.py` – core AST analysis logic
- `ai_client.py` – optional AI explanation layer (future-ready)

## Usage
```bash
python main.py

