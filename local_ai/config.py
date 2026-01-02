"""Configuration management for Local AI system."""

import os
import yaml
from typing import Dict, Any, Optional
from pathlib import Path


class Config:
    """Configuration manager for the Local AI system."""
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize configuration.
        
        Args:
            config_path: Path to configuration file. Defaults to config.yaml in project root.
        """
        if config_path is None:
            config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.yaml")
        
        self.config_path = config_path
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from YAML file."""
        try:
            with open(self.config_path, 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            print(f"Warning: Config file not found at {self.config_path}, using defaults")
            return self._get_default_config()
    
    def _get_default_config(self) -> Dict[str, Any]:
        """Return default configuration."""
        return {
            'ai_system': {'name': 'Local AI Assistant', 'version': '0.1.0'},
            'coding': {'enabled': True},
            'vision': {'enabled': True},
            'voice': {'enabled': True},
            'automation': {'enabled': True},
            'api': {'host': '127.0.0.1', 'port': 8000},
        }
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get configuration value by key.
        
        Args:
            key: Configuration key (supports dot notation, e.g., 'coding.enabled')
            default: Default value if key not found
            
        Returns:
            Configuration value
        """
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def is_module_enabled(self, module_name: str) -> bool:
        """
        Check if a module is enabled.
        
        Args:
            module_name: Name of the module (e.g., 'coding', 'vision')
            
        Returns:
            True if module is enabled, False otherwise
        """
        return self.get(f'{module_name}.enabled', False)
