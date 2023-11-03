from pathlib import Path
from typing import Optional, Union
import json
import yaml


def load_file(path: Path,
              suffix: Optional[str] = None) -> Union[list, dict, str]:
    """
    Read json or yaml file contents.

    Parameters
    ----------
    path: pathlib path object
        Path to file to read

    suffix: string, optional
        Determines the method used to load the file.

        If None, suffix is inferred from path. In case there is a file that is
        json/yaml formatted but does not end in .json or .yaml, suffix can be
        specified here to indicate how it should be read.

    Returns
    ----------
    data: Union[list, dict, str]
        contents of file loaded as python object
    """
    # load json or yaml file and add its contents to the given collection
    if suffix is None:
        suffix = path.suffix.strip('.')
    with open(path, 'r') as f:
        if suffix == 'json':
            data = json.load(f)
        elif suffix in ('yml', 'yaml'):
            data = yaml.safe_load(f)
        else:
            raise ValueError(
                f'file: {path}, suffix: {suffix} - suffix must be .json, .yml, or .yaml')
    return data

