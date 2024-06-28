import time
import os
import subprocess

def main():

    def write_test(path):
        testFile = os.path.join(path, 'testfile')
        data = b'we are testing write speed' * 1024  # Data chunk to write
        with open(testFile, 'wb+') as f:
            print('Testing write speed...')
            startTime = time.time()
            for i in range(16000):  # Writing more chunks of data to increase the file size
                f.write(data)
            f.flush()
            os.fsync(f.fileno())
            diff = time.time() - startTime
            write_speed = (os.stat(testFile).st_size / 1048576) / diff
        os.unlink(testFile)
        return write_speed

    def selectPath():
        path = os.path.curdir
        # Path option provided after detecting operating system
        if os.name == 'posix':
            print(subprocess.check_output("df", shell=True).decode())
            path = input("Please type the mounted on path of disk e.g /Volumes/ABC ")
        elif os.name == 'nt':
            path = input("Enter the Drive Letter of Removable Drive. e.g I ")
            path = f"{path}:\\"
        
        if not os.path.exists(path):
            print('Please enter a valid path')
            return selectPath()
            
        return path

    def runTests(path, iterations=5):
        write_speeds = []
        for i in range(iterations):
            print(f"Running test {i+1} of {iterations}...")
            write_speed = write_test(path)
            print(f"Test {i+1} write speed: {write_speed:.2f} MB/sec")
            write_speeds.append(write_speed)
        
        average_write_speed = sum(write_speeds) / len(write_speeds)
        return average_write_speed

    path = selectPath()
    print("Checking your Removable Drive Speed......")
    average_write_speed = runTests(path)
    print("Average write speed is {:.2f} MB/sec".format(average_write_speed))

if __name__ == "__main__":
    main()
