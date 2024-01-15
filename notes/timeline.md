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

A lot of focus this week was put on just encoding as much as possible, while also refining and adding new codes. The total amount of code segments has risen to 664, spanning around 35 documents (Stackoverflow posts). This process was relatively slow, as I spent a lot of time just trying to make sense of possible cultural implications of discussions. One thing I had previously neglected was the actual code in the examples, which turns out to be (in hindsight rather obviously), quite essential. Parsing code also requires time, so overall progress is a bit slower than I hoped it would be.
On the weekend, I primarily tried to reorganize my code system, which was substantially more difficult and work-intensive than I originally anticipated as well. Results of this are primarily:

- *One way vs. many* remains one of the most interesting and fruitful angles of enquiry, with a lot of results as one would expect (Python people disapproving of multiple options, Perl people generally embracing them), but also relatively suprising results (Perl people asking for recommended or idiomatic approaches, Python people disagreeing with idiomatic code).
- One particular issue here is on how to encapsulate how different solutions are presented. The code *Answer gives multiple options or additonal answer to what is accepted* tries to catch this, but will probably need some work in the future. What constitutes a different approach or solution is partially up for interpretation.

- A lot can be found on *how idiomatic code should look like*. This is a top level category now with multiple subcategories, that could probably reasonably be split up even further and refined. Encapsulating opinions here is not easy, given that language and opinions talking about this tend to be ambigious.
- One sub-category of this pertains to implicit vs. explicit behavior, which is a super interesting, important and controversial topic. During my next revamp, I will probably turn this into its own top-level category.

- *Referencing of external sources* has grown quite a bit. Two main sub-classes are *authorative sources* like books, conferences or official documentation and more *power-horizontal sources* like blog-posts, forums or articles. I am unsure if this is a reasonable distinction to make. Basically, there is a light mental model I'm currently working with that would suggest that One Way lends itself more to order and authority, while TIMRTOWTDI denies authority and embraces or tolerates chaos.

- *Mentionining of abstract Coding Principles* is a top level category now, I'm not sure of its direct value to the thesis yet, or but it seems interesting and relevant.

- Attempts to find cultural significance based on geography (eg. Ruby having a Japenese spirit) have been abandoned, as there is very little to find, and the risk of drifting into pseudo-science seems significant.

- *Legacy vs. modern practices* is another interesting category that emerged now, which seems very relevant to all 3 communities and quite widely discussed. Python has the big v2 to v3 split, the other two had their own issues with newer versions. Perl in particular seems to have a tendency to abandon features, while Ruby deprecates, with strong opinions in the community not to use deprecated methods.

- New category *There's a package/‚module/tool for this* is quite self-explanatory, how communities relate to external tools vs. stdlib could be interesting.

- A number of "basket categories" remain. I am not yet sure of their value, or how to better frame them. These are the *Culture categories* (Ideas about Efficiency, Truth, Beauty and Goodness), *Conversational tone*, as well as the bin basket of *There's something here, but I'm not sure what it is*.
