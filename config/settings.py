"""
Application settings and configuration
"""
import json
import os
from typing import Dict, Any


class Settings:
    """Configuration settings for the AI chat application"""
    
    def __init__(self, config_file: str = "config/settings.json"):
        self.config_file = config_file
        self.settings = self.load_settings()
    
    def load_settings(self) -> Dict[str, Any]:
        """Load settings from JSON file or create default settings"""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # Create default settings
            default_settings = {
                "models_directory": "models/",
                "default_model": None,
                "window_size": {
                    "width": 800,
                    "height": 600
                },
                "theme": {
                    "primary_color": "#1a1a1a",
                    "secondary_color": "#2d2d2d",
                    "accent_color": "#d70022"
                },
                "chat": {
                    "max_history": 100,
                    "font_size": 12
                }
            }
            self.save_settings(default_settings)
            return default_settings
    
    def save_settings(self, settings: Dict[str, Any] = None):
        """Save settings to JSON file"""
        if settings is None:
            settings = self.settings
        
        # Ensure the config directory exists
        os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
        
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(settings, f, indent=4, ensure_ascii=False)
    
    def get(self, key: str, default=None):
        """Get a setting value"""
        return self.settings.get(key, default)
    
    def set(self, key: str, value: Any):
        """Set a setting value"""
        self.settings[key] = value
        self.save_settings()


# Global settings instance
app_settings = Settings()