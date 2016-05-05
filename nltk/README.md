# [nltk](http://www.nltk.org/)
A natural language process package built with python.

Used to process twitter data(language is english).

## Install package
nltk and numpy
```bash
sudo pip install -U nltk
sudo pip install -U numpy
```
[see detail](http://www.nltk.org/install.html)

## Install nltk data

```py
import nltk
nltk.download()
```

Because of something network blocked, try to use proxy:

```py
nltk.set_proxy('http://127.0.0.1:16823/', ('USERNAME', 'PASSWORD'))
nltk.download()
```

Above proxy powered by [Lantern](https://github.com/getlantern/lantern).

[see detail](http://www.nltk.org/data.html)

## Issue tracker
[install numpy failed](http://stackoverflow.com/questions/20497339/installing-numpy-with-pip-fails-on-ubuntu)

## Links
* [如何计算两个文档的相似度三](http://www.52nlp.cn/%E5%A6%82%E4%BD%95%E8%AE%A1%E7%AE%97%E4%B8%A4%E4%B8%AA%E6%96%87%E6%A1%A3%E7%9A%84%E7%9B%B8%E4%BC%BC%E5%BA%A6%E4%B8%89)
* [nltk github](https://github.com/nltk/nltk)
