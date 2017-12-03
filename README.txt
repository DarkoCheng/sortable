Name: Darko (you know my real name :))
Date: 2017/12/02
Sortable

Build a Python program to match listing.txt with products.txt and output the
result as Json format in result.txt

Questions:
1. do you make many false matches?
Based on manufacturer, model and family, I do not think I made any false
match for the provided files.
2. how many correct matches did you make?
3263 in total.

what are the assumptions and limitations of your solution:
1.In order to increase accuracy for matching, each product in products.txt must
had manufacturer, model and family.
2. Due to time limitation, I did not fully test the program and do the error
prevention.
3. Did not optimize the algorithm, so the efficiency of my solution maybe low.

Some future test cases and error preventions:
1. The file has incorrect Json format.
2. Wrong command line arguments inputs.

how can a user build and test your program (also called the user guide):
1. type: python3 sortable.py ../TestCases/products.txt ../TestCases/listings.txt
2. Source code is in src folder, test files are in testCases folder
3. If you need to use your test files, you need to type following command:
python3 ./sortable <your products file> <your listings file>
