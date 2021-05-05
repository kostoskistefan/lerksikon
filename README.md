# Lerksikon (Лерксикон)

Lerksikon is a program that parses the Macedonian dictionary and extracts and modifies specific words to make them sound a little bit more Russian.

#### Example words:
 * Прв becomes Перв
 * Дрво becomes Дерво
 * Штрк becomes Штерк

### Algorithm

Find all words that contain the letter "р" ("r" in latin). If the letter "р" is between two consonants, then add the letter "e" before the letter "р", becoming "ер" (ER).

## Why

No idea... I find the modified words funny to say out loud.

## Requirements

 * Python 3 (tested on python 3.9)
 * Python Libraries:
   * BeautifulSoup
   * Tqdm
   * Requests
   * Re (Regex)
   * Futures

## Usage

 * Clone this repository: `git clone https://github.com/kostoskistefan/lerksikon.git`
 * Open the downloaded folder
 * Run `pip install -r requrements.txt`
 * Run `python lerksikon.py > lerksikon.txt`
 * Wait until it finishes
 * You should have your up to date lerksikon ready for usage. Look for a file named `lerksikon.txt` in the same folder in which you ran the script.
