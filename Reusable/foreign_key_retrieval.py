

# THis is the same as many to one relationship

# if an article has reporter as a foreign key here then we can do below
from datetime import date

from Util.foreign_key import Article, Reporter

Article.objects.filter(reporter__first_name='John')




# ALl article has access to its reporter here

# If you were to create a reporter
r = Reporter(first_name='John', last_name='Smith', email='john@example.com')
a = Article(id=None, headline="This is a test", pub_date=date(2005, 7, 27), reporter=r)
r = a.reporter

#If you want to do a reverse lookup, use article_set
r.article_set.all()
r.article_set.count()       # Will tell u how many articles there are as well