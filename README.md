GridInstrument (aka Launchpad Scale-mode)
============

Did you ever wish you could use your Launchpad as a MIDI instrument? Do you covet the **Scale Mode** on the Launchpad Pro or Ableton Push, but not have the cash to buy them? Now you can play scales on any Novation Launchpad. 


Here's a quick [video demo](https://youtu.be/JJA2fm-2NVg).

**There is also an iOS app version of this code [here](https://itunes.apple.com/us/app/gridinstrument/id1296511558?mt=8).**

At it's core, **GridInstrument** is a library that allows you to display a scale grid on your Novation Launchpad. It functions very similarly to the scale mode on Henri David's _fantastic_  [Launchpad95](http://motscousus.com/stuff/2011-07_Novation_Launchpad_Ableton_Live_Scripts/) scripts for Ableton Live, and also similarly to the [scale mode](https://global.novationmusic.com/launchpad-pro-scale-mode) on a Launchpad Pro.

Features:

* Can be used as a standalone app or incorporate into another Python project.
* Key switching (you know, so that you're not stuck in the key of C)
* Scale switching between the same 26 musical modes as Launchpad95
* Works on Raspberry Pi and Mac OS (probably Windows, too, but not tested).
* Two layouts (Diatonic 4th and Chromatic)
* Works with all Novation Launchpads

## Requirements

Before you try to do anything, make sure you have **Python 2** and **pip** installed.

## How to Use it as a Standalone App

Download the source code from github and install prerequisites:

    git clone https://github.com/dhilowitz/GridInstrument
    cd GridInstrument; pip install launchpad_rtmidi_py

Run the app:

    python play.py

If all goes well, you should see your grid light up. Next, go into another piece of software that can receive MIDI signals (sforzando is a good, free choice), and you should see a new MIDI device called "Grid Instrument (Virtual Port)"

### How to Use it as a Python Library

You have two options for how to install it.

### Option 1: Install it Manually

Download the source code from github:

    git clone https://github.com/dhilowitz/GridInstrument
    cd GridInstrument

Install it:

    python setup.py install

#### Option 2: Install it with Pip

    pip install grid_instrument