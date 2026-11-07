# Release notes

<!-- do not remove -->

## 0.2.50

### New Features

- Move display repr/init patches to ipymini.term.display, wrap DisplayFormatter.format for prose marking ([#264](https://github.com/AnswerDotAI/dialoghelper/issues/264))


## 0.2.49

### New Features

- Use jupyasyncclient for rustygate CommTransport and JSON requests, drop local transport and `names_containing`, add jupyasyncclient dep ([#263](https://github.com/AnswerDotAI/dialoghelper/issues/263))


## 0.2.48

### New Features

- Move message selection, conversion, frontmatter and import logic to rustygate API routes; drop jupyasyncclient, fasttransport, pyyaml deps ([#262](https://github.com/AnswerDotAI/dialoghelper/issues/262))
- Add `refresh_dlg` to ask all browsers showing the dialog to re-render current messages and templates; bump rustygate dev dep to 0.1.32 ([#261](https://github.com/AnswerDotAI/dialoghelper/issues/261))
- Add `import_dlg` to copy messages between dialogs ([#221](https://github.com/AnswerDotAI/dialoghelper/pull/221)), thanks to [@ncoop57](https://github.com/ncoop57)


## 0.2.47

### New Features

- Add `add_msgs` for ordered batch inserts; batch msg edits and deletes into single cells requests with one combined change log note ([#260](https://github.com/AnswerDotAI/dialoghelper/issues/260))


## 0.2.46

### New Features

- Remove Channel websocket relay and websockets dep; switch fasthtml imports to fastcore.xml ([#257](https://github.com/AnswerDotAI/dialoghelper/issues/257))
