# Configure Your IDE

## Problem

You want an IDE that your are comfortable and productive with.

## Solution

Install [VS Code](https://code.visualstudio.com/)

Open the Command Palette in VS Code with `cmd-shift-p` and run "Install code command in PATH".

From the command palette - run "Open Settings (JSON)":

```json
{
    "workbench.editor.enablePreview": false
}
```

From the command palette - run "Open Keyboard Shortcuts (JSON)":

```json
[
    {
        "key": "cmd+t",
        "command": "workbench.action.quickOpen"
    },
    {
        "key": "cmd+p",
        "command": "-workbench.action.quickOpen"
    }
]
```

Recommended [extensions](https://marketplace.visualstudio.com) to install in your IDE:

* GitLens
* ESLint
* Visual Studio IntelliCode
* Debugger for Chrome
* GitHub Extension for Visual Studio
