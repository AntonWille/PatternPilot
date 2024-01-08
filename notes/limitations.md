# Limitations

## Grounded Theory as a methodology

Grounded Theory Methodology is an excellent tool for asking qualitative questions, however core concepts such as *Groundedness* and *Theoretical Saturation* can be best achieved in longer-term, collaborative projects. To mitigate this, we have purposefully narrowed the scope as much as possible, **and are thinking about simulating a half-collaboration using GPT 4.5**

## Representativeness

Stackoverflow as a community does not necessarily adequately represent the underlying programming language communities, and may favor specific types of personality and demographics.[0] Vasilescu et al. for example find that StackOveflow tends to be an *unfriendly* community for women to engage in.[1] Given the pseudonomous nature of interaction on stackoverflow, it is difficult to infer if the analysed demographic is representative of the community at large.
The findings of this thesis should thus be supplemented with further research on other online communities, possibly with other research methods offering more control over representativeness, such as surveys or interviews.

One other potential issue lies with the way we chose posts: We simply chose the 100 most-voted questions of all-time tagged with either of the programming languages. The selection is biased towards older posts (bad), and more heavily-discussed and controversial topics (good).

Another one arises from the way our script exports posts: By doing a search over tags, but only downloading a question once, if a question is tagged with fe. "Python, Perl", it will only get downloaded once and randomly assigned a category. This is especially visible with Perl, which is often compared to Python, but has a smaller community, so the ceiling of upvotes is substantially lower.

[0] https://www.sciencedirect.com/science/article/pii/S0747563215000163
[1] Bogdan Vasilescu, Andrea Capiluppi, Alexander Serebrenik, Gender, Representation and Online Participation: A Quantitative Study, Interacting with Computers, Volume 26, Issue 5, September 2014, Pages 488–511, https://doi.org/10.1093/iwc/iwt047
