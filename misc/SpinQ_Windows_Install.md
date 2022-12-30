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
curl 'https://uniwa-my.sharepoint.com/personal/21469154_student_uwa_edu_au/_layouts/15/download.aspx?SourceUrl=%2Fpersonal%2F21469154%5Fstudent%5Fuwa%5Fedu%5Fau%2FDocuments%2FSpinQ%2Ezip' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'Referer: https://uniwa-my.sharepoint.com/personal/21469154_student_uwa_edu_au/_layouts/15/onedrive.aspx?id=%2Fpersonal%2F21469154%5Fstudent%5Fuwa%5Fedu%5Fau%2FDocuments%2FSpinQ%2Ezip&parent=%2Fpersonal%2F21469154%5Fstudent%5Fuwa%5Fedu%5Fau%2FDocuments&ct=1670320886877&or=OWA%2DNT&cid=6b24fc99%2D40a7%2Dd8fd%2D6edd%2Dec9dd6d26579&ga=1' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: iframe' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: same-origin' -H 'Connection: keep-alive' -H 'Cookie: MicrosoftApplicationsTelemetryDeviceId=91ac2e59-5203-d7c2-0f7a-1ddcccebc28b; MicrosoftApplicationsTelemetryFirstLaunchTime=1670309695188; rtFa=0/A8itDjxSeArtCTEhN73uEB3JD9aJvRqPLAggMQT70mMDU4OTRBRjAtQ0IyOC00NkQ4LTg3MTYtNzRDREI0NkUyMjI2IzEzMzE0NzgzMzcwMDkyMTYyMCM1NDg2N0ZBMC0wMEFDLTEwMDAtRTlFMC0xNjVFRjI4RUVFMDAjMjExMDg5MDUlNDBTVFVERU5ULlVXQS5FRFUuQVUDUgm2pPA6pDEYmnXeJEJwwo++EEch+enMSER9RTE7QhwOwiLAGnfQbuMTaxULpchRGVVequqf/S6LDyw3LfKFZOgFAw1oyz/77D68vdCOIu4Skuiew3ZPRRAiVJgmfhicqWt2qfJU1NWIyjzCOhpBf+tawJqV3Gh7T3g/E9HTihPCx/bKPMCZX/OsaXcN5QEhMsTRaCzCao5FZr8RZOsfn3E7t28Rxj+GRJxkgpF5OEwiNzHTGhOSCOme+ph02XqqYMFyF778ESvbD8H6E0dgMaTvGVN5mvzesBXQ+/K73j0KDbEcBW8ygW6MjnDBllRq4i/tYnpZQMpUWHlPz4pnmwAAAA==; SIMI=eyJzdCI6MH0=; FedAuth=77u/PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48U1A+VjEzLDBoLmZ8bWVtYmVyc2hpcHwxMDAzMjAwMGNmMjQzZjJiQGxpdmUuY29tLDAjLmZ8bWVtYmVyc2hpcHwyMTEwODkwNUBzdHVkZW50LnV3YS5lZHUuYXUsMTMzMDc3ODQ0NjcwMDAwMDAwLDEzMzA0NzU4MDQxMDAwMDAwMCwxMzMxNTIyNTc0NDU4NTYyMTYsMTI0LjE4OC4yMjYuMjAzLDMsMDU4OTRhZjAtY2IyOC00NmQ4LTg3MTYtNzRjZGI0NmUyMjI2LCwzOTdhNmI2MC1hOWQ2LTRhMjYtYWIzYi0xN2YyN2ViNTU4OGEsNTQ4NjdmYTAtMDBhYy0xMDAwLWU5ZTAtMTY1ZWYyOGVlZTAwLDM5OTA3ZmEwLWUwODAtMTAwMC1lOWUwLTE1NTIzMDI5NzRmOCwsMCwxMzMxNDc5NzM0NDU3MDAwNjAsMTMzMTUwNTI5NDQ1NzAwMDYwLCwsZXlKNGJYTmZZMk1pT2lKYlhDSkRVREZjSWwwaUxDSjRiWE5mYzNOdElqb2lNU0lzSW1GamNuTWlPaUpiWENKMWNtNDZkWE5sY2pweVpXZHBjM1JsY25ObFkzVnlhWFI1YVc1bWIxd2lYU0lzSW5CeVpXWmxjbkpsWkY5MWMyVnlibUZ0WlNJNklqSXhNVEE0T1RBMVFITjBkV1JsYm5RdWRYZGhMbVZrZFM1aGRTSXNJblYwYVNJNkluRjJXV3h4YW5aMVFUQkRTRmc1TkRkRk9FTjRRVUVpZlE9PSwxMzMxNDc4Njk3MDA3NjY2MTAsMTMzMTQ3ODMzNjkwMDAwMDAwLGE0YjA0YmQyLWM4ZTEtNGRjZS05ZTRhLTMwNmFjNDY2ZjNiYywsLCwsLDAsLEFVU18yMTdfQ29udGVudCxDYlJBRkxEYlNTRC9rNXRYM0c1T2NhbzFkWUNwdXY2MzVuRzM0eTZWUFdRMmFBZ3VZcnZ6eUR0cU9neTRpRWc0S3B5V0ZkQ0UydERiQ3k4ZEdjNVlSdTlqWHlHTjBTUTBHaVJjc1U2VzNVZFo2cXRQTmlaTkhLSURKZERMOFFvT1ZGKzg5VktUcjBWZUFxbThqQ09hN3ZQUmtUS0RwUTByV3lRVmxSTkJkUWpCNWMwem5Mc2pCdWJraDV3bndwbVpSdWZJTG9MRGVCdlBKd1RieGlTUG1QUXlEYkc5blQzRnBRSkhMSGJORFZOK2MzaWQrS0hQeXlobnNhcEw5cWRrVkVMMElPMXRuRTZwaU1MQUtOckJkanlQd0c0UlpLbzMwZzNvSEJ0cW9oNHNWNkcxT1MwdXJDeXNaYjFOSHNhM0x5UTlRVWhZZ1BOQjNyeXBvODZZZFE9PTwvU1A+; cucg=0; odbn=1' --output SpinQ.zip
```