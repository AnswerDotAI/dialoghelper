"""Helper functions for solveit dialogs

Modules:

- `dialoghelper.solveitskill`: Read, search, edit, and manage Solveit dialogs using dialoghelper.core, including dialog/message addressing, line-numbered inspection, targeted message edits, add/update/delete/copy/paste workflows, and safe editing patterns.
- `dialoghelper.test`: Run dialogs' code messages through a live solveit, `nbdev-test`-style
- `dialoghelper.tmux`: Capture and inspect content from tmux sessions, windows, and panes — locally or over SSH. Useful for sharing terminal output with LLMs, debugging across multiple terminals, or monitoring long-running processes."""

__version__ = "0.2.42"
from .core import *
