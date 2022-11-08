# CS5 Gold, Lab 3
# Filename: hw3pr1.py
# Name:
# Problem description: Lab 3 problem, "Sounds Good!"

import time
import random
import math
import csaudio
from csaudio import *
import wave
wave.big_endian = 0  # needed long ago
# if you are having trouble, comment out the above line...



# a function to get started with a reminder
# about list comprehensions...
def three_ize(L):
    """three_ize is the motto of the green CS 5 alien.
       It's also a function that accepts a list and
       returns a list of elements each three times as large.
    """
    # this is an example of a list comprehension
    LC = [3 * x for x in L]
    return LC



# Function to write #1:  scale

def scale(L, scale_factor):
    """ A function that takes in a list and
        returns a list of elements each "scale_factor" times as large.
    """
    # this is an example of a list comprehension
    LC = [ scale_factor * x for x in L ]
    return LC




# here is an example of a different method
# for writing the three_ize function:
def three_ize_by_index(L):
    """three_ize_by_index has the same behavior as three_ize
       but it uses the INDEX of each element, instead of
       using the elements themselves -- this is much more flexible!
    """
    # we get the length of L first, in order to use it in range:
    N = len(L)
    LC = [3 * L[i] for i in range(N)]
    return LC



# Function to write #2:  add_2

def add_2( L, M):
    """ This function joins two list together, based on the index of the elements
    """
    return [ L[i] + M[i] for i in range( len(L) ) ]




# Function to write #3:  add_3






# Function to write #4:  add_scale_2


def add_scale_2(L, M, L_scale, M_scale):
    """ This function multiplies every element in the list by the correspoinding scale and joins them together based on index
    """
    return [ ( L[i] * L_scale ) + ( M[i] * M_scale) for i in range( len(L) ) ]





# Helper function:  randomize

def randomize(x, chance_of_replacing):
    """randomize accepts an original value, x
       and a fraction named chance_of_replacing.

       With the "chance_of_replacing" chance, it
       should return a random float from -32767 to 32767.

       Otherwise, it should return x (not replacing it).
    """
    r = random.uniform(0, 1)
    if r < chance_of_replacing:
        return random.uniform(-32768, 32767)
    else:
        return x






# Function to write #5:  replace_some

def replace_some(L, chance_of_replacing):
    """ This function has a chance_of_replacing chance of replacing every value in a list with a random nmber """
    return [ randomize( L[i], chance_of_replacing ) for i in range(len(L))]









#
# below are functions that relate to sound-processing ...
#


# a function to make sure everything is working
def test():
    """A test function that plays swfaith.wav
       You'll need swfaith.wav in this folder.
    """
    play('swfaith.wav')


# The example changeSpeed function
def changeSpeed(filename, newsr):
    """changeSpeed allows the user to change an audio file's speed.
       Arguments: filename, the name of the original file
                  newsr, the new sampling rate in samples per second
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sound...")
    play(filename)

    samps, sr = readwav(filename)   # get samps and sr from the file!

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    # we don't really need this line, but for consistency...
    newsr = newsr             # from the input! (not needed, a reminder!) 
    newsamps = samps          # same samples as before
    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'



def flipflop(filename):
    """flipflop swaps the halves of an audio file
       Argument: filename, the name of the original file
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sound...")
    play(filename)

    samps, sr = readwav(filename)   # get samps and sr from the file!

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    print("Computing new sound...")
    # this gets the midpoint and calls it x
    x = len(samps)//2
    newsamps = samps[x:] + samps[:x]
    newsr = sr               # same sr as before

    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'




# Sound function to write #1:  reverse


def reverse(filename):
    """ reverse is a function to reverse the audio
        input: filename, the name of the original file
        output: no return value, but
                this creates the sound file 'out.wav'
                and plays it
    """
    print ("Reading in the sound data...")
    samps, sr = readwav(filename)

    print ("Computing new sound...")
    # this gets the midpoint and calls it x
    newsamps = samps[::-1]
    newsr = sr

    writewav( newsamps, newsr, "out.wav" )
    print ("Playing new sound...")
    play( 'out.wav' )




# Sound function to write #2:  volume

