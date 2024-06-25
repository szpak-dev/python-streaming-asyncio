# Data Streaming with Python and asyncio
In order to initiate and start Lab, run:

```bash
poetry install
poetry shell
```

## 1. Data Streaming

### Streams
**Data streaming** refers to the continuous and real-time transfer of data. It is designed to handle a constant flow of
data that is processed incrementally as it arrives. Data streaming is commonly used for real-time analytics, 
monitoring, and other applications requiring timely processing of information.

**Key Characteristics:**
- **Continuous Data Flow**: Data is continuously generated and sent, often in small chunks.
- **Low Latency**: Designed for real-time or near-real-time data processing.
- **Event-Driven**: Data processing is triggered by the arrival of new data.
- **Examples**: Real-time analytics, financial market data feeds, sensor data, live video/audio feeds.

1. **Data Sources**: Data can come from various sources such as sensors, log files, social media feeds, or user interactions.
2. **Data Processing**: This involves transforming, filtering, and analyzing the data in real-time.
3. **Data Storage**: Processed data can be stored in databases, data lakes, or other storage systems.
4. **Data Consumption**: Applications or users consume the processed data for various purposes, such as visualization, alerting, or further analysis.

### Requesting Data via HTTP
Requesting data via **HTTP** typically involves making a discrete request to a server and waiting for a response. 
This is the standard model for fetching resources from the web, such as HTML pages, JSON data, or files.

**Key Characteristics:**
- **Discrete Requests**: Each request is a separate transaction between the client and server.
- **Higher Latency**: Involves more overhead due to the request-response cycle.
- **Client-Initiated**: The client must initiate each request.
- **Examples**: Fetching web pages, RESTful API calls, downloading files.

### HTTP Streams
**HTTP streams** combine aspects of both traditional HTTP requests and data streaming. They allow a server to send a
continuous stream of data to the client over a single HTTP connection. This is useful for scenarios where the client
needs to receive real-time updates without repeatedly making new requests.

**Key Characteristics:**
- **Persistent Connection**: Maintains an open connection between client and server for continuous data transfer.
- **Real-Time Updates**: Server can push updates to the client as they become available.
- **Client-Server Communication**: Suitable for real-time data delivery with HTTP semantics.
- **Examples**: Server-Sent Events (SSE), WebSockets, HTTP/2 streams.

To see HTTP Streaming in practice, do the following:

```bash
cd data_streaming

uvicorn http_stream:app
```

### Practical Implications
- **Data Streaming**: Ideal for scenarios where data needs to be processed in real-time as it is generated, such as monitoring system logs, processing sensor data, or analyzing financial transactions.
- **HTTP Requests**: Suitable for fetching data that is not time-sensitive, such as requesting data from a REST API or downloading files.
- **HTTP Streams**: Best for applications that require real-time updates but benefit from using HTTP protocols, such as live notifications, real-time charts, or collaborative applications.

### Summary
| Feature                   | Data Streaming                        | HTTP Requests                      | HTTP Streams                        |
|---------------------------|---------------------------------------|------------------------------------|-------------------------------------|
| **Data Flow**             | Continuous, real-time                 | Discrete, request-response         | Continuous, real-time               |
| **Latency**               | Low                                   | Higher due to request overhead     | Low                                 |
| **Client Role**           | Consumes data as it arrives           | Initiates each request             | Establishes connection and listens  |
| **Server Role**           | Continuously sends data               | Responds to client requests        | Continuously sends data over a single connection |
| **Use Cases**             | Real-time analytics, monitoring       | Fetching web pages, API data       | Real-time updates, live feeds       |
| **Examples**              | Apache Kafka, Spark Streaming         | REST APIs, file downloads          | SSE, WebSockets, HTTP/2 streams     |

### Python Libraries for Data Streaming
Several libraries in Python for handling data streaming:

1. **Apache Kafka**: A distributed streaming platform that can handle real-time data feeds.
2. **Apache Spark Streaming**: Part of the Apache Spark ecosystem, used for processing large streams of data.
3. **Flask or FastAPI**: These web frameworks can be used to stream data over HTTP.
4. **PySpark**: The Python API for Spark, useful for large-scale data processing.
5. **RxPy (ReactiveX)**: A library for composing asynchronous and event-based programs using observable sequences.
6. **Asyncio**: A library to write concurrent code using the async/await syntax.


## 2. Asynchronous Programming
**Asynchronous programming** is a programming paradigm that enables tasks to run independently of the main program 
flow, allowing other operations to continue before the first task has finished. This is particularly useful for 
I/O-bound operations, where the program would otherwise be waiting for an external event, such as a network 
response or file read/write operation, to complete.

### Key Concepts:
- **Concurrency**: Multiple tasks can start, run, and complete in overlapping time periods.
- **Parallelism**: Multiple tasks can run simultaneously on multiple processors or cores.

