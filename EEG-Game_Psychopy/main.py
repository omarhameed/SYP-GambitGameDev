import EEG_Experiment as eeg_exp

def RunExperiment():
    expInfo = eeg_exp.expInfo  # Direct reference to the expInfo from EEG_Experiment module

    expInfo = eeg_exp.showExpInfoDlg(expInfo=expInfo)
    thisExp = eeg_exp.setupData(expInfo=expInfo)
    logFile = eeg_exp.setupLogging(filename=thisExp.dataFileName)
    win = eeg_exp.setupWindow(expInfo=expInfo)
    inputs = eeg_exp.setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    eeg_exp.run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    eeg_exp.saveData(thisExp=thisExp)
    eeg_exp.quit(thisExp=thisExp, win=win, inputs=inputs)

RunExperiment()
