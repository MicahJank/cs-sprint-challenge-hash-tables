# Your code here
# files is a list of filepath strings
# queries are strings of searched files
# need to return a list of files that have the search queries in them


# PLAN
# loop through the files list
# split the string into a list using the seperator '/' 
# loop through the new list of strings and add them to the dictionary as keys - values would be the path that those strings belong to
# after the dictionary is filled i can loop through the queries
# check to see if each query is in the dictionary
# if it is put the value of that dictionary key (the path) in the results list
# return the result list after completed
paths_dict = {}

# 2.8s!!!
# def populatePathsDict(files):
#     for file in files:
#         queries = file.split('/')

#         for query in queries:
#             if query not in paths_dict:
#                 paths_dict[query] = [file]
#             else:
#                 paths_dict[query].append(file)

# def finder(files, queries):
#     result = []
#     populatePathsDict(files)

#     for query in queries:
#         if query in paths_dict:
#             result += paths_dict[query]

#     return result

# decrease to 1.4s
def populatePathsDict(files):
    for file in files:
        queries = file.split('/')

        # gives the last item in the queries list -i.e the query a user would search
        query = queries[-1]

        if query not in paths_dict:
            paths_dict[query] = [file]
        else:
            paths_dict[query].append(file)

def finder(files, queries):
    result = []
    populatePathsDict(files)

    for query in queries:
        if query in paths_dict:
            result += paths_dict[query]

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
