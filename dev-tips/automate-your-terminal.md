# Automate Your Terminal

## Problem

You have a developer setup where you need to open a number of terminal tabs in different source code directories on your computer (i.e. Mac), start a number of services (i.e. web apps and APIs) and also open your IDE in those directories.

## Solution

Dependencies:

* Node.js
* The [ttab](https://github.com/mklement0/ttab) npm package (`npm install ttab -g`)

This particular example uses these technologies:

* [VS Code](https://code.visualstudio.com) with shell command installed
* [Git](https://git-scm.com/)

Add a script `~/bin/start` that knows how to start a service in a particular source code directory:

```sh
#!/usr/bin/env bash

dir=$(basename $(pwd))

if [ "$dir" == "hyperion" ]; then
   command="env IRIS_HOST=http://localhost:4000 npm start"
elif [ "$dir" == "iris-core" ]; then
   command="env LOG_LEVEL=debug IRIS_SITE=aftonbladet npm run start:dev:watch"
else
   echo "Don't know how to start app in dir $dir"
   exit 1
fi

echo "starting app in $dir: $command"
$command
```

Add a script `~/bin/open-dev` that can bootstrap your developer setup:

```sh
#!/usr/bin/env bash

ttab "cd ~/src/hyperion && git pull && code ."
ttab "cd ~/src/hyperion && start"

ttab "cd ~/src/iris-core && git pull && code ."
ttab "cd ~/src/iris-core && start"
```
