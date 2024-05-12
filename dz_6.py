from collections import namedtuple
import pathlib
import sys

File = namedtuple("File", ["filename", "extension", "is_directory", "parent"])

def get_dir_info(path: pathlib.Path | str) -> list[File]:
    base_dir = pathlib.Path(path)
    result = []
    for file in base_dir.iterdir():
        result.append(File(file.name, file.suffix, file.is_dir(), file.parent))
    return result

def command_run(*args) -> pathlib.Path:
    if len(args) == 1:
        return pathlib.Path.cwd()
    _, path, *_ = args
    return pathlib.Path(path)

if __name__ == "__main__":
    path = command_run(*sys.argv)
    print(path)
    print(*get_dir_info(path), sep='\n')