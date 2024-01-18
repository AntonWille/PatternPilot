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
You can download the 100 top questions and their answers. Adding a number indicates the page, so

`python scripts/stack_api/download_so_data.py 2`

will download posts 101 to 200 of the most popular posts. The tag currently needs to be changed in the main function.
If a valid DB exists, it will write these to the defined tables, and save copies in JSON format in the data-folder.

Once in the database, you can extract the posts to html with

`python scripts/full_post_generator.py`

Note: One caveat  of this script is that Questions are only added once. So a question tagged "Ruby Python Perl" would only get added one, to the stack of of posts that was executed first!
