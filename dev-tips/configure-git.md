# Configure Git

```sh
git config --global core.pager ''
```

To support [multiline commits in an editor](https://stackoverflow.com/questions/9725160/aborting-commit-due-to-empty-commit-message):

```sh
git config --global core.editor 'code -w'
```

The global config is stored in `~/.gitconfig`:

```
[alias]
    st = status
[push]
	default = current
[user]
	email = peter.marklund@schibsted.com
	name = Peter Marklund
[core]
	pager =
	editor = code
```