### Blocking vs. Non-Blocking Operations
#### Blocking:
- **Blocking operations** halt the execution of a program until the operation completes.
- Example: Reading a file from disk, waiting for a network request to complete.
- **Disadvantage**: If a program performs a blocking operation, it cannot execute any other code until that operation - finishes, leading to inefficient use of resources and potentially poor performance.

#### Non-Blocking:
- **Non-blocking operations** allow the program to continue executing other code while waiting for the operation to complete. - Example: Asynchronous file read/write, non-blocking network requests.
- **Advantage**: Increases the efficiency and responsiveness of applications, especially those that involve I/O-bound tasks.

### Use Cases of Asynchronous Programming
1. **I/O-Bound Tasks**:
   - **File Operations**: Reading from or writing to files, especially large files.
   - **Database Queries**: Fetching data from a database where the data retrieval time can be unpredictable.
   - **Network Requests**: Sending and receiving data over a network, such as HTTP requests, WebSocket communication.

2. **Real-Time Applications**:
   - **Chat Applications**: Handling multiple chat messages in real-time without blocking the user interface.
   - **Online Gaming**: Managing real-time interactions and state updates for multiple players.

3. **Background Tasks**:
   - **Email Sending**: Sending emails in the background while the user continues to use the application.
   - **Scheduled Tasks**: Running scheduled tasks, like backups or data synchronization, without interrupting the main application flow.

4. **User Interfaces**:
   - **Responsive UIs**: Keeping the user interface responsive while performing background operations, such as fetching data for display or processing user input.

### Summary
- **Asynchronous programming** allows tasks to run independently and concurrently, improving the efficiency and responsiveness of applications.
- **Blocking operations** halt the program execution, whereas **non-blocking operations** allow other code to run concurrently.
- Asynchronous programming is particularly beneficial for I/O-bound tasks, real-time applications, background processing, and maintaining responsive user interfaces.


## 3. Exchange
To run simple exchange with broker, consumer and producer:

```bash
cd exchange

# start broker
python broker.py

# then start consumer
python consumer.py

# last but not least - produce some messages
python produce.py
```

### Explanation
Our Exchange consists of:

- **Broker (Server)**:
  - Listens for connections from both producers and consumers.
  - When a producer connects, it handles incoming data and places it in a queue.
  - When a consumer connects, it retrieves data from the queue and sends it to the consumer.
- **Producer (Client)**:
  - Connects to the broker and identifies itself as a producer.
  - Sends data to the broker.
- **Consumer (Client)**:
  - Connects to the broker and identifies itself as a consumer.
  - Receives data from the broker.

Run the broker code first, then the producer and consumer code. The producer will send messages to the broker, 
which will place them in the queue, and the consumer will retrieve and print them.


## Time to Practice
Create a program that streams real-time environmental sensor data from a public API, processes the data asynchronously,
and visualizes insights about environmental conditions.

### Components

1. **Public Sensor API Integration:**
   - Identify a public API that streams environmental sensor data, such as air quality (e.g., from OpenAQ), weather data (e.g., from OpenWeatherMap), or any other relevant sensor data (e.g., from IoT platforms like Adafruit.io).
   - Use `aiohttp` or another async HTTP client library to connect to this API and stream data asynchronously.

2. **Data Processing and Analysis:**
   - Asynchronously receive and process incoming sensor data.
   - Perform real-time analysis on the data, such as calculating averages, identifying trends, or detecting anomalies.

3. **Real-Time Visualization:**
   - Utilize a visualization library like `matplotlib`, `Plotly`, or `Dash` to create real-time graphs, charts, or maps displaying sensor data trends.
   - Update the visualizations dynamically as new data streams in.

4. **Concurrency and Asynchronous Handling:**
   - Use `asyncio` to manage concurrent tasks such as streaming sensor data, processing data, and updating visualizations without blocking the main event loop.
   - Ensure efficient resource utilization and responsiveness by handling multiple streams and tasks concurrently.

5. **User Interaction:**
   - Provide interactive features such as selecting different sensor types or locations, adjusting visualization parameters (e.g., time range, aggregation level), or displaying detailed information about specific data points.

### Goals
- **Asyncio Fundamentals:** Practice handling asynchronous tasks, managing event loops, and coordinating multiple coroutines effectively.
- **Streaming Data:** Gain experience in streaming real-time data from public APIs and processing it asynchronously.
- **Data Analysis:** Implement real-time data analysis techniques appropriate for sensor data, such as statistical analysis or anomaly detection.
- **Visualization:** Learn to visualize real-time sensor data dynamically, improving understanding and presentation of environmental conditions.

### Potential Extensions
- **Multiple Sensor Sources:** Integrate data streams from multiple sensor APIs to provide a comprehensive view of environmental conditions across different locations.
- **Alerting Mechanisms:** Implement alerts or notifications based on predefined thresholds for certain environmental parameters.
- **Geospatial Visualization:** Visualize sensor data on maps to provide spatial context and geographical patterns of environmental conditions.
- **Historical Analysis:** Store and analyze historical sensor data to identify long-term trends or patterns.
