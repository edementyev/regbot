import logging

from aiogram.utils import executor
from aiogram.utils.exceptions import TerminatedByOtherGetUpdates

from app import dp as dispatcher, config, navigation_context


async def on_startup(dp):
    logging.warning('Powering up.')
    logging.warning('Config is:' + str(config))


async def on_shutdown(dp):
    logging.warning('Shutting down..')

    # Close DB connection (if used)
    await dp.storage.close()
    await dp.storage.wait_closed()

    await navigation_context.storage.close()
    await navigation_context.storage.wait_closed()

    logging.warning('Bye!')

if __name__ == '__main__':
    try:
        executor.start_polling(dispatcher,
                               on_startup=on_startup,
                               on_shutdown=on_shutdown,
                               timeout=20)
    except TerminatedByOtherGetUpdates as e:
        exit(0)
        pass
