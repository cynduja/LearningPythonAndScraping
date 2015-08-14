import requests
import json
from operator import itemgetter, attrgetter

response = requests.get("http://www.compjour.org/files/code/json-examples/nyt-books-bestsellers-hardcover-fiction.json")
text = response.text
data = json.loads(text)
books = data['results']['books']
#Way 1 without list comprehension
# b=0
# for bo in books:
# 	if bo['publisher'] == "Scribner":
# 		b+=1
#print "A.",b
#Way 2 with lc
# a = [b for b in books if b['publisher'] == "Scribner"]
# len a
print "A.", len([b for b in books if b['publisher'] == "Scribner"])
print "B.", len([b for b in books if "detective" in b['description'].lower()])
b=sorted(books, key=itemgetter('weeks_on_list'), reverse = True)
print "C. %s|%s"% (b[0]['title'], b[0]['weeks_on_list'])
b=sorted(books, key=itemgetter('rank_last_week'), reverse=True)
print "D. %s|%s|%s"%(b[0]['title'], b[0]['rank'], b[0]['rank_last_week'])
print "E.",len([b for b in books if b['rank_last_week']==0])
books_unranked_last_Week = [b for b in books if b['rank_last_week']==0]
new_book = min(books_unranked_last_Week, key=itemgetter('rank'))
print "F.", new_book['title'], new_book['rank']
books_ranked_last_week = [b for b in books if b['rank_last_week'] > 0]
# define a helper function
def calc_rank_change(book_obj):
	return book_obj["rank_last_week"] - book_obj["rank"]

x = max(books_ranked_last_week, key=calc_rank_change)
s = "|".join([x['title'], str(x['rank']), str(calc_rank_change(x))])
print "G.", s

x = min(books_ranked_last_week, key=calc_rank_change)
s="|".join([x['title'], str(x['rank']), str(calc_rank_change(x))])
print "H.", s

changes = [calc_rank_change(b) for b in books_ranked_last_week]
#print changes
x = [c for c in changes if c>0]
print "I.",sum(x)

books_dropped = [b for b in books_ranked_last_week if calc_rank_change(b)<0]
x = [c for c in changes if c<0]
print "J.", len(books_dropped),"|",sum(x) 
highest_count = [max(len(str(b['title'])) for b in books)]
print "K.", highest_count[0]
avg_count = [sum(len(str(b['title'])) for b in books)/len(books)]
print "L.",avg_count[0]

