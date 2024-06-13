import json
from pathlib import Path
import os as os
import pandas as pd
import numpy as np


def walk_bids_root(root_dir, data_type="beh", extension=None):
    """
    Traverse a nested BIDS directory and return all relevant files with their metadata.

    This function navigates through the specified BIDS (Brain Imaging Data Structure) directory, identifying files with
    specified extensions (defaulting to .tsv) in directories containing the specified data type (default is 'beh').
    It extracts relevant BIDS fields from each filename to facilitate the generation of sidecar JSON files.

    Args:
        root_dir (str): The root directory of the BIDS dataset to traverse.
        data_type (str, optional): The data type directory to search within (default is "beh").
        extension (str): File extensions to include (default is [".tsv"]).

    Returns:
        list: A list of dictionaries, each containing information about a relevant file, including its path, filename,
        and BIDS fields (subject, session, run, task).

    Example usage:
        files_infos = walk_bids_root('/path/to/bids_dataset')

    Example output:
        [
            {
                "file_path": "/path/to/bids_dataset/sub-01/ses-01/beh",
                "fname": "sub-01_ses-01_run-01_task-test_events.tsv",
                "subject": "sub-01",
                "session": "ses-01",
                "run": "run-01",
                "task": "task-test"
            },
            ...
        ]
    """
    if extension is None:
        extension = ["tsv"]
    files_infos = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if 'events' in filename and data_type in dirpath and filename.endswith(extension):
                # Extract details from the filename
                parts = filename.split('_')
                # Get all the parts of that file:
                bids_path = {
                    "file_path": dirpath,
                    "fname": filename,
                    "subject": parts[0],
                    "session": parts[1],
                    "run": parts[2],
                    "task": parts[3]
                }
                files_infos.append(bids_path)

    return files_infos


def create_beh_events_sidecar(beh_events_tsvs, task_description: dict, events_col_description: dict,
                              verbose=True, overwrite=False):
    """
    Create JSON sidecar files for behavioral events TSV files following BIDS conventions.

    This function generates sidecar JSON files for each behavioral events TSV file, incorporating task descriptions and
    column metadata as specified in the BIDS (Brain Imaging Data Structure) standards.

    Args:
        beh_events_tsvs (list of dict): List of dictionaries, each containing information about an events file,
        including "task", "file_path", and "fname".
        task_description (dict): A dictionary containing descriptions for each task found within this dataset.
        events_col_description (dict): A dictionary containing metadata for each column in the log files associated
        with each task in this dataset.
        verbose (bool, optional): If True, print progress and status messages. Default is True.
        overwrite (bool, optional): If True, overwrite existing sidecar JSON files if they exist. Default is False.

    Returns:
        list: The original list of behavioral events TSV file information.

    Notes:
        - The function ensures that each task described in the TSV files is present in the task_description and
        events_col_description dictionaries.
        - If the sidecar file already exists and overwrite is set to False, a warning message will be printed
        (if verbose is True).
        - The JSON sidecar files include task descriptions and metadata for each column.

    Example usage:
        create_beh_events_sidecar(beh_events_tsvs, task_description, events_col_description)
    """
    # Loop through each file to save the corresponding json sidecar:
    for f in beh_events_tsvs:
        # Get the task of the current file
        task = f["task"].split('-')[1]
        assert task in list(task_description.keys()), "The task-{} does not exist in the task_description dictionary!"
        assert task in list(events_col_description.keys()), ("The task-{} does not exist in the events_col_description"
                                                             " dictionary!")
        # Combine the task description and the metadata for the column:
        json_sidecar = {"task": task_description[task], **events_col_description[task]}
        # Create the json sidecar file:
        sidecar_file = Path(f["file_path"], f["fname"].split('.')[0] + ".json")
        if os.path.isfile(sidecar_file) and not overwrite:
            if verbose:
                print("=" * 40)
                print("WARNING: The file {} already exists. If you want to overwrite it, set overwrite to true!"
                      .format(sidecar_file))
        else:
            if verbose:
                print("=" * 40)
                print("Saving {}".format(sidecar_file))
            with open(sidecar_file, 'w') as fl:
                json.dump(json_sidecar, fl, indent=2)

    return beh_events_tsvs


