"""Helper functions for solveit dialogs

Modules:

- `dialoghelper.solveitskill`: Read, search, edit, and manage Solveit dialogs using dialoghelper.core, including dialog/message addressing, line-numbered inspection, targeted message edits, add/update/delete/copy/paste workflows, and safe editing patterns.
- `dialoghelper.termskill`: Read and edit Solveit dialog (or Jupyter) .ipynb files from a CLI / script. Solveit is an online notebook application (like Jupyter with AI integration) where each notebook is called a "dialog" and is stored as an `.ipynb` file containing `code`, `note` (markdown), and `prompt` (markdown with a special delimiter) messages (aka "cells"). The `dialoghelper` package provides tools for reading, searching, adding, updating, and deleting those messages.
- `dialoghelper.tmux`: Capture and inspect content from tmux sessions, windows, and panes — locally or over SSH. Useful for sharing terminal output with LLMs, debugging across multiple terminals, or monitoring long-running processes."""

__version__ = "0.2.42"
from .core import *
