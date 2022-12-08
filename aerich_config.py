"""
Title      : Aerich migration configuration for Tortoise ORM.
Create Time: 2022/12/05
Author     : IOInfinity x 源碼無限
"""
ORM_MIGRATION_SQLITE = {
    "connections": {
        "default": "sqlite://product.db",
    },
    "apps": {
        "models": {
            "models": ["tests.models", "aerich.models"],
            "default_connection": "default",
        }
    }
}