def create_participants_tsv(bids_root, beh_events_tsvs, verbose=True, overwrite=False):
    """
    Create a participants.tsv file at the root of the BIDS directory.

    This function generates a participants.tsv file, listing all subjects found in the behavioral events TSV files.
    It initializes columns for participant ID, age, and sex, with age and sex set to NaN.

    Args:
        bids_root (str): The root directory of the BIDS dataset.
        beh_events_tsvs (list): A list of dictionaries containing behavioral events information, each with a "subject"
        key.
        verbose (bool, optional): If True, print progress and status messages. Default is True.
        overwrite (bool, optional): If True, overwrite the existing participants.tsv file if it exists. Default is
        False.

    Returns:
        pandas.DataFrame: The created participants.tsv as a pandas DataFrame.

    Notes:
        - The function extracts unique subject IDs from the behavioral events TSV files.
        - If the file already exists and overwrite is set to False, a warning message will be printed (if verbose is
        True).
        - The age and sex columns are initialized with NaN values, and the user should update these fields with actual
        data.

    Example usage:
        create_participants_tsv('/path/to/bids_dataset', beh_events_tsvs)
    """
    if verbose:
        print("=" * 40)
        print("Create the participants tsv file")
    # Extract all subjects found within the data set:
    subjects_list = list(set([fl["subject"] for fl in beh_events_tsvs]))

    # Create pandas data frame:
    participants_tsv = pd.DataFrame({
        "participant_id": subjects_list,
        "age": [np.nan] * len(subjects_list),
        "sex": [np.nan] * len(subjects_list)
    })
    participants_tsv_file = Path(bids_root, "participants.tsv")
    # Save to file:
    if os.path.isfile(participants_tsv_file) and not overwrite:
        if verbose:
            print("=" * 40)
            print("WARNING: The file {} already exists. If you want to overwrite it, set overwrite to true!"
                  .format(participants_tsv_file))
    else:
        if verbose:
            print("=" * 40)
            print("Saving {}".format(participants_tsv_file))
        participants_tsv.to_csv(participants_tsv_file, sep="\t")
    return participants_tsv


def create_participants_json(bids_root, participants_tsv, verbose=True, overwrite=False):
    """
    Create a participants.json file based on the columns present in the participants.tsv file.

    This function generates a participants.json file with descriptions for each column in the participants.tsv file,
    following BIDS (Brain Imaging Data Structure) standards. The file is saved in the specified BIDS root directory.

    Args:
        bids_root (str): The root directory of the BIDS dataset.
        participants_tsv (pandas.DataFrame): The participants.tsv file loaded as a pandas DataFrame.
        verbose (bool, optional): If True, print progress and status messages. Default is True.
        overwrite (bool, optional): If True, overwrite the existing participants.json file if it exists. Default is
        False.

    Returns:
        None

    Notes:
        - The function provides predefined descriptions for the "age" and "sex" columns.
        - For any additional columns in the participants.tsv, the function adds a placeholder description, which the
        user should manually update.
        - If the file already exists and overwrite is set to False, a warning message will be printed (if verbose is
        True).

    Example usage:
        create_participants_json('/path/to/bids_dataset', participants_tsv)
    """
    # Prepare the participants json:
    participants_json = {}
    json_file_name = Path(bids_root, "participants.json")

    # Extract the column:
    cols = list(participants_tsv.columns)

    # Loop through each of the column
    for col in cols:
        if col == "age":
            col_dict = {
                "age": {
                    "Description": "Age of the participant",
                    "Units": "years"
                }
            }
            participants_json.update(col_dict)
        elif col == "sex":
            col_dict = {
                "sex": {
                    "Description": "sex of the participant as reported by the participant",
                    "Levels": {
                        "m": "male",
                        "f": "female"
                    }
                }
            }
            participants_json.update(col_dict)
        else:
            print("WARNING: You have added extra column in your participants.tsv file. ")
            print("Make sure to describe the added column under:")
            print(json_file_name)
            col_dict = {
                col: {
                    "Description": "",
                    "Levels": {
                    },
                    "Units": ""
                }
            }
            participants_json.update(col_dict)
    # Save the dict:
    # Save to file:
    if os.path.isfile(json_file_name) and not overwrite:
        if verbose:
            print("=" * 40)
            print("WARNING: The file {} already exists. If you want to overwrite it, set overwrite to true!"
                  .format(json_file_name))
    else:
        if verbose:
            print("=" * 40)
            print("Saving {}".format(json_file_name))
        with open(json_file_name, 'w') as fl:
            json.dump(participants_json, fl, indent=2)


