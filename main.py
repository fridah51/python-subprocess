from flask import Flask, request, jsonify
import subprocess


app = Flask(__name__)

@app.route('/deploy/<string:subdomain>')
def deploy(subdomain):
    if not subdomain:
        return jsonify({"error": "Missing subdomain"}), 400
    
    script_path = "/home/python-subprocess/scripts/deploy.sh"

    try:
        # 1. Make it executable
        subprocess.run(["chmod", "+x", script_path], check=True)
        print(f"Permissions set for {script_path}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to set permissions: {e.stderr}")

    try:
        
        # 2. Run the script and pass the event via stdin
        cmd = [
            "nsenter", "-t", "1", "-m", "-u", "-n", "-i",
            "bash", script_path, subdomain
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)

        return jsonify({"output": result.stdout})

    except subprocess.CalledProcessError as e:
            return jsonify({"error": e.stderr}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)