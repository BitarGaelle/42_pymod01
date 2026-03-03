_This project has been created as part of the 42 curriculum by gbitar_
## Python Object-Oriented Garden Systems
### Overview

This project explores advanced Python concepts by modeling a digital garden ecosystem. It emphasizes object-oriented design, method types, data management, and modular code organization.

### Classes & Objects
- Classes model real-world entities (e.g., Plant, Garden).
- Objects are instances of classes with their own state and behavior.
- Use ``__init__()`` to initialize objects with attributes.

### Inheritance
- Child classes can inherit from parent classes to reuse code.
- Override methods to provide specialized behavior.
- Use ``super()`` to call parent methods or constructors.

### Methods
- Instance methods: operate on specific object data (``self``).
- Class methods: operate on class-level data (``cls``).
- Static methods: utility functions that do not rely on ``self`` or ``cls``.
- Use type hints for clarity in inputs and outputs.

### Encapsulation
- Protect sensitive data with private attributes or controlled access.
- Use getter and setter methods to validate changes.
- Ensures data integrity and prevents invalid operations.

### Data Management
- Maintain collections of objects in lists or dictionaries.
- Track statistics such as total plants, growth, and types.
- Analytics helpers (nested classes) organize operations on data.

### Loops & Iteration
- Use for loops to iterate over object collections.
- Can calculate totals, growth, or other metrics dynamically.
- Avoid global state; operate through class or object methods.

### Code Organization
- Keep functions and operations within appropriate classes.
- Avoid scattered global functions.
- Modular design supports readability, maintenance, and scalability.

### Testing & Validation
- Include test cases with if ``__name__ == "__main__"``:
- Validate inputs and outputs before updating object state.
- Print outputs to verify behavior during development.