from pathlib import Path


src_dir = '/etc'
dst_dir = '/home/dima/etc'


def mk_tree(src: str, dst: str) -> None:
    src_glob = Path(src_dir).glob('*')
    dst_path = Path(dst_dir)
    for path in src_glob:
        curr_path = dst_path / path.relative_to(src_dir)
        if path.is_dir():
            curr_path.mkdir(exist_ok=True)
        elif path.is_file():
            curr_path.touch()


if __name__ == "__main__": # simple comment
    Path(dst_dir).mkdir()
    mk_tree(src_dir, dst_dir)
