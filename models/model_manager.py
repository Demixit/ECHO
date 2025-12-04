"""
Model Manager for handling different AI models
"""
import os
from typing import Dict, List, Optional


class ModelManager:
    def __init__(self):
        self.models: Dict[str, str] = {}
        self.current_model = None
        
    def discover_models(self, models_dir: str = "models/") -> List[str]:
        """
        Discover available AI models in the models directory
        """
        available_models = []
        if os.path.exists(models_dir):
            for item in os.listdir(models_dir):
                item_path = os.path.join(models_dir, item)
                if os.path.isdir(item_path) and item != "__pycache__":
                    available_models.append(item)
        return available_models
    
    def load_model(self, model_name: str) -> bool:
        """
        Load the specified AI model
        """
        # This would be implemented based on the specific model type
        # For now, just set the current model
        self.current_model = model_name
        return True
    
    def get_model_info(self, model_name: str) -> Dict:
        """
        Get information about a specific model
        """
        return {
            "name": model_name,
            "path": os.path.join("models", model_name),
            "type": "AI Model"
        }