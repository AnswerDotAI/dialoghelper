# Release notes

<!-- do not remove -->

## 0.2.7

### New Features

- Replace PrintCollector with direct stdout/stderr capture via redirect ([#144](https://github.com/AnswerDotAI/dialoghelper/issues/144))
- Remove `find_msg_id` and implicit `__msg_id` usage; let server track current message ([#143](https://github.com/AnswerDotAI/dialoghelper/issues/143))
- Add `view_msg`/`stop_dialog`, rename `create_dialog`→`create_or_run_dialog` ([#142](https://github.com/AnswerDotAI/dialoghelper/issues/142))


## 0.2.4

### New Features

- Add max and min builtins to safe Python execution ([#136](https://github.com/AnswerDotAI/dialoghelper/pull/136)), thanks to [@ncoop57](https://github.com/ncoop57)
- Add `add_prompt`


## 0.2.3

### New Features

- Split `__pytools__` from `__llmtools__` ([#135](https://github.com/AnswerDotAI/dialoghelper/issues/135))
- Add `__import__` to sandbox, expand stdlib allowlist ([#135](https://github.com/AnswerDotAI/dialoghelper/issues/135))
- Add `docs`/`solveit_docs`/`dialog_link` tools ([#135](https://github.com/AnswerDotAI/dialoghelper/issues/135))


## 0.2.2

### New Features

- add support for async/await ([#134](https://github.com/AnswerDotAI/dialoghelper/issues/134))
- Collect print/warn/errs in `python` and return structured dict with stdout/warnings/result ([#133](https://github.com/AnswerDotAI/dialoghelper/issues/133))
- Add sandbox symbol export via `_` suffix, safe type constructors, and improved error handling in `python` ([#128](https://github.com/AnswerDotAI/dialoghelper/issues/128))
- Add `allow` helper for tool registration, improve RunPython sandbox access and error handling ([#127](https://github.com/AnswerDotAI/dialoghelper/issues/127))
- Add `toggle_bookmark` tool and `add_to_dlg` param to `read_msgid` ([#125](https://github.com/AnswerDotAI/dialoghelper/issues/125))
- Let `python` to use user globals, not .core globals to access tools and variables. ([#122](https://github.com/AnswerDotAI/dialoghelper/pull/122)), thanks to [@PiotrCzapla](https://github.com/PiotrCzapla)

### Bugs Squashed

- Missing type hint in `safe_type` param ([#130](https://github.com/AnswerDotAI/dialoghelper/issues/130))


## 0.2.1

### New Features

- Add parameter annotations and shared docstring to message editing tools ([#124](https://github.com/AnswerDotAI/dialoghelper/issues/124))


## 0.2.0

### Breaking Changes

- asyncify ([#123](https://github.com/AnswerDotAI/dialoghelper/issues/123))


## 0.1.21

### New Features

- Add restricted Python execution tool for LLM with sandboxed builtins ([#120](https://github.com/AnswerDotAI/dialoghelper/issues/120))
- Add `display_response` for separate display/LLM tool outputs ([#117](https://github.com/AnswerDotAI/dialoghelper/issues/117))
- `log_changed` ([#116](https://github.com/AnswerDotAI/dialoghelper/issues/116))
- DRY up dname docstrings with llmtool templates ([#114](https://github.com/AnswerDotAI/dialoghelper/pull/114)), thanks to [@ncoop57](https://github.com/ncoop57)

### Bugs Squashed

- fix log update ([#118](https://github.com/AnswerDotAI/dialoghelper/pull/118)), thanks to [@RensDimmendaal](https://github.com/RensDimmendaal)


## 0.1.18

### New Features

- Add `dialog_link` function and `update_output` param to message editing tools ([#110](https://github.com/AnswerDotAI/dialoghelper/issues/110))
- add `only_exp` to `find_msgs` tool ([#103](https://github.com/AnswerDotAI/dialoghelper/pull/103)), thanks to [@KeremTurgutlu](https://github.com/KeremTurgutlu)

### Bugs Squashed

- Update `add_scr` to use ephemeral OOB target ([#109](https://github.com/AnswerDotAI/dialoghelper/pull/109)), thanks to [@erikgaas](https://github.com/erikgaas)
- Fix cross dlg pollution ([#108](https://github.com/AnswerDotAI/dialoghelper/pull/108)), thanks to [@civvic](https://github.com/civvic)


## 0.1.17

### New Features

- Add `dialoghelper_explain_dialog_editing` ([#107](https://github.com/AnswerDotAI/dialoghelper/issues/107))


## 0.1.16

### New Features

- Refactor: move inspecttools to toolslm, add @llmtool decorators, extract tracetools ([#106](https://github.com/AnswerDotAI/dialoghelper/issues/106))
- Support adding after/before a message in other dlgs; add `headers_only`/`header_section` params to `find_msgs` ([#105](https://github.com/AnswerDotAI/dialoghelper/issues/105))
- Rename `get*` to `sym*`, add multi-symbol support to symtype/symval, add `symtype_val` ([#104](https://github.com/AnswerDotAI/dialoghelper/issues/104))


## 0.1.15

### Bugs Squashed

- Fix _diff_dialog to check explicit dname parameter ([#102](https://github.com/AnswerDotAI/dialoghelper/issues/102))


## 0.1.14

### New Features

- Add `create_dialog` and `rm_dialog` helper functions ([#101](https://github.com/AnswerDotAI/dialoghelper/issues/101))


## 0.1.12

### New Features

- Add ids filter to `find_msgs` ([#100](https://github.com/AnswerDotAI/dialoghelper/issues/100))


## 0.1.11

### New Features

- Improve symsrc with linecache fallback, add SymbolNotFound exception, rename doimport to importmodule ([#99](https://github.com/AnswerDotAI/dialoghelper/issues/99))
- Handle error responses in `find_msgs` ([#96](https://github.com/AnswerDotAI/dialoghelper/issues/96))

### Bugs Squashed

- Use json=False for `del_msg` to match `rm_msg_` response ([#97](https://github.com/AnswerDotAI/dialoghelper/pull/97)), thanks to [@erikgaas](https://github.com/erikgaas)


## 0.1.9

### New Features

- Add `trunc_in` param to `find_msgs` and `view_dlg` ([#95](https://github.com/AnswerDotAI/dialoghelper/pull/95)), thanks to [@erikgaas](https://github.com/erikgaas)


## 0.1.8

### New Features

- Add `fmt_trace` markdown formatter ([#94](https://github.com/AnswerDotAI/dialoghelper/issues/94))
- Add `tracetool` ([#93](https://github.com/AnswerDotAI/dialoghelper/issues/93))
- Improve docstrings and parameter annotations; change symsearch to use regex:bool flag ([#92](https://github.com/AnswerDotAI/dialoghelper/issues/92))
- Add `trunc_out` ([#91](https://github.com/AnswerDotAI/dialoghelper/issues/91))


## 0.1.6

### New Features

- Add `view_dlg` for concise XML dialog output; extend `find_msgs` with XML/metadata options ([#90](https://github.com/AnswerDotAI/dialoghelper/issues/90))


## 0.1.5

### New Features

- Add `move_lines` ([#89](https://github.com/AnswerDotAI/dialoghelper/issues/89))
- Add sym manipulation tools for strings and lists ([#86](https://github.com/AnswerDotAI/dialoghelper/pull/86)), thanks to [@ncoop57](https://github.com/ncoop57)


## 0.1.2

### New Features

- Add `sigs_only` ([#88](https://github.com/AnswerDotAI/dialoghelper/issues/88))
- More find API params ([#87](https://github.com/AnswerDotAI/dialoghelper/issues/87))
- Add sym manipulation tools for strings and lists ([#86](https://github.com/AnswerDotAI/dialoghelper/pull/86)), thanks to [@ncoop57](https://github.com/ncoop57)


## 0.1.1

### New Features

- Add mermaid ([#85](https://github.com/AnswerDotAI/dialoghelper/issues/85))


## 0.1.0

### Breaking Changes

- `msgid` param is now called `id`; `msgids` param is now called `ids`

### New Features

- Support updated solveit API ([#84](https://github.com/AnswerDotAI/dialoghelper/issues/84))
- Add `toggle_header` ([#83](https://github.com/AnswerDotAI/dialoghelper/issues/83))


## 0.0.62

### New Features

- Add copy/paste msgs ([#82](https://github.com/AnswerDotAI/dialoghelper/issues/82))


## 0.0.61

### New Features

- Remove unneeded fastlite and claudette deps ([#81](https://github.com/AnswerDotAI/dialoghelper/issues/81))
- Add type annotations to `shell_ret` for proper `is_usable_tool` report ([#72](https://github.com/AnswerDotAI/dialoghelper/pull/72)), thanks to [@civvic](https://github.com/civvic)

### Bugs Squashed

- Fix resolve() to handle direct list indexing ([#76](https://github.com/AnswerDotAI/dialoghelper/pull/76)), thanks to [@civvic](https://github.com/civvic)


## 0.0.60

### New Features

- Handle relative dname param ([#79](https://github.com/AnswerDotAI/dialoghelper/issues/79))


## 0.0.59

### New Features

- Add `raw` param to ctx funcs ([#78](https://github.com/AnswerDotAI/dialoghelper/issues/78))


## 0.0.58

### New Features

- Add wrappers for sym ctx toolslm funcs ([#77](https://github.com/AnswerDotAI/dialoghelper/issues/77))


## 0.0.57

### New Features

- Add `get_folder` ([#74](https://github.com/AnswerDotAI/dialoghelper/issues/74))
- Improve docstrings ([#73](https://github.com/AnswerDotAI/dialoghelper/issues/73))


## 0.0.56

### Bugs Squashed

- `run_msg` now requires `msgids` ([#71](https://github.com/AnswerDotAI/dialoghelper/issues/71))


## 0.0.55

### New Features

- Add `get_repo` ([#70](https://github.com/AnswerDotAI/dialoghelper/issues/70))

### Bugs Squashed

- `msg` param to `update_msg` does nothing ([#69](https://github.com/AnswerDotAI/dialoghelper/issues/69))


## 0.0.54

### New Features

- add ssh option to tmux ([#66](https://github.com/AnswerDotAI/dialoghelper/pull/66)), thanks to [@KeremTurgutlu](https://github.com/KeremTurgutlu)
- Add dialoghelper.tmux ([#64](https://github.com/AnswerDotAI/dialoghelper/issues/64))
- Improvements to `capture_screen` ([#63](https://github.com/AnswerDotAI/dialoghelper/pull/63)), thanks to [@curtis-allan](https://github.com/curtis-allan)

### Bugs Squashed

- fix import ([#65](https://github.com/AnswerDotAI/dialoghelper/pull/65)), thanks to [@ncoop57](https://github.com/ncoop57)


## 0.0.50

### New Features

- Add `dialoghelper.stdtools` ([#60](https://github.com/AnswerDotAI/dialoghelper/issues/60))


## 0.0.49

### New Features

- Wrap `dict2obj` around json results ([#59](https://github.com/AnswerDotAI/dialoghelper/issues/59))
- Add `run_code_interactive` and `showsrc` and improve other inspecttools ([#58](https://github.com/AnswerDotAI/dialoghelper/issues/58))


## 0.0.48

### New Features

- Do text edit api stuff locally; add `msg_del_lines` ([#57](https://github.com/AnswerDotAI/dialoghelper/issues/57))
- Add json header to calls; use in `del_msg` ([#56](https://github.com/AnswerDotAI/dialoghelper/issues/56))
- handle `find_msg_id` when target dlg different ([#54](https://github.com/AnswerDotAI/dialoghelper/pull/54)), thanks to [@KeremTurgutlu](https://github.com/KeremTurgutlu)

### Bugs Squashed

- use `call_endp` to pop ([#55](https://github.com/AnswerDotAI/dialoghelper/pull/55)), thanks to [@ncoop57](https://github.com/ncoop57)
- handle `find_msg_id` when target dlg different ([#54](https://github.com/AnswerDotAI/dialoghelper/pull/54)), thanks to [@KeremTurgutlu](https://github.com/KeremTurgutlu)


## 0.0.47

### New Features

- Add `dialoghelper.inspecttools` ([#52](https://github.com/AnswerDotAI/dialoghelper/issues/52))


## 0.0.46

### New Features

- Add `dname` to `dh_settings` ([#51](https://github.com/AnswerDotAI/dialoghelper/issues/51))
- enhance url2note ([#50](https://github.com/AnswerDotAI/dialoghelper/pull/50)), thanks to [@RensDimmendaal](https://github.com/RensDimmendaal)


## 0.0.45

### New Features

- `capture_screen` returns a PIL image ([#49](https://github.com/AnswerDotAI/dialoghelper/issues/49))


## 0.0.43

### New Features

- add `event_get` ([#48](https://github.com/AnswerDotAI/dialoghelper/issues/48))


## 0.0.42

### New Features

- Add `add_scr`, `pop_data`, and `fire_event` ([#47](https://github.com/AnswerDotAI/dialoghelper/issues/47))


## 0.0.40

- Rename `dialog.experimental` to `dialog.capture`


## 0.0.39

### New Features

- add timeout ([#46](https://github.com/AnswerDotAI/dialoghelper/pull/46)), thanks to [@ncoop57](https://github.com/ncoop57)

### Bugs Squashed

- `relative=False` is not working in `read_msg()`


## 0.0.38

### New Features

- Use new `update_msg_` API ([#45](https://github.com/AnswerDotAI/dialoghelper/issues/45))


## 0.0.37

### New Features

- simplify screen cap ([#43](https://github.com/AnswerDotAI/dialoghelper/pull/43)), thanks to [@ncoop57](https://github.com/ncoop57)


## 0.0.36

### New Features

- Add `add_styles` ([#42](https://github.com/AnswerDotAI/dialoghelper/issues/42))
- Set `__msg_id` in `add_var` et al ([#41](https://github.com/AnswerDotAI/dialoghelper/issues/41))


## 0.0.35

### New Features

- Text edit tools for msgs ([#38](https://github.com/AnswerDotAI/dialoghelper/pull/38)), thanks to [@KeremTurgutlu](https://github.com/KeremTurgutlu)
- Add text/bash tools and tests ([#34](https://github.com/AnswerDotAI/dialoghelper/pull/34)), thanks to [@ncoop57](https://github.com/ncoop57)


## 0.0.34

### New Features

- Add `fc_tool_info` ([#37](https://github.com/AnswerDotAI/dialoghelper/issues/37))


## 0.0.32

### New Features

- Add ast grep ([#36](https://github.com/AnswerDotAI/dialoghelper/issues/36))


## 0.0.31

### New Features

- Add `url2note` ([#35](https://github.com/AnswerDotAI/dialoghelper/issues/35))


## 0.0.30

### New Features

- Updates for multi-kernel ([#33](https://github.com/AnswerDotAI/dialoghelper/issues/33))


## 0.0.29

### New Features

- capture cleanup ([#31](https://github.com/AnswerDotAI/dialoghelper/issues/31))


## 0.0.28

### Bugs Squashed

- js not in manifest ([#32](https://github.com/AnswerDotAI/dialoghelper/issues/32))


## 0.0.27

### New Features

- Increase screen capture resolution ([#30](https://github.com/AnswerDotAI/dialoghelper/pull/30)), thanks to [@austinvhuang](https://github.com/austinvhuang)

## 0.0.25

### New Features

- Unify return signals to use the blocking endpoint for getting signals/return values ([#29](https://github.com/AnswerDotAI/dialoghelper/pull/29)), thanks to [@austinvhuang](https://github.com/austinvhuang)

## 0.0.24

### Bugs Squashed

- remove isCapturing restriction in capture_screen ([#26](https://github.com/AnswerDotAI/dialoghelper/pull/26)), thanks to [@austinvhuang](https://github.com/austinvhuang)


## 0.0.22

### New Features

- Experimental support to capture screen contents and return b64 encoded image ([#21](https://github.com/AnswerDotAI/dialoghelper/pull/21)), thanks to [@austinvhuang](https://github.com/austinvhuang)


## 0.0.21

### New Features

- Do not make content required in update ([#25](https://github.com/AnswerDotAI/dialoghelper/issues/25))


## 0.0.20

### New Features

- Add `curr_dialog` ([#24](https://github.com/AnswerDotAI/dialoghelper/issues/24))


## 0.0.19

### Bugs Squashed

- kwargs does not work with add_schema ([#23](https://github.com/AnswerDotAI/dialoghelper/issues/23))


## 0.0.18

### Breaking Changes

- Update for new ipynb solveit ([#22](https://github.com/AnswerDotAI/dialoghelper/issues/22))


## 0.0.17

### Bugs Squashed

- `update_msg` could delete contents ([#20](https://github.com/AnswerDotAI/dialoghelper/issues/20))


## 0.0.16

### New Features

- Add `add_html` ([#19](https://github.com/AnswerDotAI/dialoghelper/issues/19))


## 0.0.15

### Bugs Squashed

- Not using UNSET where needed ([#18](https://github.com/AnswerDotAI/dialoghelper/issues/18))


## 0.0.14

### New Features

- return `add_msg` ([#17](https://github.com/AnswerDotAI/dialoghelper/issues/17))


## 0.0.13

### New Features

- Use httpx for dialog editing ([#16](https://github.com/AnswerDotAI/dialoghelper/issues/16))
- Add `tool_info` ([#16](https://github.com/AnswerDotAI/dialoghelper/issues/16))
- Add `_add_msg_unsafe` ([#15](https://github.com/AnswerDotAI/dialoghelper/issues/15))
- Use module docstring in `import_gist` ([#14](https://github.com/AnswerDotAI/dialoghelper/issues/14))


## 0.0.12

### New Features

- Improve `import_gist` - `import_wildcard` and `create_msg` ([#13](https://github.com/AnswerDotAI/dialoghelper/issues/13))


## 0.0.11

### New Features

- Add `Placements` ([#11](https://github.com/AnswerDotAI/dialoghelper/issues/11))


## 0.0.10

### New Features

- add export_dialog, import_dialog functionality ([#10](https://github.com/AnswerDotAI/dialoghelper/pull/10)), thanks to [@austinvhuang](https://github.com/austinvhuang)


## 0.0.9

### Bugs Squashed

- do not remove sid from msg ([#9](https://github.com/AnswerDotAI/dialoghelper/issues/9))


## 0.0.8

### Bugs Squashed

- sid not being used from dict in `update_msg` ([#8](https://github.com/AnswerDotAI/dialoghelper/issues/8))


## 0.0.7

### New Features

- Improve update/add msg funcs ([#7](https://github.com/AnswerDotAI/dialoghelper/issues/7))


## 0.0.6

### New Features

- Clarify sid vs mid ([#6](https://github.com/AnswerDotAI/dialoghelper/issues/6))


## 0.0.5

- `update_msg` fixes


## 0.0.4

### Bugs Squashed

- `add_msg` missing types ([#3](https://github.com/AnswerDotAI/dialoghelper/issues/3))


## 0.0.3

### New Features

- Support `skipped` and other `Message` fields in `update_msg` ([#2](https://github.com/AnswerDotAI/dialoghelper/pull/2)), thanks to [@austinvhuang](https://github.com/austinvhuang)

### Bugs Squashed


## 0.0.2

### New Features

- Add types ([#1](https://github.com/AnswerDotAI/dialoghelper/issues/1))


## 0.0.1

- init version

