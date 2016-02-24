#Data Visualization: Loan Data from Prosper
#by Carlos Hernandez

##Summary

This project shows 2 different charts. It shows lending total amount and average lending  amount per year from 2006 to 2013.


##Design

###Exploratory Data Analysis and Cleaning (Tableau)

I use Tableau Public to get a sense from the data, I was curious how lending amounts has grown in the Prosper's history, so I took Loan Origination Date and Loan Origination Amount. I noticed 3 things: the first one is that 2013 was the year with the greater lending amount, the second one, 2009 was the lower, maybe because in fall 2008 SEC requested Prosper to temporarily stop taking new loans as it evaluated whether the company should register as a securities broker, the third, the Prosper dataset contains incomplete data for 2005 and 2014 (please refer to Exploratory.png image).

Exploring the data, I wondered if the lending amount increase in 2013 has the same behaviour with the average lending amount and how the interest rates were related.

 I use Excel to do some data munging (remove incomplete data from 2005 and 2014), created new column called "LoanOriginationYear" to extract the year from the "LoanOriginationDate". 


###Data Visualization (dimple.js)

I decided to use dimple.js in order to simplify code.

I consider using line  and bar charts to show trends over time, maintaining one color in all the charts because only one category is used.  The percentage symbol (%) was included on y axis ticks in order to get a clear interest rate understanding. The first version is drawn from index initial.html.

After reviewing feedback I've decided to exclude interest rate chart and focus the visualization on loan origination history, the titles were changed to emphasize Prosper's highest growth on lending total amount and average lending amount in 2013.

##Feedback

I gathered retro from 3 different people, this is a summary of all of them.

###Retro 1

The highest loan origination amount obtained was on 2013,I wonder which were the causes that motivated this raise? which were the data sources?. 2009 and 2010 were the worst years maybe because of the financial crisis of 2008, and finally the charts goal is not clear.

###Retro 2

Chart titles and data context are not clear. Lending behaviour, trends and amounts are good, there is a relation between the loan origination amounts and the years over time, the main conclusion is the trend on loan amounts and interest rates in the defined period.

###Retro 3

In year 2009, Lending total amount had the lowest level, after Prosper defined a growth strategy, better results were seen from 2010 to 2013. It would be great if this metric could be compared with the loan original amount goal for the same period. Please provide the objective and the context of the charts.

###Retro 4.

<desc>

###Retro 5.

<desc>


##Resources

https://www.prosper.com/plp/about/
https://www.prosper.com/help/topics/how-to-read-a-loan-listing/
http://www.magnifymoney.com/blog/pay-down-my-debt/prosper-personal-loan-review820481381
http://www.lendacademy.com/prosper-205-million-december/
https://www.sba.gov/content/7a-loan-amounts-fees-interest-rates
http://bits.blogs.nytimes.com/2009/04/28/prospercom-reopens-for-lending/?_r=0
http://www.nytimes.com/2008/10/16/technology/start-ups/16peer.html?_r=0
http://dimplejs.org/
http://dimplejs.org/advanced_examples_viewer.html?id=advanced_storyboard_control
https://github.com/PMSI-AlignAlytics/dimple/wiki/dimple.chart
https://github.com/PMSI-AlignAlytics/dimple/wiki/dimple.series

##Data

prosperLoanData7.csv. Summarized dataset for better performance.

prosperLoanData8.csv. Dataset with detail data for 2013 year.
