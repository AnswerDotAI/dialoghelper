"""Read, search, edit, and manage Solveit dialogs using dialoghelper.core, including dialog/message addressing, line-numbered inspection, targeted message edits, add/update/delete/copy/paste workflows, and safe editing patterns.

## Core Concepts

- **Dialog addressing**: All functions accepting `dname` resolve paths relative to current dialog (no leading `/`) or absolute from Solveit's
  runtime data path (with leading `/`; but NOT from the disk root path). The `.ipynb` extension is never included.
- **Message addressing**: Messages have stable `id` strings (e.g., `_a9cb5512`). Solveit sets the "current message" to the most recently run message.
- **Implicit state**: After `add_msg`/`update_msg`, the "current message" is updated to the new/modified message. This enables chaining: successive `add_msg` calls create messages in sequence.

## Workflow Patterns

### Reading dialog state
- `view_dlg` — fastest way to see entire dialog structure with line numbers for editing
- `find_msgs` — search with regex, filter by type/errors/changes
- `read_msg` — navigate relative to current message
- `view_msg` (content+line numbers only) or `read_msgid` (including metadata and output)  — direct access when you have the id

**Key insight**: Messages above the current prompt are already in LLM context—their content and outputs are always up-to-date. Do NOT use read functions just to review content you can already see. Use read functions only for: (1) getting line numbers immediately before editing, (2) accessing messages below current prompt (if you're sure the user wants you to "look ahead"), (3) accessing other dialogs.

**dname**: Many functions take an optional `dname` parameter, to choose which dialog to view/edit. If `dname` is None, the current dialog is used (if any). If `dname` is an open dialog, it will be updated interactively with real-time updates to the browser. If it is a closed dialog, it will be updated on disk. Dialog names must be paths relative to solveit root (if starting with `/`, e.g. `/myproject/dlg`) or relative to the current dialog's folder (if not starting with `/`), and should *not* include the .ipynb extension. **Use absolute paths when targeting dialogs outside the current dialog's folder tree.**

### Modifying dialogs
- `add_msg` — placement can be `add_after`/`add_before` (relative to current) or `at_start`/`at_end` (absolute)
  - **NB** When not passing a message id, it defaults to the *current* message. So if you call it multiple times with no message id, the messages will be added in REVERSE! Instead, get the return value of `add_msg` after each call, and use that for the next call
- `update_msg` — partial updates; only pass fields to change
- `del_msg` — use sparingly, only when explicitly requested
`copy_msg` → `paste_msg` — for moving/duplicating messages within running dialogs.

## Non-decorated Functions Worth Knowing

**Dangerous (not allowed by default):**
- `_add_msg_unsafe(content, run_mode='run', ...)` — add AND execute message (code or prompt)
- `run_msg(ids)` — queue messages for execution
- `rm_dialog(name)` — delete entire dialog

## Important Patterns

### Key Principles

1. **Always re-read before editing.** Past call results in chat history may be TRUNCATED.
2. **Work backwards.** When making multiple edits to a message, start from the end and work towards the beginning. This prevents line number shifts from invalidating your planned edits.
3. **Don't guess when functions fail.** If a function returns an error, STOP and ask for clarification. Do not retry with guessed parameters. Better still, call doc() first!

### Typical Editing Workflow

Message editing uses exhash. View `doc(exhash.skill)` first. Then follow these steps:

```
0. Find message id in dynamic contenxt, or using `view_dlg` or  `find_msgs`
1. msg_lnhashview(id)
2. Identify lines to change
3. msg_exhash(...)
4. If more edits needed: re-read, then repeat from step 2
```

Note that all dialoghelper functions are async (so await them), and also using `print()` in `python` will return stdout, so you can use that to read multiple messages (for instance) by using multiple prints, instead of just having a single return value.
"""

from dialoghelper.core import *
from dialoghelper.exhash import *
from pyskills.core import allow

__all__ = [
    'curr_dialog', 'msg_idx', 'realpath', 'list_dialogs', 'msg_lnhashview', 'msg_exhash',
    'read_msg', 'find_msgs', 'view_dlg', 'add_msg', 'read_msgid', 'view_msg',
    'del_msg', 'update_msg', 'copy_msg', 'paste_msg', 'toggle_header', 'toggle_bookmark', 'toggle_comment',
    'create_or_run_dialog', 'stop_dialog', 'load_dialog', 'run_code_interactive', 'solveit_docs', 'dialog_link', 'spawn_agent',
]

allow(
    curr_dialog, msg_idx, realpath, list_dialogs, read_msg, find_msgs, view_dlg, add_msg, read_msgid, view_msg,
    del_msg, update_msg, copy_msg, paste_msg, toggle_header, toggle_bookmark, toggle_comment,
    create_or_run_dialog, stop_dialog, load_dialog, solveit_docs, dialog_link, spawn_agent, msg_lnhashview, msg_exhash
)
