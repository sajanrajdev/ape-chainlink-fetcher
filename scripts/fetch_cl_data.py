from ape import Contract
import pandas as pd

# Examples:

# ETH/BTC: https://data.chain.link/feeds/ethereum/mainnet/eth-btc
# START_TIME = 1643511664 # Unix timestamp for the oldest round to fetch
# FEED_ADDRESS = "0xAc559F25B1619171CbC396a50854A3240b6A4e99"

# stETH/ETH: https://data.chain.link/feeds/ethereum/mainnet/steth-eth
# START_TIME = 1643511664 # Unix timestamp for the oldest round to fetch
# FEED_ADDRESS = "0x86392dC19c0b719886221c78AB11eb8Cf5c52812"

# BTC/USD: https://data.chain.link/feeds/ethereum/mainnet/steth-eth
# START_TIME = 1643511664 # Unix timestamp for the oldest round to fetch
# FEED_ADDRESS = "0xF4030086522a5bEEa4988F8cA5B36dbC97BeE88c"

# ETH/USD: https://data.chain.link/feeds/ethereum/mainnet/eth-usd
START_TIME = 1643511664 # Unix timestamp for the oldest round to fetch
FEED_ADDRESS = "0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419"

def main():
    feed = Contract(FEED_ADDRESS, abi="abi.json")
    (latest_round, answer, start, last_time, answeredInRound) = feed.latestRoundData()

    feed_data = []
    while (last_time > START_TIME):
        print(f"Fetching round {latest_round}...")
        (round, answer, start, update, answeredInRound) = feed.getRoundData(latest_round)
        latest_round -= 1
        last_time = update
        feed_data.append(
            {
                "round": round,
                "answer": answer,
                "start": start,
                "update": update,
                "answeredInRound": answeredInRound,
            }
        )

    # build dataframe
    df = pd.DataFrame(feed_data)
    # Dump result
    df.to_csv(
        f"data/{FEED_ADDRESS}.csv"
    )