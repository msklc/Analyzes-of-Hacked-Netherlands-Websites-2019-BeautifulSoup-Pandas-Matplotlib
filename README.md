# Analyzes of Hacked Netherlands Websites (2019)

In this study, we analyzed the hacked (attacked by various methods) Netherlands Websites (extension of .nl) in 2019. We get the data (scraping the data) from zone-h.org, which is an open-source database formed by attackers themselves. Because of the captcha warn, we use the cookies of our own browser which we used to access  the site before.

We analyze the data 4 different aspect and reach the below results;

- 1558 (.nl) websites are attacked (hacked) in the first 3Q of 2019.
- Websites are attacked by 199 different attackers.
- Websites are attacked nearly the same average in every month, except March.
- __356 websites (23% of total) are also attacked before.__
- Websites exist 16 different country and 20% them are located outside of Netherlands.

## Why 199 hackers preferred to attack .NL websites?
The second part of the study; we tried to find answers;
- Who are these 199 attackers?
- Why they preferred the .NL websites for hacking?
- What is their motivation?

So, we scraped the 199 attackers' both total attacks numbers and only .NL attacks numbers from zone-h.org. Then, we calculated the ratios of these two numbers for every hacker. 
As a conclusion;
- The %95 of the hackers attacked to .NL web sites randomly and I think there isn't any special reason. But it is also possible could be done for masking the real attacks. So every attack should be investigated in detailly.
- We don't have enough data for 10 hackers (especially 3 hackers) to make an evaluation. But with the index messages gave us a clue that there isn't any special reason (espionage, political, social, economic, religion..etc) for attacking the .NL web sites.
- In summary, the targets are selected by the automatic scan tools, which detect vulnerabilities of servers (IP ranges). So, the motivation of hackers can be just fun, proving oneself, announcing something.

Detail of the second part: https://www.linkedin.com/pulse/why-199-hackers-preferred-attack-nl-websites-mehmet-serkan-kılıç/

### Used Libraries;
- BeautifulSoup
- Pandas
- Matplotlib

If the .ipynb couldnt see, please try:

https://nbviewer.jupyter.org/github/msklc/Analyzes-of-Hacked-Netherlands-Websites-2019-BeautifulSoup-Pandas-Matplotlib/blob/master/Hacked_NL_WebSites_3Q_2019.ipynb
