from flask import Flask
import subprocess


app = Flask(__name__)

@app.route('/hello')
def hello():
    # event = "deploy_script.sh flask sasa 5002 fridah51"
    event = "sasa"

    script_path = '/hom/python-subprocess/scripts/hello.sh'

    # 1. Make it executable
    subprocess.run(['chmod', '+x', script_path], check=True)

    # 2. Run the script and pass the event via stdin

    # OPTION 1
    # result = subprocess.run(['bash', script_path], capture_output=True, text=True)
    # print("STDOUT:", result.stdout)
    # print("STDERR:", result.stderr)
    # return "hello you!"


    # OPTION 2
    process = subprocess.Popen(
        ['bash',script_path],              # path to script (you already chmod’d it)
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True                          # for string I/O instead of bytes
    )

    stdout, stderr = process.communicate(input=event)

    return {
            "status": "success" if process.returncode == 0 else "error",
            "stdout": stdout,
            "stderr": stderr
        }





if __name__ == '__main__':
    app.run(debug=True, port=5001)