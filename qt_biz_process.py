import time

def biz_process():
    """
    Return the process_status using yield into the pyqt main.
    
    You can customize the status of your Biz. process using yield.
    Your biz logic have to be located between yield.
    """
    print("Biz. process is starting...")
    yield 100
    time.sleep(5)

    print("Biz. process is in progress...")
    yield 50

    time.sleep(5)
    print("Biz. process is completed.")
    yield 100

    time.sleep(5)