from depending.variables import bind, scope, dependency


@dependency
async def foo():
    return "pig"


async def test_variables():
    @bind
    async def function(foo):
        print(foo)

    async with scope(foo="bar"):
        await function()

    async with scope(foo="cat"):
        await function()

    await function(foo="bulldog")
    await function()

    raise
