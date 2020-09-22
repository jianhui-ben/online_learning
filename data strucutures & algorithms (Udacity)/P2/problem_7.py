# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root=RouteTrieNode()

    def insert(self, path, handler_name=''):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        cur_node= self.root
        sub_dir_list= path.split('/')
        ori_handler_name=handler_name
        for dir in sub_dir_list[1:]: ## remove the first root node
            cur_node.insert(dir)
            cur_node=cur_node.children[dir]
            if handler_name:
                handler_name+=dir +' '
        if ori_handler_name!='':
            cur_node.handler=ori_handler_name
        elif not ori_handler_name:
            cur_node.handler=None
        else:
            cur_node.handler=handler_name+'handler'
        
    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        cur_node= self.root
        sub_dir_list= path.split('/')
        for dir in sub_dir_list[1:]:
            if dir!='':
                if dir not in cur_node.children:
                    return None
                else:
                    cur_node=cur_node.children[dir]
        return cur_node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.handler= None
        self.children={}

    def insert(self, sub_dir):
        # Insert the node as before
        if sub_dir not in self.children:
            self.children[sub_dir]=RouteTrieNode()

### test case for RouteTrie:
#MyRouteTrie=RouteTrie()
#path='/path/a/b'
#MyRouteTrie.insert(path)
#MyRouteTrie.find('/path/a/')

# The Router class will wrap the Trie and handler 
class Router:
    def __init__(self, root_handler='root handler', not_found_handler= 'not found handler'):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routeTrie=RouteTrie()
        self.routeTrie.root.handler= root_handler
        self.not_found_handler=not_found_handler

    def add_handler(self, path, handler_name):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.routeTrie.insert(path, handler_name)


    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        handler= self.routeTrie.find(path)
        if handler:
            return handler
        return self.not_found_handler

    ##this similar method I have defined at the class RouteTrie
    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        l=path.split('/')
        return [i for i in l if i!='']




# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

router.add_handler("/home/about/work", None)  # add a route with None as the handler name; this will show 'not found handler'

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one


print(router.lookup("/home/about/work"))  ##'not found handler'

router.add_handler("", None)  # this will change the root handler to None
print(router.lookup("/")) # should print 'not found' for the root node