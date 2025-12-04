# Project Structure

This document describes the structure of the Nier Automata styled AI Chat Application.

## Directory Structure

```
/workspace/
├── main.py                 # Main application entry point
├── README.md              # Project overview and instructions
├── LICENSE               # License information
├── requirements.txt      # Python dependencies
├── .gitignore           # Files and directories to ignore in Git
├── models/              # AI model management
│   ├── __init__.py
│   └── model_manager.py # Handles loading and managing AI models
├── ui/                  # User interface components
│   ├── __init__.py
│   └── nier_style.py    # Nier Automata themed UI elements
├── assets/              # Game assets and styling resources
│   └── __init__.py
└── config/              # Configuration files
    ├── __init__.py
    └── settings.py      # Application settings and configuration
```

## Key Components

### main.py
The main entry point of the application that initializes components and starts the UI.

### models/model_manager.py
Handles the discovery, loading, and management of different AI models. Allows users to select from multiple locally downloaded models.

### ui/nier_style.py
Contains the Nier Automata themed user interface components, including styling and the main window class.

### config/settings.py
Manages application settings and configuration, including window size, theme colors, and chat settings.

## Features

- Model Selection: Choose from multiple locally downloaded AI models at startup
- Themed UI: Nier Automata inspired design with signature color scheme
- Chat Interface: Clean, functional chat interface for AI interaction
- Configurable: Settings can be adjusted via configuration files