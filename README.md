# prepare-paper

**你是不是也遇到了读一篇paper，但是里面有太多英文单词不认识的问题？**

这个脚本帮你先把所有的陌生单词都查好，并且按照paper里出现的次数由多到少排列，这样你看paper时，就可以先过一遍这些单词了。

##使用方法

1. 从paper的 pdf 格式生成 txt, 可以安装[pdfminer](https://github.com/euske/pdfminer)
	
		pdf2txt.py ~/Desktop/cassowary-tr.pdf > ~/Desktop/cassowary.txt
		
2. 分词，并查询所有词 

		./prepare_paper.py  ~/Desktop/cassowary.txt known_words.txt > ~/Desktop/explanation.txt
		
		
##注意

1. known_words.txt放你已经认识的不需要再查询的词，你可以自己添加，原始的词来源自[ the top 5,000 words in American English](http://www.wordfrequency.info/top5000.asp)

2. 目前只支持Mac OS X上运行，因为使用了[PyObjc call Dictionary Services](http://macscripter.net/viewtopic.php?id=26675)

3. 使用时要让prepare_paper.py execuable， 不要用`python  prepare_paper.py` 这样来运行，因为纯python运行时下没有Dictionary Service

		sudo chmod a+x prepare_paper.py 
