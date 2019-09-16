# complex-networks-COS010
Repository for assigments of Complex Networks COS010, class of 2019-1

## TP1

### How to Convert Graphs to Graph-Tools Format

* graphParserAmazon 
	* parses external Amazon graph file into .gt
	* execute: `python3 graphParserAmazon`
* graphParserReddit
	* parses external Reddit graph file into .gt
	* execute: `python3 graphParserReddit`

### How to Obtain Statistics
* genStatsDirectedGraph
	* generate statistics from directed graph enconded in .gt format
	* execute: `python3 genStatsDirectedGraph <graph-filename>`

### Graphs Used
Some are in Directory `/tp1/exampleGRaphs/`. Some are not provided in the repository due to large size
* [Amazon0302.txt](http://snap.stanford.edu/data/amazon0302.html)
* [soc-redditHyperlinks-body.tsv](http://snap.stanford.edu/data/soc-RedditHyperlinks.html)
* [web-Google.txt](http://snap.stanford.edu/data/web-Google.html)
* [com-youtube.ungraph](http://snap.stanford.edu/data/com-Youtube.html)

## Dependencies
* python3
* [graph-tool](https://graph-tool.skewed.de/)
	* [Helpful Documentation](https://graph-tool.skewed.de/static/doc/graph_tool.html#available-subpackages)
