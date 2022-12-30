# Requirements

This guide outlines how to install the SpinQ Triangulum software. It assumes a fresh install of Windows and no other software.

# Steps

1. Install Python

Download the latest version from https://www.python.org/downloads/windows/
Run the executable
Check the install worked by typing into the console:
```python
py --version
```

2. Install pybind
```python
py -m pip install pybind11
```

3. Install CMake
Download the Windows installer from https://cmake.org/download/
Run the executable
During the installation, make sure to check the option to add CMake to the system path
Restart the console after the install is complete
Check the install worked by typing into the console:
```python
cmake --version
```

4. SpinQ Software
Download the following GitHub repository as a zip file: https://github.com/SpinQTech/SpinQKit.git
Extract it into a location of your choice (7zip is a good tool to do this)

Open your console in the same location that you extracted the above files
Execute the following command:
```python
curl "https://uniwa-my.sharepoint.com/personal/21469154_student_uwa_edu_au/_layouts/15/download.aspx?SourceUrl="%"2Fpersonal"%"2F21469154"%"5Fstudent"%"5Fuwa"%"5Fedu"%"5Fau"%"2FDocuments"%"2FSpinQ"%"2Ezip" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8" -H "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate, br" -H "Referer: https://uniwa-my.sharepoint.com/personal/21469154_student_uwa_edu_au/_layouts/15/onedrive.aspx?id="%"2Fpersonal"%"2F21469154"%"5Fstudent"%"5Fuwa"%"5Fedu"%"5Fau"%"2FDocuments"%"2FSpinQ"%"2Ezip&parent="%"2Fpersonal"%"2F21469154"%"5Fstudent"%"5Fuwa"%"5Fedu"%"5Fau"%"2FDocuments&ct=1672380993515&or=OWA"%"2DNT&cid=8b04e8c1"%"2D201c"%"2Dd65e"%"2Dcb08"%"2D6e81a4f2fa20&ga=1" -H "Upgrade-Insecure-Requests: 1" -H "Sec-Fetch-Dest: iframe" -H "Sec-Fetch-Mode: navigate" -H "Sec-Fetch-Site: same-origin" -H "DNT: 1" -H "Sec-GPC: 1" -H "Connection: keep-alive" -H "Cookie: MicrosoftApplicationsTelemetryDeviceId=e0c609a5-9d07-618f-1b61-eea4dc81aae2; MicrosoftApplicationsTelemetryFirstLaunchTime=1669137768438; PowerPointWacDataCenter=GAU3; WacDataCenter=GAU3; rtFa=4wFwSJGW7VtzHUPjOOEUsx9gqMLfFECk0uX+Zs3aL3AmMDU4OTRBRjAtQ0IyOC00NkQ4LTg3MTYtNzRDREI0NkUyMjI2IzEzMzE2ODU0NTk2MjE2Nzg4MSM5QjNEODdBMC1CMDIwLTEwMDAtRTlFMC0xODdDOTkxRjEyQzUjMjExMDg5MDUlNDBTVFVERU5ULlVXQS5FRFUuQVWTgdlvPubEIWFcO24ZR9r1DVRTE+1mnD7RvfFI9v6TT09BQu26CvJ09OPnc1xAm0tACcdt2md42rsV8UEFy0dLFGdNw8vByYeDLO6Sjl0rvP4ph/wO3gtM/z4LGg6f5snJWYgn15O23KS+7EzfGMUjTbD1QVXZJTqp7raxGA+RcZpRAGn0qCfI8DND33f0jTmxem2NXhgamyS4KXcCDiQekl486W3yJnl/hHUTh8QBbiDD1XkHp9Vr+ZYQMev+qgAempBdK6MSswNF7LiZBX2BhnesU31Mgi4qcEUg6g3wMfWOikiTko0iQBQTo8MM9VRjnrgjHxl9+hARyHuTBMJgmwAAAA==; SIMI=eyJzdCI6MH0=; FedAuth=77u/PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48U1A+VjEzLDBoLmZ8bWVtYmVyc2hpcHwxMDAzMjAwMGNmMjQzZjJiQGxpdmUuY29tLDAjLmZ8bWVtYmVyc2hpcHwyMTEwODkwNUBzdHVkZW50LnV3YS5lZHUuYXUsMTMzMDQ3NTgwNTIwMDAwMDAwLDEzMzA0NzU4MDQxMDAwMDAwMCwxMzMxNzI4NjU5NjIwMTE3NTYsMTI0LjE4OC4yMjYuMjAzLDMsMDU4OTRhZjAtY2IyOC00NmQ4LTg3MTYtNzRjZGI0NmUyMjI2LCw5ZGRhMjk1ZS0wM2E1LTRhZjAtOTZhYy0wNDU1NjMzOTg5MDcsOWIzZDg3YTAtYjAyMC0xMDAwLWU5ZTAtMTg3Yzk5MWYxMmM1LDliM2Q4N2EwLWIwMjAtMTAwMC1lOWUwLTE4N2M5OTFmMTJjNSwsMCwxMzMxNjg1ODE5NjE1NDI5ODAsMTMzMTcxMTM3OTYxNTQyOTgwLCwsZXlKNGJYTmZZMk1pT2lKYlhDSkRVREZjSWwwaUxDSjRiWE5mYzNOdElqb2lNU0lzSW1GamNuTWlPaUpiWENKMWNtNDZkWE5sY2pweVpXZHBjM1JsY25ObFkzVnlhWFI1YVc1bWIxd2lYU0lzSW5CeVpXWmxjbkpsWkY5MWMyVnlibUZ0WlNJNklqSXhNVEE0T1RBMVFITjBkV1JsYm5RdWRYZGhMbVZrZFM1aGRTSXNJblYwYVNJNkltbFVkVzlOY0Vacll6Qlhka3d4YlVkRlptbG5RVkVpZlE9PSwxMzMxNjg1ODE5NjIwMTE3NTYsMTMzMTY4NTQ1OTUwMDAwMDAwLGE0YjA0YmQyLWM4ZTEtNGRjZS05ZTRhLTMwNmFjNDY2ZjNiYywsLCwsLDAsLEFVU18yMTdfQ29udGVudCxYUnRVSjBnbmZnS1o0K1NKZlBTbHFrcnhLdS9ZYlhWZmgrYUVsRkkxS3FvaHUrU0hHUkx4N0crbFJpZE9TSktwSzRGSVVEaUJ5L0IrVGRsVDZBUHBOanFja1ZEOW5qN0lFOXhJUngrZk1Jby80czRvcmhnRmMyWVN6NWR2dmpVNkFmSGg3UGpHaStCd3FSTzhqL1JWNzBFVzVFQlk2ZmVUWTVianhWaUNDNVhLMlhUaEkvbUY1QW50RUFHQ1I5bXRJWmxXZFJ1dXJicERCTW5aM054UUN1ODR2c0RKekRzVzlUbWlVWVM3b0U5TS9Nb09hcHNDRkpzMndjc250YXg5VkpzaHlJYVREekFTcFVFZEZ3cHo4Y2t5c3NzcFpaYS9MTnUzSGdUdmo3Q2d2R1VUNno4RUtrNnRoMzNFUjVNMjR2ZmpRc1FSYllTdnhjdDcvczhWT0E9PTwvU1A+; cucg=0" --output SpinQ.zip
```