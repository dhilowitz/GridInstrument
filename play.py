#!/usr/bin/env python
#
# Quick usage example of "grid_instrument" with MIDI output port.
# Works with all Launchpads: Mk1, Mk2, S/Mini, Pro, XL and LaunchKey
# 
#
# David Hilowitz 1/15/19
# decided.ly / davehilowitz.com
#

import grid_instrument
from grid_instrument import grid_instrument
import rtmidi
import time

def note_callback(messageType, midiNote, velocity):
	if messageType is "note_on":
		midiout.sendMessage(rtmidi.MidiMessage.noteOn(0x90, midiNote, velocity))
	elif messageType is "note_off":
		midiout.sendMessage(rtmidi.MidiMessage.noteOff(0x80, midiNote))

# Create a MIDI output port
midiout = rtmidi.RtMidiOut()
midiout.openVirtualPort("Grid Instrument (Virtual Port)")

# Set up GridInstrument
instrument = grid_instrument.GridInstrument()
instrument.intro_message = 'grid'
instrument.note_callback = note_callback
instrument.launchpad_pro_velocity_multiplier = 2.5
instrument.min_velocity = 100
instrument.max_velocity = 100
instrument.default_velocity = 100

instrument.start()