import datetime
import pathlib
import sys
import time

from file_IO_handler import save_json
from openai_handler import OpenAIModelSettings, call_openai_api


def save_simulation_result_to_unique_location(
        res: dict,
        save_folder: pathlib.Path
) -> None:
    datetimeStr = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
    experiment_descriptor = res["input"]["experiment_descriptor"]
    prompt_descriptor = res["input"]["prompt_descriptor"]
    params_descriptor = res["model"]["params_descriptor"]
    engine = res["model"]["engine"]
    prompt_index = res["input"]["index"]

    save_string = save_folder.joinpath(
        f"{datetimeStr}_experiment_{experiment_descriptor}_prompt_{prompt_descriptor}_params_{params_descriptor}_engine_{engine}_promptindex_{prompt_index}.json"
    )
    save_json(obj=res, filename=save_string)
    print("\ninput, output, and model params saved to: ", save_string)
    return None


def run_single_simulation(
        prompt: str,
        model_settings: OpenAIModelSettings,
        seconds_to_sleep_before_query: int = 2,
        seconds_to_sleep_after_failed_query: int = 60,
        max_attempts: int = 3
) -> dict | None:
    for attempt_count in range(max_attempts):
        time.sleep(seconds_to_sleep_before_query)
        try:
            return call_openai_api(prompt, model_settings)
        except Exception:
            print("Exception occured:", sys.exc_info())
            print(f"Try again in {seconds_to_sleep_after_failed_query} seconds, attempt {attempt_count}")
            time.sleep(seconds_to_sleep_after_failed_query)

    return None
