from glob import glob
from setuptools import find_packages, setup

package_name = "omokai_executor"

setup(
    name=package_name,
    version="0.1.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        (
            "share/ament_index/resource_index/packages",
            ["resource/" + package_name],
        ),
        (
            "share/" + package_name,
            ["package.xml"],
        ),
        (
            "share/" + package_name + "/launch",
            glob("launch/*.launch.py"),
        ),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Joel Viju",
    maintainer_email="joelviju2002@gmail.com",
    description="Deterministic mission executor for the Omokai Robotics take-home task.",
    license="MIT",
    extras_require={
        "test": ["pytest"],
    },
    entry_points={
        "console_scripts": [
            "executor = omokai_executor.executor:main",
        ],
    },
)