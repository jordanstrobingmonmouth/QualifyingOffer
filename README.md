# QualifyingOffer

First, I would like to thank the Phillies for the opportunity to build this program. It was extremely fun to build this and learn BeautifulSoup along the way.

To run this program, just put it in your IDE or console and it will display the correct output. Make sure to have BeautifulSoup, requests, and html5lib installed. 

If you don't, put this into the console:

pip install requests

pip install html5lib

pip install bs4

Link to the file that I uploaded to DropBox: https://www.dropbox.com/sh/mk12zunn1wnxxwf/AAAw1G8RQn0J0GShWYFmSkVka?dl=0

Sample ouput: 

![image](https://user-images.githubusercontent.com/71049431/138570241-7227e26c-28e1-4893-b9a5-261af0fb5ead.png)

Here's a step by step outline of how the program works:

1. I created the URL variable and set r to be able to retrieve the URL.
![image](https://user-images.githubusercontent.com/71049431/138570274-b37e1048-c88c-4752-a63f-41631d8f90bd.png)

2. I created the soup object to be able to parse the HTML page.
![image](https://user-images.githubusercontent.com/71049431/138570290-9124438a-996f-4d5a-936c-df8e39785a39.png)

3. I created a salaries variable that uses soup to find every player in the MLB's salary. This was achieved by using the td tag and then narrowing it down into player-salary.
![image](https://user-images.githubusercontent.com/71049431/138570299-a0df7f97-e677-4288-a926-718df783d6cf.png)

4. I created an empty list called salaryInt that will fill up with all the salaries.
![image](https://user-images.githubusercontent.com/71049431/138570317-6c0b900b-a556-475a-9d64-14e53901f706.png)

5. I started a for loop that iterated over every single salary in the MLB. Within the for loop I created an empty string and changed salary to a string data type.
![image](https://user-images.githubusercontent.com/71049431/138570342-b003c484-9d07-4868-a4a9-3f42e1be3692.png)

6. Within the original for loop, I created a nested for loop that iterated over the string and detected if any character was a digit. If a character was a digit, it was concatenated onto the once empty string.
![image](https://user-images.githubusercontent.com/71049431/138570356-44636d31-f64c-4129-8c88-466b963f1e66.png)

7. Still within the original for loop, I created an if statement to handle the errror of empty salaries. If there was an empty string, I continued to the next iteration. If not, I appended the string to the list AND converted it to a float. Loop ends.
![image](https://user-images.githubusercontent.com/71049431/138570365-ece1a9fe-5710-41b9-aa6c-0891a9edc8e4.png)

8. After the list was filled with all salaries, I used the heapq library's nlargest function. This allowed me to isolate the 125 highest salaries into a new list called qoPlayers.
![image](https://user-images.githubusercontent.com/71049431/138570374-00c5a20b-ebf6-47c5-9b59-68b880e4f3aa.png)

9. I created a sum variable, then added every salary in qoPlayers using a for loop to get the total salary of the 125 highest paid players.
![image](https://user-images.githubusercontent.com/71049431/138570392-3b447744-cae9-463d-8c92-b88dbe97e352.png)

10. Next, I got the value of the qualifying offer by dividing the total salary of the top 125 by 125.

11. I then used string formatting to get commas between every three digits, so that the number is more readable to the user.
![image](https://user-images.githubusercontent.com/71049431/138570413-380315cf-c5b0-44b8-9926-90e1a6ab0043.png)

12. Finally, I displayed the value of the qualifying offer to the user. I also added the total salary of the top 125 players because I thought it was interesting. The QO value changes on every iteration, but it stays in a similar range.
![image](https://user-images.githubusercontent.com/71049431/138570421-571613cb-886b-45fd-ae16-9b531c785def.png)

Something extra I'd like to mention is I think my error handling of this program worked out well. I looked through the first 50 and last 50 players' salaries and all were correct in my scraping.
