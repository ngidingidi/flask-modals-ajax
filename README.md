This is a demonstration of how to incorporate AJAX (asynchronous javascript and xml) in a Flask web application to display modal pop-ups when a user clicks a button on a table. 

AJAX is powerful because it allows information to be displayed on the same web page without reloading the page and that makes for an improved user experience. You can read more about the details of how AJAX works in this article: https://www.w3schools.com/xml/ajax_intro.asp

After spending some time researching how to incorporate AJAX in Flask, I thought it would be beneficial to share my learnings. In this project, I created fake data which is just a csv file which contains the cost price of famous brands (nike, adidas, puma) for a short time period. I use flask to display the data in the form of a bootstrap html table on the web. I add a clickable button to each table row. When a user clicks on the button, a modal pops up and displays a scatterplot of the cost of a brand (from that particular row) over time. 

To achieve this goal, I use jQuery to obtain the row value of the brand column each time a user clicks on the row. Then I use AJAX to send the selected row value to the server (Python Flask) in a POST request. In Flask, I use this value to create a dataframe subset which contains data from that specific brand. I create a scatterplot chart using the Plotly visualization library and send that chart in JSON format back to the client side (AJAX takes care of the POST and GET request). On the client side, I open a modal pop up and render the response (which is a JSON Plotly chart) inside the modal.

Here are some of the resources which helped me achieve this:

https://stackoverflow.com/questions/2315600/jquery-getting-the-text-value-of-a-table-cell-in-the-same-row-as-a-clicked-ele
https://stackoverflow.com/questions/37631388/how-to-get-data-in-flask-from-ajax-post
https://codehandbook.org/python-flask-jquery-ajax-post/
https://www.bogotobogo.com/python/Flask/Python_Flask_with_AJAX_JQuery.php
https://blog.heptanalytics.com/flask-plotly-dashboard/

I hope someone will find this helpful. I certainly benefitted from what others had shared on the web. If you have any questions, feel free to email me at sicelomasango@gmail.com. 