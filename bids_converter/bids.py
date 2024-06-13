import os
import json
from pathlib import Path
import pandas as pd
import numpy as np


def walk_bids_root(root_dir, extensions=None):
    """
    This function loops through a nested bids directory and returns every single file within it alongside its actual
    directory. For each file, it parses each relevant BIDS fields to generate sidecars json files
    :param root_dir:
    :param extensions:
    :return:
    """
    if extensions is None:
        extensions = [".tsv"]
    files_infos = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if 'events' in filename and 'beh' in dirpath:
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


def create_participants_tsv(bids_root, beh_events_tsvs, verbose=True, overwrite=False):
    """
    This files creates the participants tsv at the root of the bids directory
    :param bids_root:
    :param beh_events_tsvs:
    :param verbose:
    :param overwrite:
    :return:
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
    This file creates the participants json based on the participants tsv file
    :param bids_root:
    :param participants_tsv:
    :param verbose:
    :param overwrite:
    :return:
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
    This function creates the template dataset_description.json from the bids conventions and saves it to file.
    It does not populate this file however
    :param bids_root:
    :param verbose:
    :param overwrite:
    :return:
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
