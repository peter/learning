# Command Line Scripts

## Command Line Arguments

Python:

```python
#!/usr/bin/env python3
# Invoke script with --help to get usage details

import argparse

def arg_parser():
    parser = argparse.ArgumentParser(description='Look up the URL of a service/API')
    parser.add_argument('service', help='Name of service to look up')
    parser.add_argument('--epochs', type=int, default=50)
    parser.add_argument('--prod', action='store_true', help='Use production environment')
    parser.add_argument('--all', action='store_true', help='Print URLs of all nodes')
    return parser

if __name__ == "__main__":
  args = arg_parser().parse_args()
  print(args.service, args.prod, args.all)
```
