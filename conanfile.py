from conan import ConanFile
from conan.tools.files import collect_libs
from conan.tools.cmake import CMakeToolchain, CMake, CMakeDeps, cmake_layout
from conan.tools.system import package_manager


# --user rigsofrods --channel custom
class OisConan(ConanFile):
    name = "ois"
    version = "1.4.1"
    license = "zlib"
    author = "Edgar Edgar@AnotherFoxGuy.com"
    url = "https://github.com/AnotherFoxGuy/conan-OIS/"
    description = "Object oriented Input System"
    topics = ("Input", "System")
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = [
        "includes/*",
        "src/*",
        "CMakeLists.txt"
    ]

    def layout(self):
        cmake_layout(self)

    def requirements(self):
        if self.settings.os == "Windows":
            self.requires("directx-sdk/9.0@anotherfoxguy/stable")

    def system_requirements(self):
        package_manager.Apt(self).install(["libx11-dev"])

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables["OIS_BUILD_DEMOS"] = "OFF"
        tc.variables["CMAKE_DEBUG_POSTFIX"] = "d"
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.includedirs = ['include', 'include/OIS']
        self.cpp_info.libs = collect_libs(self)
