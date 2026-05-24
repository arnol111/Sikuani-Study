# Sikuani Study

A terminal text editor (TUI) built with Python and `curses`. A study project to explore the **Model-View-Presenter (MVP)** pattern in pure Python console applications.

## Description

Sikuani Study is a **learning project under active construction**. It is a terminal application that allows writing and editing text directly in the console using a color-based visual interface with a title bar and footer. The main goal is to learn and practice clean architecture principles — specifically the MVP pattern — with clearly separated layers, abstract interfaces, and dependency injection. Expect breaking changes and incomplete features as the project evolves.

## Architecture

```
src/
├── interfaces/               # Abstract contracts (ABC)
│   ├── IWindow.py
│   ├── IContentView.py
│   ├── IDocHandlingPresenter.py
│   └── IDocumentHandling.py
├── models/                   # Pure state and business logic — no curses
│   ├── FileDocument.py       # Document state: lines, cursor position
│   ├── KeyMapper.py          # Domain key enum (EditorKey) and KeyEvent
│   └── services/
│       └── DocumentServices.py  # File I/O (load/save)
├── views/                    # Rendering and input capture — only layer that knows curses
│   ├── ContentView.py        # Translates curses input → KeyEvent, renders text
│   ├── FooterView.py         # Footer bar
│   └── TittleBarView.py      # Title bar
└── presenters/               # Coordination — no curses, no direct rendering
    ├── Window.py             # Builds layout, assembles dependencies
    └── Doc_HandlingPresenter.py  # Handles editing logic, drives Model and View
```

### MVP Layer Responsibilities

| Layer | Knows curses | Knows disk | Contains logic |
|---|---|---|---|
| `FileDocument` | No | No | State only |
| `DocumentServices` | No | Yes | No |
| `ContentView` | Yes — translates to `KeyEvent` | No | No |
| `Doc_HandlingPresenter` | No | No | Yes — coordinates |
| `Window` | Yes — layout only | No | No |

## Requirements

- Python 3.11+
- Terminal with color support

## Usage

```bash
python3 app.py
```

- Type printable ASCII characters to write
- `Enter` to insert a new line
- `Backspace` to delete a character
- `q` to quit

## Status

Active development. Core MVP structure is in place. Editing features (cursor movement, file load/save) are under active implementation.
