from flask import Flask, jsonify
import datetime
import socket

## endpoints
#  '/api/v1/details'
#  '/api/v1/healtz'

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    return jsonify({"time": datetime.datetime.now().strftime("%I:%M:%S %p on %B %d, %Y"),
                    "hostname": socket.gethostname(),
                    "message": "Welcome to the Flask application!!  :) <3 (:",
                    "deployed_by": "Devesh Parashar",
                    "deployment_method": "GitHub Actions CI/CD Pipeline with ArgoCD",
                    "deloyed_on": "Kubernetes Cluster with Nginx Ingress Controller"
                    }), 200

@app.route('/api/v1/healtz')
def healtz():
    return jsonify({"status": "up"}), 200
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)