import bot_core

if __name__ == "__main__":
    if hasattr(bot_core, 'main'):
        bot_core.main()
    elif hasattr(bot_core, 'run'):
        bot_core.run()
