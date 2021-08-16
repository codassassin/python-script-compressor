# python-script-compressor
This is a python script that compresses python scripts into single liner python command.

## How to use?
* Firstly:
```
git clone https://github.com/codassassin/python-script-compressor.git
```
* Then run the compress_python_scripts.py as follows:
```
python compress_python_scripts.py test.py
```
* Then open the scripts.csv file and copy the script corresponding to the taget file and copy the command and paste it in a terminal and run it:
```
python -c "exec(compile(chr(112)+chr(114)+chr(105)+chr(110)+chr(116)+chr(40)+chr(34)+chr(72)+chr(101)+chr(121)+chr(32)+chr(98)+chr(114)+chr(111)+chr(46)+chr(46)+chr(46)+chr(46)+chr(34)+chr(41)+chr(13)+chr(10)+chr(112)+chr(114)+chr(105)+chr(110)+chr(116)+chr(40)+chr(34)+chr(84)+chr(104)+chr(105)+chr(115)+chr(32)+chr(105)+chr(115)+chr(32)+chr(97)+chr(32)+chr(116)+chr(101)+chr(115)+chr(116)+chr(46)+chr(46)+chr(46)+chr(46)+chr(34)+chr(41)+chr(13)+chr(10)+chr(13)+chr(10)+chr(102)+chr(111)+chr(114)+chr(32)+chr(105)+chr(32)+chr(105)+chr(110)+chr(32)+chr(114)+chr(97)+chr(110)+chr(103)+chr(101)+chr(40)+chr(50)+chr(48)+chr(41)+chr(58)+chr(13)+chr(10)+chr(32)+chr(32)+chr(32)+chr(32)+chr(105)+chr(32)+chr(43)+chr(61)+chr(32)+chr(49)+chr(13)+chr(10)+chr(32)+chr(32)+chr(32)+chr(32)+chr(112)+chr(114)+chr(105)+chr(110)+chr(116)+chr(40)+chr(105)+chr(41)+chr(13)+chr(10), chr(60)+chr(115)+chr(99)+chr(114)+chr(105)+chr(112)+chr(116)+chr(62), chr(101)+chr(120)+chr(101)+chr(99)))"
```

## Result Images
* Test file run:

<img src="https://github.com/codassassin/python-script-compressor/blob/main/images/001.png"/>

* compress_python_scripts.py run:

<img src="https://github.com/codassassin/python-script-compressor/blob/main/images/002.png"/>

* Running the compressed command:

<img src="https://github.com/codassassin/python-script-compressor/blob/main/images/003.png"/>


### Disclaimer !!

> This tool is only for testing and academic purposes and can only be used where strict consent has been given. Do not use it for
> illegal purposes! It is the end user’s responsibility to obey all applicable local, state and federal laws. Developers assume no
> liability and are not responsible for any misuse or damage caused by this tool and software in general.
 
