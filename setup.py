from distutils.core import setup


setup(
    name = "xi",
    version = "0.0dev",
    author = "startling",
    author_email = "tdixon51793@gmail.com",
    description = "A little script for copying through unix pipes.",
    scripts = ['scripts/xi'],
    install_requires = ['argent', 'clint', 'xerox'],
)
