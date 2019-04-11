# Parse and Pipe Output on the Command Line

## Problem

Commands used on the command line (like `ps`, `ls` etc.) typically yield output in an ad-hoc text format and not on a structured data format (i.e. JSON). Still, you sometimes need to automate the task of extracting information from such output, such as the process ID of a certain program etc.

## Solution

Pipe your output to one or more [sed](https://www.gnu.org/software/sed/manual/sed.html) and `grep` (see [mac grep](https://ss64.com/osx/grep.html) and [gnu grep](https://www.gnu.org/software/grep/manual/grep.html)) commands to parse the output.

In this example we would like to get the ID of the most recently started [Convox](https://convox.com) process and start a shell in that process:

```sh
alias convox-ps-first-id="convox ps | sed -n 2p | sed 's/^\([a-z0-9-]*\).*/\1/'"
convox exec $(convox-ps-first-id) bash
```
