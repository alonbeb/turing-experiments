import gzip
import json
import os
import pathlib
from typing import Any


def get_plaintext_file_contents(path_to_file: pathlib.Path) -> str:
    with open(path_to_file, "r") as f:
        return f.read()


def save_json(obj: Any, filename: pathlib.Path, make_dirs_if_necessary=False, indent=2, **kwargs) -> None:
    if make_dirs_if_necessary:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
    if filename.suffix == ".gz":
        with gzip.open(filename, "wt") as f:
            json.dump(obj, f, indent=indent, **kwargs)
    with open(filename, "w", encoding="utf8") as f:
        json.dump(obj, f, indent=indent, **kwargs)

    return None


def load_json(filename: pathlib.Path) -> Any:
    if filename.suffix == ".gz":
        with gzip.open(filename, "rt") as f:
            return json.load(f)
    with open(filename, "r", encoding="utf8") as f:
        return json.load(f)
