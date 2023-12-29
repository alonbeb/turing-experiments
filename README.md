## Requirements

1. Install necessary dependencies with conda:

```
conda env create -n turing-experiments -f environment.yml
conda activate turing-experiments
```

2. To use OpenAI's language model engines to generate responses add your api key and organization as plaintext to `openai_api_key.txt` and `openai_organization.txt` in the root directory (these are ignored by `.gitignore`).

3. To download the authors' data files, install and enable [git LFS](https://git-lfs.com/). Then download the data files using:

```
git lfs pull
```

The data files are large, so it might take several minutes (~5-10 min) for git LFS to download them from the remote server. Alternatively, the data files can be downloaded from GitHub using the "download raw files" button.

## Usage

For the _Ultimatum Game_ TE, _Garden Path_ TE, and the _Wisdom of Crowds_ TE, we provide all prompt templates and simulation result data to aid both re-running simulations or re-analyzing results.

For the _Milgram Shock_ TE we provide all prompt templates and, due to space concerns, a selection of representative result data files for both the original and alternative experiment scenarios.

- `scripts/` folder - contains jupyter notebooks and Python scripts for running and analyzing the experiments.
- `src/` folder - contains reusable modules and helper functions
- `data/` folder - contains data files
- `results/` folder - contains final analysis products, like figures

## 1. Ultimatum Game TE

[/scripts/Simulate_Ultimatum_Game_Experiment.ipynb](/scripts/Simulate_Ultimatum_Game_Experiment.ipynb) contains a notebook to run and analyze the Ultimatum Game TE. The prompt templates are given in

- [/data/prompt-templates/ultimatum_game/no-complete-accept.txt](/data/prompt-templates/ultimatum_game/no-complete-accept.txt)
- [/data/prompt-templates/ultimatum_game/no-complete-reject.txt](/data/prompt-templates/ultimatum_game/no-complete-reject.txt)

To query the OpenAI language models and generate new simulation results, uncomment "Section 4. Run Experiment".

Enable git LFS and run `git lfs pull` to see the authors' consolidated results data files in the `data/simulation_results_consolidated/ultimatum_game/` folder.

```
.
└── data
    ...
    └── simulation_results_consolidated
        └── ultimatum_game
            ├── README.md
            ├── UG_surnames_total_money_10_text-ada-001_no-complete-accept.json.gz
            ├── UG_surnames_total_money_10_text-ada-001_no-complete-reject.json.gz
            ├── UG_surnames_total_money_10_text-babbage-001_no-complete-accept.json.gz
            ├── UG_surnames_total_money_10_text-babbage-001_no-complete-reject.json.gz
            ├── UG_surnames_total_money_10_text-curie-001_no-complete-accept.json.gz
            ├── UG_surnames_total_money_10_text-curie-001_no-complete-reject.json.gz
            ├── UG_surnames_total_money_10_text-davinci-001_no-complete-accept.json.gz
            ├── UG_surnames_total_money_10_text-davinci-001_no-complete-reject.json.gz
            ├── UG_surnames_total_money_10_text-davinci-002_no-complete-accept.json.gz
            └── UG_surnames_total_money_10_text-davinci-002_no-complete-reject.json.gz
```

Then run the jupyter notebook to generate the analysis figures.

# Legal Notices

Microsoft and any contributors grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the
[LICENSE](LICENSE) file, and grant you a license to the Microsoft documentation and other data
in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode),
see the [DATA_LICENSE](data/DATA_LICENSE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation
may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries.
The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks.
Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents,
or trademarks, whether by implication, estoppel or otherwise.
