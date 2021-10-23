# QualifyingOffer

First, I would like to thank the Phillies for the opportunity to build this program. It was extremely fun to build this and learn BeautifulSoup along the way.

To run this program, just put it in your IDE or console and it will display the correct output. Make sure to have BeautifulSoup, requests, and html5lib installed. 

If you don't, put this into the console
pip install requests
pip install html5lib
pip install bs4

Link to the file that I uploaded to DropBox: https://www.dropbox.com/sh/mk12zunn1wnxxwf/AAAw1G8RQn0J0GShWYFmSkVka?dl=0

Here's a step by step outline of how the program works:

1. I created the URL variable and set r to be able to retrieve the URL.

2. I created the soup object to be able to parse the HTML page.

3. I created a salaries variable that uses soup to find every player in the MLB's salary. This was achieved by using the td tag and then narrowing it down into player-salary.

4. I created an empty list called salaryInt that will fill up with all the salaries.

5. I started a for loop that iterated over every single salary in the MLB. Within the for loop I created an empty string and changed salary to a string data type.

6. Within the original for loop, I created a nested for loop that iterated over the string and detected if any character was a digit. If a character was a digit, it was concatenated onto the once empty string.

7. Still within the original for loop, I created an if statement to handle the errror of empty salaries. If there was an empty string, I continued to the next iteration. If not, I appended the string to the list AND converted it to a float. Loop ends.

8. After the list was filled with all salaries, I used the heapq library's nlargest function. This allowed me to isolate the 125 highest salaries into a new list called qoPlayers.

9. I created a sum variable, then added every salary in qoPlayers to get the total salary of the 125 highest paid players.

10. Next, I got the value of the qualifying offer by dividing the total salary of the top 125 by 125.

11. I then used string formatting to get commas between every three digits, so that the number is more readable to the user.

12. Finally, I displayed the value of the qualifying offer to the user. I also added the total salary of the top 125 players because I thought it was interesting. The QO value changes on every iteration, but it stays in a similar range.

Something extra I'd like to mention is I think my error handling of this program worked out well. I looked through the first 50 and last 50 players' salaries and all were correct in my scraping.
