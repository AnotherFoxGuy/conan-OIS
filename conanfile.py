from conans import ConanFile, CMake, tools
from conans.tools import os_info, SystemPackageTool


class OisConan(ConanFile):
    name = "ois"
    version = "1.4"
    license = "zlib"
    author = "Edgar Edgar@AnotherFoxGuy.com"
    url = "https://github.com/AnotherFoxGuy/conan-OIS/"
    description = "Object oriented Input System"
    topics = ("Input", "System")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake_find_package"
    exports_sources = [
        "includes/*",
        "src/*",
        "CMakeLists.txt"
    ]

    def requirements(self):
        if os_info.is_windows:
            self.requires("directx-sdk/9.0@anotherfoxguy/stable")

    def system_requirements(self):
        if os_info.is_linux:
            if os_info.with_apt:
                installer = SystemPackageTool()
                installer.install("libx11-dev")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.includedirs = ['include', 'include/ois']
        self.cpp_info.libs = tools.collect_libs(self)
