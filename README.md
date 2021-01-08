## Catsay
>Catsay is a CLI application, like [cowsay](https://github.com/schacon/cowsay) but written in Python.
When you invoke catsay, a smol catto will greet you with a quote. The quotes are converted to lolcat, by making use of a [scraper](https://gist.github.com/thisisjustinm/bfcc14f04ea1f55d15e0ef44be6f483f). And no, the name is not in Pig Latin.

### Installation
Go to directory in which setup.py is present and run ```python setup.py install```.

### Usage
```justin@root:~$ catsay```

```
┌────────────────────────────────────┐
│ CHANCE FAVORS TEH PREPARD MIND.    │
└────────────────────────────────────┘
     |
     |
      \
    _                ___       _.--.
    \`.|\..----...-'`   `-._.-'_.-'`
    /  ' `         ,       __.--'
    )/' _/     \   `-_,   /
    `-'" `"\_  ,_.-;_.-\_ ',
        _.-'_./   {_.'   ; /
       {_.-``-'         {_/
```

### Extra

* Use ```-h``` flag for help
    ```
        usage: catsay [-h] [-a] [-m]
        Make cats say stuff.
        optional arguments:
          -h, --help       show this help message and exit
          -a , --animal    change the animal | default : catto
          -m , --myquote   make animal say your quote
    ```
 * Use ```-a``` flag to change animal (choose from ```birb``` and ```doge```)
 * Use ```-m``` flag to make the animal say anything you want

