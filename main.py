from flask import Flask, request, jsonify
import subprocess


app = Flask(__name__)

@app.route('/deploy/<string:subdomain>')
def deploy(subdomain):
    if not subdomain:
        return jsonify({"error": "Missing subdomain"}), 400

    try:
        script_path = '/home/python-subprocess/scripts/hello.sh'
        # 1. Make it executable
        subprocess.run(['chmod', '+x', script_path], check=True)

        # 2. Run the script and pass the event via stdin

        # OPTION 1
        cmd = [
            "nsenter", "-t", "1", "-m", "-u", "-n", "-i",
            "bash", script_path, subdomain
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)

        return jsonify({"output": result.stdout})


        # OPTION 2
        # 
        # process = subprocess.Popen(
        #     cmd,              # path to script (you already chmod’d it)
        #     stdin=subprocess.PIPE,
        #     stdout=subprocess.PIPE,
        #     stderr=subprocess.PIPE,
        #     text=True                          # for string I/O instead of bytes
        # )

        # # stdout, stderr = process.communicate()

        # return {
        #         "status": "success" if process.returncode == 0 else "error",
        #         "stdout": stdout,
        #     }

    except subprocess.CalledProcessError as e:
            return jsonify({"error": e.stderr}), 500










if __name__ == '__main__':
    app.run(debug=True, port=5001)