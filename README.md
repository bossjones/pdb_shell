pdb_shell
===========

  add new mode, shell mode, to pdbpp. When you are in shell mode, anything you type will be python code, instead of pdb command.


How to use
-------------
```
(pdb++) !_pdb_shell = 1 # enable shell mode.
(pdb++) c # it will show variable c, instead of pdb continue command.
(pdb++) _pdb_shell = 0 # disable shell mode.
(pdb++) c # it means pdb continue command instead of variable c.
```

Notice
-------------
`_pdb_shell` is stored in current frame. If you change frame, for example call another function, shell mode will be disable. And you code can't use `_pdb_shell` as variable name.


Just for fun.

