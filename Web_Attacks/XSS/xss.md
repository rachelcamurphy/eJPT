#XSS
#RCM 8/21
Javascript Test:
Stored XSS test:
<script>alert('xss');</script>
- shows pop up as a stored XSS.

#Stealing cookies with XSS Stored and Reflected Vulnerabilities
<script>alert('document.cookie')</script>
- cookies should be displayed in alert pop up box.
- don't want users to see the "alert"
