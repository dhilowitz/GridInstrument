from setuptools import setup
import sys

if not sys.version_info[0] == 2:
	sys.exit("Error: grid_instrument requires Python 2")

setup(
	name = "grid_instrument",
	version = "0.6.2",
	description = "Turn your Novation Launchpad into a MIDI instrument.",
	long_description = open('README.rst').read(),
	author = "Dave Hilowitz",
	author_email = "dhilowitz@gmail.com",
	license = "MIT License",
	keywords = "novation launchpad scales midi",
	url = "https://github.com/dhilowitz/GridInstrument",
	packages = ["grid_instrument"],
	install_requires = ["launchpad_rtmidi_py", "python-rtmidi"]
)
