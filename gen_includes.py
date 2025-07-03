import os


def get_platformio_packages_dir():
    return os.environ.get(
        "PLATFORMIO_PACKAGES_DIR", os.path.expanduser("~/.platformio/packages/")
    )


def get_framework():
    try:
        with open(".framework", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return ""  # default fallback


def gen_recursive_include_path(base_dir):
    include_paths = []
    for dir_path, dir_names, file_names in os.walk(base_dir):
        if "src" in dir_names:
            s = os.path.join(dir_path, "src")
            include_paths.append(f"-I{s}")
    return include_paths


lib_dir = os.path.join(get_platformio_packages_dir(), get_framework(), "libraries")


flags = " ".join(gen_recursive_include_path(lib_dir))
print(flags)
