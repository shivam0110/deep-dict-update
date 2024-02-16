# deep-dict-update

<!--[![PyPI version](https://badge.fury.io/py/deep-dict-update.svg)](https://badge.fury.io/py/deep-dict-update)-->
<!--[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)-->

A Python package for recursively updating nested dictionaries with the content of another dictionary.

## Installation

You can install `deep-dict-update` via pip:

```sh
pip install deep-dict-update
```

## Usage

``` python
from deep_dict_update import deep_dict_update

orig_dict = {
    'data': [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'}
    ]
}

new_dict = {
    'data': [
        {'id': 3, 'name': 'Charlie'},
        {'id': 4, 'name': 'David'}
    ]
}

updated_dict = deep_dict_update(orig_dict, new_dict)
print(updated_dict)
```

## Output

``` python
{
    'data': [
        {'id': 3, 'name': 'Charlie'},
        {'id': 4, 'name': 'David'}
    ]
}
```

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
