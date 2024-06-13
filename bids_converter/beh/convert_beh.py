import os
import json
from pathlib import Path
from ..bids import create_participants_tsv, create_participants_json, create_dataset_desc_json, create_readme, walk_bids_root   

def create_beh_events_sidecar(beh_events_tsvs, task_description, events_col_description,
                              verbose=True, overwrite=False):
    """
    This function creates side car files for the behavioral events tsv files according to the BIDS conventions.
    :param beh_events_tsvs: (list of path) List of all events files found within the bids directory
    :param task_description: (dict) contains the description of each task found within this data set
    :param events_col_description: (dict) contains the metadata for each column in the log files associated with each
    task in this data set
    :param verbose: (boolean)
    :param overwrite:
    :return: beh_events_tsvs: the list
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

def beh_bids_metadata(bids_root, task_descriptions, logs_descriptions, verbose=True, overwrite=False):
    """

    :param bids_root:
    :param task_descriptions:
    :param logs_descriptions:
    :param verbose:
    :param overwrite:
    :return:
    """
    # 1. List all the events files in the directory:
    evts_files = walk_bids_root(bids_root)

    # 2. For each events file, create the events sidecar, describing each column:
    create_beh_events_sidecar(evts_files, task_descriptions, logs_descriptions,
                              verbose=verbose, overwrite=overwrite)

    # 3. Create the participants tsv:
    participants_tsv = create_participants_tsv(bids_root, evts_files, verbose=verbose, overwrite=overwrite)

    # 4. Create the participants json file:
    create_participants_json(bids_root, participants_tsv, verbose=verbose, overwrite=overwrite)

    # 5. Create the dataset_description.json:
    create_dataset_desc_json(bids_root, verbose=verbose, overwrite=overwrite)

    # 6. Create the README.md:
    create_readme(bids_root, verbose=verbose, overwrite=overwrite)

    print("Done!")
    return None


if __name__ == "__main__":
    from ..example_var import task_desc_prp, logs_metadata_prp, ev
    # Load the text information from files:
    task_desc = task_desc_prp.tasks_descriptions
    log_desc = logs_metadata_prp.logs_column_descriptions
    # Create the bids metadata:
    beh_bids_metadata(ev.bids_root, task_desc, log_desc, verbose=True, overwrite=False)

