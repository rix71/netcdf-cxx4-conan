# NetCDF C++ Conan Package

[Conan](https://conan.io) package for [NetCDF-C++](https://github.com/Unidata/netcdf-cxx4/tree/master) library. Inspired by [Chrismarsh](https://github.com/Chrismarsh/conan-netcdf-cxx4/tree/stable/4.x).

## Usage
Clone this repository and run the following command to create the package:

```bash
cd netcdf-cxx4-conan
conan create . --build=missing [-s build_type=Debug]
```
That should do it. You can now use the package in your projects.
In your project's `conanfile.py` add:
```python
def requirements(self):
        self.requires("netcdf-cxx4/4.3.1")
```
and in your `CMakeLists.txt`:
```cmake
find_package(netcdf-cxx4 CONFIG REQUIRED)
target_link_libraries(executable PUBLIC netcdf-cxx4::netcdf-cxx4)
```