def create_dataset_desc_json(bids_root, verbose=True, overwrite=False):
    """
    Create a template dataset_description.json file in accordance with BIDS conventions.

    This function generates a dataset_description.json file with a predefined structure based on BIDS (Brain Imaging
    Data Structure) standards. The file is saved in the specified BIDS root directory. The function does not populate
    the fields, leaving them for the user to fill in.

    Args:
        bids_root (str): The root directory of the BIDS dataset.
        verbose (bool, optional): If True, print progress and status messages. Default is True.
        overwrite (bool, optional): If True, overwrite the existing dataset_description.json file if it exists.
        Default is False.

    Returns:
        None

    Notes:
        - The generated JSON file will include placeholders for various metadata fields, such as the dataset name,
        authors, funding sources, etc.
        - If the file already exists and overwrite is set to False, a warning message will be printed
        (if verbose is True).

    Example usage:
        create_dataset_desc_json('/path/to/bids_dataset')
    """
    # Create file name:
    json_file_name = Path(bids_root, 'dataset_description.json')

    # Pre-allocate dictionary:
    dataset_desc = {
        "Name": "",
        "BIDSVersion": "1.9.0",
        "DatasetType": "raw",
        "License": "",
        "Authors": [
            "",
            ""
        ],
        "Acknowledgements": "",
        "HowToAcknowledge": "",
        "Funding": [
            "",
            ""
        ],
        "EthicsApprovals": [
            ""
        ],
        "ReferencesAndLinks": [
            "",
            ""
        ],
        "DatasetDOI": "",
        "HEDVersion": "",
        "SourceDatasets": [
            {
                "URL": "s3://dicoms/studies/correlates",
                "Version": "April 11 2011"
            }
        ]
    }

    # Save to file:
    if os.path.isfile(json_file_name) and not overwrite:
        if verbose:
            print("=" * 40)
            print("WARNING: The file {} already exists. If you want to overwrite it, set overwrite to true!"
                  .format(json_file_name))
    else:
        if verbose:
            print("=" * 40)
            print("Saving {}".format(json_file_name))
        with open(json_file_name, 'w') as fl:
            json.dump(dataset_desc, fl, indent=2)


def create_readme(bids_root, verbose=True, overwrite=False):
    """
    This function creates the template README.md from the bids conventions and saves it to file.
    It does not populate this file however!
    :param bids_root:
    :param verbose:
    :param overwrite:
    :return:
    """
    readme_file = Path(bids_root, "README.md")

    # Write a template readme:
    markdown_content = "#Write an extensive description of your experiment!\n\n"
    markdown_content += "Here are a few nice readmes examples: \n\n"
    markdown_content += "- https://github.com/bids-standard/bids-starter-kit/blob/main/templates/README.MD"

    # Save to file:
    if os.path.isfile(readme_file) and not overwrite:
        if verbose:
            print("=" * 40)
            print("WARNING: The file {} already exists. If you want to overwrite it, set overwrite to true!"
                  .format(readme_file))
    else:
        if verbose:
            print("=" * 40)
            print("Saving {}".format(readme_file))
        with open(readme_file, 'w') as fl:
            fl.write(markdown_content)
