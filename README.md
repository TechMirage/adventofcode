# Advent of Code Solutions
Solutions to the Advent of Code puzzles!

For those of you that don't know, Advent of Code is a series of programming challenges/puzzles that are designed by Eric Wastl and released as an Advent calendar every year since 2015. Each year has a loose story connecting the puzzles and there are two puzzles a day. They are excellent both for learning new things, but also to practice weird and esoteric things that you may not have reason to play with most of the time. 

Over the course of the next few months, I hope to use this repo to consolidate all of my solutions that I've worked on over the years into this one repo for cleaning purposes. They will be categorized first by year, then by day, then by language (since I hope in the future to have more time to add solutions in other languages). My main goal will be to do them all first in Python and then see where I go from there. This repo will hold 2020's solutions as well and continue to be filled out as I finish them. 

I'm not sure how I will go about documenting necessarily, but here's hoping we figure something out as the repo grows!

[Advent of Code](http://adventofcode.com) is the website to check out the original puzzles!

### Installation

2020 is the only year that uses something non-standard yet. It uses a library called "advent-of-code-data" to pull data directly from the site so that you don't have to create an input.txt, like the previous years so far. There is a requirements.txt that can be pip installed or you can pip install the library directly. It requires that you have your session ID saved as an environment variable called "SESSION_ID", which you can retrieve from the input page header information on their site.
