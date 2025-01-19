# python-iso20022

A Python package that automatically generates and updates dataclasses from ISO20022 schemas daily, making it easy to integrate and validate financial message data.

## Features

- **Daily Updates**: Clones the [ISO20022 Message Catalogue](https://github.com/galactixx/iso20022-message-catalogue) repository at 9 AM CST to retrieve the latest ISO20022 schemas.
- **Dataclass Generation**: Converts ISO20022 schema definitions into Python dataclasses for easy usage.
- **Refactored Code**: Automatically refactors generated dataclass models and associated code for seamless integration.
- **Validation Ready**: Provides tools to validate financial messages against ISO20022 standards.

## **Installation**

To install python-iso20022, run the following command:

```bash
pip install python-iso20022
```

## Repository Structure

```
python-iso20022/
├── .github/workflows            # CI/CD workflows
├── python_iso20022/             # Top-level package directory
│   ├── acmt/                    # Example of a message set directory
│   │   ├── acmt_001_001_08/     # Directory for a specific message
│   │   │   ├── __init__.py      # Standard __init__.py file
│   │   │   ├── enums.py         # Enums specific to this message (optional)
│   │   │   ├── models.py        # Models for this message
│   │   ├── __init__.py          # Standard __init__.py file
│   │   ├── enums.py             # Enums specific to this message set (optional)
│   ├── __init__.py              # Standard __init__.py file
│   ├── enums.py                 # Enums used across multiple message sets
├── tests/                       # Test suite for the package
├── .gitignore                   # Git ignore file
├── LICENSE                      # Project license
├── README.md                    # Project documentation
├── generate.py                  # Python script that generates all code
├── poetry.lock                  # Lock file for dependencies
├── pyproject.toml               # Project configuration for Poetry
├── requirements-action.txt      # Action-specific requirements
```

## How It Works

The `python_iso20022` package leverages the ISO20022 schemas maintained in the [ISO20022 Message Catalogue](https://github.com/galactixx/iso20022-message-catalogue) repository. Every day at 9 AM CST, this repository clones the catalogue and uses its XSD schemas to:

1. Generate Python dataclass models for all messages.
2. Refactor the generated models to ensure consistency and usability.
3. Automatically generate associated code, including parsers and enumerations.

### Message Set Structure

The `python_iso20022` package is organized into directories for each message set, such as `acmt` and `auth`, among others. Each message set directory contains subdirectories for specific messages, such as `acmt_001_001_08`. Each message subdirectory contains:

- **`models.py`**: Defines the primary dataclasses for the message.
- **`enums.py` (optional)**: Contains enumerations specific to the message, if applicable.

Each message set directory also contains a `enums.py` file for enums that are shared across multiple messages within the same message set.

Additionally, the top-level `enums.py` file in the `python_iso20022` package contains enums that are used across multiple message sets.

## Usage

To parse an XML file for a specific message, import the appropriate class from either the module of the relevant message set or specific message.

```python
from python_iso20022.acmt import Acmt00100108
```

or 

```python
from python_iso20022.acmt.acmt_001_001_08 import Acmt00100108
```

For example, to parse an XML file representing the `acmt.001.001.08` message:

```python
from python_iso20022.acmt import Acmt00100108

# XML file path
xml_file_path = "path/to/your/file.xml"

# Parse the XML into a dataclass
parsed_message = Acmt00100108.from_iso20022_xml(xml_file_path)

# Use the parsed dataclass
print(parsed_message)
```

This approach ensures that the XML file is correctly deserialized into the corresponding dataclass for further processing.

## Models Overview

Each generated dataclass inherits from one of the below classes.

### `ISO20022Message`
This subclass represents a top-level ISO20022 message and provides additional functionality specific to complete ISO20022 XML documents.

**Methods:**
- `write_to_iso20022_xml(path: Path) -> None`: Writes the XML representation to a specified file.

### `ISO20022MessageElement`
This subclass represents individual components of an ISO20022 message. It is designed for use within the context of a larger message.

---

Each class above inherits from `AbstractISO20022Model` which provides access to the following methods:
- `to_iso20022_xml(pretty_print: bool = True) -> str`: Abstract method for serializing the instance to an ISO20022-compliant XML string.
- `deep_copy() -> AbstractISO20022Model`: Creates and returns a deep copy of the instance.
- `from_iso20022_xml(source: Union[str, Path, bytes, IO]) -> AbstractISO20022Model`: Class method for creating an instance from an ISO20022 XML source.
- `to_json(pretty_print: bool = True) -> str`: Serializes the instance to a JSON string.
- `is_equal_to(other: AbstractISO20022Model) -> bool`: Compares two instances by their XML representation.

## Workflow Details

The GitHub Actions configuration in `.github/workflows` automates daily updates by cloning the [ISO20022 Message Catalogue](https://github.com/galactixx/iso20022-message-catalogue) and processing its schemas.

- **Daily Update Workflow**: Clones the catalogue repository and generates/refactors code based on its schemas at 9 AM CST.

## License

This project is licensed under the terms of the [MIT License](LICENSE).
