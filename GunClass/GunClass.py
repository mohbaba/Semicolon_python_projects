# from GunType import GunType
from GunClass.GunType import GunType
import time


class Gun:
    is_flash_on = False
    is_laser_on = False
    is_shot_gun = False
    ammo_left = 0

    def __init__(self, gun_type: GunType):
        self.is_clip_empty = True
        self.gun_type = gun_type

        if self.gun_type == gun_type.ASSAULT:
            self.clip_size = 100
        elif self.gun_type in (gun_type.PISTOL, gun_type.SNIPER):
            self.clip_size = 30
        elif self.gun_type == gun_type.SHOTGUN:
            self.clip_size = 20
            self.is_shot_gun = True

    def reload(self, ammo):
        if ammo > self.clip_size:
            raise Exception(f"Gun clip size is {self.clip_size}, insufficient space for number of bullets provided ")
        self.ammo_left = ammo
        self.is_clip_empty = False

    def shoot(self):
        if self.is_clip_empty:
            raise Exception("Clip is empty, reload gun")
        if self.is_shot_gun and self.ammo_left != 0:
            self.ammo_left -= 4
        elif self.ammo_left != 0:
            self.ammo_left -= 1
        else:
            self.is_clip_empty = True

    def toggle_laser(self):
        self.is_laser_on = not self.is_laser_on

    def toggle_light(self):
        self.is_flash_on = not self.is_flash_on



