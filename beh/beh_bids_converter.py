import environment_variables as ev
from beh import task_desc_prp, logs_metadata_prp
from beh.helper_function import (walk_bids_root, create_participants_json, create_participants_tsv,
                                 create_beh_events_sidecar, create_readme, create_dataset_desc_json)


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
    # Load the text information from files:
    task_desc = task_desc_prp.tasks_descriptions
    log_desc = logs_metadata_prp.logs_column_descriptions
    # Create the bids metadata:
    beh_bids_metadata(ev.bids_root, task_desc, log_desc, verbose=True, overwrite=False)

