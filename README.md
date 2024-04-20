# QuintoAndar Case

Imagine you've just been hired as a Data Analyst to join one of our Data Squads, responsible for leveraging the products team and operation team to make better decisions based on data and provide insights that improve the our stakeholders decisions.

This quarter, your main goal is to help the product team to **increase the number of contracts signed**, which **has been in steady decline** since early this year.

## What seems to be happening?

Try to understand main bottlenecks along the funnel and raise hypotheses that may have caused each behavior.

The data on contracts signed per visit suggests that most of the time, initial visits are not converted into signed contracts (Figure [01](#fig01)). This is also evident in the contract funnel with the **number of tenants making offers** (Figures [02](#fig02) and [03](#fig03)).

Perhaps if tenants made more visits, the likelihood of making an offer and consequently signing a contract would increase. Another possibility is to create a better impression or a better match during the initial visits. To achieve this, improving the likelihood of the ads could help: many reviews indicate discrepancies between the house and the ad, such as it not being as well-maintained or being larger in the photos (Figure [06](#fig06)). People are going to the visits with different expectations than what they will find. By showing ads that better portray the condition of the house, it may result in aligned expectations during the initial visits and a higher probability of making an offer and signing a contract.

Additionally, the **number of houses visited** seems to be another bottleneck, which limits the entire funnel below: number of offers, number of tenants making offers, and consequently, the number of contracts. This is the largest gap in the funnel chart (Figures [02](#fig02) and [03](#fig03)). Consequently, even with the visit ratings practically constant over time (Figure [05](#fig05)), the number of signed contracts continues to decline.

## Is there any other information that would be relevant to your analysis?

Why would it be relevant? What would be the outputs with the new data available?

- It would be interesting to know which visits resulted in contracts.
- How many visits each tenant made up to that point.

In other words, it would be useful to have the other two tables at the same granularity as the visit table and keys to be able to combine these tables. With this additional data, we could connect the information from the three provided tables and obtain more precise and in-depth insights.

## Can you think of 3 other analyses that could help our stakeholders with our quarter goal?

Please describe the analysis as well as the benefits of each one for our stakeholders. Try to explain how the idea could be implemented, connecting strategy with the product team and how these analyses can make an impact on our stakeholders' decisions.

- Analyze the quality of the ads and what to do to better align customer expectations on the first visit.
- Analyze how to improve ad filters/ad recommendation, so that the customer can get a better match and thus a higher probability of signing a contract on the first visit.
- Analyze/understand what causes the number of houses visited to be lower. Perhaps, again, this is related to the quality of the ads, location, etc.

## Figures

<a name="fig01">Figure 01: Number of customers who signed vs. did not sign (left) and the proportion of customers who signed (right).</a>
![fig01](images/fig01.png)

<a name="fig02">Figure 02: Contract funnel each month.</a>
![fig02](images/fig02.png)

<a name="fig03">Figure 03: Evolution of the contract funnel over time.</a>
![fig03](images/fig03.png)

<a name="fig04">Figure 04: Correlations between funnel variables.</a>
![fig04](images/fig04.png)

<a name="fig05">Figure 05: Distribution of Reviews over months.</a>
![fig05](images/fig05.png)

<a name="fig06">Figure 06: Proportion of negative opinions over time.</a>
![fig06](images/fig06.png)
