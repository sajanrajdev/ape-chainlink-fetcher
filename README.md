# ape-chainlink-fetcher

Simple script to fetch historical round data for a specific Chainlink Feed during a time period.

**NOTE:** This script will perform an individual rpc call for each round data of the feed.
Volatile feeds with constant updates may require a numerous amount of calls when iterating
over long periods of time.

## Installation
1. Create a virtual python environment for local dependency management:
```
python3 -m venv venv
```
2. Launch your local virtual environment:
```
source venv/bin/activate
```
2. Install the dependencies:
```
pip install requirements.txt
```

## Usage
1. Add your Alchemy's RPC URI to the ape-config.yaml file.
2. Modify the script parameters within the [fetch_cl_data.py](scrips/fetch_cl_data.py) file according to your query requirements:
- `START_TIME`: The Unix timestamp of the oldest round you want to query.
- `FEED_ADDRESS`: The address of the CL price aggregator proxy in matter (EACAggregatorProxy).
