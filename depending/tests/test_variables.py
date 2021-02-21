from depending.variables import bind, dependencies, dependency


@dependency
async def foo():
    return "pig"


async def test_variables():
    @bind
    async def function(foo):
        print(foo)

    async with dependencies(foo="bar"):
        await function()

    async with dependencies(foo="cat") as dumb:
        await function()

    await function(foo="bulldog")
    await function()

    raise
