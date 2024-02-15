# deep-dict-update

<!--[![PyPI version](https://badge.fury.io/py/deep-dict-update.svg)](https://badge.fury.io/py/deep-dict-update)-->
<!--[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)-->

A Python package for recursively updating nested dictionaries with the content of another dictionary.

## Installation

You can install `dict-update` via pip:

```sh
pip install dict-update
```

## Usage

``` python
from dict_update import dict_update

orig_dict = {
    'a': {
        'b': 2,
        'c': {
            'd': 3
        }
    }
}

new_dict = {
    'a': {
        'c': {
            'e': 4
        },
        'f': 5
    },
    'g': 6
}

updated_dict = dict_update(orig_dict, new_dict)
print(updated_dict)
```

## Output

``` python
{
    'a': {
        'b': 2,
        'c': {
            'd': 3,
            'e': 4
        },
        'f': 5
    },
    'g': 6
}
```

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
