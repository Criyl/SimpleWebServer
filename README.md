[![CI Pipeline](https://github.com/Criyl/SimpleWebServer/actions/workflows/ci.yml/badge.svg)](https://github.com/Criyl/SimpleWebServer/actions/workflows/ci.yml)
[![CD Pipeline](https://github.com/Criyl/SimpleWebServer/actions/workflows/cd.yml/badge.svg?branch=main)](https://github.com/Criyl/SimpleWebServer/actions/workflows/cd.yml)

This project functions as a challenge/assessment for the purpose of learning the following technologies and concepts.

- FastAPI: High performance lightweight web framework
- Poetry: Python dependency manager
- Pre-Commit: Framework for maintaining pre-commit git-hooks.
- Flake8: Python linter
- MyPy: Python static-type checker 
- PyTest: Python testing framework
- Kubernetes: Container orchestration system
- Continuous Integration: A development practice for teams that need to integrate work frequently.
- Continuous Deployment: A development practice that facilitates frequent delivery with automated deployments.
- Semantic Versioning: Set of rules and requirements that dictate how version numbers are assigned and incremented.

---

<details>
  <summary>How to Perform Local Development</summary>
      
---
*Install Poetry & Dependancies*
```
pip install poetry
poetry install
```
  
*Install Pre-Commit Hook*
```
pre-commit install
```
  
 *Host Local Test Server @ http://localhost:8000/*
```
poetry run uvicorn server:app
```
</details>


<details>
  <summary>How to Run Tests</summary>
    
---
```
poetry run pytest ./tests
```
</details>


<details>
    <summary>How to Build and Run Container</summary>
  
---
```
docker build -t simple_web_server .
docker run -p 8000:8000 simple_web_server
```
 
</details>


<details>
  <summary>How to Deploy Manifest Locally</summary>

---
  
*This assumes you have both [minikube](https://minikube.sigs.k8s.io/docs/start/) and [kubectl](https://kubernetes.io/docs/tasks/tools/) installed*
```
minikube start
kubectl create -f manifest.yml
kubectl expose deployment simple-web-server --type=LoadBalancer --name=simple-service
minikube tunnel simple-service --log_file service.log
```

</details>

<details>
  <summary>Tasks Runner</summary>

---
  
*A Taskfile is provided for easier execution of common tasks* 

*How to install Task*
https://taskfile.dev/#/installation

</details>
