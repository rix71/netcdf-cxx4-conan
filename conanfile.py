from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.files import get


class NetCDFCxx4Recipe(ConanFile):
    name = "netcdf-cxx4"
    version = "4.3.1"
    package_type = "library"

    license = "MIT"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "netcdf-cxx4 conan package"

    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    def source(self):
        get(
            self,
            url="https://github.com/Unidata/netcdf-cxx4/archive/refs/tags/v4.3.1.tar.gz",
            strip_root=True,
        )

    def requirements(self):
        self.requires("netcdf/4.8.1")
        self.requires("hdf5/1.14.1")

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.rm_safe("fPIC")

    def layout(self):
        cmake_layout(self, src_folder="netcdf-cxx4")

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables["NCXX_ENABLE_TESTS"] = False
        tc.variables["BUILD_SHARED_LIBS"] = self.options.shared

        # We need to add `hdf5` to the include directory because the netCDF-cxx4 tries
        # to `#include <hdf5.h>` from the `hdf5` package, but I guess the conan HDF5 package
        # sets the include directory so that it has to be `#include <hdf5/hdf5.h>`
        # ! Note: this was only an issue with the `-s build_type=Debug` flag
        hdf5_includedir = self.dependencies["hdf5"].cpp_info.includedirs[0]
        # This is the important part
        tc.variables["CMAKE_C_FLAGS"] = f"-I{hdf5_includedir}/hdf5"
        # Might as well add it to the CXX flags
        tc.variables["CMAKE_CXX_FLAGS"] = f"-I{hdf5_includedir}/hdf5"
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["netcdf-cxx4"]
