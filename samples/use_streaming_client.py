from td.credentials import TdCredentials
from td.client import TdAmeritradeClient
from td.config import TdConfiguration
from td.utils.enums import LevelOneQuotes
from td.utils.enums import LevelOneOptions
from td.utils.enums import LevelOneFutures
from td.utils.enums import LevelOneForex
from td.utils.enums import LevelOneFuturesOptions
from td.utils.enums import NewsHeadlines
from td.utils.enums import ChartServices
from td.utils.enums import ChartEquity
from td.utils.enums import TimesaleServices
from td.utils.enums import Timesale
from td.utils.enums import ActivesServices
from td.utils.enums import ActivesVenues
from td.utils.enums import ActivesDurations
from td.utils.enums import ChartFuturesFrequencies
from td.utils.enums import ChartFuturesPeriods
from td.utils.enums import LevelTwoQuotes
from td.utils.enums import LevelTwoOptions

config = TdConfiguration()

# Initialize the `TdAmeritradeClient`
td_client = TdAmeritradeClient()

# Initialize the `StreamingApiClient` service.
streaming_api_service = td_client.streaming_api_client()

# Let's see what services we have access to.
streaming_services = streaming_api_service.services()

# Set the Quality of Service.
streaming_services.quality_of_service(
    qos_level='0'
)

# # Grab level one quotes.
# streaming_services.level_one_quotes(
#     symbols=['MSFT'],
#     fields=LevelOneQuotes.All
# )

# # Grab level one options quotes.
# streaming_services.level_one_options(
#     symbols=['MSFT_043021C120'],
#     fields=LevelOneOptions.All
# )

# # Grab level one futures quotes.
# streaming_services.level_one_futures(
#     symbols=['/ES'],
#     fields=LevelOneFutures.All
# )

# # Grab level one forex quotes.
# streaming_services.level_one_forex(
#     symbols=['EUR/USD'],
#     fields=LevelOneForex.All
# )

# # Stream News Headlines.
# streaming_services.news_headline(
#     symbols=['MSFT', 'GOOG', 'AAPL'],
#     fields=NewsHeadlines.All
# )

# # Stream Level One Futures Options.
# streaming_services.level_one_futures_options(
#     symbols=['./CLM21P625'],
#     fields=LevelOneFuturesOptions.All
# )

# # Stream equity bars.
# streaming_services.chart(
#     service=ChartServices.ChartEquity,
#     symbols=['MSFT', 'GOOG', 'AAPL'],
#     fields=ChartEquity.All
# )

# # Stream Time & Sales data.
# streaming_services.timesale(
#     service=TimesaleServices.TimesaleEquity,
#     symbols=['MSFT', 'GOOG', 'AAPL'],
#     fields=Timesale.All
# )

# # Stream the Actives.
# streaming_services.actives(
#     service=ActivesServices.ActivesNasdaq,
#     venue=ActivesVenues.NasdaqExchange,
#     duration=ActivesDurations.All
# )

# # Stream Historical Futures Prices.
# streaming_services.chart_history_futures(
#     symbols=['/ES'],
#     frequency=ChartFuturesFrequencies.OneMinute,
#     period=ChartFuturesPeriods.OneDay
# )

# # Stream Level Two Quotes.
# streaming_services.level_two_quotes(
#     symbols=['MSFT', 'PINS'],
#     fields=LevelTwoQuotes.All
# )

# # Stream Level Two Quotes.
# streaming_services.level_two_options(
#     symbols=['MSFT_043021C120'],
#     fields=LevelTwoOptions.All
# )

# streaming_services.timesale(
#     service="TIMESALE_FUTURES",
#     symbols=["/ES"],
#     fields=Timesale.All
# )

# Stream equity bars.
streaming_services.chart(
    service=ChartServices._ChartFutures,
    symbols=["/ES", "/NQ"],
    fields=ChartEquity.All
)

# Start Streaming.
streaming_api_service.open_stream()
