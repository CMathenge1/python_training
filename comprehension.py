#generate numbers between 1000 and 10000
# ls= []
# for i in range(1000,10001):
#     if i%7==0:
#         ls.append(i)
# print(ls)
#comprehension
# lsc = [i for i in range(10,50) if i%7==0]
# print(lsc)
#can be a set , and can be converted to a tuple in either; list & set

blogs= [{"id":1, "title":"PCI", "description": "Starting..", "status":0},
        {"id":2, "title":"TSI", "description": "Starting..", "status":0},
        {"id":3, "title":"VS", "description": "Starting..", "status":1},
        {"id":4, "title":"K4", "description": "Starting..", "status":0},
        {"id":5, "title":"ZX", "description": "Starting..", "status":1},]

#Filter in the list only active blogs and change title to title case. use only maps and comprehension
# active_blogs= [blog for blog in blogs if blog['status']==1]
# print(active_blogs)

# def change_case(x):
#     x["title"] = x["title"].title()
#     return(x)

# clean_blog= list(map(change_case, active_blogs))
# print(clean_blog)

ab=[]
for blog in blogs: 
     if blog['status']==1:
        blog["title"] = blog["title"].title()
        ab.append(blog)
print(ab)


          


