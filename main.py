from flask import Flask
import subprocess


app = Flask(__name__)

@app.route('/hello')
def hello():
    event = "deploy_script.sh flask sasa 5002 fridah51"
    script_path = '/scripts/hello.sh'

    # 1. Make it executable
    # subprocess.run(['chmod', '+x', script_path], check=True)

    # 2. Run the script and pass the event via stdin
    process = subprocess.Popen(
        [script_path],              # path to script (you already chmod’d it)
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True                   # for string I/O instead of bytes
    )

    stdout, stderr = process.communicate(input=event)

    print("STDOUT:", stdout)
    print("STDERR:", stderr)
    print("Exit code:", process.returncode)

    return "hello you!"


if __name__ == '__main__':
    app.run(debug=True, port=5001)