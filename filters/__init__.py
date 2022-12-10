
from loader import dp
from .admim import AdminFilter


if __name__ == "filters":
    dp.filters_factory.bind(AdminFilter)
