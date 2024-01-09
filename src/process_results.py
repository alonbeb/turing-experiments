import datetime
import math
import pathlib
from collections import defaultdict

import pandas as pd
from tqdm import tqdm

from file_IO_handler import load_json, save_json


def consolidate_jsons_to_mega_json(
        open_folder: pathlib.Path,
        save_file_path: pathlib.Path
) -> int:
    mega = []
    list_of_data_files = open_folder.glob("**/*.json")

    print(f"Got {len(list_of_data_files)} in folder {open_folder}")

    for data_file in list_of_data_files:
        file_contents = load_json(data_file)
        mega.append(file_contents)

    print("Started saving at: ", str(datetime.datetime.now()))
    save_json(mega, save_file_path)
    print("Started saving at: ", str(datetime.datetime.now()))
    return len(list_of_data_files)


def process_mega_json_for_no_complete_prompt(
        path_to_megajson: pathlib.Path,
        completion_is_last_n_tokens_of_echoed_prompt: int,
        filter_by_prompt_descriptor: None | str = None
):
    results = defaultdict(list)

    mega = load_json(filename=path_to_megajson)
    print(f"Found {len(mega)} items in mega .json.gz")

    for res in tqdm(mega):
        if filter_by_prompt_descriptor is None or res["input"]["prompt_descriptor"] == filter_by_prompt_descriptor:
            results["index"].append(res["input"]["index"])
            results["engine"].append(res["model"]["engine"])

            choice = res["output"]["choices"][0]
            res["output"]["echo_logprobs"] = choice["logprobs"]

            tokens_list = []
            logprob_sum = 0
            tokens = res["output"]["echo_logprobs"]["tokens"]
            token_logprobs = res["output"]["echo_logprobs"]["token_logprobs"]
            for i in range(1, completion_is_last_n_tokens_of_echoed_prompt + 1):
                tokens_list.append(tokens[-i])
                logprob_sum += token_logprobs[-i]
            tokens_list.reverse()
            results["tokens"].append("-".join(tokens_list).strip())
            results["probability"].append(math.exp(logprob_sum))

    df_results = pd.DataFrame(results)

    return df_results
