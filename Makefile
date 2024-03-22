all:
	(python3 mapper.py text.txt Australia | python3 combiner.py | python3 reducer.py) > percentage.txt
