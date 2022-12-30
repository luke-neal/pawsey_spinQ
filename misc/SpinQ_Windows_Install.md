# Requirements

This guide outlines how to install the SpinQ Triangulum software. It assumes a fresh install of Windows and no other software.

# Steps

1. Install Python

Download the latest version from https://www.python.org/downloads/windows/
Run the executable
Check the install worked by typing into the terminal:
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
Restart the terminal after the install is complete
Check the install worked by typing into the terminal:
```python
cmake --version
```

4. Install Visual Studio
Download the Windows installer from https://visualstudio.microsoft.com/downloads/
Run the executable
Make sure to select 'Desktop development with C++' in the installation options

5. SpinQ Software
Open a terminal in a folder of your choice
Execute the following command:
```python
curl "https://uniwa-my.sharepoint.com/personal/21469154_student_uwa_edu_au/_layouts/15/download.aspx?SourceUrl="%"2Fpersonal"%"2F21469154"%"5Fstudent"%"5Fuwa"%"5Fedu"%"5Fau"%"2FDocuments"%"2FSpinQ"%"2Ezip" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8" -H "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate, br" -H "Referer: https://uniwa-my.sharepoint.com/personal/21469154_student_uwa_edu_au/_layouts/15/onedrive.aspx?id="%"2Fpersonal"%"2F21469154"%"5Fstudent"%"5Fuwa"%"5Fedu"%"5Fau"%"2FDocuments"%"2FSpinQ"%"2Ezip&parent="%"2Fpersonal"%"2F21469154"%"5Fstudent"%"5Fuwa"%"5Fedu"%"5Fau"%"2FDocuments&ct=1672381408441&or=OWA"%"2DNT&cid=9579c3af"%"2D1dfc"%"2D52e0"%"2Ddc24"%"2D85b86f8416c1&ga=1" -H "Upgrade-Insecure-Requests: 1" -H "Sec-Fetch-Dest: iframe" -H "Sec-Fetch-Mode: navigate" -H "Sec-Fetch-Site: same-origin" -H "Connection: keep-alive" -H "Cookie: MicrosoftApplicationsTelemetryDeviceId=4dbebebf-63e2-0049-ae7a-bce4e2c402a1; MicrosoftApplicationsTelemetryFirstLaunchTime=1672381411549; rtFa=Z3LmLQdd7ddM17hfbiS9X3134cJTz3Pa1gPlEGUQhSAmMDU4OTRBRjAtQ0IyOC00NkQ4LTg3MTYtNzRDREI0NkUyMjI2IzEzMzE2ODU1MDEwNTk2OTA3NiMwMDNFODdBMC02MDRELTEwMDAtRkQyNi05OUIzOTgyNEFCNDQjMjExMDg5MDUlNDBTVFVERU5ULlVXQS5FRFUuQVVMG8XLVyjXZOLOCOiEy8zmnj4N/uo3klPqcGE/xKo+Yet8TEWVAXNgYQAxwBOoW2wEJ0TxFGUrFRa/eGNIwCPSy2cdG9bTbk0gGIPVCPLKUCgswZE5naophXz1ay6CJ3p65+M4MO+jgllF0MAHmtCW4Js/2mUfJkzKCsT143dA5tcMBhwmGgb6xvRGl8f586gm9cm3hlg6x1qpILdwZWT9MBvrPN8xLTm/3K/RTVMA3bttiE54mAykYP/DQlY9OtB+vjBA/h0A/PHwd2e4c05w6G5bMmNmlsO5S8Cpo+MHF91bCMuEtFsmoMry3A+TX86mP3uFo9YHDNSLXgtW49Y0mwAAAA==; SIMI=eyJzdCI6MH0=; FedAuth=77u/PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48U1A+VjEzLDBoLmZ8bWVtYmVyc2hpcHwxMDAzMjAwMGNmMjQzZjJiQGxpdmUuY29tLDAjLmZ8bWVtYmVyc2hpcHwyMTEwODkwNUBzdHVkZW50LnV3YS5lZHUuYXUsMTMzMTY4NTQ5NjgwMDAwMDAwLDEzMzA0NzU4MDQxMDAwMDAwMCwxMzMxNzI4NzAxMDU4MTIzODksMTI0LjE4OC4yMjYuMjAzLDMsMDU4OTRhZjAtY2IyOC00NmQ4LTg3MTYtNzRjZGI0NmUyMjI2LCw1YTk0MTU2Ni0wYWM5LTQ0MjctYTM3Yi1iNjUyNjJjMmZmNzAsMDAzZTg3YTAtNjA0ZC0xMDAwLWZkMjYtOTliMzk4MjRhYjQ0LDAwM2U4N2EwLTYwNGQtMTAwMC1mZDI2LTk5YjM5ODI0YWI0NCwsMCwxMzMxNjg1ODYxMDU0OTk3ODksMTMzMTcxMTQyMTA1NDk5Nzg5LCwsZXlKNGJYTmZZMk1pT2lKYlhDSkRVREZjSWwwaUxDSjRiWE5mYzNOdElqb2lNU0lzSW1GamNuTWlPaUpiWENKMWNtNDZkWE5sY2pweVpXZHBjM1JsY25ObFkzVnlhWFI1YVc1bWIxd2lYU0lzSW5CeVpXWmxjbkpsWkY5MWMyVnlibUZ0WlNJNklqSXhNVEE0T1RBMVFITjBkV1JsYm5RdWRYZGhMbVZrZFM1aGRTSXNJblYwYVNJNkltdDJVVXRpVldGeWNUQnBaWE5OZVVkVFowcG5RVkVpZlE9PSwxMzMxNjg1ODYxMDU4MTIzODksMTMzMTY4NTUwMTAwMDAwMDAwLGE0YjA0YmQyLWM4ZTEtNGRjZS05ZTRhLTMwNmFjNDY2ZjNiYywsLCwsLDAsLEFVU18yMTdfQ29udGVudCxHK25QcGFXYmN3T1Z2cUtMNU40Sm10U05Ea0xmakJTcFBGaG8yakN2bXFZd3l6Y3F5N09xLzlXOEMyNFkwb2ZESFlaM3k5YzBTSUN6Wm1zOGZxbEh3clNPdWY1c0tQaVl0YlhPYXY2TkxIemkyUmdleThBbzJoNUFQcThFVnN1REo3anFGd0ZtZk5kMGpJWk1TZjlLd0FPZjFkeUhnVEMvVExSeEovLzhwRDNxaVFzN2J1UTZ5Zk5vaHhSL0JRcVdmUjVPNkhrUkFUSVk5ZW91R2xoN010aTB1VzA3ZENNM05wRC9TTFpGWHNUYzd6NTE1UlJjYlY5dlNPVS9LQWdHR0ZXdVlzUldnN3RHTUt0QVlYK1JUejlndTBmUVJ5NVRVZi9qdGJvN1k5V1AvdmtSV29ocmpTNk9laERYOVhhR25TZTJiQUxjK1NrbXp3NWxxR0gwZmc9PTwvU1A+; cucg=0" --output SpinQ.zip
```
Extract the zip file (7zip is a good tool to do this)

Download the following GitHub repository as a zip file: https://github.com/SpinQTech/SpinQKit.git
Extract the zip file into the same location as the first folder
You should see two folders: SpinQ and SpinQKit-main
Open a terminal from the SpinQKit-main folder
Execute the following command:
```python
py setup.py install --user
```