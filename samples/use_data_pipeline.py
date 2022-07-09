import asyncio
from pprint import pprint
from td.client import TdAmeritradeClient
from td.utils.enums import LevelOneQuotes
from td.utils.enums import LevelTwoQuotes


# Initialize the `TdAmeritradeClient`
td_client = TdAmeritradeClient()

# Initialize the `StreamingApiClient` service.
streaming_api_service = td_client.streaming_api_client()

# Let's see what services we have access to.
streaming_services = streaming_api_service.services()

# Grab level one quotes.
streaming_services.level_one_quotes(
    symbols=['MSFT'],
    fields=LevelOneQuotes.All.value
)

# Stream Level Two Quotes.
streaming_services.level_two_quotes(
    symbols=['MSFT', 'PINS'],
    fields=LevelTwoQuotes.All.value
)


async def data_pipeline():
    """
    This is an example of how to build a data pipeline,
    using the library. A common scenario that would warrant
    using a pipeline is taking data that is sent back to the stream
    and processing it so it can be used in other programs or functions.

    Generally speaking, you will need to wrap the operations that process
    and handle the data inside an async function. The reason being is so
    that you can await the return of data.

    However, operations like creating the client, and subscribing to services
    can be performed outside the async function. In the example below, we demonstrate
    building the pipline, which is connecting to the websocket and logging in.

    We then start the pipeline, which is where the services are subscribed to and data
    begins streaming. The `start_pipeline()` will return the data as it comes in. From
    there, we process the data however we choose.

    Additionally, we can also see how to unsubscribe from a stream using logic and how
    to close the socket mid-stream.
    """

    data_response_count = 0
    heartbeat_response_count = 0

    # Build the Pipeline.
    await streaming_api_service.build_pipeline()

    # Keep going as long as we can receive data.

    eqs = '=' * 80
    hyp = '-' * 80
    while True:

        # Start the Pipeline.
        data = await streaming_api_service.start_pipeline()

        # Grab the Data, if there was any. Remember not every message will have `data.`
        if data and 'data' in data:
            print(eqs)
            data_content = data['data'][0]['content']
            pprint(data_content, indent=4)

            # Here I can grab data as it comes in and do something with it.
            if 'key' in data_content[0]:
                print(f"Here is my key: {data_content[0]['key']}")

            print(hyp)
            data_response_count += 1

        elif data and 'notify' in data:
            print(data['notify'][0])
            heartbeat_response_count += 1

        # Once we have 1 data responses, we can unsubscribe from a service.
        if data_response_count == 1:
            unsub = await streaming_api_service.unsubscribe(service='LEVELONE_QUOTES')
            data_response_count += 1
            print(eqs)
            print(unsub)
            print(hyp)

        # Once we have 5 heartbeats, let's close the stream. Make sure to break the while loop.
        # or else you will encounter an exception.
        if heartbeat_response_count == 3:
            await streaming_api_service.close_stream()
            break

        heartbeat_response_count += 1

# Run the pipeline.
asyncio.run(data_pipeline())
