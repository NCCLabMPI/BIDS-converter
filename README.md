# BIDS-converter
This repository contains custom scripts from the NCC lab to convert data to brain imaging data standards (BIDS). This is the standard for data storage and documentation in our lab (as well as in many other places)
and it makes data sharing easier. In our lab, we recommend everyone to convert everyting to BIDS right after they collected their data. That way, any analysis pipeline that is designed in our lab is inter-operable, 
i.e. it can be applied to all other data sets without too much effort.

This is an ongoing effort, as the BIDS specification are also evolving. Our aim is to provide converters for any data that 
we collect in our lab, which encompasses behavioral data, MEG, EEG, iEEG and fMRI. We also collect eyetracking data, but there
are as of yet no finalized BIDS standard for that data.

## Install:
- Option 1: Go to https://github.com/NCCLabMPI/BIDS-converter and download the data
- Option 2: Install the repository as a package:
```
conda install git
conda install pip
pip install git+git://github.com/NCCLabMPI/BIDS-converter.git
```

## beh module:

### Prepare the data:
This module creates all the files required by BIDS in case you ran a behavioral (beh) study. For that type of data,
the requirements (described [here](https://bids-specification.readthedocs.io/en/stable/modality-specific-files/behavioral-experiments.html))
are simple. As is the case for any data in bids, the data should be organized in sub-folders:
```
bids_root/
    sub-<label>/
        [ses-<labels>]/
            beh/
```
In other words, each subject's data should be stored in a subfolder. If your recordings were obtained throughout different
sessions, you should have an extra sub-directory to store the data of each session separately. Finally, you should at the lowest
level have a folder called beh, to specify that behavioral data are stored in there. 

Within the beh folder, the files storing the behavioral data (i.e. the log files) should follow the standard bids conventions:
```
sub-<label>[_ses-<label>]_task-<label>[_acq-<label>][_run-<index>]_beh.tsv
```
In other words, each file should be identify by the subject it belongs to, the session it was recorded in, the task
that was conducted by the participants (and optionally the acquisition label and run if applicable).

For the BIDS conversion of behavioral data, you need to make sure that your data are organized that way first. Ideally,
your experiment should have programmed such that it outputs the data with that structure. If it does not, we recommend writing
a script that organizes that accordingly. Unfortunately, there is no straight forward way to write a standard script to do so, 
due to the high degree of freedom of each researcher to write the experimental data to file.

### Create the metadata:
Our bids converter for behavioral data creates all the metadata that are required by BIDS. To put it simply, there
are basically 2 things you need to document: 
- Describe your task: In plain words, describe the set of tasks that were used in your experiment. Think of what you would write in your method section
- Describe your log file columns: each task is different and therefore, each log file is too. The log file stores all the information necessary to analyze the data down the line. Our converters assume that the log files are tables with 1 row per trial and 1 column per variable of interest. As the variable of interest is different for each task, it is crucial clearly document what exactly each column stores. 

You should create two dictionaries storing for each task in your data set the task description and the description of the log file columns. Following the bids convention, this should look like so:
```
tasks_descriptions = {
    "TASK1NAME: "Participants were presented with two conscecutive tasks. The first (T1) consisted of visual stimuli of "
           "4 different categories (faces, objects, letters and symbols) being presented in 3 different orientations "
           "(center, left and right) for 3 different durations (0.5, 1.0 and 1.5s) one after another (interrupted by "
           "blank screen). In the beginning of each block, participants were presented with 2 targets (a specific face "
           "and object or letter and symbol) which they had to detect among the stimuli by pressing a button and remain"
           "passive otherwise (target detection task). Stimuli of the same category as the targets are task relevant"
           "and stimuli of a different category are task irrelevant. For the second task (T2), high and low pitch tone "
           "were presented on every single trial at various SOA (0, 0.116, 0.232, 0.466) from visual stimuli onset or "
           "offset of the visual stimuli which they had to discriminate between (2AFC).",
    "TASK2NAME: "...",
    }
logs_column_descriptions = {
    "TASK1NAME": {
        "trial": {
            "LongName": "Trial number",
            "Description": "Number of the current trial",
        },
        "task": {
            "LongName": "Task",
            "Description": "Task this log file corresponds to",
            "Levels": {
                "prp": "prp task"
            }

        },
    "TASK2NAME": {
        "trial": {
            "LongName": "Trial number",
            "Description": "Number of the current trial",
        },
        "task": {
            "LongName": "Task",
            "Description": "Task this log file corresponds to",
            "Levels": {
                "prp": "prp task"
            }

        },
    ...
    }
```
These are just examples. But basically, for each task you ran, you should have the descriptions stored in the first
dictionary. For the log file specific to each task, you should have each column described in the second dictionary.

Based on this information, our pipeline will find each behavioral log file stored in your bids directory and create the metadata 
according to the BIDS specification. In addition, our script will create the modality agnostic files. These are required by
bids and are stored at the level of the bids roots. Here is the list of what's necessary:
- `data_description.json`
- `README.md`
- `participants.json`
- `participants.tsv`

These will also be created based on what is documented in the files above. Once we know which files are in the 
bids directory, we also know all participants names, we also know which tasks are relevant to this particular data set... So these files
can be created programatically. There are a few additional info we can't get though. To make sure your doc is complete,
you will need to go to these files and edit them to fill in the gaps. 

In summary, the bids conversion can be executed in 6 steps:
```
from beh.helper_function import (walk_bids_root, create_participants_json, create_participants_tsv,
                                 create_beh_events_sidecar, create_readme, create_dataset_desc_json)
# 1. List all the events files in the directory:
evts_files = walk_bids_root(bids_root)

# 2. For each events file, create the events sidecar, describing each column:
create_beh_events_sidecar(evts_files, task_descriptions, logs_descriptions,
                          verbose=verbose, overwrite=overwrite)
                          
# 3. Create the participants.tsv:
participants_tsv = create_participants_tsv(bids_root, evts_files, verbose=verbose, overwrite=overwrite)

# 4. Create the participants.tsv:
create_participants_json(bids_root, evts_files, verbose=verbose, overwrite=overwrite)

# 5. Create the dataset_description.json:
create_participants_tsv(bids_root, verbose=verbose, overwrite=overwrite)

# 6. Create the README.md:
create_dataset_desc_json(bids_root, verbose=verbose, overwrite=overwrite)
```


