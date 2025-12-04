"""
Main entry point for the Nier Automata styled AI Chat Application
"""
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.model_manager import ModelManager
from ui.nier_style import NierMainWindow
from config.settings import app_settings


def main():
    """Main application function"""
    print("Starting Nier Automata AI Chat Application...")
    
    # Initialize model manager
    model_manager = ModelManager()
    
    # Discover available models
    available_models = model_manager.discover_models(app_settings.get("models_directory", "models/"))
    print(f"Available models: {available_models}")
    
    # Create and run the main UI window
    app = NierMainWindow()
    
    # Populate the model dropdown with available models
    if hasattr(app, 'model_dropdown'):
        app.model_dropdown['values'] = available_models
        if available_models:
            app.model_dropdown.current(0)
    
    # Run the application
    app.run()


if __name__ == "__main__":
    main()