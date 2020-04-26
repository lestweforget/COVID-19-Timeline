This folder contain the new version of the web for wuhan2020-timeline projects.

* Official website: https://pratitya.github.io/wuhan2020-timeline/

* Preview website: https://weileizeng.github.io/wuhan2020-timeline/

### [Sitemap](https://weileizeng.github.io/wuhan2020-timeline/sitemap)
* home page
* reversed/latest
* about
* sitemap

The original files are in the root folder. All files for the website are in this doc/ folder. For this reason, you can switch to this website by choosing "master branch/docs" in setting-github pages section. You can switch back by choosing the "master branch"

### Features
* reformat ../时间线TIMELINE.md to make it compatible to markdown and the web version
* copy ../README.md to the about page of the web
* extract data in ../时间线TIMELINE.md into array of data (in yaml format). We can rearrange these data to make, e.g. a reversed version.
* to be added


### tasks:
- [x] copy 时间线TIMELINE.md to docs/index.md. Index.md will be the homepage of the website. I also replace | by a dot, because markdown use | for tables.
- [x] use a python script to extract data in docs/index.md into docs/_data/news.yml. This .yml file save each entry of the news in an array, so that we can change the layout or order as we want.
- [x] for a test of the data, I create docs/reversed.md to show all the news in reversed order, so that the newest post will come first.
- [x] Use a github action (.github/workflows/push-web.yml) to do the previous three steps automatically at every push. Note that it would show a commit fail, If none of 时间线TIMELINE.md or README.md changes. One can ignore this error message.
- [x] Some of the links might need to fix. For example, the first link in the read me page 疫情与舆情：武汉新冠肺炎时间线TIMELINE should change to [疫情与舆情：武汉新冠肺炎时间线TIMELINE](index), such that it will go from the "about" page to the "homepage"
- [x] In README.md, the | should replace by dot by hand.
- [x] Add "scroll to bottom button in index"


