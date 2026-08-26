def process_file():
    try:
        f=open("c:\\aamairs\\sahas.txt")
        print("file opend succesfully")
        x=1/0
    except FileNotFoundError:
        print('file not found error')
    except ZeroDivisionError:
        print("division by zero is nolt posssible")
    finally:
        try:
            f.close()
            print("file closed succesfully")
        except NameError:
            print("Error:file was never opend and nothing to close")
process_file()