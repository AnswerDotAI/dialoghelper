# NB: this file is designed for an LLM reader, not a human. Add it to your LLM's context and ask it to explain.
"""Read, search, edit, and manage Solveit dialogs using dialoghelper.core, including dialog/message addressing, line-numbered inspection, targeted message edits, add/update/delete/copy/paste workflows, and safe editing patterns.

notation: /why

- dialog: notebook of note, code, prompt and raw messages; open: changes live in browser; closed: on disk
- `await` every call except `dialog_link`, `msg_ref`, `find_dname`, `realpath`
- `py` tool returns stdout only: print each of several results
- `doc()` each function before first use; failed call: stop, ask user; never retry with guessed arguments
- message id: stable, e.g. `a9cb5512`; Markdown link target `#_a9cb5512`, from `msg_ref`
- current message: running cell; in a tool call, prompt being answered
- `dname`: dialog filename, `.ipynb` optional, relative to current dialog's folder; leading `/`: gateway root, not disk root
- messages above current prompt: in context, content and outputs current: don't reread; read only for fresh addresses before editing (earlier tool results may be truncated), messages below prompt (only when sure user wants them), or another dialog
- text edits: `lnhashview_msg(id)`, then `msg_exhash(id, *cmds)`; `doc(exhash.skill)` first
- `copy_msgs`, `paste_msgs`: same clipboard as Solveit's own copy and paste
- not allowed by default: `run_cells`, `run_prompt`, `browser` (JavaScript in pages showing this dialog), `rm_dialog`    /they run code or prompts, or delete data
"""

from dialoghelper.core import *
from dialoghelper.exhash import *
from pyskills.core import allow

__all__ = [
    'realpath', 'list_dialogs', 'lnhashview_msg', 'msg_exhash',
    'read_msg', 'find_msgs', 'view_dlg', 'add_msg', 'add_msgs', 'read_msgid', 'view_msg',
    'del_msgs', 'update_msg', 'copy_msgs', 'paste_msgs', 'toggle_header', 'toggle_bookmark', 'toggle_comment',
    'create_or_run_dialog', 'stop_dialog', 'run_code_interactive', 'solveit_docs', 'dialog_link',
]

allow(
    realpath, list_dialogs, read_msg, find_msgs, view_dlg, add_msg, add_msgs, read_msgid, view_msg,
    del_msgs, update_msg, copy_msgs, paste_msgs, toggle_header, toggle_bookmark, toggle_comment,
    create_or_run_dialog, stop_dialog, solveit_docs, dialog_link, lnhashview_msg, msg_exhash
)

