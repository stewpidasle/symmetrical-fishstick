#!/usr/bin/env python3
"""
Main entry point for the Local AI Assistant.

This script initializes and runs the Local AI system with all enabled modules.
"""

import argparse
import asyncio
from local_ai import LocalAI


def main():
    """Main function to run the Local AI Assistant."""
    parser = argparse.ArgumentParser(
        description='Local AI Assistant - Free, local AI with coding, vision, voice, and automation'
    )
    parser.add_argument(
        '--config',
        type=str,
        default=None,
        help='Path to configuration file (default: config.yaml)'
    )
    parser.add_argument(
        '--mode',
        type=str,
        choices=['interactive', 'voice', 'api'],
        default='interactive',
        help='Running mode: interactive (CLI), voice (voice commands), or api (REST API)'
    )
    parser.add_argument(
        '--command',
        type=str,
        help='Single command to execute (non-interactive mode)'
    )
    
    args = parser.parse_args()
    
    # Initialize the AI system
    print("=" * 60)
    print("🤖 Local AI Assistant")
    print("=" * 60)
    print("Initializing system...")
    print()
    
    ai = LocalAI(config_path=args.config)
    
    print()
    print("=" * 60)
    print("System initialized successfully!")
    print("=" * 60)
    print()
    
    try:
        if args.command:
            # Execute single command
            response = ai.process_request(args.command)
            print(f"\nResponse: {response}")
        
        elif args.mode == 'interactive':
            run_interactive_mode(ai)
        
        elif args.mode == 'voice':
            run_voice_mode(ai)
        
        elif args.mode == 'api':
            run_api_mode(ai)
    
    except KeyboardInterrupt:
        print("\n\nShutting down...")
    finally:
        ai.shutdown()
        print("Goodbye!")


def run_interactive_mode(ai: LocalAI):
    """Run in interactive CLI mode."""
    print("Interactive Mode")
    print("-" * 60)
    print("Type your commands below. Type 'exit' or 'quit' to exit.")
    print("Examples:")
    print("  - 'Write a Python function to calculate fibonacci'")
    print("  - 'Take a screenshot and describe what you see'")
    print("  - 'Click at position 100, 200'")
    print("-" * 60)
    print()
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['exit', 'quit', 'bye']:
                break
            
            # Process the request
            response = ai.process_request(user_input)
            print(f"\nAssistant: {response}\n")
        
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}\n")


def run_voice_mode(ai: LocalAI):
    """Run in voice interaction mode."""
    print("Voice Mode")
    print("-" * 60)
    print("Starting voice listener...")
    print("Say the wake word to activate.")
    print("Press Ctrl+C to exit.")
    print("-" * 60)
    print()
    
    voice_module = ai.get_module('voice')
    if not voice_module:
        print("Error: Voice module not enabled!")
        return
    
    def handle_voice_command(text: str) -> str:
        """Handle voice command and return response."""
        print(f"\nYou said: {text}")
        response = ai.process_request(text)
        print(f"Response: {response}")
        return response
    
    # Run async voice listener
    asyncio.run(voice_module.start_listening(callback=handle_voice_command))


def run_api_mode(ai: LocalAI):
    """Run in API server mode."""
    try:
        from fastapi import FastAPI, HTTPException
        from pydantic import BaseModel
        import uvicorn
    except ImportError:
        print("Error: FastAPI not installed. Install with: pip install fastapi uvicorn")
        return
    
    app = FastAPI(title="Local AI Assistant API", version="0.1.0")
    
    class RequestModel(BaseModel):
        request: str
        context: dict = {}
    
    class ResponseModel(BaseModel):
        response: str
        status: str = "success"
    
    @app.post("/process", response_model=ResponseModel)
    async def process_request(req: RequestModel):
        """Process an AI request."""
        try:
            response = ai.process_request(req.request, req.context)
            return ResponseModel(response=response)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    @app.get("/health")
    async def health_check():
        """Health check endpoint."""
        return {"status": "healthy", "modules": list(ai.modules.keys())}
    
    @app.get("/")
    async def root():
        """Root endpoint."""
        return {
            "name": "Local AI Assistant API",
            "version": "0.1.0",
            "modules": list(ai.modules.keys())
        }
    
    print("API Mode")
    print("-" * 60)
    print("Starting API server...")
    
    host = ai.config.get('api.host', '127.0.0.1')
    port = ai.config.get('api.port', 8000)
    
    print(f"API available at: http://{host}:{port}")
    print(f"Docs available at: http://{host}:{port}/docs")
    print("Press Ctrl+C to exit.")
    print("-" * 60)
    print()
    
    uvicorn.run(app, host=host, port=port)


if __name__ == '__main__':
    main()
