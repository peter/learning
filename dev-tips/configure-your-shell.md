# Configure Your Shell

## Problem

You want to be able to:

* Quickly execute commands at the terminal
* Be able to access the command history (ctrl-r)
* Have an informative prompt

## Solution

If you prefer bash over zsh you need to change login shell for your user as [zsh is the default shell on Mac](https://scriptingosx.com/2019/06/moving-to-zsh/) as of Catalina (10.15): `chsh -s /bin/bash`.

Add a `~/.bashrc` [startup file](https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html):

```sh
alias l='ls -l'
alias git='git --no-pager'
alias chrome="/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"

export HISTSIZE=50000
export PS1='\u@\h \w]\$ '

export PATH=~/bin:$PATH

# git prompt
# https://github.com/magicmonty/bash-git-prompt/blob/master/README.md
if [ -f "$(brew --prefix)/opt/bash-git-prompt/share/gitprompt.sh" ]; then
  __GIT_PROMPT_DIR=$(brew --prefix)/opt/bash-git-prompt/share
  GIT_PROMPT_ONLY_IN_REPO=1
  GIT_PROMPT_THEME="Single_line"
  source "$(brew --prefix)/opt/bash-git-prompt/share/gitprompt.sh"
fi
```

For the git prompt above, you need to install [Homebrew](https://brew.sh) and the `bash-git-prompt` package:

```sh
brew update
brew install bash-git-prompt
```

Make sure your startup file is sourced on login by `~/.bash_profile`:

```sh
source ~/.bashrc
```

You can set environment variables in `~/.bashrc` and inline when executing commands and you can execute a command with `env -i` to block out environment variables. To run a command with environment variables specified as `KEY=VALUE` in an `.env` file (one entry per line) you can do something like this:

```sh
env $(cat .env | xargs) my-command
```

## Resources

* [What is a shell?](https://www.gnu.org/software/bash/manual/html_node/What-is-a-shell_003f.html#What-is-a-shell_003f)
* [Bash Manual](https://www.gnu.org/software/bash/manual/html_node/index.html#SEC_Contents)
