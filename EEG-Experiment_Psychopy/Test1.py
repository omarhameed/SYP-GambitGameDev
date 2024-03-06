#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on Sun Mar  3 00:26:26 2024
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'Test1'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Applications/PsychoPy.app/Contents/Resources/EEG_Experiment/Test1.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1920, 1080], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "WelcomeScreen" ---
    welcome_message = visual.TextStim(win=win, name='welcome_message',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='red', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    cation_sign = visual.ImageStim(
        win=win,
        name='cation_sign', 
        image='/Users/omarg/Desktop/SYP/Floor_Sign_Yield_Caution_Sign_Creative_Safety_Supply__92002.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.3, 0.3), size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    
    # --- Initialize components for Routine "Test_1" ---
    ob1_t1 = visual.Rect(
        win=win, name='ob1_t1',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=(0,0), anchor='top-right',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "blank1s" ---
    blank_screen = visual.TextStim(win=win, name='blank_screen',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "test_2" ---
    obj1_t2 = visual.Rect(
        win=win, name='obj1_t2',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=(0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='black',
        opacity=None, depth=0.0, interpolate=True)
    obj2_t2 = visual.Rect(
        win=win, name='obj2_t2',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=(-0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    obj3_t2 = visual.Rect(
        win=win, name='obj3_t2',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    
    # --- Initialize components for Routine "Test_3" ---
    obj1_t3 = visual.Rect(
        win=win, name='obj1_t3',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=(0.25, 0.1), anchor='top-right',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    obj2_t3 = visual.Rect(
        win=win, name='obj2_t3',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=(-0.25, 0.1), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    obj3_t3 = visual.Rect(
        win=win, name='obj3_t3',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=(0.25, -0.1), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    obj4_t3 = visual.Rect(
        win=win, name='obj4_t3',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=(0.25, 0.1), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='white',
        opacity=None, depth=-3.0, interpolate=True)
    
    # --- Initialize components for Routine "Test_4" ---
    obj1_t4 = visual.Rect(
        win=win, name='obj1_t4',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    obj2_t4 = visual.Rect(
        win=win, name='obj2_t4',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=(-0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    obj3_t4 = visual.Rect(
        win=win, name='obj3_t4',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=(0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    obj4_t4 = visual.Rect(
        win=win, name='obj4_t4',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=(-0.25, 0.1), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-3.0, interpolate=True)
    obj5_t4 = visual.Rect(
        win=win, name='obj5_t4',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=(0.25, 0.1), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-4.0, interpolate=True)
    obj6_t4 = visual.Rect(
        win=win, name='obj6_t4',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=(0, 0.1), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-5.0, interpolate=True)
    obj7_t4 = visual.Rect(
        win=win, name='obj7_t4',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=(-0.25, -0.1), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-6.0, interpolate=True)
    obj8_t4 = visual.Rect(
        win=win, name='obj8_t4',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=(0.25, -0.1), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-7.0, interpolate=True)
    obj9_t4 = visual.Rect(
        win=win, name='obj9_t4',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=(0, -0.1), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-8.0, interpolate=True)
    sound_1 = sound.Sound('song.mp3', secs=1.0, stereo=True, hamming=True,
        name='sound_1')
    sound_1.setVolume(1.0)
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "WelcomeScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('WelcomeScreen.started', globalClock.getTime())
    # keep track of which components have finished
    WelcomeScreenComponents = [welcome_message, cation_sign]
    for thisComponent in WelcomeScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "WelcomeScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 10.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *welcome_message* updates
        
        # if welcome_message is starting this frame...
        if welcome_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcome_message.frameNStart = frameN  # exact frame index
            welcome_message.tStart = t  # local t and not account for scr refresh
            welcome_message.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcome_message, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'welcome_message.started')
            # update status
            welcome_message.status = STARTED
            welcome_message.setAutoDraw(True)
        
        # if welcome_message is active this frame...
        if welcome_message.status == STARTED:
            # update params
            welcome_message.setText("\n\nWelcome to the Experiment!! \n\nDisclaimer: This experiment involves viewing flickering objects. If you are prone to photosensitive epilepsy or have other visual sensitivities, please proceed with caution or consider not participating. Just so we're clear, we can't take responsibility for any discomfort or issues that arise.", log=False)
        
        # if welcome_message is stopping this frame...
        if welcome_message.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > welcome_message.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                welcome_message.tStop = t  # not accounting for scr refresh
                welcome_message.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'welcome_message.stopped')
                # update status
                welcome_message.status = FINISHED
                welcome_message.setAutoDraw(False)
        
        # *cation_sign* updates
        
        # if cation_sign is starting this frame...
        if cation_sign.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cation_sign.frameNStart = frameN  # exact frame index
            cation_sign.tStart = t  # local t and not account for scr refresh
            cation_sign.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cation_sign, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cation_sign.started')
            # update status
            cation_sign.status = STARTED
            cation_sign.setAutoDraw(True)
        
        # if cation_sign is active this frame...
        if cation_sign.status == STARTED:
            # update params
            pass
        
        # if cation_sign is stopping this frame...
        if cation_sign.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cation_sign.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                cation_sign.tStop = t  # not accounting for scr refresh
                cation_sign.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cation_sign.stopped')
                # update status
                cation_sign.status = FINISHED
                cation_sign.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in WelcomeScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "WelcomeScreen" ---
    for thisComponent in WelcomeScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('WelcomeScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-10.000000)
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=5.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            globals()[paramName] = thisTrial_2[paramName]
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                globals()[paramName] = thisTrial_2[paramName]
        
        # --- Prepare to start Routine "Test_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Test_1.started', globalClock.getTime())
        # keep track of which components have finished
        Test_1Components = [ob1_t1]
        for thisComponent in Test_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Test_1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 10.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ob1_t1* updates
            
            # if ob1_t1 is starting this frame...
            if ob1_t1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ob1_t1.frameNStart = frameN  # exact frame index
                ob1_t1.tStart = t  # local t and not account for scr refresh
                ob1_t1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ob1_t1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ob1_t1.started')
                # update status
                ob1_t1.status = STARTED
                ob1_t1.setAutoDraw(True)
            
            # if ob1_t1 is active this frame...
            if ob1_t1.status == STARTED:
                # update params
                pass
            
            # if ob1_t1 is stopping this frame...
            if ob1_t1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ob1_t1.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    ob1_t1.tStop = t  # not accounting for scr refresh
                    ob1_t1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ob1_t1.stopped')
                    # update status
                    ob1_t1.status = FINISHED
                    ob1_t1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Test_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Test_1" ---
        for thisComponent in Test_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Test_1.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-10.000000)
        
        # --- Prepare to start Routine "blank1s" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('blank1s.started', globalClock.getTime())
        # keep track of which components have finished
        blank1sComponents = [blank_screen]
        for thisComponent in blank1sComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank1s" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > 1-frameTolerance:
                continueRoutine = False
            
            # *blank_screen* updates
            
            # if blank_screen is starting this frame...
            if blank_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blank_screen.frameNStart = frameN  # exact frame index
                blank_screen.tStart = t  # local t and not account for scr refresh
                blank_screen.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blank_screen, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blank_screen.started')
                # update status
                blank_screen.status = STARTED
                blank_screen.setAutoDraw(True)
            
            # if blank_screen is active this frame...
            if blank_screen.status == STARTED:
                # update params
                pass
            
            # if blank_screen is stopping this frame...
            if blank_screen.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blank_screen.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    blank_screen.tStop = t  # not accounting for scr refresh
                    blank_screen.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'blank_screen.stopped')
                    # update status
                    blank_screen.status = FINISHED
                    blank_screen.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank1sComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank1s" ---
        for thisComponent in blank1sComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('blank1s.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 5.0 repeats of 'trials_2'
    
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=2.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "test_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('test_2.started', globalClock.getTime())
        # keep track of which components have finished
        test_2Components = [obj1_t2, obj2_t2, obj3_t2]
        for thisComponent in test_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "test_2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 5.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *obj1_t2* updates
            
            # if obj1_t2 is starting this frame...
            if obj1_t2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                obj1_t2.frameNStart = frameN  # exact frame index
                obj1_t2.tStart = t  # local t and not account for scr refresh
                obj1_t2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(obj1_t2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'obj1_t2.started')
                # update status
                obj1_t2.status = STARTED
                obj1_t2.setAutoDraw(True)
            
            # if obj1_t2 is active this frame...
            if obj1_t2.status == STARTED:
                # update params
                pass
            
            # if obj1_t2 is stopping this frame...
            if obj1_t2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > obj1_t2.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    obj1_t2.tStop = t  # not accounting for scr refresh
                    obj1_t2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'obj1_t2.stopped')
                    # update status
                    obj1_t2.status = FINISHED
                    obj1_t2.setAutoDraw(False)
            
            # *obj2_t2* updates
            
            # if obj2_t2 is starting this frame...
            if obj2_t2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                obj2_t2.frameNStart = frameN  # exact frame index
                obj2_t2.tStart = t  # local t and not account for scr refresh
                obj2_t2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(obj2_t2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'obj2_t2.started')
                # update status
                obj2_t2.status = STARTED
                obj2_t2.setAutoDraw(True)
            
            # if obj2_t2 is active this frame...
            if obj2_t2.status == STARTED:
                # update params
                pass
            
            # if obj2_t2 is stopping this frame...
            if obj2_t2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > obj2_t2.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    obj2_t2.tStop = t  # not accounting for scr refresh
                    obj2_t2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'obj2_t2.stopped')
                    # update status
                    obj2_t2.status = FINISHED
                    obj2_t2.setAutoDraw(False)
            
            # *obj3_t2* updates
            
            # if obj3_t2 is starting this frame...
            if obj3_t2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                obj3_t2.frameNStart = frameN  # exact frame index
                obj3_t2.tStart = t  # local t and not account for scr refresh
                obj3_t2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(obj3_t2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'obj3_t2.started')
                # update status
                obj3_t2.status = STARTED
                obj3_t2.setAutoDraw(True)
            
            # if obj3_t2 is active this frame...
            if obj3_t2.status == STARTED:
                # update params
                pass
            
            # if obj3_t2 is stopping this frame...
            if obj3_t2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > obj3_t2.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    obj3_t2.tStop = t  # not accounting for scr refresh
                    obj3_t2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'obj3_t2.stopped')
                    # update status
                    obj3_t2.status = FINISHED
                    obj3_t2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in test_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "test_2" ---
        for thisComponent in test_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('test_2.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 2.0 repeats of 'trials'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_3 = data.TrialHandler(nReps=10.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_3')
    thisExp.addLoop(trials_3)  # add the loop to the experiment
    thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            globals()[paramName] = thisTrial_3[paramName]
    
    for thisTrial_3 in trials_3:
        currentLoop = trials_3
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                globals()[paramName] = thisTrial_3[paramName]
        
        # --- Prepare to start Routine "Test_3" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Test_3.started', globalClock.getTime())
        # keep track of which components have finished
        Test_3Components = [obj1_t3, obj2_t3, obj3_t3, obj4_t3]
        for thisComponent in Test_3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Test_3" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 5.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *obj1_t3* updates
            
            # if obj1_t3 is starting this frame...
            if obj1_t3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                obj1_t3.frameNStart = frameN  # exact frame index
                obj1_t3.tStart = t  # local t and not account for scr refresh
                obj1_t3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(obj1_t3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'obj1_t3.started')
                # update status
                obj1_t3.status = STARTED
                obj1_t3.setAutoDraw(True)
            
            # if obj1_t3 is active this frame...
            if obj1_t3.status == STARTED:
                # update params
                pass
            
            # if obj1_t3 is stopping this frame...
            if obj1_t3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > obj1_t3.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    obj1_t3.tStop = t  # not accounting for scr refresh
                    obj1_t3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'obj1_t3.stopped')
                    # update status
                    obj1_t3.status = FINISHED
                    obj1_t3.setAutoDraw(False)
            
            # *obj2_t3* updates
            
            # if obj2_t3 is starting this frame...
            if obj2_t3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                obj2_t3.frameNStart = frameN  # exact frame index
                obj2_t3.tStart = t  # local t and not account for scr refresh
                obj2_t3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(obj2_t3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'obj2_t3.started')
                # update status
                obj2_t3.status = STARTED
                obj2_t3.setAutoDraw(True)
            
            # if obj2_t3 is active this frame...
            if obj2_t3.status == STARTED:
                # update params
                pass
            
            # if obj2_t3 is stopping this frame...
            if obj2_t3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > obj2_t3.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    obj2_t3.tStop = t  # not accounting for scr refresh
                    obj2_t3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'obj2_t3.stopped')
                    # update status
                    obj2_t3.status = FINISHED
                    obj2_t3.setAutoDraw(False)
            
            # *obj3_t3* updates
            
            # if obj3_t3 is starting this frame...
            if obj3_t3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                obj3_t3.frameNStart = frameN  # exact frame index
                obj3_t3.tStart = t  # local t and not account for scr refresh
                obj3_t3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(obj3_t3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'obj3_t3.started')
                # update status
                obj3_t3.status = STARTED
                obj3_t3.setAutoDraw(True)
            
            # if obj3_t3 is active this frame...
            if obj3_t3.status == STARTED:
                # update params
                pass
            
            # if obj3_t3 is stopping this frame...
            if obj3_t3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > obj3_t3.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    obj3_t3.tStop = t  # not accounting for scr refresh
                    obj3_t3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'obj3_t3.stopped')
                    # update status
                    obj3_t3.status = FINISHED
                    obj3_t3.setAutoDraw(False)
            
            # *obj4_t3* updates
            
            # if obj4_t3 is starting this frame...
            if obj4_t3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                obj4_t3.frameNStart = frameN  # exact frame index
                obj4_t3.tStart = t  # local t and not account for scr refresh
                obj4_t3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(obj4_t3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'obj4_t3.started')
                # update status
                obj4_t3.status = STARTED
                obj4_t3.setAutoDraw(True)
            
            # if obj4_t3 is active this frame...
            if obj4_t3.status == STARTED:
                # update params
                pass
            
            # if obj4_t3 is stopping this frame...
            if obj4_t3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > obj4_t3.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    obj4_t3.tStop = t  # not accounting for scr refresh
                    obj4_t3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'obj4_t3.stopped')
                    # update status
                    obj4_t3.status = FINISHED
                    obj4_t3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Test_3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Test_3" ---
        for thisComponent in Test_3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Test_3.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 10.0 repeats of 'trials_3'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_4 = data.TrialHandler(nReps=10.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_4')
    thisExp.addLoop(trials_4)  # add the loop to the experiment
    thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            globals()[paramName] = thisTrial_4[paramName]
    
    for thisTrial_4 in trials_4:
        currentLoop = trials_4
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
        if thisTrial_4 != None:
            for paramName in thisTrial_4:
                globals()[paramName] = thisTrial_4[paramName]
        
        # --- Prepare to start Routine "Test_4" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Test_4.started', globalClock.getTime())
        sound_1.setSound('song.mp3', secs=1.0, hamming=True)
        sound_1.setVolume(1.0, log=False)
        sound_1.seek(0)
        # keep track of which components have finished
        Test_4Components = [obj1_t4, obj2_t4, obj3_t4, obj4_t4, obj5_t4, obj6_t4, obj7_t4, obj8_t4, obj9_t4, sound_1]
        for thisComponent in Test_4Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Test_4" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 5.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *obj1_t4* updates
            
            # if obj1_t4 is starting this frame...
            if obj1_t4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                obj1_t4.frameNStart = frameN  # exact frame index
                obj1_t4.tStart = t  # local t and not account for scr refresh
                obj1_t4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(obj1_t4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'obj1_t4.started')
                # update status
                obj1_t4.status = STARTED
                obj1_t4.setAutoDraw(True)
            
            # if obj1_t4 is active this frame...
            if obj1_t4.status == STARTED:
                # update params
                pass
            
            # if obj1_t4 is stopping this frame...
            if obj1_t4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > obj1_t4.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    obj1_t4.tStop = t  # not accounting for scr refresh
                    obj1_t4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'obj1_t4.stopped')
                    # update status
                    obj1_t4.status = FINISHED
                    obj1_t4.setAutoDraw(False)
            
            # *obj2_t4* updates
            
            # if obj2_t4 is starting this frame...
            if obj2_t4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                obj2_t4.frameNStart = frameN  # exact frame index
                obj2_t4.tStart = t  # local t and not account for scr refresh
                obj2_t4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(obj2_t4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'obj2_t4.started')
                # update status
                obj2_t4.status = STARTED
                obj2_t4.setAutoDraw(True)
            
            # if obj2_t4 is active this frame...
            if obj2_t4.status == STARTED:
                # update params
                pass
            
            # if obj2_t4 is stopping this frame...
            if obj2_t4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > obj2_t4.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    obj2_t4.tStop = t  # not accounting for scr refresh
                    obj2_t4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'obj2_t4.stopped')
                    # update status
                    obj2_t4.status = FINISHED
                    obj2_t4.setAutoDraw(False)
            
            # *obj3_t4* updates
            
            # if obj3_t4 is starting this frame...
            if obj3_t4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                obj3_t4.frameNStart = frameN  # exact frame index
                obj3_t4.tStart = t  # local t and not account for scr refresh
                obj3_t4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(obj3_t4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'obj3_t4.started')
                # update status
                obj3_t4.status = STARTED
                obj3_t4.setAutoDraw(True)
            
            # if obj3_t4 is active this frame...
            if obj3_t4.status == STARTED:
                # update params
                pass
            
            # if obj3_t4 is stopping this frame...
            if obj3_t4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > obj3_t4.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    obj3_t4.tStop = t  # not accounting for scr refresh
                    obj3_t4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'obj3_t4.stopped')
                    # update status
                    obj3_t4.status = FINISHED
                    obj3_t4.setAutoDraw(False)
            
            # *obj4_t4* updates
            
            # if obj4_t4 is starting this frame...
            if obj4_t4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                obj4_t4.frameNStart = frameN  # exact frame index
                obj4_t4.tStart = t  # local t and not account for scr refresh
                obj4_t4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(obj4_t4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'obj4_t4.started')
                # update status
                obj4_t4.status = STARTED
                obj4_t4.setAutoDraw(True)
            
            # if obj4_t4 is active this frame...
            if obj4_t4.status == STARTED:
                # update params
                pass
            
            # if obj4_t4 is stopping this frame...
            if obj4_t4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > obj4_t4.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    obj4_t4.tStop = t  # not accounting for scr refresh
                    obj4_t4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'obj4_t4.stopped')
                    # update status
                    obj4_t4.status = FINISHED
                    obj4_t4.setAutoDraw(False)
            
            # *obj5_t4* updates
            
            # if obj5_t4 is starting this frame...
            if obj5_t4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                obj5_t4.frameNStart = frameN  # exact frame index
                obj5_t4.tStart = t  # local t and not account for scr refresh
                obj5_t4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(obj5_t4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'obj5_t4.started')
                # update status
                obj5_t4.status = STARTED
                obj5_t4.setAutoDraw(True)
            
            # if obj5_t4 is active this frame...
            if obj5_t4.status == STARTED:
                # update params
                pass
            
            # if obj5_t4 is stopping this frame...
            if obj5_t4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > obj5_t4.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    obj5_t4.tStop = t  # not accounting for scr refresh
                    obj5_t4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'obj5_t4.stopped')
                    # update status
                    obj5_t4.status = FINISHED
                    obj5_t4.setAutoDraw(False)
            
            # *obj6_t4* updates
            
            # if obj6_t4 is starting this frame...
            if obj6_t4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                obj6_t4.frameNStart = frameN  # exact frame index
                obj6_t4.tStart = t  # local t and not account for scr refresh
                obj6_t4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(obj6_t4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'obj6_t4.started')
                # update status
                obj6_t4.status = STARTED
                obj6_t4.setAutoDraw(True)
            
            # if obj6_t4 is active this frame...
            if obj6_t4.status == STARTED:
                # update params
                pass
            
            # if obj6_t4 is stopping this frame...
            if obj6_t4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > obj6_t4.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    obj6_t4.tStop = t  # not accounting for scr refresh
                    obj6_t4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'obj6_t4.stopped')
                    # update status
                    obj6_t4.status = FINISHED
                    obj6_t4.setAutoDraw(False)
            
            # *obj7_t4* updates
            
            # if obj7_t4 is starting this frame...
            if obj7_t4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                obj7_t4.frameNStart = frameN  # exact frame index
                obj7_t4.tStart = t  # local t and not account for scr refresh
                obj7_t4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(obj7_t4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'obj7_t4.started')
                # update status
                obj7_t4.status = STARTED
                obj7_t4.setAutoDraw(True)
            
            # if obj7_t4 is active this frame...
            if obj7_t4.status == STARTED:
                # update params
                pass
            
            # if obj7_t4 is stopping this frame...
            if obj7_t4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > obj7_t4.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    obj7_t4.tStop = t  # not accounting for scr refresh
                    obj7_t4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'obj7_t4.stopped')
                    # update status
                    obj7_t4.status = FINISHED
                    obj7_t4.setAutoDraw(False)
            
            # *obj8_t4* updates
            
            # if obj8_t4 is starting this frame...
            if obj8_t4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                obj8_t4.frameNStart = frameN  # exact frame index
                obj8_t4.tStart = t  # local t and not account for scr refresh
                obj8_t4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(obj8_t4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'obj8_t4.started')
                # update status
                obj8_t4.status = STARTED
                obj8_t4.setAutoDraw(True)
            
            # if obj8_t4 is active this frame...
            if obj8_t4.status == STARTED:
                # update params
                pass
            
            # if obj8_t4 is stopping this frame...
            if obj8_t4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > obj8_t4.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    obj8_t4.tStop = t  # not accounting for scr refresh
                    obj8_t4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'obj8_t4.stopped')
                    # update status
                    obj8_t4.status = FINISHED
                    obj8_t4.setAutoDraw(False)
            
            # *obj9_t4* updates
            
            # if obj9_t4 is starting this frame...
            if obj9_t4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                obj9_t4.frameNStart = frameN  # exact frame index
                obj9_t4.tStart = t  # local t and not account for scr refresh
                obj9_t4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(obj9_t4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'obj9_t4.started')
                # update status
                obj9_t4.status = STARTED
                obj9_t4.setAutoDraw(True)
            
            # if obj9_t4 is active this frame...
            if obj9_t4.status == STARTED:
                # update params
                pass
            
            # if obj9_t4 is stopping this frame...
            if obj9_t4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > obj9_t4.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    obj9_t4.tStop = t  # not accounting for scr refresh
                    obj9_t4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'obj9_t4.stopped')
                    # update status
                    obj9_t4.status = FINISHED
                    obj9_t4.setAutoDraw(False)
            
            # if sound_1 is starting this frame...
            if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sound_1.frameNStart = frameN  # exact frame index
                sound_1.tStart = t  # local t and not account for scr refresh
                sound_1.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('sound_1.started', tThisFlipGlobal)
                # update status
                sound_1.status = STARTED
                sound_1.play(when=win)  # sync with win flip
            
            # if sound_1 is stopping this frame...
            if sound_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_1.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_1.tStop = t  # not accounting for scr refresh
                    sound_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sound_1.stopped')
                    # update status
                    sound_1.status = FINISHED
                    sound_1.stop()
            # update sound_1 status according to whether it's playing
            if sound_1.isPlaying:
                sound_1.status = STARTED
            elif sound_1.isFinished:
                sound_1.status = FINISHED
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Test_4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Test_4" ---
        for thisComponent in Test_4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Test_4.stopped', globalClock.getTime())
        sound_1.pause()  # ensure sound has stopped at end of Routine
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 10.0 repeats of 'trials_4'
    
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
