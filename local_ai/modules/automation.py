"""Automation module for computer task automation."""

from typing import Dict, Any, Optional
import time


class AutomationModule:
    """Handles computer automation tasks like mouse, keyboard, and system control."""
    
    def __init__(self, config):
        """
        Initialize the automation module.
        
        Args:
            config: Configuration object
        """
        self.config = config
        self.confirm_actions = config.get('automation.safety.confirm_actions', True)
        self.restricted_ops = config.get('automation.safety.restricted_operations', [])
        self.capabilities = config.get('automation.capabilities', [])
        print(f"  Automation module configured (safety mode: {self.confirm_actions})")
    
    def process(self, request: str, context: Optional[Dict[str, Any]] = None) -> str:
        """
        Process an automation request.
        
        Args:
            request: The automation request
            context: Additional context (coordinates, text, etc.)
            
        Returns:
            Result of the automation action
        """
        context = context or {}
        
        # Determine the type of automation task
        task_type = self._identify_automation_task(request)
        
        if task_type == 'mouse':
            return self._handle_mouse_action(request, context)
        elif task_type == 'keyboard':
            return self._handle_keyboard_action(request, context)
        elif task_type == 'window':
            return self._handle_window_action(request, context)
        elif task_type == 'file':
            return self._handle_file_action(request, context)
        elif task_type == 'process':
            return self._handle_process_action(request, context)
        else:
            return "Automation task type not recognized. I can help with mouse, keyboard, window, file, and process operations."
    
    def _identify_automation_task(self, request: str) -> str:
        """Identify the type of automation task."""
        request_lower = request.lower()
        
        if any(word in request_lower for word in ['click', 'move mouse', 'drag', 'scroll']):
            return 'mouse'
        elif any(word in request_lower for word in ['type', 'press', 'keyboard', 'hotkey']):
            return 'keyboard'
        elif any(word in request_lower for word in ['window', 'minimize', 'maximize', 'switch']):
            return 'window'
        elif any(word in request_lower for word in ['file', 'folder', 'directory', 'copy', 'move']):
            return 'file'
        elif any(word in request_lower for word in ['process', 'application', 'program', 'launch', 'kill']):
            return 'process'
        else:
            return 'unknown'
    
    def _check_safety(self, operation: str) -> bool:
        """Check if operation is safe to perform."""
        if operation in self.restricted_ops and self.confirm_actions:
            print(f"⚠️  Warning: '{operation}' is a restricted operation.")
            print("This would require user confirmation in production.")
            return False
        return True
    
    def _handle_mouse_action(self, request: str, context: Dict[str, Any]) -> str:
        """Handle mouse-related actions."""
        try:
            import pyautogui
            
            if 'click' in request.lower():
                x = context.get('x')
                y = context.get('y')
                
                if x is not None and y is not None:
                    pyautogui.click(x, y)
                    return f"Clicked at position ({x}, {y})"
                else:
                    pyautogui.click()
                    return "Clicked at current mouse position"
            
            elif 'move' in request.lower():
                x = context.get('x')
                y = context.get('y')
                
                if x is not None and y is not None:
                    pyautogui.moveTo(x, y)
                    return f"Moved mouse to ({x}, {y})"
                else:
                    return "Please provide x and y coordinates"
            
            elif 'scroll' in request.lower():
                amount = context.get('amount', 3)
                pyautogui.scroll(amount)
                return f"Scrolled {amount} units"
            
            else:
                return "Mouse action not recognized. Supported: click, move, scroll"
        
        except ImportError:
            return "PyAutoGUI not installed. Install with: pip install pyautogui"
        except Exception as e:
            return f"Error performing mouse action: {e}"
    
    def _handle_keyboard_action(self, request: str, context: Dict[str, Any]) -> str:
        """Handle keyboard-related actions."""
        try:
            import pyautogui
            
            if 'type' in request.lower():
                text = context.get('text', '')
                if text:
                    pyautogui.write(text, interval=0.05)
                    return f"Typed: {text}"
                else:
                    return "Please provide text to type"
            
            elif 'press' in request.lower() or 'hotkey' in request.lower():
                keys = context.get('keys', [])
                if keys:
                    if len(keys) > 1:
                        pyautogui.hotkey(*keys)
                        return f"Pressed hotkey: {'+'.join(keys)}"
                    else:
                        pyautogui.press(keys[0])
                        return f"Pressed key: {keys[0]}"
                else:
                    return "Please provide keys to press"
            
            else:
                return "Keyboard action not recognized. Supported: type, press, hotkey"
        
        except ImportError:
            return "PyAutoGUI not installed. Install with: pip install pyautogui"
        except Exception as e:
            return f"Error performing keyboard action: {e}"
    
    def _handle_window_action(self, request: str, context: Dict[str, Any]) -> str:
        """Handle window management actions."""
        try:
            import pyautogui
            
            # Note: Window management capabilities vary by OS
            if 'minimize' in request.lower():
                pyautogui.hotkey('win', 'down')  # Windows
                return "Minimized active window"
            
            elif 'maximize' in request.lower():
                pyautogui.hotkey('win', 'up')  # Windows
                return "Maximized active window"
            
            else:
                return "Window action not fully implemented. This requires OS-specific libraries."
        
        except Exception as e:
            return f"Error performing window action: {e}"
    
    def _handle_file_action(self, request: str, context: Dict[str, Any]) -> str:
        """Handle file system operations."""
        import os
        import shutil
        
        try:
            if 'delete' in request.lower():
                if not self._check_safety('file_deletion'):
                    return "File deletion requires confirmation (safety mode enabled)"
                
                file_path = context.get('path', '')
                if file_path and os.path.exists(file_path):
                    os.remove(file_path)
                    return f"Deleted file: {file_path}"
                else:
                    return "File path not provided or doesn't exist"
            
            elif 'copy' in request.lower():
                src = context.get('source', '')
                dst = context.get('destination', '')
                
                if src and dst:
                    shutil.copy2(src, dst)
                    return f"Copied {src} to {dst}"
                else:
                    return "Please provide source and destination paths"
            
            elif 'move' in request.lower():
                src = context.get('source', '')
                dst = context.get('destination', '')
                
                if src and dst:
                    shutil.move(src, dst)
                    return f"Moved {src} to {dst}"
                else:
                    return "Please provide source and destination paths"
            
            else:
                return "File operation not recognized. Supported: copy, move, delete"
        
        except Exception as e:
            return f"Error performing file operation: {e}"
    
    def _handle_process_action(self, request: str, context: Dict[str, Any]) -> str:
        """Handle process management."""
        import subprocess
        
        try:
            if 'launch' in request.lower() or 'open' in request.lower():
                program = context.get('program', '')
                
                if program:
                    subprocess.Popen([program])
                    return f"Launched: {program}"
                else:
                    return "Please provide program name or path"
            
            elif 'list' in request.lower():
                import psutil
                processes = [(p.pid, p.name()) for p in psutil.process_iter(['pid', 'name'])]
                return f"Found {len(processes)} running processes"
            
            else:
                return "Process action not recognized. Supported: launch, list"
        
        except ImportError:
            return "psutil not installed. Install with: pip install psutil"
        except Exception as e:
            return f"Error performing process action: {e}"
    
    def execute_complex_task(self, task_description: str) -> str:
        """
        Execute a complex multi-step task.
        
        Args:
            task_description: Description of the complex task
            
        Returns:
            Result of task execution
        """
        return f"""Complex Task Execution (Placeholder):

Task: {task_description}

This would:
1. Break down the task into steps
2. Execute each step using appropriate automation
3. Handle errors and retries
4. Report progress and results

To fully implement this, integrate with the coding module to:
- Parse natural language task descriptions
- Generate automation scripts
- Execute with safety checks
"""
    
    def cleanup(self):
        """Cleanup resources."""
        pass
