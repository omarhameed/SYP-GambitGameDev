# Project Repository Overview

This repository is structured to support the development and analysis of a game or experiment involving EEG (electroencephalogram) data. It is divided into several key directories, each with a specific focus. Below is an overview of these directories and their contents.

## Data_Analysis

This directory is dedicated to the analysis of EEG data collected during gameplay. It includes Python scripts that serve various analytical functions:

- `BrainVoltageCalc.py`: Calculates brain voltage.
- `TimeDomainPlt.py`: Plots time domain data.
- `Welch_modified_periodogram.py`: Generates a modified Welch periodogram.
- `Gambit.py`: Handles the game's data analysis aspect.

Additionally, this directory contains a subdirectory (`DataCH4`) and sample data for script testing purposes.

## EEG-Experiment

Focused on conducting EEG experiments, this folder contains Python scripts and CSV data files:

- `main.py`: Likely the primary driver script, encompassing data collection or analysis.
- `flicker_data.csv`: Contains data from the experiments.
- `target.py`: Defines targets or parameters for the experiments.

The `music` subdirectory may include audio files or scripts related to the auditory aspects of the experiments.

## MindGameGUI

This directory emphasizes the graphical user interface (GUI) for the game or experiment. It includes:

- Python files (`GUI.py`, `MindGameGUI.py`) for creating and managing the GUI.
- `MindGame.ui`: A UI file for visual design, possibly with Qt Designer or similar tools.
- Project and solution files (`MindGameGUI.pyproj`, `MindGameGUI.sln`) for development with Python and Visual Studio, indicating a blend of these tools in GUI development.

## EEG-Experiment-psychopy

This new directory focuses on the implementation of EEG experiments using PsychoPy, a powerful software package for creating psychology stimuli in Python. The provided script, created with PsychoPy3 Experiment Builder (v2023.2.3), outlines a structured approach to running an EEG experiment. It includes the initialization of experiment parameters, participant information gathering, and the setup for data collection and logging. This script represents a comprehensive framework for executing behavioral experiments with EEG data collection, showcasing the integration of PsychoPy's capabilities into the project's experimental design framework.

Overall, the repository is geared towards the development of an EEG-based game or experiment, with a significant focus on data analysis, experimental setup, and user interface design.
