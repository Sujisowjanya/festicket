**Instructions for Mac**
1. Install required packages selenium pytest
   **pip install selenium pytest**
   
2. Clone the repository and navigate to tests directory
3. Run the test using the following command
   **py.test -sv Login_tests.py**
   
   
**Instructions for Windows**
1. Install Python and pip first
2. Install required packages selenium pytest
   pip install selenium pytest
   
3. Clone the repository and navigate to tests directory
4. Run the test using the following command
   py.test -sv Login_tests.py
   
   
**Instructions for Linux**
1. Install pip using yum or apt-get
2. Install required packages selenium pytest
   pip install selenium pytest
   
3. Clone the repository and navigate to tests directory
4. Run the test using the following command
   py.test -sv Login_tests.py
   

**Analysis**

1. Some locators were hard to find so i had to use absolute xpath
2. timing issues where the page load takes longer time so i created wait for method to handle that
3. if there was more time i will change all the absolute xpath to relative xpath or css
4. the html for the profile icon differs when when its on home page and on account edit page so had to use two different locators
5. I have used pytest as my framework as its open source and provide more robustness with test execution


   
