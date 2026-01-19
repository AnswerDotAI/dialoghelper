# dialoghelper

A Python library for programmatic dialog manipulation in [Solveit](https://solve.it.com), fast.ai's Dialog Engineering web application. It provides both user-callable functions and AI-accessible tools for creating, reading, updating, and managing dialog messages.

## What is Solveit?

**Solveit** is a "Dialog Engineering" web application that combines interactive code execution with AI assistance. Unlike ChatGPT (pure chat) or Jupyter (pure code), Solveit merges both paradigms into a single workspace.

### Core Concepts

- **Instance**: A persistent Linux container with your files and running kernels. Each user can have multiple instances.
- **Dialog**: An `.ipynb` file containing messages. Like a Jupyter notebook, but with AI integration. Each open dialog runs its own Python kernel.
- **Message**: The fundamental unit—similar to a Jupyter cell, but with three types:

| Type | Purpose | Example |
|------|---------|---------|
| `code` | Python execution | `print("hello")` |
| `note` | Markdown documentation | `# My Notes` |
| `prompt` | AI interaction | "Explain this function" |

### How AI Context Works

When you send a prompt to the AI:

1. **All messages above** the current prompt are collected
2. Messages marked as "hidden" (`skipped=True`) are excluded
3. If context exceeds the model limit, oldest non-pinned messages are dropped
4. The AI sees code, outputs, notes, and previous prompts/responses

Key implications:
- Working at the **bottom** of a dialog = **more context** (all messages above)
- Working **higher up** = less context
- **Pinning** a message (`p` key) keeps it in context even when truncation occurs

### Tools: AI-Callable Functions

Solveit lets the AI call Python functions directly. Users declare tools in messages using `&` followed by backticks:

```
&`my_function`                    # Expose single tool
&`[func1, func2, func3]`          # Expose multiple tools
```

When the AI needs to use a tool, Solveit executes it in the kernel and returns the result.

## Installation

The latest version is always pre-installed in Solveit. To manually install (not recommended):

```bash
pip install dialoghelper
```

## What is dialoghelper?

dialoghelper is a programmatic interface to Solveit dialogs. It enables:

- **Dialog manipulation**: Add, update, delete, and search messages
- **AI tool integration**: Expose functions as tools the AI can call
- **Context generation**: Convert folders, repos, and symbols into AI context
- **Screen capture**: Capture browser screenshots for AI analysis
- **Tmux integration**: Read terminal buffers from tmux sessions

## Modules

| Module | Source Notebook | Description |
|--------|-----------------|-------------|
| `core` | `nbs/00_core.ipynb` | Core dialog manipulation (add/update/delete messages, search, context helpers) |
| `capture` | `nbs/01_capture.ipynb` | Screen capture functionality for AI vision |
| `inspecttools` | `nbs/02_inspecttools.ipynb` | Symbol inspection (`symsrc`, `getval`, `getdir`, etc.) |
| `tmux` | `nbs/03_tmux.ipynb` | Tmux buffer reading tools |
| `stdtools` | — | Re-exports all tools from dialoghelper + fastcore.tools |

## Solveit Tools

**Tools** are functions the AI can call directly during a conversation. A function is usable as a tool if it has:

1. **Type annotations** for ALL parameters
2. **A docstring** describing what it does

```python
# Valid tool
def greet(name: str) -> str:
    "Greet someone by name"
    return f"Hello, {name}!"

# Not a tool (missing type annotation)
def greet(name):
    "Greet someone by name"
    return f"Hello, {name}!"

# Not a tool (missing docstring)
def greet(name: str) -> str: return f"Hello, {name}!"
```

### Exposing Tools to the AI

In a Solveit dialog, reference tools using `&` followed by backticks:

```
&`greet`                           # Single tool
&`[add_msg, update_msg, del_msg]`  # Multiple tools
```

### Tool Info Functions

These functions add notes to your dialog listing available tools:

| Function | Lists tools from |
|----------|------------------|
| `tool_info()` | `dialoghelper.core` |
| `fc_tool_info()` | `fastcore.tools` (rg, sed, view, create, etc.) |
| `inspect_tool_info()` | `dialoghelper.inspecttools` |
| `tmux_tool_info()` | `dialoghelper.tmux` |

### Tools vs Programmatic Functions

Some functions are designed for AI tool use; others are meant to be called directly from code:

| AI Tools | Programmatic Use |
|----------|------------------|
| `add_msg`, `update_msg`, `del_msg` |  |
| `find_msgs`, `read_msg`, `view_dlg` | `call_endp` (raw endpoint access) |
| `symsrc`, `getval`, `getdir` | `resolve` (returns actual Python object) |

## Usage Examples

```python
from dialoghelper import *

# Add a note message
add_msg("Hello from code!", msg_type='note')

# Add a code message
add_msg("print('Hello')", msg_type='code')

# Search for messages
results = find_msgs("pattern", msg_type='code')

# View entire dialog structure
print(view_dlg())

# Generate context from a folder
ctx_folder('.', types='py', max_total=5000)
```

## Development: nbdev Project Structure

dialoghelper is an [nbdev](https://nbdev.fast.ai) project. **Notebooks are the source of truth**—the `.py` files are auto-generated.

### Notebook ↔ Python File Mapping

| Notebook | Generated File |
|----------|----------------|
| `nbs/00_core.ipynb` | `dialoghelper/core.py` |
| `nbs/01_capture.ipynb` | `dialoghelper/capture.py` |
| `nbs/02_inspecttools.ipynb` | `dialoghelper/inspecttools.py` |
| `nbs/03_tmux.ipynb` | `dialoghelper/tmux.py` |

### Workflow

1. Edit notebooks in `nbs/`
2. Run `nbdev_export()` to generate `.py` files
3. Never edit `.py` files directly—they'll be overwritten

## License

Apache 2.0

