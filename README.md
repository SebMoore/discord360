# discord360
Discord Rich Presence add-in for Autodesk Fusion 360

[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

## Installation
Simply download or clone this repository, and place the files inside a new folder named "Discord360" located at the add-in path indicated in [this Autodesk help article.](https://knowledge.autodesk.com/support/fusion-360/troubleshooting/caas/sfdcarticles/sfdcarticles/How-to-install-an-ADD-IN-and-Script-in-Fusion-360.html)

Your final folder structure should look something like the following:
```
add-in path/
└── Discord360/
    ├── commands/
    ├── lib/
    ├── pypresence/
    ├── Discord360.manifest
    ├── Discord360.py
    └── config.py
```

The add-in will run automatically on Fusion 360 startup.

## Troubleshooting
Make sure you have Discord open (or running in the background) before you launch Fusion 360, otherwise the add-in won't start and the Rich Presence won't appear if you subsequently start Discord.

If you quit Discord while Fusion 360 is open (minimizing it is fine, as long as it's still running), the presence won't appear if you then start Discord again.

To fix both of the above issues, you can simply restart the add-in: to do this, click on `Utilities (in the Fusion 360 navigation bar) -> Add-Ins -> Select "Add-Ins" in the dialog box that appears -> Discord360 -> Stop -> Run`
