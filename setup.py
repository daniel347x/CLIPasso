import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deepclipasso",
    py_modules=["deepclipasso"],
    version="1.0.0",
    author="Microsoft ASG ML Team",
    description="CLIPasso applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://devicesasg.visualstudio.com/Incubation/_git/DeepInk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
