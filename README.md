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
│   │   ├── parse.py             # Parsing functions for messages in the message set
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

The `python_iso20022` package is organized into directories for each message set, such as `acmt`, `auth`, and `tsrv`. Each message set directory contains subdirectories for specific messages, such as `acmt_001_001_08`. Each message subdirectory contains:

- **`models.py`**: Defines the primary dataclasses for the message.
- **`enums.py` (optional)**: Contains enumerations specific to the message, if applicable.

Each message set directory also contains a `enums.py` file for enums that are shared across multiple messages within the same message set.

Additionally, the top-level `enums.py` file in the `python_iso20022` package contains enums that are used across multiple message sets.

Each message set directory also includes a `parse.py` file, which consolidates imports of all message models in the set and provides parsing functions to deserialize XML sources into the corresponding dataclasses.

### Example

In `python_iso20022/acmt/parse.py`:

```python
from python_iso20022.acmt.acmt_001_001_08.models import Acmt00100108
from python_iso20022.acmt.acmt_002_001_08.models import Acmt00200108
# ... other imports ...
from python_iso20022.utils import XmlSource, read_xml_source

def parse_acmt_001_001_08(source: XmlSource) -> Acmt00100108:
    return read_xml_source(source, Acmt00100108)

def parse_acmt_002_001_08(source: XmlSource) -> Acmt00200108:
    return read_xml_source(source, Acmt00200108)
```

## Usage

To parse an XML file for a specific message, import the appropriate function from the parsing module of the relevant message set. For example, to parse `acmt_001_001_08`:

```python
from python_iso20022.acmt.parse import parse_acmt_001_001_08

# XML file path
xml_file_path = "path/to/your/file.xml"

# Parse the XML into a dataclass
parsed_message = parse_acmt_001_001_08(xml_file_path)

# Use the parsed dataclass
print(parsed_message)
```

This approach ensures that the XML file is correctly deserialized into the corresponding dataclass for further processing.

### Workflow Details

The GitHub Actions configuration in `.github/workflows` automates daily updates by cloning the [ISO20022 Message Catalogue](https://github.com/galactixx/iso20022-message-catalogue) and processing its schemas.

- **Daily Update Workflow**: Clones the catalogue repository and generates/refactors code based on its schemas at 9 AM CST.

## License

This project is licensed under the terms of the [MIT License](LICENSE).
