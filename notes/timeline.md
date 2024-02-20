## Timeline

### WEEK 1
Week 1 was spent creating scripts to export data from stack-overflow and then import them into a tool for encoding. Partially, this was already done before, however I noticed some formatting issues I wanted to take care off, as well as add some other missing data-points to be able to do some easy data validation. In addition, I refactored some of the code in case someone else needs or wants to use the code in the future.
Shortly, I also considered doing the encoding with a very basic custom web-interface built in Ruby, however in the end chose to use MaxQDA, as the research group uses this and my university offers a license for students. I set that up on my Macbook, and on my home Linux-machine within a VM.

### WEEK 2
Week 2 was primarily a holiday spent with the family and friends (Week of Christmas). I read some of the extracted posts, and thought more about possible directions, while also having some discussions with my father, also a Software Engineer, and my girlfriend, who previously used Grounded Theory in her MSc.
In this week I also tried to get a better overview of the existing  literature and started organizing a Zotero project.

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
On the weekend, I primarily tried to reorganize my code system, which was substantially more difficult than I originally anticipated as well, but ultimately quite sucessful. Results of this are primarily:

- *One way vs. many* remains one of the most interesting and fruitful angles of enquiry, with a lot of results as one would expect (Python people disapproving of multiple options, Perl people generally embracing them), but also relatively suprising results (Perl people asking for recommended or idiomatic approaches, Python people disagreeing with idiomatic code).
- One particular issue here is on how to encapsulate how different solutions are presented. The code *Answer gives multiple options or additonal answer to what is accepted* tries to catch this, but will probably need some work in the future. What constitutes a different approach or solution is partially up for interpretation.

- A lot can be found on *how idiomatic code should look like*. This is a top level category now with multiple subcategories, that could reasonably be split up even further and refined. Encapsulating opinions here is not easy, given that they and the language used to describe them tend to be rather ambigious.
- One sub-category of this pertains to implicit vs. explicit behavior, which is a super interesting, important and controversial topic. During my next revamp, I will probably turn this into its own top-level category.

- *Referencing of external sources* has grown quite a bit. Two main sub-classes are *authorative sources* like books, conferences or official documentation and more *power-horizontal sources* like blog-posts, forums or articles. I am unsure if this is a reasonable distinction to make. Basically, there is a light mental model I'm currently working with that would suggest that One Way lends itself more to order and authority, while TIMRTOWTDI denies authority and embraces or tolerates chaos. So far the data doesn't seem to support this connection though.

- *Mentionining of abstract Coding Principles* is a top level category now, I'm not sure of its direct value to the thesis yet, or but it seems interesting and relevant.

- Attempts to find cultural significance based on geography (eg. Ruby having a Japenese spirit) have been abandoned, as there is very little to find, and the risk of drifting into pseudo-science seems significant.

- *Legacy vs. modern practices* is another interesting category that emerged now, which seems very relevant to all 3 communities and quite widely discussed. Python has the big v2 to v3 split, the other two had their own issues with newer versions. Perl in particular seems to have a tendency to abandon features, while Ruby deprecates, with strong opinions in the community not to use deprecated methods.

- New category *There's a package/‚module/tool for this* is quite self-explanatory, how communities relate to external tools vs. stdlib could be interesting.

- A number of "basket categories" remain. I am not yet sure of their value, or how to better frame them. These are the *Culture categories* (Ideas about Efficiency, Truth, Beauty and Goodness), *Conversational tone*, as well as the bin basket of *There's something here, but I'm not sure what it is*. The plan is to refine these into their own more descriptive categories next weekend.

Plan for the coming week:
- Read most of the papers I only scanned so far and start framing a literature overview
- Encode to the point of having at least half of the 300 documents
- Rework t he coding system over the weekend

## Week 5

