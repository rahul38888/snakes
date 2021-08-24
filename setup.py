setup(
    name="snakes",
    version="1.0.0",
    description="The classic snakes",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/rahul38888/snakes",
    author="Rahul",
    author_email="rahul38888@google.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["snakes"],
    include_package_data=True,
    install_requires=[
        "asciimatics"
    ],
    entry_points={"console_scripts": ["snakes=src.game.__main__.main"]},
)