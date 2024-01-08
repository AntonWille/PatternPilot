## Timeline

### WEEK 1
Week 1 was spent creating scripts to export data and re-import. Partially, this was already done before, however I realized some things wouldn't work as expected initially, so I had to go back and update the scripts. In addition, I also refactored a little bit for cleanness in expectation that someone else might have to read the code in the future.
Shortly, I also thought about doing the encoding with a very basic custom web-interface built in Ruby, however in the end chose to use MaxQDA, as the research group uses this and offers a license for students. I set that up on my Macbook and home Linux-machine within a VM.

### WEEK 2
Week 2 was primarily a holiday spent with the family and friends. I read some of the extracted posts, and thought more about possible directions, while also having some discussions with my father (also a Software Engineer) and my girlfriend, who previously used Grounded Theory in her MSc. In this week I also tried to get a better overview of the existing  literature and started organizing a Zotero project.

### WEEK 3
After doing everything I could before actually starting with the important work; encoding the Stackoverflow Posts, I finally started doing this in earnest.
The Code-System that developed over this week can be found in `data/code_system_07_01_24`.
Anxiety to not be able to find interesting cultural differences or cultural occorunces in general was quickly replaced with some concerns that there is too much volume to fit into a Bachelor thesis: Posts average around 1000 lines, so there is a very substantial amount of discussion in just these 300 posts.

Some early thoughts:
- The culture is in the comments: A lot of the most interesting tidbits so far where within the comments to answers.
- One comment mentions ‘explicit is better than implicit’ - another python mantra that’s explicitly in contrast to how the ruby community does things. I have so far not encountered this in Perl, but some research is in order. This mantra actually pairs quite well and is related to "one way vs. many".
- Unsurprisingly, how to handle imports / how to setup a virtualenv for a Python project is a hugely controversial topic and very related to the discussion on "one way vs. many"

So far, I went through 18 posts in detail, 5 for each language, finding 278 Codes. Overall, the "one way vs. many" seems to be a widely approachable, interesting and relevant topic, so I will continue to lay more focus on this. There are some others that are less relevant but might still be nice to have, in Week 4 I have to spend some time on consolidating, expanding and reordering the code-system.

### WEEK 4
