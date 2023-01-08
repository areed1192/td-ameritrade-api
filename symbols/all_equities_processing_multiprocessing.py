from td.credentials import TdCredentials
from td.client import TdAmeritradeClient
from td.config.get_config import config
from td.utils.enums import FrequencyType
from datetime import datetime
from datetime import timedelta
import pandas as pd
import multiprocessing as mp
import concurrent.futures
from ratemate import RateLimit

#
# Doesn't work yet, concurrency issues somewhere in main td code with client/session/credentials/other
#

#
# Constructs a symbol list for equities that are actively traded
#  metric chosen is 80% of 1 min candles during normal market hours have data
#  for the average of the last 30 days
#  .8 * 6.5 * 60 = 312
#

def check_actively_traded(price_history_service, equity, end_date, start_date): #pylint: disable=redefined-outer-name
    print(equity)
    print("meep1 - check_actively_traded")
    print(price_history_service)
    # Grab the Price History, custom time frame.
    price_history = price_history_service.get_price_history(
        symbol=equity,
        frequency_type=FrequencyType.Minute,
        frequency=1,
        start_date=start_date,
        end_date=end_date,
        extended_hours_needed=False
    )
    print("meep2 - check_actively_traded")
    print(price_history)


    df = pd.DataFrame.from_records(price_history['candles'])
    df.sort_values(by="datetime", ascending=True, inplace=True)

    df["date"] = pd.to_datetime(df['datetime'], unit='ms')

    date_count_df = df['date'].dt.normalize().value_counts().sort_index().to_frame()
    if (date_count_df["date"].mean() > 312):
        return True
    return False


if __name__ == '__main__':
    rate_limit = RateLimit(max_count=50, per=1.7, greedy=True)
    full_equities_path= config.get('symbols', 'full_equities_list_path')
    actively_traded_equities_path = config.get('symbols', 'actively_traded_equities_path')

    full_equities_df = pd.read_csv(full_equities_path)
    full_equities_list = full_equities_df["Symbol"].to_list()
    actively_traded_equity_list = []

    actively_traded_manager = mp.Manager()
    actively_traded_lock = actively_traded_manager.Lock() # pylint: disable=no-member

    # Initialize our `Credentials` object.
    td_credentials = TdCredentials.authentication_default()

    # Initialize the `TdAmeritradeClient`
    td_client = TdAmeritradeClient(
        credentials=td_credentials
    )
    # Initialize the `PriceHistory` service.
    price_history_service = td_client.price_history()

    # The max look back period for minute data is 31 Days.
    end_date = datetime.now()
    start_date = datetime.now() - timedelta(days=31)

    full_equities_list = ["GME"]

    # multiprocessing
    with concurrent.futures.ProcessPoolExecutor(max_workers=1) as executor:
        results = {}
        for equity in full_equities_list:
            rate_limit.wait()
            results[executor.submit(check_actively_traded, price_history_service, equity, end_date, start_date)] = equity
        for result in concurrent.futures.as_completed(results):
            try:
                print("meep")
                data = result.result()
                print(f"checked {results[result]} - result {data}")
                if (data):
                    with actively_traded_lock:
                        actively_traded_equity_list.append(results[result])
            except Exception as e:
                print(f"\n\n\n\n\n\n\n{e}\n\n\n\n\n\n\n\n")