def volume(filename, scale_factor):
    """ volume scales the volume of a file with scale_factor
        input: filename: the name of the original file and volume: scale_factor with 100% = 1
        output: no return value, but
                this creates the sound file 'out.wav'
                and plays it
    """
    print ("Reading in the sound data...")
    samps, sr = readwav(filename)

    print ("Computing new sound...")
    # this gets the midpoint and calls it x
    newsamps = [ scale_factor * samps[x] for x in range( len(samps) ) ]
    newsr = sr

    writewav( newsamps, newsr, "out.wav" )
    print ("Playing new sound...")
    play( 'out.wav' )





# Sound function to write #3:  static


def static(filename, probability_of_static):
    """ this function replaces some of the samples with white noise, the chance of this is probability_of_static
        input: filename: the name of the original file and
        output: no return value, but
                this creates the sound file 'out.wav'
                and plays it
    """
    print ("Reading in the sound data...")
    samps, sr = readwav(filename)

    print ("Computing new sound...")
    # this gets the midpoint and calls it x
    newsamps = replace_some(samps, probability_of_static)
    newsr = sr

    writewav( newsamps, newsr, "out.wav" )
    print ("Playing new sound...")
    play( 'out.wav' )





# Sound function to write #4:  overlay


def overlay(filename1, filename2):
    """ This function overlays one piece of track with another.
        input: filename1: the name of the original file and filename2: the name of a second file
        output: no return value, but
                this creates the sound file 'out.wav'
                and plays it
    """
    print ("Reading in the sound data...")
    samps1, sr1 = readwav(filename1)
    samps2, sr2 = readwav(filename2)

    print ("Computing new sound...")
    # this gets the midpoint and calls it x
    newsamps = add_scale_2(samps1, samps2, 0.5, 0.5)
    newsr = sr1

    writewav( newsamps, newsr, "out.wav" )
    print ("Playing new sound...")
    play( 'out.wav' )




# Sound function to write #5:  echo


def echo(filename, time_delay):
    """ echo overlays the same track again after time_delay ms, to create echo
        input: filename, the name of the original file and time_delay in ms
        output: no return value, but
                this creates the sound file 'out.wav'
                and plays it
    """
    print ("Reading in the sound data...")
    samps, sr = readwav(filename)

    print ("Computing new sound...")
    # this gets the midpoint and calls it x
    echo_samps = [0] * int(sr * time_delay) + samps

    newsamps = add_scale_2(samps, echo_samps, 0.5, 0.5)

    writewav( newsamps, sr, "out.wav" )
    print ("Playing new sound...")
    play( 'out.wav' )





# Helper function for generating pure tones
def gen_pure_tone(freq, seconds):
    """pure_tone returns the y-values of a cosine wave
       whose frequency is freq Hertz.
       It returns nsamples values, taken once every 1/44100 of a second.
       Thus, the sampling rate is 44100 hertz.
       0.5 second (22050 samples) is probably enough.
    """
    # we get to pick our own sampling rate, sr
    sr = 22050
    # how many data samples to create
    nsamples = int(seconds*sr) # rounds down
    # our frequency-scaling coefficient, f
    f = 2*math.pi/sr   # converts from samples to Hz
    # our amplitude-scaling coefficient, a
    a = 32767.0
    
    # now, create the sound!
    samps = [a*math.sin(f*n*freq) for n in range(nsamples)]
    sr = sr   # not needed, but a reminder
    return [samps,sr]


def pure_tone(freq, time_in_seconds):
    """Generates and plays a pure tone of the given frequence."""
    print("Generating tone...")
    samps, sr = gen_pure_tone(freq, time_in_seconds)

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    print("Writing out the sound data...")
    write_wav([samps, sr], "out.wav") # write data to out.wav

    print("Playing new sound...")
    play('out.wav')




# Sound function to write #6:  chord

def chord(f1, f2, f3, time_in_seconds):
    """ chord generate a chord based on three frequencies
        input: three different frequencies (f1, f2, f3) and time_in_seconds
        output: no return value, but
                this creates the sound file 'out.wav'
                and plays it
    """
    samps1, sr1 = gen_pure_tone(f1, time_in_seconds)
    samps2, sr2 = gen_pure_tone(f2, time_in_seconds)
    samps3, sr3 = gen_pure_tone(f3, time_in_seconds)
    newsamps = add_scale_2(samps1, samps2, 0.5, 0.5)
    newsamps = add_scale_2(newsamps, samps3, 0.6666, 0.3333)
    newsr = sr1

    writewav( newsamps, newsr, "out.wav" )
    print ("Playing new sound...")
    play( 'out.wav' )
    pass