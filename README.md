# magicimport

Voldemort's Python import helper

```
pip install magicimport
```

## Import from uninstalled Python directories

Say you have a directory (relative path `../../dir_a`) like this:

```
    ├── ../../dir_a
        ├── utils
        │   ├── util_a.py
        │   └── ...
        └── ...
```

You want `func_a` from `utils.util_a.py`:

```
from magicimport import import_from
with import_from('../../'):
    from utils.util_a import func_a

func_a()  # use func_a
```

The advantage of **magicimport** is: outside of the `with` statement, your `sys.path` remains unchanged.
