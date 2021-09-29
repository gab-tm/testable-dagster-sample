import setuptools

setuptools.setup(
    name="cool_beans",
    packages=setuptools.find_packages(exclude=["cool_beans_tests"]),
    install_requires=[
        "dagster==0.12.11",
        "dagit==0.12.11",
        "dagster-docker==0.12.11",
        "essential-generators==1.0",
        "pytest",
    ],
)
