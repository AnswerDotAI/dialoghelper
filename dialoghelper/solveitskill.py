"""Read, search, edit, and manage Solveit dialogs using dialoghelper.core, including dialog/message addressing, line-numbered inspection, targeted message edits, add/update/delete/copy/paste workflows, and safe editing patterns.

A dialog is a notebook of messages (note, code, prompt, raw). Call functions with `await`, except the ordinary functions `dialog_link`, `msg_ref`, `find_dname`. The `python` tool returns only stdout: print each result when one call produces several. Read a function's `doc()` before first use; if a call fails, stop and ask the user rather than retrying with guessed arguments.

## Addressing

Messages have stable ids (`a9cb5512`). The current message is the most recently run one (Solveit sets it); `read_msg`, `add_msg`, and `update_msg` use it when `id` is omitted. Markdown refs to a message use its DOM anchor, with a `_` prefix (`#_a9cb5512`); `msg_ref` builds them. `dname` names another dialog by its `.ipynb` filename: relative to the current dialog's folder, or from the gateway root (not the disk root) with a leading `/`; default the current dialog. Open dialogs update live in the browser; closed ones update on disk.

## Reading

Messages above the current prompt are already in your context, with up-to-date content and outputs: don't reread them. Read only to get fresh addresses just before editing (earlier tool results may be truncated), to see messages below the prompt when you're sure the user wants that, or to see another dialog. `view_dlg`: whole dialog, usually the quickest start. `find_msgs`: regex search, filters by type, errors, or changes. `read_msg`: relative to the current message. `view_msg`: content; `read_msgid`: content plus metadata and output.

## Changing messages

`add_msg` inserts after the current message, which doesn't move: repeated calls without `id` come out reversed, so pass each returned id as the next call's `id`. `update_msg` changes only the fields passed. `del_msgs` only when the user asks for a deletion. `copy_msgs`/`paste_msgs` move or duplicate messages within running dialogs. `toggle_header`/`toggle_bookmark`/`toggle_comment` switch a message's collapsed heading, numbered bookmark, or line comments.

Text edits use exhash (read `doc(exhash.skill)` first): take the id from context, `view_dlg`, or `find_msgs`; view with `lnhashview_msg(id)`; apply `msg_exhash(id, *cmds)`; view again before further edits.

## Dialogs and other tools

`curr_dialog`: current dialog info. `list_dialogs`: dialogs and folders under a path. `realpath`: on-disk path. `create_or_run_dialog`/`stop_dialog`: create a dialog or start its kernel / stop it. `dialog_link`: link that opens a dialog in Solveit. `run_code_interactive`: puts code in the user's dialog for them to run; only when no other function does the job. `solveit_docs`: Solveit reference docs. `spawn_agent`: starts a subagent; call it as a tool, not from Python.

Not allowed by default, because they run code or delete data: `_add_msg_unsafe` (adds and runs a message), `run_msg` (queues messages to run), `rm_dialog` (deletes a dialog).
"""

from dialoghelper.core import *
from dialoghelper.exhash import *
from pyskills.core import allow

__all__ = [
    'curr_dialog', 'realpath', 'list_dialogs', 'lnhashview_msg', 'msg_exhash',
    'read_msg', 'find_msgs', 'view_dlg', 'add_msg', 'read_msgid', 'view_msg',
    'del_msgs', 'update_msg', 'copy_msgs', 'paste_msgs', 'toggle_header', 'toggle_bookmark', 'toggle_comment',
    'create_or_run_dialog', 'stop_dialog', 'run_code_interactive', 'solveit_docs', 'dialog_link', 'spawn_agent',
]

allow(
    curr_dialog, realpath, list_dialogs, read_msg, find_msgs, view_dlg, add_msg, read_msgid, view_msg,
    del_msgs, update_msg, copy_msgs, paste_msgs, toggle_header, toggle_bookmark, toggle_comment,
    create_or_run_dialog, stop_dialog, solveit_docs, dialog_link, spawn_agent, lnhashview_msg, msg_exhash
)

from dialoghelper.core import *
from dialoghelper.exhash import *
