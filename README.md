## Catsay
>Catsay is a CLI application, like [cowsay](https://github.com/schacon/cowsay) but written in Python.
When you invoke catsay, a smol catto will greet you with a quote. The quotes are converted to lolcat, by making use of a [scraper](https://gist.github.com/thisisjustinm/bfcc14f04ea1f55d15e0ef44be6f483f). And no, the name is not in Pig Latin.

### Installation
Go to directory in which setup.py is present and run ```python setup.py install```.

Alternatively, you can run the command ```pip install git+https://github.com/thisisjustinm/catsay.git@<LATEST_COMMIT_HASH>```. Replace ```<LATEST_COMMIT_HASH>``` with the latest commit hash available here on Github.

### Usage
```user@root:~$ catsay```

```
┌──────────────────────────────────────────┐
│ RESPECT IZ NOT SOMETHIN DAT U CAN ASK 4, │
│  BUY OR BORROW. RESPECT IZ WUT U EARN FR │
│ UM EACH PERSON NO MATTR THEIR BAKGROUND  │
│ OR STATUS.                               │
└──────────────────────────────────────────┘
     |
     |
      \
     ,_     _
     |\_,-~/
     / _  _ |    ,--.
    (  @  @ )   / ,-'
     \  _T_/-._( (
     /         `. \
    |         _  \ |
     \ \ ,  /    |
      || |-_\__   /
     ((_/`(____,-'
    
```

### Extra

* Use ```-h``` flag for help
    ```
        usage: catsay [-h] [-a] [-q]
        Make cats say stuff.
        optional arguments:
          -h, --help       show this help message and exit
          -a , --animal    change the animal | default : catto
          -q , --quote   make animal say your quote
    ```
 * Use ```-a``` flag to change animal
 * Use ```-q``` flag to make the animal say anything you want

