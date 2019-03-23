from . models import Projectile

__all__ = ['simulate_collision']


def _dot_product(a, b):
    pass


def simulate_collision(a, b):
    after_a = Projectile(-a.mass, -a.velocity)
    after_b = Projectile(-b.mass, -b.velocity)
    return after_a, after_b

