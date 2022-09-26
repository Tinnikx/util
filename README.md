# util
This project base on python3.9, It only has the basic GUI.

It contains UUID generator, URL encoder/decoder, timestamp translator.



## Package

```
pyinstaller --paths=/home/kaixiang/dev/cutomized-workspace/util -F -w app.py
```



## Development

After active venv, set `LD_LIBRARY_PATH` to the shell env:
```
source venv/bin/activate
export LD_LIBRARY_PATH=./venv/lib/python3.9/site-packages/PySide6/Qt/lib/
```

`app.py` is the entrypoint, use `python app.py` to start the project.
