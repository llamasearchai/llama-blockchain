# Examples

This page provides examples of using Llama Blockchain for various tasks.

## Basic Usage

```python

from llama_blockchain import Pipeline, Component

# Create a pipeline with components
pipeline = Pipeline([
    Component1(),
    Component2(),
    Component3()
])

# Process data through the pipeline
result = pipeline.run(input_data)
print(result)
```

## Advanced Usage

```python
from llama_blockchain import Pipeline, Component
from typing import Dict, Any

# Define custom component
class CustomProcessor(Component):
    def __init__(self, factor=2.0):
        super().__init__()
        self.factor = factor
    
    def process(self, data: Any) -> Any:
        # Process the data
        if isinstance(data, (int, float)):
            return data * self.factor
        return data

# Create a pipeline with the custom component
pipeline = Pipeline([
    CustomProcessor(factor=3.0)
])

# Process data
result = pipeline.run(10)
print(result)  # Output: 30.0
```

For more examples, check out the [examples directory](https://github.com/llamasearchai/llama-blockchain/tree/main/examples) in the GitHub repository.
