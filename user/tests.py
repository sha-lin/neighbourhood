from django.test import TestCase
from .models import Profile

# Create your tests here.


class ProfileTestClass(TestCase):
    def setUp(self):
        self.new_profile = Profile(user='dollah',
                                   bio='i love coding',
                                   profile_photo='image.png')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def update_profile(self):
        self.new_profile.save_profile()
        profile_id = self.new_profile.id
        Profile.update_profile(id, "test_update")
        self.assertEqual(self.caption.caption, "test_update")

    def test_delete_profile(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)