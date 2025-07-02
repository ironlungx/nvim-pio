import os


def gen_recursive_include_path(dir):
    include_path = []
    for dir_path, dir_names, file_names in os.walk(dir):
        if "src" in dir_names:
            s = dir_path + "/src"
            include_path.extend([" -I", s])
    return include_path


flags = ""
flags = flags + "".join(
    gen_recursive_include_path(
        os.path.expanduser("~")
        + "/.platformio/packages/framework-arduinoespressif32/libraries/"
    )
)
print(flags)
