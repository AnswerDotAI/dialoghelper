"""Read, search, edit, and manage Solveit dialogs using dialoghelper.core tools, including dialog/message addressing, line-numbered inspection, targeted message edits, add/update/delete/copy/paste workflows, and safe editing patterns.

## Core Concepts

- **Dialog addressing**: All functions accepting `dname` resolve paths relative to current dialog (no leading `/`) or absolute from Solveit's runtime data path (with leading `/`). The `.ipynb` extension is never included.
- **Message addressing**: Messages have stable `id` strings (e.g., `_a9cb5512`). Solveit sets the "current message" to the most recently run message.
- **Implicit state**: After `add_msg`/`update_msg`, the "current message" is updated to the new/modified message. This enables chaining: successive `add_msg` calls create messages in sequence.

## Tool Workflow Patterns

### Reading dialog state
- `view_dlg` — fastest way to see entire dialog structure with line numbers for editing
- `find_msgs` — search with regex, filter by type/errors/changes
- `read_msg` — navigate relative to current message
- `view_msg` (content+line numbers only) or `read_msgid` (including metadata and output)  — direct access when you have the id

**Key insight**: Messages above the current prompt are already in LLM context—their content and outputs are always up-to-date. Do NOT use read tools just to review content you can already see. Use read tools only for: (1) getting line numbers immediately before editing, (2) accessing messages below current prompt (if you're sure the user wants you to "look ahead"), (3) accessing other dialogs.

### Modifying dialogs
- `add_msg` — placement can be `add_after`/`add_before` (relative to current) or `at_start`/`at_end` (absolute)
  - **NB** When not passing a message id, it defaults to the *current* message. So if you call it multiple times with no message id, the messages will be added in REVERSE! Instead, get the return value of `add_msg` after each call, and use that for the next call
- `update_msg` — partial updates; only pass fields to change
- `del_msg` — use sparingly, only when explicitly requested
`copy_msg` → `paste_msg` — for moving/duplicating messages within running dialogs.

## Non-decorated Functions Worth Knowing

There are additional functions available that can be added to fenced blocks, or the user may add as tools; they are not included in schemas by default.

**Browser integration:**
- `add_html(content)` — inject HTML with `hx-swap-oob` into live browser DOM
- `iife(code)` — execute JavaScript immediately in browser
- `fire_event(evt, data)` / `event_get(evt)` — trigger/await browser events

**Content helpers:**
- `url2note(url, ...)` — fetch URL as markdown, add as note message
- `mermaid(code)` / `enable_mermaid()` — render mermaid diagrams
- `add_styles(s)` — apply solveit's MonsterUI styling to HTML

**Dangerous (not exposed by default):**
- `_add_msg_unsafe(content, run_mode='run', ...)` — add AND execute message (code or prompt)
- `run_msg(ids)` — queue messages for execution
- `rm_dialog(name)` — delete entire dialog

## Important Patterns

### Key Principles

1. **Always re-read before editing.** Past tool call results in chat history are TRUNCATED. Never rely on line numbers from earlier in the conversation—call `view_msg(id)` immediately before any edit operation.
2. **Work backwards.** When making multiple edits to a message, start from the end and work towards the beginning. This prevents line number shifts from invalidating your planned edits.
3. **Don't guess when tools fail.** If a tool call returns an error, STOP and ask for clarification. Do not retry with guessed parameters.
4. **Verify after complex edits.** After significant changes, re-read the affected region to confirm the edit worked as expected before proceeding.

### Typical Workflow

```
1. view_msg(id)           # Get current state with line numbers
2. Identify lines to change
3. msg_replace_lines(...) or msg_str_replace(...)  # Make edit
4. If more edits needed: re-read, then repeat from step 2
```

### Tool Selection

- **`msg_replace_lines`**: Best for replacing/inserting contiguous blocks. Use `view_range` on read to focus on the area.
- **`msg_str_replace`**: Best for targeted single small string replacements when you know the exact text.
- **`msg_strs_replace`**: Best for multiple small independent replacements in one call.
- **`msg_insert_line`**: Best for adding new content without replacing existing lines.
- **`msg_del_lines`**: Best for removing content.

**Rough rule of thumb:** Prefer `msg_replace_lines` over `msg_str(s)_replace` unless there's >1 match to change or it's just a word or two. Use the insert/delete functions for inserting/deleting; don't use `msg_str(s)_replace` for that.

### Common Mistakes to Avoid

- Using line numbers from a truncated earlier result
- Making multiple edits without re-reading between them
- Guessing line numbers when a view_range was truncated
- Always call `view_msg(id)` first to get accurate line numbers
- String-based tools (`msg_str_replace`, `msg_strs_replace`) fail if the search string appears zero or multiple times—use exact unique substrings.
""" 

from dialoghelper.core import *
from pyskills.core import allow

__all__ = [
    'curr_dialog', 'msg_idx', 'realpath', 'list_dialogs',
    'read_msg', 'find_msgs', 'view_dlg', 'add_msg', 'read_msgid', 'view_msg',
    'del_msg', 'update_msg', 'copy_msg', 'paste_msg',
    'toggle_header', 'toggle_bookmark', 'toggle_comment',
    'create_or_run_dialog', 'stop_dialog', 'load_dialog', 'run_code_interactive',
    'ast_grep', 'read_pr', 'dialoghelper_explain_dialog_editing',
    'solveit_docs', 'dialog_link', 'spawn_agent',
    'msg_str_replace', 'msg_strs_replace', 'msg_replace_lines',
    'msg_insert_line', 'msg_del_lines', 'msg_ast_replace', 'msg_pyrun',
]

allow(
    curr_dialog, msg_idx, realpath, list_dialogs,
    read_msg, find_msgs, view_dlg, add_msg, read_msgid, view_msg,
    del_msg, update_msg, copy_msg, paste_msg,
    toggle_header, toggle_bookmark, toggle_comment,
    create_or_run_dialog, stop_dialog, load_dialog, run_code_interactive,
    ast_grep, read_pr, dialoghelper_explain_dialog_editing,
    solveit_docs, dialog_link, spawn_agent,
    msg_str_replace, msg_strs_replace, msg_replace_lines,
    msg_insert_line, msg_del_lines, msg_ast_replace, msg_pyrun,
)