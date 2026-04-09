from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "running", "port": 5200})

@app.route('/health')
def health():
    return jsonify({"health": "ok"})

@app.route('/info')
def info():
    return jsonify({"app": "Flask DevOps Automation", "author": "Subashraj"})

@app.route('/run_script/<script_name>')
def run_script(script_name):
    try:
        output = subprocess.check_output(['python', f'scripts/{script_name}.py'])
        return jsonify({"output": output.decode('utf-8')})
    except Exception as e:
        return jsonify({"error": str(e)})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5200)