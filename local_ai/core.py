"""Core orchestrator for the Local AI system."""

import asyncio
from typing import Optional, Dict, Any
from .config import Config
from .modules.coding import CodingModule
from .modules.vision import VisionModule
from .modules.voice import VoiceModule
from .modules.automation import AutomationModule


class LocalAI:
    """Main orchestrator for the Local AI system."""
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the Local AI system.
        
        Args:
            config_path: Path to configuration file
        """
        self.config = Config(config_path)
        self.modules = {}
        self._initialize_modules()
    
    def _initialize_modules(self):
        """Initialize all enabled modules."""
        if self.config.is_module_enabled('coding'):
            self.modules['coding'] = CodingModule(self.config)
            print("✓ Coding module initialized")
        
        if self.config.is_module_enabled('vision'):
            self.modules['vision'] = VisionModule(self.config)
            print("✓ Vision module initialized")
        
        if self.config.is_module_enabled('voice'):
            self.modules['voice'] = VoiceModule(self.config)
            print("✓ Voice module initialized")
        
        if self.config.is_module_enabled('automation'):
            self.modules['automation'] = AutomationModule(self.config)
            print("✓ Automation module initialized")
    
    def process_request(self, request: str, context: Optional[Dict[str, Any]] = None) -> str:
        """
        Process a user request using appropriate modules.
        
        Args:
            request: User's request/query
            context: Additional context (e.g., image data, file paths)
            
        Returns:
            Response from the AI system
        """
        context = context or {}
        
        # Determine which module(s) should handle the request
        if self._is_coding_request(request):
            return self.modules['coding'].process(request, context)
        elif self._is_vision_request(request, context):
            return self.modules['vision'].process(request, context)
        elif self._is_automation_request(request):
            return self.modules['automation'].process(request, context)
        else:
            return self._general_response(request)
    
    def _is_coding_request(self, request: str) -> bool:
        """Determine if request is coding-related."""
        coding_keywords = ['code', 'function', 'class', 'debug', 'implement', 'refactor', 
                          'python', 'javascript', 'program', 'script', 'algorithm']
        return any(keyword in request.lower() for keyword in coding_keywords)
    
    def _is_vision_request(self, request: str, context: Dict[str, Any]) -> bool:
        """Determine if request is vision-related."""
        return 'image' in context or 'screenshot' in request.lower() or 'see' in request.lower()
    
    def _is_automation_request(self, request: str) -> bool:
        """Determine if request is automation-related."""
        automation_keywords = ['click', 'type', 'open', 'close', 'move', 'automate', 
                              'task', 'window', 'file', 'folder']
        return any(keyword in request.lower() for keyword in automation_keywords)
    
    def _general_response(self, request: str) -> str:
        """Handle general requests."""
        return f"I understand you're asking: '{request}'. I can help with coding, vision analysis, voice interaction, and computer automation. Please specify what you'd like me to do."
    
    async def listen_for_voice_commands(self):
        """Start listening for voice commands (async)."""
        if 'voice' in self.modules:
            await self.modules['voice'].start_listening()
    
    def get_module(self, module_name: str):
        """Get a specific module by name."""
        return self.modules.get(module_name)
    
    def shutdown(self):
        """Shutdown all modules and cleanup resources."""
        for module_name, module in self.modules.items():
            if hasattr(module, 'cleanup'):
                module.cleanup()
            print(f"✓ {module_name.capitalize()} module shut down")
