# What is ClickHouse?

ClickHouse is:

* An OLAP database rather than an OLTP database. OLAP databases are optimized for analytical queries, not for transactional updates. Analytics is fundamentally about answering questions and providing insights.
* Column oriented rather than Row oriented. Every column is stored in its own optimized/compressed binary file
* Highly optimized in terms of query response time, i.e. it's up to 1000x faster than a traditional OLTP database
* Able to utilize all available cores, all available memory, and multiple servers
* A database that enables real time analytics of logs and events, typically ingested via Kafka
* Open Source
* Able to run on your laptop or your own server or as a managed service
* Used by Posthog, Sentry, Disney+, Cloudflare, Ebay, Uber etc.
* Compliant with ANSI SQL column data types and those are aliases to the internal data types that ClickHouse uses
* ClickHouse is implemented in C++

You can evaluate ClickHouse cloud for free during a 30 day trial period (with 300 USD credits)
