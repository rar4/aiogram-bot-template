import asyncio

import asyncpg

from data import config

from rpg.utilities import  loader


class Database:
    def __init__(self):
        loop = asyncio.get_event_loop()
        self.pool = loop.run_until_complete(
            asyncpg.create_pool(
                database=config.DATABASE,
                user=config.USER,
                password=config.PASSWORD,
                host=config.HOST,
                port=config.PORT


            )
        )

    async def save(self, coins, usid):
        sql = f"""
            UPDATE "games"
            SET coins = '{coins}'
            Where id = {usid}
            """

        await self.pool.execute(sql)

    async def create_user_table(self):
        sql = """ 
        CREATE TABLE IF NOT EXISTS "games"(
        id integer NOT NULL,
        name character varying NOT NULL,
        coins integer,
        CONSTRAINT games_pkey PRIMARY KEY (id)
        )
        """
        await self.pool.execute(sql)

    async def create_user(self, usid, name, coins):
        sql = f"""
        INSERT INTO "games"( id, name, coins)
        VALUES({usid}, '{name}', '{coins}')
        """
        try:
            await self.pool.execute(sql)
        except asyncpg.exceptions.UniqueViolationError:
            pass


    async def load(self, id):
        sql = f"""
        select coins
        from public.games
        WHERE id = {id}
        """

        a = await self.pool.fethrow(sql)
        loader.player.coins = a



