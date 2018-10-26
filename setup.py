# setup.py
from distutils.core import setup
import py2exe
setup(name="rsync.py",
    version="2.1",
    description="Python port of rsync. Should help to synchronize folders.",
    long_description="""
This script mimics rsync. It is a sort of advanced version of xcopy. Its aim is
to selectively synchronize folders. More precisely it copy selective parts of a
folder to a destination folder and in addition can remove parts of the
destination folder that do not correspond to parts of the original folder.""",
    author="Vivian De Smedt",
    author_email="vivian@vdesmedt.com",
    url="https://bitbucket.org/vds2212/rsync.py",
    download_url="https://bitbucket.org/vds2212/rsync.py/downloads/rsync-2.1.zip",
    keywords = ["rsync", "windows", "win32", "backup", "synchronize", "copy", "xcopy"],
    license="Python",
    classifiers=["Development Status :: 5 - Production/Stable"],
    platforms=["windows", "linux"],
    console=["rsync.py"],
    scripts = ["rsync.py"],
    windows = [
        {
            "script": "rsync.py",
            "icon_resources": [(1, "rsync.ico")]
        }
    ],
)
