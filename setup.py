from setuptools import setup

setup(
    name="clishow",
    version="1.0",
    entry_points={
        "console_scripts": ["clishow=clishow:run_cli"],
    },
    install_requires=["opencv-python", "matplotlib", "numpy", "wave"],
)