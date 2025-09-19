# ClickHouse Query Optimization

## Checklist for Query Optimization

* Selection of `PRIMARY KEY` or `ORDER BY` columns. Should be the main columns that you filter by in where clauses with the columns with lowest cardinality first. If you have the need for multiple primary keys due to different filters for different queries you can make use of materialized views and projections
* Selection of column data types, see list below
* Avoiding NULL values in columns
* Vertical and horizontal scaling of hardware

Column type recommendations:

* `UInt8` instead of `Int64` if you are storing small positive numbers
* `Float32` or `Decimal32` (to avoid rounding errors) instead of `Float64`
* `LowCardinality(String)` or `Enum8('impression' = 1, 'viewable' = 2, 'click' = 3, 'conversion' = 4)` (stored as integers) instead of `String` when you have fewer than 10k unique values
* `FixedString(16)` instead of `String` for an ID of known length
* `DateTime` (with second precision) instead of `DateTime64` (with milli/micro/nano second precision) etc.

There is a [clickhouse benchmark tool](https://clickhouse.com/docs/operations/utilities/clickhouse-benchmark) that you can use for performance testing.

## Resources

* [ClickHouse Learning](https://learn.clickhouse.com)
* [ClickHouse Query Optimization Workshop September 2025 (Pablo Musa)](https://learn.clickhouse.com/visitor_catalog_class/show/1786439)
* [ClickHouse Cloud](https://console.clickhouse.cloud)
