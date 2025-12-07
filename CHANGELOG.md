# Release notes

<!-- do not remove -->

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