The plan to encode towards 150 documents was significantly over-ambitious. Instead I spent a lot of time searching for literature, which mostly did not yield the desired results. There does not seem to be any research closely resembling what I am doing, although I cannot be sure, as it is difficult to search for, especially with my lacking experience in the field. Primarily, I found scholars of philosophy interested in cultural aspects of programming language communities, scholars of SE and adjacent fields that apply GTM to "techy" online-communities like stack-overflow, albeit usually with a slightly different focus. Where "techy" culture is concerned, it is usally applied on a different level, for example comparing open-source vs. corporate culture, FAANG vs. start-up, "hacker" vs. "enterprise" etc.

While a lot of the things found were really interesting, and could either inspire or help apply the method, it was frustrating to not find the kind of "golden goose", where some good researchers apply a similar method on similar data with a similar motive. In addition, I'm a bit nervous about finding mostly Software Engineering and Philosophy papers, as these are the two research fields I'm a bit more familiar with.

I used 3 1/2 different methods to find papers:

1. Search the web via google-scholar, arxiv, libgen etc.
2. Look at literature reviews that seem promising and scan the papers reviewed there
3. Ask people around me who might not know
   3.5 Ask ChatGPT and Gemini to find interesting scholarship on the topic

Suprisingly, method 1 and 3.5 yielded the most results here. The fact that 2. and 3. did not yield much gives me hope that I am not missing much. None of the literature reviews seem to have a category for this kind of research, and the social scientists in my circle that I asked basically said "Sounds interesting, I can't find anything either, but send me the text once you are done".

## Week 6

This week again was mostly spent on encoding and re-evaluating the coding system, as well as grounding and updating memos. The number of codes is up to 1000 over 45 documents. Basically, the number of codes per document goes up significantly as the code-system matures, so I will have to go back to the older documents and do some re-encoding there.
I think I hit a bit of an emotional low-point this week, as I was very unsure if what I am doing makes sense and if it is going in an acceptable direction. Meeting my supervisor on Thursday luckily alleviated much of my concerns and reignited my motivation. Over the weekend I continued encoding and tried to formualte tenable and more concrete goals of the research.

## Week 7

This week was mostly spent preparing for next weeks presentation in the Research Group. First and foremost was writing a draft of a literature review and an introduction, as well as trying to close gaps in my literature review and understanding in the method. During this, I realized several mistakes I made during execution so far:
1. I went in with quite a lot of theoretical presuppositions, not all of them clearly labelled as such.
2. Related, I did not do Grounding in a very structured way. While it was always part of my thought process, I did not use the tools given by the method, like carefully writing Memos and noting down answers to questions.
3. While I did perform Open Coding, it was already guided by "axis", and as such I might have missed very interesting or promising strings. This is a minor point, as I rather have too many directions thank too few, but could have made my life easier.

Given these slight regrets, I spent some time writing careful memos, resorting things, and finally going through the "bin"-code that was "There's something here, I am not sure what it is" to really try to carefully encode these.

## Week 8

This week I presented my thesis within the seminar 'Beiträge zum Software Engineering'. This took sinificant preparation, and my main focus was on finishing the slides, double-checking that everything is correct and doing a couple of test runs to note sound too wooden. This was my first in-person presentation since 2019, so I was quite nervous before hand.

The presentation itself went quite well in my opinion. Attendants were quite enthusiastic, and I received really valuable feedback and tips on how to continue. Writing the presentation itself was also really valuable, as I was able to spot flaws in my approach, increase my theoretical knowledge of the method I use, and had to "frame" my research, which will be good preparation for the final write-up.

On the weekend, I mostly focused on preparing for my last math exam, but also set up the LaTeX document for the final paper, and did some minor work on the paper as well.

## Week 9

I was struck down by Covid this week, and could not do any work from Monday to Friday. On the weekend, the scripts were revised and the formatting issues resolved, as well as the new formatting applied to the old documents. In addition, I increased the number of documents from 100 for each tag to 300, to prepare for selective coding. Some progress was made on writing the paper itself, and I started selectively encoding documents.

## Week 10

## Week 11

## Week 12
