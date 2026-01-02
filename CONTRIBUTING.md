# Contributing to Local AI Assistant

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- System information (OS, Python version, etc.)
- Error messages or logs

### Suggesting Features

Feature suggestions are welcome! Please:
- Check if the feature already exists or is planned
- Describe the use case and benefits
- Consider implementation complexity
- Be open to discussion

### Code Contributions

1. **Fork the Repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/symmetrical-fishstick.git
   cd symmetrical-fishstick
   ```

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**
   - Follow the code style (PEP 8 for Python)
   - Add docstrings to functions and classes
   - Update documentation if needed
   - Add tests if applicable

4. **Test Your Changes**
   ```bash
   python -m pytest tests/  # If tests exist
   python main.py --command "test"
   ```

5. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "feat: Add feature description"
   ```

   Use conventional commit messages:
   - `feat:` New feature
   - `fix:` Bug fix
   - `docs:` Documentation changes
   - `refactor:` Code refactoring
   - `test:` Adding tests
   - `chore:` Maintenance tasks

6. **Push and Create Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```
   Then open a PR on GitHub.

## Development Setup

### Environment Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies (if any)
pip install pytest black flake8
```

### Running Tests
```bash
# Run all tests
python -m pytest

# Run specific test
python -m pytest tests/test_module.py

# Run with coverage
python -m pytest --cov=local_ai
```

### Code Style

We follow PEP 8 guidelines:

```bash
# Format code
black local_ai/

# Check style
flake8 local_ai/

# Sort imports
isort local_ai/
```

## Project Structure

```
local_ai/
├── __init__.py       # Package initialization
├── config.py         # Configuration management
├── core.py           # Main orchestrator
├── modules/          # Individual modules
│   ├── coding.py     # Coding capabilities
│   ├── vision.py     # Vision capabilities
│   ├── voice.py      # Voice capabilities
│   └── automation.py # Automation capabilities
└── utils/            # Utility functions
```

## Adding New Features

### Adding a New Module

1. Create module file in `local_ai/modules/`
2. Implement module class with:
   - `__init__(self, config)`: Initialize module
   - `process(self, request, context)`: Handle requests
   - `cleanup(self)`: Cleanup resources

3. Register module in `core.py`:
   ```python
   if self.config.is_module_enabled('new_module'):
       self.modules['new_module'] = NewModule(self.config)
   ```

4. Add configuration in `config.yaml`
5. Update documentation

### Adding Model Support

1. Add model loading in module
2. Update `docs/MODELS.md` with download instructions
3. Add configuration options in `config.yaml`
4. Test with the new model

## Documentation

When adding features:
- Update README.md if needed
- Add docstrings to new functions/classes
- Update API.md for API changes
- Add examples in `examples/` directory
- Update relevant documentation files

## Testing Guidelines

- Test on multiple operating systems if possible
- Test with and without models
- Test error handling
- Test edge cases
- Keep tests independent

## Code Review Process

1. Ensure CI passes (if set up)
2. Get at least one review
3. Address feedback
4. Maintain backward compatibility when possible
5. Update CHANGELOG.md

## Community Guidelines

- Be respectful and inclusive
- Provide constructive feedback
- Help others learn
- Credit contributors
- Follow the Code of Conduct

## Questions?

- Open an issue for clarification
- Check existing issues and PRs
- Read the documentation

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Credited in documentation

Thank you for making Local AI Assistant better! 🎉
