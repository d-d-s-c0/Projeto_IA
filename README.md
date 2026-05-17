<center><h1 style="margin-bottom: 0px;">Artificial Intelligence (25/26)</h1></center>
<center><h2 style="margin-top: 0px;">Pop Out Gamen </h2></center>

#### <center> Joana Antunes (202405702), Sílvia Pinto (202405988) </center> <br>

#### **Introduction** <br>
<div style="text-align: justify;"><p style="text-indent: 2em;">POP OUT is an adaptation of the well-known game Connect 4. The main change between these two games is that, in Pop Out, it is possible to remove discs from the bottom row, as well as inserting them. There are three modes:</div>

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Player VS Player** *allows two players to take turns in placing their disks, facing eachother in a match;*

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Player VS Computer** *allows one player to play against the computer, trained with various search algorithms;*

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Computer VS Computer** *shows us the results of the computer playing for both opponents in a match.* 

#### **Installation Guide** <br>
<div style="text-align: justify;"><p style="text-indent: 2em;">To install Python in Windows,</div>

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1.** *Download: https://www.python.org/downloads/*

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2.** *Select "Add Python to PATH"*

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**3.** *Verify installation: python --version*

<div style="text-align: justify;"><p style="text-indent: 2em;">To install Python in Linux,</div>

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1.** *sudo apt update*

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2.** *sudo apt install python3*

<div style="text-align: justify;"><p style="text-indent: 2em;">To install Python in MacOs,</div>

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1.** *brew install python*

<div style="text-align: justify;"><p style="text-indent: 2em;">The following libraries should also be installed: copy, math, random, collections, pandas, numpy, seaborn, matplotlib, multiprocessing, csv. </div>
<div style="text-align: justify;"><p style="text-indent: 2em;">This repository contains Python code stored in `.ipynb` files, which are Jupyter Notebooks. To set up your environment and run these files, it is recommended to use VS Code, which has excellent, built-in support for Jupyter Notebooks.</div>

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1. Install VS Code** *Download and install [VS Code](https://code.visualstudio.com/)*

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2. Install Extensions** *Open VS Code, go to the Extensions tab (`Ctrl+Shift+X` or `Cmd+Shift+X`), and install both Python and Jupyter extensions, by Microsoft.*

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**3. Open the File** *Open your project folder in VS Code and click on the `.ipynb` file.*

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**4. Select a Kernel** *In the top-right corner of the notebook, click Select Kernel and choose your Python environment.*

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**5. Run Cells** *Click the Play button next to an individual cell to run it, or click Run All at the top.*

<div style="text-align: justify;"><p style="text-indent: 2em;">If you don't want to install anything locally, you can run the notebook in your browser using Google Colab.</div>

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1.** *Go to [Google Colab](https://colab.research.google.com/).*

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2.** *Click on the Upload tab.*

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**3.** *Drag and drop your `.ipynb` file.*

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**4.** *Click Connect in the top-right corner to allocate cloud resources.*

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**5.** *Run cells using the Play button on the left of each cell, or press `Shift + Enter`.*

> **Note:** If the notebook requires external datasets, you will need to upload them to your Colab session or mount your Google Drive.

<div style="text-align: justify;"><p style="text-indent: 2em;">If you prefer working in a web browser locally via the command line, you can install Jupyter directly. Make sure you have Python installed. Then, open your terminal (macOS/Linux) or Command Prompt (Windows) and install Jupyter with the command "pip install jupyterlab" or "pip install notebook".</div>

#### **Execution Guide** <br>
<div style="text-align: justify;"><p style="text-indent: 2em;">The game can be initialized by executing the command</div>
<div style="text-align: center;">ipython -c "%run PLAY.ipynb"</div>
<div style="text-align: justify;">in the terminal. There, by interacting with text menus through the terminal, all of the game's features will be accessible, as well as the rules and commands. . </div>

#### **Code Architecture** <br>
<div style="text-align: justify;"><p style="text-indent: 2em;">The notebooks should be read and executed in the following order:</div>

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AuxiliarFunctions.ipynb** *contains terminal interface functions and game mode helpers.*

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PopOut.ipynb** *contains the `Pop_Out` class.*

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MCTS.ipynb** *defines the Monte Carlo algorithms.*

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DecisionTrees.ipynb** *defines the Decision Trees with ID3 procedure algorithm.*

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IRIS.ipynb** *applies Decision Trees to iris.csv to create predictions.*

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PopOutDataset.ipynb** *generates the dataset for the Pop Out game.*

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MAIN.ipynb** *contains terminal menu and allows to play the game.*

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Model Comparisons.ipynb** *final performance analysis of our search models.*

