def filemanip(inputFile, outputFile):
    try:
        with open(inputFile, 'r') as f:
            with open(outputFile, 'w') as outF:
                data = f.readlines()
                data.append("Text read")
                for line in data:
                    outF.write(line)
                print("Updated file copied successfully!")
    except FileNotFoundError:
        print("File not found")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
        
