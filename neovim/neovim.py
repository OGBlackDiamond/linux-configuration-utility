import pathlib
import shutil


class NeoVim:

    nvim_directory: pathlib.PosixPath

    lua_directory: pathlib.PosixPath
    plugins_directory: pathlib.PosixPath

    def __init__(self, configure) -> None:
        self.nvim_directory = configure.get_home_directory().joinpath(".config/nvim/")
        self.lua_directory = self.nvim_directory.joinpath("lua/")
        self.plugins_directory = self.lua_directory.joinpath("plugins/")

    def ensure_fs(self) -> None:
        self.nvim_directory.mkdir(parents=True, exist_ok=True)
        self.lua_directory.mkdir(parents=True, exist_ok=True)
        self.plugins_directory.mkdir(parents=True, exist_ok=True)

    def copy_all(self) -> None:
        shutil.copytree("src/", self.nvim_directory, dirs_exist_ok=False)

    def remove_all(self) -> None:
        shutil.rmtree(self.nvim_directory)
