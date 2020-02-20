email = 'andy.bazualdo@jalasoftdevelopment.onmicrosoft.com'
subj = 'testing new account'
subj2 = 'Meet for lunch?'
filterSubject = "$select=sender,subject,body&$filter=Subject eq 'testing new account'"
emailToSent = '{"message": {"subject": "Meet for lunch?","body": {"contentType": "text","content": "The new ' \
              'cafeteria is open."},"toRecipients": [{"emailAddress": {"address": ' \
              '"andy.bazualdo@jalasoftdevelopment.onmicrosoft.com"}}],' \
              '"ccRecipients": [{"emailAddress": {"address": "andy2@mailinator.com"}}]},"saveToSentItems": "true"}'
