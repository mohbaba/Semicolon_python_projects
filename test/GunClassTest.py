import unittest

from GunClass.GunClass import Gun
from GunClass.GunType import GunType


class MyTestCase(unittest.TestCase):

    def test_that_gun_class_has_accurate_magazine(self):
        auto_rifle: Gun = Gun(GunType.ASSAULT)
        pistol: Gun = Gun(GunType.PISTOL)
        shot_gun: Gun = Gun(GunType.SHOTGUN)
        sniper: Gun = Gun(GunType.SNIPER)

        self.assertEqual(100, auto_rifle.clip_size)
        self.assertEqual(30, pistol.clip_size)
        self.assertEqual(20, shot_gun.clip_size)
        self.assertEqual(30, sniper.clip_size)

    def test_that_gun_will_not_shoot_if_not_loaded_with_bullets(self):
        assault_rifle: Gun = Gun(GunType.ASSAULT)
        with self.assertRaises(Exception):
            assault_rifle.shoot()

    def test_that_gun_will_shoot_when_loaded_with_bullets(self):
        assault_rifle: Gun = Gun(GunType.ASSAULT)
        assault_rifle.reload(30)
        assault_rifle.shoot()
        self.assertEqual(29, assault_rifle.ammo_left)

    def test_that_Gun_cannot_shoot_negative_bullets(self):
        pistol: Gun = Gun(GunType.PISTOL)
        pistol.reload(30)

        with self.assertRaises(Exception):
            for bullet in range(40):
                pistol.shoot()

    def test_that_gun_will_raise_exception_when_more_bullets_are_added_to_the_clip_than_clip_size(self):
        sniper: Gun = Gun(GunType.SNIPER)
        with self.assertRaises(Exception):
            sniper.reload(40)

    def test_that_shotgun_cannot_shoot_negative_bullets(self):
        shotgun: Gun = Gun(GunType.SHOTGUN)
        shotgun.reload(20)

        with self.assertRaises(Exception):
            for bullet in range(40):
                shotgun.shoot()

    def test_that_shotgun_shoots_four_bullets_at_a_time(self):
        shotgun: Gun = Gun(GunType.SHOTGUN)
        shotgun.reload(20)
        shotgun.shoot()

        self.assertEqual(16, shotgun.ammo_left)


    def test_that_flash_can_on(self):
        shotgun: Gun = Gun(GunType.SHOTGUN)
        shotgun.toggle_light()
        self.assertEqual(True, shotgun.is_flash_on)

    def test_that_laser_can_on(self):
        shotgun: Gun = Gun(GunType.SHOTGUN)
        shotgun.toggle_laser()
        self.assertEqual(True, shotgun.is_laser_on)