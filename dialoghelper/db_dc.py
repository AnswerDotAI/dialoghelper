__all__ = ["_Meta", "Attachment", "Completion", "Completion_Mode", "Context", "Dialog", "Message", "Secret", "User"]
from dataclasses import dataclass
@dataclass
class _Meta:
    id: int | None = None
    version: int | None = 0

@dataclass
class Attachment:
    id: str | None = None
    data: bytes | None = None
    content_type: str | None = None
    sid: int | None = None

@dataclass
class Completion:
    req_id: str | None = None
    did: int | None = None
    mid: int | None = None
    mtype: str | None = None
    pfx: str | None = None
    sfx: str | None = None
    ctx: str | None = ''
    mode: str | None = None
    comp: str | None = None
    logprobs: str | None = None
    status: str | None = None

@dataclass
class Completion_Mode:
    id: int | None = None
    name: str | None = None
    c_acceptichars: int | None = None
    c_scon: int | None = None
    c_triggerc: str | None = None
    c_triggeronaccept: int | None = None
    c_mftp: float | None = None
    c_model: str | None = None
    c_nlines: str | None = None
    c_temp: float | None = None
    p_acceptichars: int | None = None
    p_scon: int | None = None
    p_triggerc: str | None = None
    p_triggeronaccept: int | None = None
    p_mftp: float | None = None
    p_model: str | None = None
    p_nlines: str | None = None
    p_temp: float | None = None

@dataclass
class Context:
    name: str | None = None
    context: str | None = None
    token_count: int | None = 0
    did: int | None = None

@dataclass
class Dialog:
    id: int | None = None
    name: str | None = None
    mode: int | None = 2

@dataclass
class Message:
    sid: str | None = None
    mid: str | None = None
    content: str | None = None
    output: str | None = ''
    input_tokens: int | None = '0'
    output_tokens: int | None = '0'
    msg_type: str | None = 'code'
    time_run: str | None = ''
    is_exported: int | None = '0'
    skipped: int | None = '0'
    did: int | None = None
    i_collapsed: int | None = '0'
    o_collapsed: int | None = '0'
    header_collapsed: int | None = '0'
    pinned: int | None = '0'
    use_thinking: int | None = 0

@dataclass
class Secret:
    name: str | None = None
    secret: str | None = None

@dataclass
class User:
    id: int | None = None
    version: int | None = None
    settings: str | None = None

