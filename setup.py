#!/usr/bin/env python3
"""
Llama Blockchain - Python package for LlamaSearch AI
"""

from setuptools import setup, find_packages

setup(
    name="llama_blockchain",
    version="0.1.0",
    description="[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)]() <!-- Add appropriate Python version support -->",
    long_description="""# llama-blockchain

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)]() <!-- Add appropriate Python version support -->

## Installation

```bash
pip install -e .
```

## Usage

```python
from llama_blockchain import LlamaBlockchainClient

# Initialize the client
client = LlamaBlockchainClient(api_key="your-api-key")
result = client.query("your query")
print(result)
```

## Features

- Fast and efficient
- Easy to use API
- Comprehensive documentation

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/nikjois/llama-blockchain.git
cd llama-blockchain

# Install development dependencies
pip install -e ".[dev]"
```

### Testing

```bash
pytest
```

## License

MIT

## Author

Nik Jois (nikjois@llamasearch.ai)
""",
    long_description_content_type="text/markdown",
    author="Nik Jois",
    author_email="nikjois@llamasearch.ai",
    url="https://github.com/llamasearchai/llama-blockchain",
    project_urls={
        "Documentation": "https://github.com/llamasearchai/llama-blockchain",
        "Bug Tracker": "https://github.com/llamasearchai/llama-blockchain/issues",
        "Source Code": "https://github.com/llamasearchai/llama-blockchain",
    },
    packages='src.llama_blockchain',
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
)
