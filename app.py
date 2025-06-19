from factory import MessageFactory

def main():
    factory = MessageFactory()
    message = factory.create_message()
    print(message)

if __name__ == "__main__":
    main()
