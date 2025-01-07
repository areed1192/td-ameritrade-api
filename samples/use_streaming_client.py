"""Demonstrates how to use the Schwab Streaming API Client."""

from configparser import ConfigParser

from schwab.client import CharlesSchwabClient
from schwab.credentials import CharlesSchwabCredentials


from schwab.utils.enums import LevelOneQuotes
from schwab.utils.enums import LevelOneOptions
from schwab.utils.enums import LevelOneFutures
from schwab.utils.enums import LevelOneForex
from schwab.utils.enums import LevelOneFuturesOptions
from schwab.utils.enums import NewsHeadlines
from schwab.utils.enums import ChartServices
from schwab.utils.enums import ChartEquity
from schwab.utils.enums import TimesaleServices
from schwab.utils.enums import Timesale
from schwab.utils.enums import ActivesServices
from schwab.utils.enums import ActivesVenues
from schwab.utils.enums import ActivesDurations
from schwab.utils.enums import ChartFuturesFrequencies
from schwab.utils.enums import ChartFuturesPeriods
from schwab.utils.enums import LevelTwoQuotes
from schwab.utils.enums import LevelTwoOptions


# Initialize the Parser.
config = ConfigParser()

# Read the file.
config.read("config/config.ini")

# Get the specified credentials.
client_id = config.get("main", "client_id")
redirect_uri = config.get("main", "redirect_uri")
account_number = config.get("main", "account_number")

# Get the specified credentials.
client_id = config.get("main", "client_id")
client_secret = config.get("main", "client_secret")
redirect_uri = config.get("main", "redirect_uri")

# Intialize our `CharlesSchwabCredentials` object.
credentials = CharlesSchwabCredentials(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    credential_file="config/credentials.json",
)

# Initalize the `CharlesSchwabClient`
client = CharlesSchwabClient(credentials=credentials)

# Initialize the `StreamingApiClient` service.
streaming_api_service = client.streaming_api_client()

# Let's see what services we have access to.
streaming_services = streaming_api_service.services()

# Set the Quality of Service.
streaming_services.quality_of_service(qos_level="1")

# Grab level one quotes.
streaming_services.level_one_quotes(symbols=["MSFT"], fields=LevelOneQuotes.All)

# Grab level one options quotes.
streaming_services.level_one_options(
    symbols=["MSFT_043021C120"], fields=LevelOneOptions.All
)

# Grab level one futures quotes.
streaming_services.level_one_futures(
    symbols=["/ESM4", "/ES"], fields=LevelOneFutures.All
)

# Grab level one forex quotes.
streaming_services.level_one_forex(symbols=["EUR/USD"], fields=LevelOneForex.All)

# Stream News Headlines.
streaming_services.news_headline(
    symbols=["MSFT", "GOOG", "AAPL"], fields=NewsHeadlines.All
)

# Stream Level One Futures Options.
streaming_services.level_one_futures_options(
    symbols=["./CLM21P625"], fields=LevelOneFuturesOptions.All
)

# Stream equity bars.
streaming_services.chart(
    service=ChartServices.ChartEquity,
    symbols=["MSFT", "GOOG", "AAPL"],
    fields=ChartEquity.All,
)

# Stream Time & Sales data.
streaming_services.timesale(
    service=TimesaleServices.TimesaleEquity,
    symbols=["MSFT", "GOOG", "AAPL"],
    fields=Timesale.All,
)

# Stream the Actives.
streaming_services.actives(
    service=ActivesServices.ActivesNasdaq,
    venue=ActivesVenues.NasdaqExchange,
    duration=ActivesDurations.All,
)

# Stream Historical Futures Prices.
streaming_services.chart_history_futures(
    symbols=["/ES", "/CL"],
    frequency=ChartFuturesFrequencies.OneMinute,
    period=ChartFuturesPeriods.OneDay,
)

# Stream Level Two Quotes.
streaming_services.level_two_quotes(symbols=["MSFT", "PINS"], fields=LevelTwoQuotes.All)

# Stream Level Two Quotes.
streaming_services.level_two_options(
    symbols=["MSFT_043021C120"], fields=LevelTwoOptions.All
)

# Start Streaming.
streaming_api_service.open_stream()
