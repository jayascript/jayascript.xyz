Title: Non-Native Speaker Essay Evaluation
Date: 2018-02-27
Modified: 2020-06-20
Lang: en
Category: Projects
Slug: projects/nns-essay-eval
Cover: images/articles/nns-essay-eval/by-group-grammar.jpg
Tags: statistics, excel, spss, data analysis
Summary: An analysis of essay grading by native and non-native Japanese speakers.

# An Analysis of Essay Grading By Native and Non-Native Japanese Speakers

This statistical analysis exercise was completed in partial fulfillment of the requirements for the course Research Statistics I. I audited this graduate-level course while on a research scholarship at Sophia University in Tokyo, Japan. The instructor, [Prof. Yoshinori Watanabe](http://rscdb.cc.sophia.ac.jp/Profiles/65/0006461/prof_e.html), researches language testing and assessment.

The project was the first major stats exercise I completed after taking Basic Statistics through the University of Amsterdam on Coursera. It was so exciting to see everything I’d learned in class applied to a real-life situation!

* [Description](#description)
* [Data](#data)
    * [Download](#download) <sub>*Data sources and collection process.*</sub>
    * [Dissection](#dissection) <sub>*Data analysis.*</sub>
* [Discussion](#discussion)
    * [Debug](#debug) <sub>*Mistakes were made.*</sub>
    * [Directions](#directions) <sub>*Ideas for future research.*</sub>
* [Disseminate](#disseminate)

## <a id="description"></a>Description

In this exercise, we examined an essay written in the Japanese language by a non-native speaker of Japanese. The essay was scored by 14 native speakers of Japanese, as well as 14 non-native speakers of Japanese. These graders evaluated the essay on three categories:

1. Content
2. Organization
3. Grammar

Scores were provided on a scale of 0 to 10.

The purpose of this exercise was to determine whether there was a difference in the average evaluation score between the two groups.

## <a id="data"></a>Data

## <a id="download"></a>Download

The essay and scores were provided by Professor Watanabe. The files were downloaded from a USB drive, and the stats were computed on a personal computer.

<p align="center">
  <img src="/images/articles/nns-essay-eval/ns-nns-scores.jpg" alt="graders" width="100%" height="" style="">
  <p style="text-align:center;"><sup><em>Group 1 is Non-Native Speakers (NNS), Group 2 is Native Speakers (NS). Both groups of graders evaluated a single essay on content, organization and grammar.</em></sup>
  </p>
</p>

## <a id="dissection"></a>Dissection

We loaded the Excel data into SPSS and used the software to calculate statistics and perform a t-test. We found that **non-native speakers (NNS, Group 1)** had a higher standard deviation (SD = 2.31) on the total score allotted to the essay. **Native speakers (NS, Group 2)** were much more consistent with their interpretation of the essay (SD = 1.7).

<p align="center">
  <img src="/images/articles/nns-essay-eval/ns-nns-descriptives.jpg" alt="descriptive statistics all graders" width="100%" height="" style="">
  <p style="text-align:center;"><sup><em>Descriptive statistics computed for all 28 graders.</em></sup>
  </p>
</p>

There were 28 graders in total. The average scores given on the essay (rounded up) were 8.4 for content, 7.3 for organization, 6.2 for grammar, and 21.9 total.

<p align="center">
  <img src="/images/articles/nns-essay-eval/ns-nns-groups-stats.jpg" alt="group statistics" width="100%" height="" style="">
  <p style="text-align:center;"><sup><em>Statistics computed on each category by group (NNS vs NS).</em></sup>
  </p>
</p>

The non-native speakers (Group 1) gave an average content score of 8.5, organization score of 7.9, grammar score of 6.2 and total score of 22.6. The native speakers (Group 2) gave an average content score of 8.2, organization score of 6.7, grammar score of 6.2 and total score of 21.1.

### Independent Samples Test

In our dataset, graders reported their scores for the essay, and whether or not they were a native speaker of Japanese. We want to determine if the scores given on a single essay are different depending on the native language of the grader (i.e. are they a Japanese speaker or not?). To do this, we can test whether the means for scores given by native Japanese speakers and non-native Japanese speakers are statistically different.

We use an **independent samples t-test** to compare the mean scores for native and non-native Japanese speakers. Our chosen significance level was `a = 0.05`.

<p align="center">
  <img src="/images/articles/nns-essay-eval/ns-nns-t-test.jpg" alt="independent samples test" width="100%" height="" style="">
  <p style="text-align:center;"><sup><em></em></sup>
  </p>
</p>

One thing that sticks out to me immediately is the **mean difference** of the organization scores. You can see this in the group statistics shown above. The mean difference of 1.214 tells us that the mean organization score given by the first group (non-native speakers) is significantly higher than that of the second group (native Japanese speakers).

This point is further emphasized by looking at the **Confidence Interval**. The CI for the mean difference of the content score, grammar score and total scores all contain 0. So, we can conclude that these results are not significant at the chosen significance level. (We can also conclude this by examining the p-values for the content and grammar scores, which are higher than our significance level `a = 0.05`).

However, the CI for the mean difference of the organization scores **does not** contain 0. This score also has the smallest p-value, at 0.243. So we can assume that the difference in organization scores given is statistically significant.

#### Hypothesis Test

We chose to reject the null hypothesis and conclude that there was a difference in mean score given by native and non-native speakers:

<p align="center">
  <img src="/images/articles/nns-essay-eval/hypothesis.jpg" alt="hypothesis test summary" width="100%" height="" style="">
  <p style="text-align:center;"><sup><em></em></sup>
  </p>
</p>

More specifically, there was a significant difference in the organization score given between the two groups. The average organization score given by non-native speakers was 1.214 points higher than that of native speakers. Similarly, the average total score given by non-native speakers was 1.5 points higher than that given by native Japanese speakers.

### Mann-Whitney U Tests

We used **continuous fields** and the **Mann-Whitney U test** to further examine the differences between the two independent groups. This allowed us to better see how the essay's evaluated score differed based on the native language of the grader.

#### Content Scores Given

When considering all graders, the essay received an average content score between 8 and 9:

<p align="center">
  <img src="/images/articles/nns-essay-eval/hist-content.jpg" alt="histogram of content scores" width="100%" height="" style="">
  <p style="text-align:center;"><sup><em>Content scores given by both groups.</em></sup>
  </p>
</p>

When we look at the groups independently, we can see that the scores are clustered around similar values:

<p align="center">
  <img src="/images/articles/nns-essay-eval/by-group-content.jpg" alt="content scores by group" width="100%" height="" style="">
  <p style="text-align:center;"><sup><em>Content scores given, NNS vs. NS.</em></sup>
  </p>
</p>

There seems to be no significant difference in the means, as confirmed by our t-test.

#### Organization Scores Given

While the content scores were more variable, organization scores were clustered around the 7 to 8 mark range for all graders in both groups:

<p align="center">
  <img src="/images/articles/nns-essay-eval/hist-organization.jpg" alt="histogram of organization scores" width="100%" height="" style="">
  <p style="text-align:center;"><sup><em>Organization scores given by both groups.</em></sup>
  </p>
</p>

But here, when comparing the groups separately, we can see the pronounced difference between the means:

<p align="center">
  <img src="/images/articles/nns-essay-eval/by-group-organization.jpg" alt="organization scores by group" width="100%" height="" style="">
  <p style="text-align:center;"><sup><em>Organization scores given, NNS vs. NS.</em></sup>
  </p>
</p>

The non-native speakers in Group 1 gave mostly the same organization score for the essay, while native speakers in Group 2 gave slightly lower scores. Our t-test helped us to conclude that this difference is statistically significant.

#### Grammar Scores Given

Grammar scores given showed similar variance to the content scores:

<p align="center">
  <img src="/images/articles/nns-essay-eval/hist-grammar.jpg" alt="histogram of grammar scores" width="100%" height="" style="">
  <p style="text-align:center;"><sup><em>Grammar scores given by both groups.</em></sup>
  </p>
</p>

Similar to the content scores, grammar scores given were more spread out through both groups:

<p align="center">
  <img src="/images/articles/nns-essay-eval/by-group-grammar.jpg" alt="grammar scores by group" width="100%" height="" style="">
  <p style="text-align:center;"><sup><em>Grammar scores given, NNS vs NS.</em></sup>
  </p>
</p>

Though Native Speakers in Group 2 providing slightly more high-level scores than Non-Native Speakers, we concluded that this difference was not statistically significant.

#### Total Scores Given

The essay received a total score of between 20 and 24 points from most graders:

<p align="center">
  <img src="/images/articles/nns-essay-eval/hist-total.jpg" alt="total scores given" width="100%" height="" style="">
  <p style="text-align:center;"><sup><em>Total scores given.</em></sup>
  </p>
</p>

Most graders in both groups gave the same score to the essay. However, we can see that scores given by Non-Native Speakers (Group 1) skew higher, while those given by Native Speakers (Group 2) skew lower:

<p align="center">
  <img src="/images/articles/nns-essay-eval/by-group-total.jpg" alt="total scores by group" width="100%" height="" style="">
  <p style="text-align:center;"><sup><em>Total scores given by group, NNS vs. NS.</em></sup>
  </p>
</p>

This lines up with the conclusion we drew from our t-test: that there is a statistically significant difference in scores given depending on the native language of the grader.

## <a id="discussion"></a>Discussion

One might have an intuition that native speakers may grade an essay differently than non-native speakers. Native speakers have grown up and been instructed in the language in question, so they know what to look for when evaluating an essay, as that’s what they’ve been tested on themselves. Non-native speakers, on the other hand, may not have the same level of intuition as to what constitutes a good Japanese essay.

I'm particularly excited to notice that the point of most difference was the organization score. **Content** seems to me to be a score that would be similar regardless of native language of the grader. We can all determine whether or not an essay is interesting to read and captures our attention. Similarly, I'd say that **grammar** scores should also be the same. While native Japanese speakers grow up with an intuitive understanding of their language's grammar, non-native speakers have more explicit instruction.

Still, this doesn't make non-native speakers any worse at determining the correctness of grammar. In fact, they could be better than native speakers, because they've explicitly been taught those rules and know when they're broken. Native speakers can simply "feel" through a sentence, and whether or not it "sounds" right, where as non-native speakers can explicitly point to the error. But both groups have a similar ability to determine the grammatical correctness of a sentence. So this point is not one of contention.

However, **organization** should be a place where the scores differ, especially for a Japanese essay. Traditional Japanese essay structure can differ greatly from what we know in the West. "Introduction-Body-Conclusion" is not always a structure that would constitute a "good" Japanese essay. There are several traditional Japanese essay structures that native speaker might prefer to see, because that's what they were taught.

On the other hand, non-native speakers may be coming to the essay expecting an entirely different organizational structure. I can liken this to the frequent comments I hear about Japanese media, which is known for its slow build-up, drawn-out tension and sudden twists near the end of the story. Funnily enough, this is a traditional structure of Japanese storytelling, and is used in most Japanese games, movies, comics and television shows.

If the essay was a narrative essay, then native Japanese speakers could have been looking for this traditional structure. The essay writer was a non-native speaker of Japanese, and may not have been aware of traditional Japanese essay structure. The essay writer may have used a structure similar to "Intro-Body-Conclusion" which non-native Japanese speakers are very familiar with; thus, they would have rated the organization score highly. In contrast, native Japanese speakers looking for the traditional "build up-drawn out-twist" structure may have given the essay a much lower score for lacking this organization.

### <a id="debug"></a>Debug

There's no guarantee that the non-native speakers came from the "West." Non-Native Japanese speakers could be from Korea, China, Taiwan, Kenya, Australia, Brazil, or any number of places from around the globe. Lumping them all together under the term "Non-Native Japanese speaker" fails to account for the wide linguistic variance of the group. The people in the non-native speaker group could be looking for any number of things.

In contrast, the Native Japanese speaker group mostly likely contains people from just Japan, and perhaps Korea, China and Brazil. What I mean to say is that the pool of native Japanese speakers is much smaller than the pool of non-native Japanese speakers. As such, we could expect to see much less variance than if, for example, we'd have graded an essay in English or Chinese (which has many more flavors around the world).

### <a id="directions"></a>Directions

**Will the same grader give a different score to the same essay, based on organization alone?**

Suppose two essays of similar content and grammar. The first essay is written in a traditional Japanese structure, and the second one written in a non-traditional Japanese structure. How would a group of Japanese speakers grade this essay? We saw a statistically significant difference on the organization score. We can determine if this is true by performing analysis on essays that share similar content and grammar, but differ in the organization.

## <a id="disseminate"></a>Disseminate

* A PDF generated from the tests in SPSS: [NNS_Evaluation.pdf](/files/NNS_Evaluation.pdf)
* Professor Yoshinori Watanabe's Research:
    * [Sophia University](http://rscdb.cc.sophia.ac.jp/Profiles/65/0006461/prof_e.html)
    * [ResearchMap](https://researchmap.jp/read0061850/?lang=english)
* Traditional Japanese essay structures:
    * [Ki-Sho-Ten-Ketsu](https://www.wasabi-jpn.com/how-to-speak-japanese/enhance-your-japanese-script-ki-sho-ten-ketsu/)
    * [Jo-Ha-Kyu](https://www.wasabi-jpn.com/how-to-speak-japanese/distinguish-your-japanese-script-jo-ha-kyu-structure/)
