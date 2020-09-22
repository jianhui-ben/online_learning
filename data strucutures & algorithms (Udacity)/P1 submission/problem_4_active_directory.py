class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.users:
        return True
    for sub_group in group.groups:
        return is_user_in_group(user, sub_group)
    return False

##Test cases

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
test_user='test_user'

child.add_group(sub_child)
child.add_user('child_user')
parent.add_group(child)
parent.add_user('parent_user')
parent.add_user('father_user')
test_group= Group("test")


#test1
is_user_in_group(sub_child_user, parent)
#test2: empty group
is_user_in_group(sub_child_user, test_group)
#test3: unrelated user
is_user_in_group(test_user, child)

