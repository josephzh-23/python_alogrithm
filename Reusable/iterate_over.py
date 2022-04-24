


#For iterate over property of, you can't use this outside of Django model
from tutor.models import Posting



# For iterate over property of, you can't use this outside of Django model
"""
If you use this here probably won't work 
"""
for field in Posting._meta.fields:
    print(field.name)