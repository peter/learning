# Benchmarking and Profiling

## Elapsed Time

Python:

```python
import time
start_time = time.time() # floating point seconds since epoch
# Code here
elapsed_seconds = time.time() - start_time
```

* [timeit module](https://docs.python.org/3/library/timeit.html)
* [python decorator for profiling functions](https://stackoverflow.com/questions/3620943/measuring-elapsed-time-with-the-time-module)
