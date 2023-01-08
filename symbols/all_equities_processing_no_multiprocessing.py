from datetime import datetime
from datetime import timedelta
import pandas as pd
from ratemate import RateLimit

from td.credentials import TdCredentials
from td.client import TdAmeritradeClient
from td.utils.enums import FrequencyType
from td.config import TdConfiguration

#
# Constructs a symbol list for equities that are actively traded
#  metric chosen is 80% of 1 min candles during normal market hours have data
#  for the average of the last 30 days
#  .8 * 6.5 * 60 = 312
#

if __name__ == '__main__':
    # TD Ameritrade rate limit is 120 per 60 seconds, doing 65 to be safe
    rate_limit = RateLimit(max_count=120, per=65, greedy=True)

    # Initialize our `Credentials` object.
    td_credentials = TdCredentials.authentication_default()

    # A config object
    config = TdConfiguration()

    # Initialize the `TdAmeritradeClient`
    td_client = TdAmeritradeClient(
        credentials=td_credentials,
        config=config
    )

    full_equities_path= config.full_equities_list_path
    actively_traded_equities_path = config.actively_traded_equities_path

    full_equities_df = pd.read_csv(full_equities_path)
    full_equities_list = full_equities_df["Symbol"].to_list()
    actively_traded_equity_list = []

    # Initialize the `PriceHistory` service.
    price_history_service = td_client.price_history()

    # The max look back period for minute data is 31 Days.
    end_date = datetime.now()
    start_date = datetime.now() - timedelta(days=31)

    for equity in full_equities_list:
        rate_limit.wait()
        result = False
        # Grab the Price History, custom time frame.
        price_history = price_history_service.get_price_history(
            symbol=equity,
            frequency_type=FrequencyType.Minute,
            frequency=1,
            start_date=start_date,
            end_date=end_date,
            extended_hours_needed=False
        )
        if(price_history):
            if (price_history['candles']):
                df = pd.DataFrame.from_records(price_history['candles'])

                df.sort_values(by="datetime", ascending=True, inplace=True)

                df["date"] = pd.to_datetime(df['datetime'], unit='ms')

                date_count_df = df['date'].dt.normalize().value_counts().sort_index().to_frame()
                if (date_count_df["date"].mean() > 312):
                    result = True
                    actively_traded_equity_list.append(equity)
        print(f"checked {equity} - result {result}")
    df.sort_values(by="Symbol", inplace=True)
    df.to_csv(actively_traded_equities_path, index=False)