# seawiki
The seawiki library is used to input a text and return the most similar top n  documents in Wikipedia. The main code of the seawiki library comes from Facebook's [DrQA](https://github.com/facebookresearch/DrQA) project.<br>
<br>
输入任意一个短文本，seawiki库可以检索维基百科中最相关的几篇文档，并返回标题和文档内容。seawiki库主要重构了facebook的DrQA项目的检索部分。

## installing seawiki
I recommend that you install it in a virtual environment. Of course, if you don't have a virtual environment, it doesn't matter.<br>
```python
pip install seawiki
```

You must download the pre-processed Wikipedia dataset  [docs.db](还没上传完) and the vectorized Wikipedia dataset [tfidf.npz](还没上传完).

## start demo
example:
```python
import seawiki

seawiki = seawiki.SeaWiki(wiki_path='./Sea-Wiki/wikipedia/docs.db', tfidf_path='./Sea-Wiki//wikipedia/tfidf.npz')
title, document = seawiki.search(question = 'I love you, Xi'an Jiaotong University!',
                                  top_docs=5, is_title=True, is_document=True)
```

arguments：
| wiki_path | absolute path or relative path of docs.db |
| tfidf_path | absolute path or relative path of tfidf.npz | 
| question | any text | 
| top_docs | number of documents returned |
| is_title | whether to return the title of the document |
| is_document | whether to return the content of the document |
