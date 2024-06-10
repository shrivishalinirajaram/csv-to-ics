# CSV to ICS Converter

This repository contains a script to convert a CSV file with event details into an ICS file.

## Prerequisites

- Python 3.7 or higher
- `pandas` library
- `icalendar` library
- `pytz` library

## Installation

1. Create and activate a new Conda environment:
    ```bash
    conda create --name calendar_env python=3.7
    conda activate calendar_env
    ```

2. Install the required packages:
    ```bash
    conda install -c conda-forge pandas pytz
    pip install icalendar
    ```

## Usage

1. Prepare your CSV file with the following headers:
    - `Subject`
    - `Start Date`
    - `Start Time`
    - `End Date`
    - `End Time`
    - `All Day`
    - `Description`
    - `Location`

2. Run the script:
    ```bash
    python csv_to_ics.py input.csv output.ics --timezone 'US/Eastern'
    ```

    Replace `input.csv` with the path to your CSV file and `output.ics` with the desired path for the ICS file. The time zone is set to 'US/Eastern' by default.

## Example

An example CSV file (`test_data.csv`) is provided in this repository. You can use it to test the script:

```bash
python csv_to_ics.py test_data.csv output.ics --timezone 'US/Eastern'

