# app/auth/redis.py
"""
Stubbed Redis blacklist logic for JWT tokens.

This avoids aioredis incompatibility with Python 3.12.
"""

async def add_to_blacklist(jti: str, exp: int):
    """Pretend to add a token ID to a blacklist (no-op)."""
    return True


async def is_blacklisted(jti: str) -> bool:
    """Always return False so tokens are never treated as revoked."""
    return False
