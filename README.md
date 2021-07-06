# Supermarket Sale Scraper

Scrape sale information from supermarket flyer website. The flyer is dynamically 
loaded on the webpage, therefore I used [selenium](https://selenium-python.readthedocs.io/) 
to retrieve the dynamic data.

To run the script
```bash
PATH=$PATH:./geckodriver:./chromedriver
/usr/local/bin/python3 scrape.py
```

## Requirements
```bash
pip install selenium selenium-wire
```
The script also uses `Chrome 91`

## Output
There are some example output
```
1.29     Mardi Gras Potato Salad
1.99     Asian Noodle Salad
4.99     Pepsi Products
4.99     Nando's Perinaise Sauce
4.99     Club House La Grille Signature Blend Seasoning
4.49     Lipton Iced Tea
2.99     Western Family Ketchup
7.99     Mitchell's Hot Dog Wieners
2.49     Kraft Salad Dressing
4.99     Propel Water
1.99     Bush's Best Baked Beans
3.49     Heinz Ketchup
3.49     Mott's Clamato
3.99     Hellmann's Pourable Salad Dr
```
