import json
from pathlib import Path
import os
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
        extension (str): File extensions to include (default is ".tsv").

    Returns:
        list: A list of dictionaries, each containing information about a relevant file, including its path, filename,
        and BIDS fields (subject, session, run, task).

    Example usage:
        files_infos = walk_bids_root('/path/to/bids_dataset')
    """
    if extension is None:
        extension = ".tsv"
    files_infos = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if 'events' in filename and data_type in dirpath and filename.endswith(extension):
                parts = filename.split('_')
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


def create_beh_events_sidecar(beh_events_tsvs, task_description, events_col_description, verbose=True, overwrite=False):
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

    Example usage:
        create_beh_events_sidecar(beh_events_tsvs, task_description, events_col_description)
    """
    for f in beh_events_tsvs:
        task = f["task"].split('-')[1]
        assert task in task_description, f"The task-{task} does not exist in the task_description dictionary!"
        assert task in events_col_description, f"The task-{task} does not exist in the events_col_description dictionary!"

        json_sidecar = {"task": task_description[task], **events_col_description[task]}
        sidecar_file = Path(f["file_path"], f["fname"].split('.')[0] + ".json")

        if os.path.isfile(sidecar_file) and not overwrite:
            if verbose:
                print("=" * 40)
                print(
                    f"WARNING: The file {sidecar_file} already exists. If you want to overwrite it, set overwrite to true!")
        else:
            if verbose:
                print("=" * 40)
                print(f"Saving {sidecar_file}")
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

    Example usage:
        create_participants_tsv('/path/to/bids_dataset', beh_events_tsvs)
    """
    if verbose:
        print("=" * 40)
        print("Create the participants.tsv file")

    subjects_list = list(set(fl["subject"] for fl in beh_events_tsvs))

    participants_tsv = pd.DataFrame({
        "participant_id": subjects_list,
        "age": [np.nan] * len(subjects_list),
        "sex": [np.nan] * len(subjects_list)
    })
    participants_tsv_file = Path(bids_root, "participants.tsv")

    if os.path.isfile(participants_tsv_file) and not overwrite:
        if verbose:
            print("=" * 40)
            print(
                f"WARNING: The file {participants_tsv_file} already exists. If you want to overwrite it, set overwrite to true!")
    else:
        if verbose:
            print("=" * 40)
            print(f"Saving {participants_tsv_file}")
        participants_tsv.to_csv(participants_tsv_file, sep="\t", index=False)

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

    Example usage:
        create_participants_json('/path/to/bids_dataset', participants_tsv)
    """
    participants_json = {}
    json_file_name = Path(bids_root, "participants.json")

    cols = list(participants_tsv.columns)

    for col in cols:
        if col == "age":
            col_dict = {
                "age": {
                    "Description": "Age of the participant",
                    "Units": "years"
                }
            }
        elif col == "sex":
            col_dict = {
                "sex": {
                    "Description": "Sex of the participant as reported by the participant",
                    "Levels": {
                        "m": "male",
                        "f": "female"
                    }
                }
            }
        else:
            if verbose:
                print(f"WARNING: You have added extra column {col} in your participants.tsv file.")
                print("Make sure to describe the added column under:")
                print(json_file_name)
            col_dict = {
                col: {
                    "Description": "",
                    "Levels": {},
                    "Units": ""
                }
            }
        participants_json.update(col_dict)

    if os.path.isfile(json_file_name) and not overwrite:
        if verbose:
            print("=" * 40)
            print(
                f"WARNING: The file {json_file_name} already exists. If you want to overwrite it, set overwrite to true!")
    else:
        if verbose:
            print("=" * 40)
            print(f"Saving {json_file_name}")
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

    Example usage:
        create_dataset_desc_json('/path/to/bids_dataset')
    """
    json_file_name = Path(bids_root, 'dataset_description.json')

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

    if os.path.isfile(json_file_name) and not overwrite:
        if verbose:
            print("=" * 40)
            print(
                f"WARNING: The file {json_file_name} already exists. If you want to overwrite it, set overwrite to true!")
    else:
        if verbose:
            print("=" * 40)
            print(f"Saving {json_file_name}")
        with open(json_file_name, 'w') as fl:
            json.dump(dataset_desc, fl, indent=2)


def create_readme(bids_root, verbose=True, overwrite=False):
    """
    Create a template README.md file in accordance with BIDS conventions.

    This function generates a README.md file with a template structure based on BIDS (Brain Imaging Data Structure) standards.
    The file is saved in the specified BIDS root directory. The function does not populate the content, leaving it for the user to fill in.

    Args:
        bids_root (str): The root directory of the BIDS dataset.
        verbose (bool, optional): If True, print progress and status messages. Default is True.
        overwrite (bool, optional): If True, overwrite the existing README.md file if it exists. Default is False.

    Returns:
        None

    Example usage:
        create_readme('/path/to/bids_dataset')
    """
    readme_file = Path(bids_root, "README.md")

    markdown_content = (
        "# Write an extensive description of your experiment!\n\n"
        "Here are a few nice README examples:\n\n"
        "- https://github.com/bids-standard/bids-starter-kit/blob/main/templates/README.MD"
    )

    if os.path.isfile(readme_file) and not overwrite:
        if verbose:
            print("=" * 40)
            print(
                f"WARNING: The file {readme_file} already exists. If you want to overwrite it, set overwrite to true!")
    else:
        if verbose:
            print("=" * 40)
            print(f"Saving {readme_file}")
        with open(readme_file, 'w') as fl:
            fl.write(markdown_content)


def beh_bids_metadata(bids_root, task_descriptions, logs_descriptions, verbose=True, overwrite=False):
    """
    Generate BIDS-compatible metadata for behavioral data in a BIDS directory structure.

    This function automates the creation of several BIDS-required metadata files, including:
    - Event files sidecar JSONs
    - Participants TSV and JSON files
    - Dataset description JSON
    - README file

    Args:
        bids_root (str): The root directory of the BIDS dataset.
        task_descriptions (dict): A dictionary containing descriptions for each task, used to create event sidecars.
        logs_descriptions (dict): A dictionary containing descriptions for log files, also used for event sidecars.
        verbose (bool, optional): If True, print progress and status messages. Default is True.
        overwrite (bool, optional): If True, overwrite existing files. Default is False.

    Returns:
        None

    Example usage:
        beh_bids_metadata('/path/to/bids_dataset', task_descriptions, logs_descriptions)
    """
    evts_files = walk_bids_root(bids_root)

    create_beh_events_sidecar(evts_files, task_descriptions, logs_descriptions, verbose=verbose, overwrite=overwrite)

    participants_tsv = create_participants_tsv(bids_root, evts_files, verbose=verbose, overwrite=overwrite)

    create_participants_json(bids_root, participants_tsv, verbose=verbose, overwrite=overwrite)

    create_dataset_desc_json(bids_root, verbose=verbose, overwrite=overwrite)

    create_readme(bids_root, verbose=verbose, overwrite=overwrite)

    print("Done!")
