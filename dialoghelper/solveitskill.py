"""Read, search, edit, and manage Solveit dialogs using dialoghelper.core, including dialog/message addressing, line-numbered inspection, targeted message edits, add/update/delete/copy/paste workflows, and safe editing patterns.

A dialog is a notebook of messages: notes, code, prompts, and raw text. These functions read and change dialogs. Call them with `await`, except `dialog_link`, `msg_ref`, and `find_dname`, which are ordinary functions. The `python` tool returns only stdout, so print each result you want to see when one call produces several. Read a function's `doc()` before first using it. When a call fails, stop and ask the user rather than retrying with guessed arguments.

## Addressing

Each message has a stable `id`, such as `a9cb5512`. The current message is the one most recently run, and Solveit sets it. `read_msg`, `add_msg`, and `update_msg` use the current message when you omit `id`. Markdown links to a message use its DOM anchor, which has a `_` prefix (`#_a9cb5512`). `msg_ref` builds these links.

Pass `dname` to act on another dialog, named by its `.ipynb` filename. A name without a leading `/` is relative to the current dialog's folder. A leading `/` starts from the gateway root, not the disk root. With no `dname`, functions act on the current dialog. Changes to an open dialog appear live in the browser, and changes to a closed dialog are written to disk. `find_dname` returns the gateway-root-relative form of a name, without the leading slash.

## Reading

Messages above the current prompt are already in your context, with up-to-date content and outputs. Don't read them again. Read only to:

- get fresh addresses just before editing, because earlier tool results in your context may be truncated
- see messages below the current prompt, when you are sure the user wants you to look ahead
- see another dialog

`view_dlg` shows the whole dialog at once, and is usually the quickest start. `find_msgs` searches by regex and filters by message type, errors, or changes. `read_msg` moves relative to the current message. `view_msg` returns a message's content, and `read_msgid` adds its metadata and output.

## Changing messages

`add_msg` adds a message after the current one. The current message does not move, so repeated calls without `id` come out in reverse order. Pass each call's returned id as the next call's `id`. `update_msg` changes only the fields you pass. `del_msgs` deletes messages: use it only when the user asks for a deletion. `copy_msgs` and `paste_msgs` move or duplicate messages within running dialogs. `toggle_header`, `toggle_bookmark`, and `toggle_comment` switch a message's collapsed heading, numbered bookmark, or line comments.

To edit a message's text, read `doc(exhash.skill)` first. Take the id from your context, or from `view_dlg` or `find_msgs`. View the message with `lnhashview_msg(id)`, apply commands with `msg_exhash(id, *cmds)`, and view it again before any further edit.

## Dialogs and other tools

`curr_dialog` describes the current dialog, `list_dialogs` lists the dialogs and folders under a path, and `realpath` gives the dialog's on-disk path. `create_or_run_dialog` creates a dialog or starts its kernel, and `stop_dialog` stops it. `dialog_link` returns a link that opens a dialog in Solveit. `run_code_interactive` puts code in the user's dialog for them to run: use it only when no other function does the job. `solveit_docs` returns Solveit's reference documentation. `spawn_agent` starts a subagent, and must be called as a tool, not from Python.

Three functions run code or delete data, so they are not allowed by default. `_add_msg_unsafe` adds a message and runs it, `run_msg` queues messages to run, and `rm_dialog` deletes a dialog.
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
