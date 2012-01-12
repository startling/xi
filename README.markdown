`xi` is a little tool that can copy text to your clipboard from stdin or paste text to stdout.

## Usage
Copy from stdin:

```bash
echo "copy this" | xi 
cat todo.txt | xi
```

Paste to stdout:

```bash
xi | less
xi > pasted.txt
echo `xi`
```

## Credits
I owe this thing to [kennethreitz](), who wrote both [clint][] and [xerox][]; this script is only twenty lines because of them.

[kennethreitz]: https://github.com/kennethreitz
[clint]: https://github.com/kennethreitz/clint
[xerox]: https://github.com/kennethreitz/xerox
