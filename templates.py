# Layout template

title_template= """
<div style= "background-color:#F0F0F0; border-radius:30px; padding:10px,margin:10px;">
<h4 style="color:black; text-align:center; ">{}</h4>
<h4 style="margin: 1em 0 0.5em 0;
	font-weight: 600;
	font-family: 'Titillium Web', sans-serif;
	position: relative;
	text-shadow: 0 -1px 1px rgba(0,0,0,0.4);
	font-size: 22px;
	line-height: 40px;
	color: #355681;
    text-align: center;
	text-transform: uppercase;
	border-bottom: 1px solid rgba(53,86,129, 0.3); ">{}</h4>
<h4 style="color:black; text-align:center; ">Book Title:{}</h4>
<h4 style="color:black; text-align:center; ">Author:{}</h4>
<h4 style=" display: block;
    width: 170px;
    height: 50px;
    background: #4E9CAF;
    padding: 10px;
    text-align: center;
    border-radius: 5px;
    color: white;
    font-weight: bold;
    line-height: 25px;">Date: {}</h4>
<p style="background-color:powderblue; text_align:center;border-radius:30px;">{}</p>
</div>
"""
selected_review_template= """
<div>
<h4 style="margin: 1em 0 0.5em 0;
	font-weight: 600;
	font-family: 'Titillium Web', sans-serif;
	position: relative;
	text-shadow: 0 -1px 1px rgba(0,0,0,0.4);
	font-size: 22px;
	line-height: 40px;
	color: #355681;
    text-align: center;
	text-transform: uppercase;
	border-bottom: 1px solid rgba(53,86,129, 0.3); ">{}</h4>
<h4 style="color:black; text-align:center; font-style: italic; ">By {}</h4>
<h4 style="color:black; text-align:center; ">Book Title: {}</h4>
<h4 style="color:black; text-align:center; ">Author: {}</h4>
<h4 style="color:black; text-align:center;">Date: {}</h4>
<p></p>
<p style="border:3px; border-style:solid; border-color:#355681; padding: 1em;">{}</p>
</div>
"""
