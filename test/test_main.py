import threading

from main import MainClass


def test_main():
    main = MainClass()
    threading.Thread(target=main.start).start()
    assert main.running

    main.stop()
    assert not main.running
