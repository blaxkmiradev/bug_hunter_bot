# dorks.py

# A dictionary containing categories and their corresponding dork templates.
# The {domain} placeholder will be replaced by the user's input.
DORK_TEMPLATES = {
    "SQL Injection (SQLi)": 'site:{domain} inurl:"?id=" | inurl:"?page="',
    "Exposed Documents": 'site:{domain} ext:pdf | ext:doc | ext:docx | ext:xls | ext:xlsx',
    "Directory Listing": 'site:{domain} intitle:"index of"',
    "Configuration & Log Files": 'site:{domain} ext:env | ext:log | ext:conf | ext:bak | ext:yml',
    "Login Portals": 'site:{domain} inurl:login | inurl:signin | intitle:login | intitle:admin',
    "Open Redirects": 'site:{domain} inurl:url= | inurl:return= | inurl:next= | inurl:redirect=',
    "WordPress Endpoints": 'site:{domain} inurl:wp-content | inurl:wp-includes | inurl:wp-admin',
    "Database Files": 'site:{domain} ext:sql | ext:db | ext:sqlite',
    "API Endpoints": 'site:{domain} inurl:api | inurl:v1 | inurl:v2 | ext:json',
    "Github/Git Exposures": 'site:{domain} inurl:"/.git/" | intitle:"index of /.git"'
}
