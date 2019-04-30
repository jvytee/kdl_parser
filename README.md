# kdl_parser
Provides basic functionality of [kdl_parser_py](https://github.com/ros/kdl_parser) without ROS dependencies. Includes [urdf_parser_py](https://github.com/ros/urdf_parser_py) for that purpose.

## Installation
kdl_parser depends on PyKDL, so please install the python bindings for Orocos KDL first. Sources and installation instructions are available [here](https://github.com/orocos/orocos_kinematics_dynamics).

The package was not yet pushed to PyPI, but installation with setuptools is straightforward:
```sh
git clone https://github.com/jvytee/kdl_parser.git
cd kdl_parser
python3 setup.py install --user
```
