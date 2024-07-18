import environment_variables as ev
from beh import task_desc_prp, logs_metadata_prp
from beh.helper_function import (walk_bids_root, create_participants_json, create_participants_tsv,
                                 create_beh_events_sidecar, create_readme, create_dataset_desc_json)


def beh_bids_metadata(bids_root, task_descriptions: dict, logs_descriptions: dict, verbose=True, overwrite=False):
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

    Steps:
        1. List all the event files in the specified BIDS directory.
        2. For each event file, create a corresponding sidecar JSON file describing each column.
        3. Create a participants TSV file listing all participants included in the dataset.
        4. Create a participants JSON file to describe the columns of the participants TSV.
        5. Generate a dataset description JSON file providing metadata about the dataset.
        6. Create a README.md file with a summary and description of the dataset.

    Example usage:
        beh_bids_metadata('/path/to/bids_dataset', task_descriptions, logs_descriptions)
    """

    # 1. List all the events files in the directory:
    evts_files = walk_bids_root(bids_root, data_type="beh")

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
    # Load the text information from files:
    task_desc = task_desc_prp.tasks_descriptions
    log_desc = logs_metadata_prp.logs_column_descriptions
    # Create the bids metadata:
    beh_bids_metadata(ev.bids_root, task_desc, log_desc, verbose=True, overwrite=False)
