# Streams in HTTP/2:
1. **Multiplexing:** HTTP/2 supports multiplexing, meaning multiple streams can be sent and received concurrently over a single TCP connection. Each stream is essentially an independent bi-directional sequence of frames that carries an individual message.
2. **Stream Prioritization:** Streams can be prioritized, allowing higher priority messages to be processed more quickly than lower priority ones. This helps optimize the utilization of resources.
3. **Binary Framing Layer:** HTTP/2 uses a binary framing layer that divides messages into smaller frames. Each stream is composed of these frames, which are interleaved and can be reassembled at the receiving end.
4. **Efficiency:** By multiplexing streams over a single connection, HTTP/2 reduces the overhead associated with opening and maintaining multiple TCP connections, which was a limitation in HTTP/1.x.

## Request-Response Cycle:
While HTTP/2 uses streams for concurrent communication, it still adheres to the request-response model at the 
application level. Each HTTP/2 stream can handle multiple frames that collectively represent a request or a response.
The server responds to each request with a corresponding response, and these are tied together within their respective
streams.

## Benefits of Streams in HTTP/2:
- **Efficiency:** Multiplexing streams over a single connection reduces latency and improves overall network efficiency.
- **Concurrency:** Multiple requests and responses can be handled concurrently without waiting for previous responses to complete.
- **Resource Optimization:** Stream prioritization allows critical resources to be allocated more effectively based on application needs.

## Downsides of HTTP/2 Streams
While HTTP/2 streaming offers significant advantages in terms of performance and efficiency compared to HTTP/1.x, 
there are some potential downsides and considerations to be aware of:

1. **Complexity:** Implementing and managing HTTP/2 streaming can be more complex than traditional HTTP/1.x due to the additional features like multiplexing, stream prioritization, and binary framing. This complexity can lead to more challenging debugging and troubleshooting processes.
2. **Resource Consumption:** Although HTTP/2 reduces the need for multiple TCP connections, it still requires additional resources to manage streams and maintain the connection state. Servers and clients must handle stream management efficiently to avoid resource exhaustion.
3. **Head-of-Line Blocking:** While HTTP/2 allows for multiplexing, which enables concurrent streams, it can still suffer from head-of-line blocking. This occurs when a single slow or stalled stream delays the processing of subsequent streams that are dependent on the same resources or are lower in priority.
4. **Server Push Misuse:** HTTP/2 supports server push, where servers can send resources preemptively to clients without waiting for a request. However, misuse of server push can lead to unnecessary data transmission and potential inefficiencies if not used judiciously.
5. **Compatibility Concerns:** While HTTP/2 is widely supported by modern browsers and servers, legacy systems or certain network configurations may not fully support it. This can lead to compatibility issues if HTTP/2 features are relied upon without fallback mechanisms.
6. **Increased Security Complexity:** Although not inherent to HTTP/2 streaming itself, the adoption of HTTP/2 may require more stringent security configurations (e.g., TLS 1.2+ encryption) due to browser and server requirements, which can add complexity and overhead to deployments.
7. **Network Overhead:** HTTP/2 introduces additional header compression techniques (HPACK) to reduce overhead compared to HTTP/1.x, but there can still be some overhead associated with managing streams and frames, especially for small, frequent requests.

Despite these potential disadvantages, HTTP/2 streaming generally provides substantial benefits in terms of performance,
latency reduction, and efficient resource utilization, making it a preferred choice for modern web applications.
Proper implementation and tuning can mitigate many of these concerns, ensuring optimal performance and reliability in
practice.

## Summary
In summary, HTTP/2's use of streams enhances the performance and efficiency of web communication by allowing multiple
messages to be processed simultaneously within a single connection, while still maintaining the request-response 
paradigm at the application layer.


# Streaming Response with `yield`
1. **Continuous Data Flow**:
   - The `yield` statement allows the function to produce a sequence of values over time, one at a time, rather than computing them all at once and sending them together.
   - This is useful for streaming data, where the server needs to continuously send new data to the client as it becomes available.

2. **Event-Driven Architecture**:
   - In the context of HTTP streaming, especially with Server-Sent Events (SSE), the server sends multiple events to the client over a single connection.
   - Using `yield`, the server can send an event, pause, wait for new data to generate, and then send the next event, thus maintaining an open connection.

3. **Efficient Resource Usage**:
   - Generators created with `yield` are more memory efficient than creating a complete list of data because they produce items only when requested.
   - This fits well with the nature of streaming, where data is processed and sent incrementally.

By using `yield`, the function can produce data in an on-demand manner, perfect for scenarios where you need to 
continuously stream data to the client without closing the connection.