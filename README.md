# Reproducible Research Workflows and Hosting a Technical Blog

*or...*

***"A slightly schizophrenic, jupyter-centric stroll through some useful tricks I’ve picked up for better organizing my <strike>shit</strike> work and sharing with colleagues and the wider world."***


Materials for my talk to University of Toronto Coders on python- and github-based tools for organizing and sharing code, data, and ideas. 

---


***Slideshow video:***

[![ Reproducible Research Workflows and Hosting a Technical Blog](http://img.youtube.com/vi/dVGVBMb6kzo/0.jpg)](http://www.youtube.com/watch?v=dVGVBMb6kzo "Video Title")


***Demo Materials***

The code demonstrations in the video can be found in the [misc](https://github.com/JohnGriffiths/UofT_Coders_Talk_March2018/tree/master/misc) folder. The primary two notebooks are
- [workdocs](cell tag filtering and nbconvert](https://github.com/JohnGriffiths/UofT_Coders_Talk_March2018/blob/master/misc/cell_tag_filtering__master_nb.ipynb)
- [cloudfiles](github-hosted pelican static html websites, and replacing binary objects in notebooks with urls to aws s3 buckets](https://github.com/JohnGriffiths/UofT_Coders_Talk_March2018/blob/master/misc/cloudfiles_demo__master_nb.ipynb)


***Summary***

The talk and demos cover two major components of the scientific workflow that I've developed over the years, and the software tools I've assembled to support it. 

The first uses a combination of notebook parsing + cell tag filtering and nbconvert operations to allow all major communication types of information dissemination (e.g. PDF file, Slideshow, HTML) to be produced directly from a single 'master' document, without having to copy and paste certain parts into separate files for different purposes. This helps avoid over-proliferation of files and maximizes transparency of things like results and figure generation. Check out the [ipynb-workdocs library](https://github.com/JohnGriffiths/ipynb-workdocs) for more info on this. The code in the misc folder represents the initial sketches of a code for updating ipynb-workdocs to the world of jupyter5.3+

The second major component of the scientific workflow discussed is how to turn the outputs of jupyter notebook cell tag filtering into slick github-hosted static html website and reveal.js html slideshows. I also discuss a few nice tricks like using amazon S3 buckets to host large media files.

For more info, check out some LabNotebook entries (c.f. 'OpenAccess' tag), e.g. [about the notebook](https://johngriffiths.github.io/LabNotebook/about-the-notebook.html), [about workdocs-cloudfiles](https://johngriffiths.github.io/LabNotebook/about-workdocs-cloudfiles.html), and some notes on [modelling brain stimulation](https://johngriffiths.github.io/LabNotebook/replicating-spiegler2016.html) and [macaque brain visualization](https://johngriffiths.github.io/LabNotebook/macaque-brain-conmat-viz.html).


<div>
<div>
<div align="right">JG March 2018</div>


