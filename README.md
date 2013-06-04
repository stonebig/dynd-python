DyND-Python
===========

DyND-Python is the Python exposure of the DyND library.
It supports Python 2.6, 2.7, and 3.3.

https://github.com/ContinuumIO/libdynd

https://github.com/ContinuumIO/dynd-python

Trying Out DyND
---------------

The easiest way to try it out is through the Anaconda
Python distribution. The latest release of Anaconda includes
a version of DyND.

http://continuum.io/downloads

For trying the latest updates, there is also an automated
build configured which tracks the latest git master. When
all the tests pass, it uploads conda packages to the Anaconda
dev channel. To get these versions, you need a .condarc file
which includes "http://repo.continuum.io/pkgs/dev" in its
channels list.  See http://docs.continuum.io/conda/intro.html#configuration
for more details. On windows, the .condarc file goes in
the %USERPROFILE% directory.

Here's an example .condarc file which includes the dev channel:

```
channels:
  - http://repo.continuum.io/pkgs/dev
  - http://repo.continuum.io/pkgs/free
  - http://repo.continuum.io/pkgs/pro
  - http://repo.continuum.io/pkgs/gpl
```

Developing DyND
---------------

See BUILD_INSTALL.md for details on building and installing
the software for environments not supported by Anaconda, or
if you would like to modify or contribute to the project.
