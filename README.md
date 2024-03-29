# Appveyor To Dist Downloader

[![Latest PyPI Version](https://img.shields.io/pypi/v/appveyordist.svg)](https://pypi.python.org/pypi/appveyordist)

`appveyor-dist` is a script that pulls a project's artifacts
to your local machine, normally into your `dist` directory.

[Appveyor](https://www.appveyor.com/) is a continuous integration service that allows 
Open Source projects to build releases on their system, but
to push the resulting packages onto PyPI requires a lot of 
configuration. This script lets you keep control of pushing
to PyPI while automatically pulling the files off Appveyor.

Previously I was using [appveyor-artifacts](https://github.com/Robpol86/appveyor-artifacts) for this, but
its focus is pretty much on downloading coverage files and
trying to merge them, while I really just want to use the
artifacts as-is for redistribution. I didn't wind up basing
the code off their code, as it was rather over-kill for me.

### Why the weird spelling of artefact?

That's apparently how Americans spell it, and I figure
we'll follow Appveyor's API in the spelling even if
it looks weird to Canadians and Brits.

## Installation

```
pip install appveyordist
```

## Usage

```
$ cd pyopengl
$ appveyor-dist --user MikeCFletcher --project pyopengl --dist ./dist
$ twine upload dist/PyOpenGL_accelerate-3.1.3-*.whl
```
You can pass the `-f` flag to force overwriting files in `dist`,
by default only new files will be downloaded.

Note that we do *not* expect you to process the results or read
them. We will simply crash if there's a failure, but we will 
log warnings if a job in the build/release has crashed/failed.

### Requirements

Requires Python 3 and requests module, tests require tox and pytest.

### License

MIT License

`appveyordist` is copyright 2019 `Mike C. Fletcher <mcfletch@vrplumber.com>`_.
