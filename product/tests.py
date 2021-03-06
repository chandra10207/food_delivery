# from django.test import TestCase
# from .models import Person, Group, GroupMember
#
#
# class M2MThroughTest(TestCase):
#
#     def setUp(self):
#         # Create three people:
#         self.joe = Person.objects.create(name='Joe')
#         self.jim = Person.objects.create(name='Jim')
#         self.bob = Person.objects.create(name='Bob')
#
#         # And three groups:
#         self.jocks = Group.objects.create(name='Jocks')
#         self.nerds = Group.objects.create(name='Nerds')
#         self.skaters = Group.objects.create(name='Skaters')
#
#         # Every person is a member of every group, but
#         # Joe admins jocks, Jim admins nerds, and Bob admins skaters.
#         GroupMember.objects.create(person=self.joe, group=self.jocks, type="admin")
#         GroupMember.objects.create(person=self.jim, group=self.jocks, type="member")
#         GroupMember.objects.create(person=self.bob, group=self.jocks, type="member")
#
#         GroupMember.objects.create(person=self.joe, group=self.nerds, type="member")
#         GroupMember.objects.create(person=self.jim, group=self.nerds, type="admin")
#         GroupMember.objects.create(person=self.bob, group=self.nerds, type="member")
#
#         GroupMember.objects.create(person=self.joe, group=self.skaters, type="member")
#         GroupMember.objects.create(person=self.jim, group=self.skaters, type="member")
#         GroupMember.objects.create(person=self.bob, group=self.skaters, type="admin")
#
#     def test_unfiltered_membership(self):
#         # Which groups is Jim in?
#         jims_groups = Group.objects.filter(people=self.jim)
#         self.assertEqual(list(jims_groups), [self.jocks, self.nerds, self.skaters])
#
#     def test_admin_groups(self):
#         # But which groups does Jim admin?
#         jim_admins = Group.objects.filter(people=self.jim, membership__type='admin')
#         self.assertEqual(list(jim_admins), [self.nerds])
#
#     def test_member_groups(self):
#         # And which groups is Bob just a member of?
#         bob_membership = Group.objects.filter(people=self.bob, membership__type='member')
#         self.assertEqual(list(bob_membership), [self.jocks, self.nerds])