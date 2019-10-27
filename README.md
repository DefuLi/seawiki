# seawiki
The seawiki library is used to input a text and return the most similar top n  documents in Wikipedia. The main code of the seawiki library comes from Facebook's [DrQA](https://github.com/facebookresearch/DrQA) project. I only reconstructed the retrieval part of the DrQA project.<br>

## installing seawiki
I recommend that you install it in a virtual environment, if you don't have a virtual environment, it doesn't matter.<br>
```python
pip install seawiki
```

You must download the pre-processed Wikipedia dataset  [docs.db](还没上传完) and the vectorized Wikipedia dataset [tfidf.npz](还没上传完).

## start demo
example:
```python
import seawiki

sw = seawiki.SeaWiki(wiki_path='./Sea-Wiki/wikipedia/docs.db', tfidf_path='./Sea-Wiki//wikipedia/tfidf.npz')
title, document = sw.search(question = "I love you, Xi'an Jiaotong University!",
                                  top_docs=5, is_title=True, is_document=True)
```
return:
<p align="center">
	<img src="https://github.com/DefuLi/Sea-Wiki/blob/master/Sea-Wiki/截图.png"  width="500" height="300">
	<p align="center">
		<em>返回标题和文档</em>
	</p>
</p>

| argument | explanation |
| ------------- | ------------- |
| wiki_path | absolute path or relative path of docs.db |
| tfidf_path | absolute path or relative path of tfidf.npz | 
| question | any text | 
| top_docs | number of documents returned, the default is 5 |
| is_title | whether to return the title of the document, the default is True |
| is_document | whether to return the content of the document, the default is True |
<br>

If is_title = False, then the seawiki.search() only return document.
```python
import seawiki

sw = seawiki.SeaWiki(wiki_path='./Sea-Wiki/wikipedia/docs.db', tfidf_path='./Sea-Wiki//wikipedia/tfidf.npz')
document = sw.search(question = "I love you, Xi'an Jiaotong University!",
                            top_docs=5, is_title=False, is_document=True)
```

## acknowledgement
Thanks to facebook open source DrQA project.
