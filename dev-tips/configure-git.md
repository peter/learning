# Configure Git

```sh
git config --global core.editor code
git config --global core.pager ''
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
