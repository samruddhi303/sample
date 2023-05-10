def Welcome():
    print("Hey you are welcome!!")
    print(__name__)
    if __name__ == "__main__":
        Welcome()
        #if you import it as a module into another script and call the main function from imported module,it will not output anything