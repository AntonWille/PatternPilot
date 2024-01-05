# Exploratory Analysis of Cultural Differences in Programming Language Communities

## Introduction

This is the repository of my Bachelor Thesis on cultural differences in programming language communities at Free University of Berlin. The official page for this thesis can be found [here](https://www.mi.fu-berlin.de/w/SE/ThesisProgrammingLanguageCommunites). The supervisor for this thesis is [Prof. Dr. Lutz Prechelt](https://www.mi.fu-berlin.de/en/inf/groups/ag-se/members/prechelt.html).

### Initial Outline

While much attention has been dedicated to dissecting and comparing the structural features of programming languages, less has been done to analyze the features of the communities forming around them. In this thesis, we aim to find and analyze some such differences and their origin, by taking a Grounded Theory Methodology (GTM) approach to discussions on the programming forum StackOverflow. Taking Richard A. Schweder’s definition of culture as “[...] conceptions of what is true, good, beautiful, and efficient”, we will examine conversations about how to program well in 3 different programming languages: Ruby, Python and Perl. While these 3 languages share many similarities, being first introduced in the same era, primarily as dynamically typed, high-level scripting languages, each language also exhibits distinct characteristics that merit closer examination, for example:
Perl’s motto of “There’s more than one way to do it” runs against Python’s idea of offering exactly one way to do “it”. Ruby seems to sit in the middle, both defining a “rubyesque” way of doing things while acknowledging different approaches.

All three languages thrive in different applications: Perl’s advanced regex capabilities and ubiquity on Unix systems made it a preferred tool for sys-admins. Since the inception of Ruby on Rails in 2004, Ruby found popularity in the web-development community. Python with its easy interoperability with C made it the default choice for machine learning and Data Science in general, and due to its simple, clean syntax often taught in universities and recommended to beginners.

While Perl was developed in the US, Python hails from the Netherlands, and Ruby from Japan. The cultural differences of their creators and initial communities might be reflected in the way people want to program in these languages or perceive its style.

These points can serve as a good initial focus for examination in combination with the categories we can derive from Schweder's definition of culture, however given the open nature of GTM and the broadness of the topic, the direction of the research might shift during encoding and theory building.

## Code

### Download Data from Stackoverflow

A minimal SORequests-Class is defined in stack_overflow_api.py. This works without an api-key for read-only requests, but with a limit of 300 Requests per day.
By invoking script/download_so_data.py, you can download the 100 top questions and their answers. Adding a number indicates the page, so
`script/download_so_data.py 2`
will download posts 101 to 200 of the most popular posts for each of the three tags 'ruby', 'python' and 'perl'.

If a valid DB exists, it will write these to the defined tables, and save copies in JSON format in the data-folder.


## Timeline

### WEEK 1
Week 1 was spent creating scripts to export data and re-import. Partially, this was already done before, however I realized some things wouldn't work as expected initially, so I had to go back and update the scripts. In addition, I also refactored a little bit for cleansiness in expectation that someone else might have to read the code in the future.
Shortly, I also thought about doing the encoding with a very basic custom web-interface built in Ruby, however in the end reverted to using MaxQDA, so I set that up on my Macbook and home Linux-machine within a VM.

### WEEK 2
Week 2 was primarily a holiday spent with the family and friends. I read most of the most some of the extracted posts, and thought quite a bit about possible directions, while also having some discussions with my father (also a Software Engineer) and my girlfriend, who previously used Grounded Theory in her MSc.

### WEEK 3
After doing everything I could before actually starting with the important work; encoding the Stackoverflow Posts, I finally started doing this in earnest. First, I did one more round of pre-sorting into interesting and uninteresting posts based on the 100 most-upvoted questions tagged with each Ruby, Python and Perl. This was done mostly through a heuristic of if there is any conversation outside of basic technical information.

Then I moved on with encoding all the remaining Posts with some basic codes:
- Culture
- - Beauty
- - Efficiency
- - Truth
- - Goodness
- Geographical cultural significance
- Statement of "Group-Belonging"
